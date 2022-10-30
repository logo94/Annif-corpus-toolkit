from distutils import filelist
from distutils.filelist import FileList
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilename(title = "Seleziona file",filetypes= (("PDF","*.pdf"),("Tutti i file","*.*")), multiple=True)
var = root.tk.splitlist(files)

filePaths = []
for f in var:
    filePaths.append(f)
filePaths

fileName = []
for path in filePaths:
    fileName.append(path)
fileName

for i in fileName:
    file = i.split("/")[-1]
    folder_path = i.rsplit("/", 1)[0]
    file_name = file.split(".")[0]
    txt_file = folder_path + "/" + file_name + ".txt"
    
    reader = PdfReader(i)
    pp = reader.numPages

    with open(txt_file, 'w+', encoding='utf-8', newline='') as tf:

        for p in range(1, pp):
            page = reader.pages[p]
            text = page.extractText().replace("-\n", "").replace("a`", "à ").replace("`a", "à ").replace("e`", "è ").replace("`e", "è ").replace("e´", "é ").replace("i`u", "iù ").replace("i`", "ì ").replace("`i", "ì ").replace("o`", "ò ").replace("`o", "ò ").replace("u`", "ù ").replace("`u", "ù ")
            tf.write(text)





    

