import pdfplumber
import docx

def extract_text(filepath):

    if filepath.endswith(".txt"):
        with open(
            filepath,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:
            return f.read()

    elif filepath.endswith(".pdf"):

        text = ""

        with pdfplumber.open(filepath) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    elif filepath.endswith(".docx"):

        doc = docx.Document(filepath)

        return "\n".join(
            para.text
            for para in doc.paragraphs
        )

    return ""