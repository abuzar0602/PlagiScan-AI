from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Scan(db.Model):
    __tablename__ = "scans"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    similarity_score = db.Column(
        db.Float,
        nullable=False
    )

    risk_level = db.Column(
        db.String(50),
        nullable=False
    )

    total_words = db.Column(
        db.Integer,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "similarity_score": self.similarity_score,
            "risk_level": self.risk_level,
            "total_words": self.total_words,
            "created_at": self.created_at.isoformat()
        }