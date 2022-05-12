import docx
import docx2txt as dt


def getText(filename):

    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def docx_to_text(path_to_file, images_folder, get_text=True):

    text = dt.process(path_to_file, images_folder)

    if get_text:
        print(text)


path_to_file = 'Python Mini Project - REPORT.docx'
images_folder = './images/'

docx_to_text(path_to_file, images_folder)