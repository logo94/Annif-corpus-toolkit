[![it](https://img.shields.io/badge/lang-it-green.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)

# excel2text-key
Excel2text-key allows to automatically convert data contained in an Excel file into file pairs with the extension `.txt` and `.key`.

Supported extensions: `xls`, `xlsx`, `xlsm`, `xltx` and `xltm`.

## Basic install ##
The script requires `Python 3.8+` installation, to install the correct Python version follow the instructions, based on your operating system, as reported to the following [link](https://www.python.org/downloads/).

Once the installation is done it is possible to check the current `Python` and `pip` versions via the commands:

```
python --version
```
```
pip --version
```
### Virtual environment ###
Is recommended to operate within a python virtual environment using `venv` module. `venv` already comes packaged with your Python installation and allows to use different versions of package dependencies; to create a virtual environment, do the following:

Create a virtual environment
```
python3 -m venv pyenv
```

Activate the virtual environment:
```
source pyenv/bin/activate
```

### Packages ###
Once the virtual environment has been activated, it is possible to proceed with libraries installation; 

```
pip install -r requirements.txt
```

## Setup ##
To perform the conversion correctly, the starting excel file has to be structured as follows:

* **Column 1** : unique identification code of each file to be created, without any extension. Any type of code as textual, numeric or alphanumeric can be used;
* **Column 2** : text of a document; in case the text includes secondary information, it is possible to split text of interest and secondary text with a slash (" / "). The script will only read the text positioned to the left of the slash;
* **Column 3** : list of keywords associated with the textual portion placed in Column 2. The keywords can be passed in sequence, separated by a dash (" - "), the script will automatically place one word per line inside the resulting .key file.

Each pair of files will be named as the identification code reported inside **Column 1** : the first file will contain the text of a document (**Column 2** ) with the extension `.txt`; the second file will contain the list of keywords associated with the text (**Column 3** ), listed one per line, with the extension `.key`. 

> The script parameters can be edited or added manually.

## Usage ##
Once downloaded repository and packages, is possible to run the script with the command:
```
python3 excel2textkey.py
```
The script will ask to select the file ro read, then generate, in the same directory and with the same name as the selected spreadsheet, a directory containing the file pairs `.txt-key`.
