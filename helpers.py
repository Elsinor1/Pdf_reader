import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory, askopenfilename
import PyPDF2
import concurrent.futures
import re


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
    file_path = read_path + "/" + file
    # Reads text from PDF
    text = read_pdf(file_path)
    # Gets the part number from file name by striping .pdf
    pn_split = file.split(".")
    pn = pn_split[0]
    # Outputs a list of dictionaries pn : text
    read_output.append({"pn": pn, "drawing_text": text})
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
        # pattern = f"{keyword_tuple[0]}\n((.|\n)*){keyword_tuple[1]}\d+"
        # pattern = (
        #     r"\b\w*" + keyword_tuple[1] + r"(.|\n)*" + keyword_tuple[2] + r"\w*\b"   .*?
        # )
        # pattern = r"(?:{0})(.|\n)(?:{1})".format(re.escape(keyword_tuple[1]), re.escape(keyword_tuple[2]))
        # out = re.search(pattern, text, re.IGNORECASE).group(1).strip()
        # print(out)
        # re.sub(f"{keyword_tuple[1]}", "", out, re.IGNORECASE)
        # re.sub(f"{keyword_tuple[2]}", "", out, re.IGNORECASE)

        pattern = re.compile(
            rf"{keyword_tuple[1]}\n(.*?)\n{keyword_tuple[2]}", re.DOTALL | re.IGNORECASE
        )
        # print(pattern)

        # search for the text between the start and end strings
        out = re.search(pattern, text).group(1).strip()
        if out == None:
            return "Not found3"
        else:
            return out
    except AttributeError:
        return "Not found4"
