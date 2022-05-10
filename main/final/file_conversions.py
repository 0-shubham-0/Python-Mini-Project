import docx
import pdfplumber


def pdf_to_txt(file):
    from pdfminer.pdfpage import PDFPage
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    with open(file, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num == len(searchable_pages):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                print(page.extract_text())
                text += page.extract_text()
        return [text]
    elif page_num != len(searchable_pages):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                print(page.extract_text())
                text += page.extract_text()
        return [0, text]
    else:
        return [1]


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

