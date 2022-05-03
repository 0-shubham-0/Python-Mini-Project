import pdfplumber


def pdf_to_txt(file):
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        print(first_page.extract_text())
    return first_page.extract_text()
