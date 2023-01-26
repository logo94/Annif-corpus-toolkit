![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)

# pdf2text
Script in Python per la conversione di file dal formato `.pdf` al formato `.txt`.

## Installazione ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.8+` sul proprio dispositivo, per installare Python seguire, in base al proprio sistema operativo, le istruzioni riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```
### Ambiente virtuale ###
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale indipendente dal proprio sistema; per la creazione di un ambiente virtuale procedere come segue:

Creare l'ambiente virtuale
```
python3 -m venv pyenv
```

Attivare l'ambiente virtuale:
```
source pyenv/bin/activate
```

### Librerie ###
Una volta attivato l'ambiente virtuale è possibile procedere con l'installazione delle librerie necessarie:

[pdf2text.py](https://github.com/logo94/pdf2text/blob/main/pdf2text.py) utilizza la libreria [PyPDF2](https://github.com/py-pdf/PyPDF2), per l'installazione eseguire:
```
pip install PyPDF2
```

## Utilizzo ##
Una volta scaricate le librerie necessarie e scaricato il repository, per avviare lo script sarà sufficiente eseguire il comando:
```
python3 pdf2text.py
```
Una volta avviato apparirà una finestra di dialogo tramite cui selezionare uno o più file `.pdf`, i file testuali saranno creati nella stessa cartella e con lo stesso nome dei file originali, con estensione `.txt`
