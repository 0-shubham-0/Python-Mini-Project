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
