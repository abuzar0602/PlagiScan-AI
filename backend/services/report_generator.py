from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filepath, data):

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
            f"Similarity Score: {data['similarity']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {data['risk']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total Words: {data['words']}",
            styles["Normal"]
        )
    )

    doc.build(content)