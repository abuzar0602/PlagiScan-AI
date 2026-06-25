import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filepath, data):

    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "PlagiScan AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Files: {data['filename']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Similarity Score: {data['similarity_score']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {data['risk_level']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total Words: {data['total_words']}",
            styles["Normal"]
        )
    )

    doc.build(content)