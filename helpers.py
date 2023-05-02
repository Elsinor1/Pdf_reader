import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename
import PyPDF2
import concurrent.futures
import re
import ocrmypdf


# Gets folder path input
def get_folder_path():
    # shows dialog box and return the path
    path = askdirectory(title="Select Folder")
    return path


# Gets file path input
def get_file_path():
    path = askopenfilename(title="Select a database")
    return path


# Function for reading PDF into a text
def read_pdf(path):
    try:
        file = open(path, "rb")
        fileReader = PyPDF2.PdfReader(file)
        page = fileReader.pages[0]
        text = page.extract_text()
        return text
    except:
        return "Cannot be read"


def read(path):
    # Define global variables for the function
    global read_output
    global read_path
    read_path = path
    read_output = []
    # List of files in a given directory
    files = os.listdir(read_path)
    # Creates threads to iterate through file list
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # For every file in a directory
        executor.map(read_thread, files)

    return read_output


def read_thread(file):
    # Creates path to a file
    file_path = os.path.join(read_path, file)
    # Reads text from PDF
    text = read_pdf(file_path)
    # Gets the part number from file name by striping .pdf
    file_name_split = file.split(".")
    file_name = file_name_split[0]
    # Outputs a list of dictionaries pn : text
    read_output.append({"file_name": file_name, "pdf_text": text})
    return


# Creates a db in a given path
def create_db(path):
    try:
        open(f"{path}/output.db", "x")
        return f"{path}/output.db"
    except FileExistsError:
        messagebox.showerror(message="File output.db already exists in the folder")
        return
    except FileNotFoundError:
        messagebox.showerror(message="Could not create DB in given folder")


def search_keyword(keyword, text):
    try:
        pattern = r"\b\w*" + keyword + r"\w*\b"
        # pattern = r"{{{}}}".format(keyword)
        out = re.search(pattern, text, re.IGNORECASE).group().strip()
        if out == None:
            return "Not found1"
        else:
            return out

    except AttributeError:
        return "Not found2"


def search_between(keyword_tuple, text):
    try:
        pattern = re.compile(
            rf"{keyword_tuple[1]}(.*?){keyword_tuple[2]}", re.DOTALL | re.IGNORECASE
        )
        out = re.search(pattern, text).group(1).strip()
        if out == None:
            return "Not found3"
        else:
            return out
    except AttributeError:
        return "Not found4"


def ocr_pdf(path, folder_path):
    try:
        out = os.path.join(folder_path, "out.pdf")
        ocrmypdf.ocr(path, out, deskew=True)
        fileReader = PyPDF2.PdfReader(out)
        page = fileReader.pages[0]
        text = page.extract_text()
        os.remove(out)
    except:
        return "Could not OCR"
    return text
