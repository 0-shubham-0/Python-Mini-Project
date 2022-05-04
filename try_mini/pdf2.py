import pdfplumber


def pdf_to_txt(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            print(page.extract_text())
            text += page.extract_text()
    return text
