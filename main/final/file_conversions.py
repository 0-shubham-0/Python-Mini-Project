import docx
import pdfplumber
import docx2txt as dt
import os
import shutil


def docx_to_text(path_to_file, images_folder='image', get_text=True):
    text = dt.process(path_to_file, images_folder)
    dir = os.listdir(images_folder)
    if get_text:
        if len(dir) == 0:
            print("Empty directory")
            return [text]
        else:
            print("Not empty directory")
            for root, dirs, files in os.walk(images_folder):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))

            return [0, text]  # Images exist
    else:
        return [1]  # Some error


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

