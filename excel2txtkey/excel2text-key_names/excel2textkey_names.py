import os
import tkinter as tk
from tkinter import filedialog
import xls2textkey
import xlsx2textkey

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename()

ext = ['.xlsx', '.xlsm', '.xltx', '.xltm']

if file.endswith('.xls'):
    xls2textkey.write_from_xls(file)
elif file.endswith(tuple(ext)):
    xlsx2textkey.write_from_xlsx(file)
else:    
    print("Formato non supportato")
