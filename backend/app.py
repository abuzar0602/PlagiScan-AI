from flask import send_file
from services.report_generator import generate_report
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from database.models import Scan
import os

from database.models import db, Scan
from services.parser import extract_text
from services.plagiarism import (
    preprocess,
    calculate_similarity,
    get_risk_level
)

app = Flask(__name__)

CORS(app)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///plagiscan.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all()

# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to PlagiScan AI API"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "running",
        "message": "PlagiScan AI API is working"
    })

@app.route("/api/scan", methods=["POST"])
def scan():

    files = request.files.getlist("files")

    if len(files) < 2:
        return jsonify({
            "error": "Upload at least 2 documents"
        }), 400

    documents = []

    try:

        # Save and extract text
        for file in files:

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                UPLOAD_FOLDER,
                filename
            )

            file.save(filepath)

            text = extract_text(filepath)

            documents.append({
                "filename": filename,
                "text": preprocess(text)
            })

        results = []

        highest_score = 0

        for i in range(len(documents)):
            for j in range(i + 1, len(documents)):

                similarity = calculate_similarity(
                    documents[i]["text"],
                    documents[j]["text"]
                )

                highest_score = max(
                    highest_score,
                    similarity
                )

                results.append({
                    "document_1": documents[i]["filename"],
                    "document_2": documents[j]["filename"],
                    "similarity": similarity,
                    "risk": get_risk_level(similarity)
                })

        total_words = sum(
            len(doc["text"].split())
            for doc in documents
        )

        risk = get_risk_level(highest_score)

        # Save scan history
        scan_record = Scan(
            filename=", ".join(
                doc["filename"]
                for doc in documents
            ),
            similarity_score=highest_score,
            risk_level=risk,
            total_words=total_words
        )

        db.session.add(scan_record)
        db.session.commit()

        return jsonify({
            "overall_similarity": highest_score,
            "risk_level": risk,
            "total_documents": len(documents),
            "total_words": total_words,
            "comparisons": results
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

    finally:

        for file in os.listdir(
            UPLOAD_FOLDER
        ):
            try:
                os.remove(
                    os.path.join(
                        UPLOAD_FOLDER,
                        file
                    )
                )
            except:
                pass

@app.route("/api/history")
def history():

    scans = Scan.query.order_by(
        Scan.created_at.desc()
    ).all()

    return jsonify([
        scan.to_dict()
        for scan in scans
    ])
    
@app.route("/api/test-scan")
def test_scan():

    text1 = """
    Artificial Intelligence is transforming education.
    Machine learning helps students learn efficiently.
    Python is widely used in AI applications.
    """

    text2 = """
    Artificial Intelligence is transforming education.
    Machine learning helps students learn efficiently.
    Python is used in many AI systems.
    """

    similarity = calculate_similarity(
        preprocess(text1),
        preprocess(text2)
    )

    return jsonify({
        "similarity": similarity,
        "risk": get_risk_level(similarity)
    })
@app.route("/api/report")
def download_report():

    latest_scan = Scan.query.order_by(
        Scan.id.desc()
    ).first()

    if not latest_scan:
        return {
            "error": "No scan history found"
        }, 404

    filepath = os.path.join(
        "reports",
        "plagiarism_report.pdf"
    )

    data = {
        "filename": latest_scan.filename,
        "similarity": latest_scan.similarity_score,
        "risk": latest_scan.risk_level,
        "words": latest_scan.total_words
    }

    generate_report(filepath, data)

    return send_file(
        filepath,
        as_attachment=True
    )
if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )