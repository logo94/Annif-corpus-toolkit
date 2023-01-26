![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
[![en](https://img.shields.io/badge/lang-en-yellow.svg)](https://github.com/logo94/excel2text-key/blob/main/README.en.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)

# excel2text-key
Excel2text-key permette di leggere un file Excel e generare, per ogni riga compilata, una coppia di file con estensione `.txt` e `.key`.

Lo script supporta diversi formati tra cui le estensioni: `xls`, `xlsx`, `xlsm`, `xltx` e `xltm`.


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
Una volta attivato l'ambiente virtuale è possibile procedere con l'installazione delle librerie necessarie; Excel2text-key utilizza due diverse librerie

[xls2textkey.py](https://github.com/logo94/excel2text-key/blob/main/xls2textkey.py) utilizza la libreria [xlrd](https://pypi.org/project/xlrd/), per l'installazione eseguire:
```
pip install xlrd
```

[xlsx2textkey.py](https://github.com/logo94/excel2text-key/blob/main/xlsx2textkey.py) utilizza la libreria [openpyxl](https://openpyxl.readthedocs.io/en/stable/), per l'installazione eseguire:
```
pip install openpyxl
```

## Preparazione ##
Per eseguire correttamente la conversione il file excel di partenza deve essere così strutturato:

* **Colonna 1**: codice identificativo univoco di ogni documento, senza alcuna estensione. Può essere usato qualsiasi tipo di codice che sia testuale, numerico o alfanumerico; 
* **Colonna 2**: porzione testuale di un documento; nel caso in cui il testo includa informazioni secondarie, è possibile dividere testo di interesse e testo secondario con una barra obliqua (" / "). Lo script leggerà esclusivamente il testo posizionato alla sinistra della barra obliqua; 
* **Colonna 3**: lista di parole chiave associate alla porzione testuale riportata all'interno della Colonna 2. Le parole chiave possono essere passate in sequenza, separate da un trattino (" - "), lo script disporrà automaticamente all'interno del file .key risultante una parola per ogni riga.

Ogni coppia di file sarà denominata con il codice identificativo riportato all'interno della **Colonna 1**: il primo file conterrà il testo di un documento (**Colonna 2**) con estensione `.txt`; il secondo file conterrà la lista delle parole chiave associate al testo (**Colonna 3**), disposte una per riga, con estensione `.key`. 

>I parametri dello script possono essere modificati o aggiunti, in base alle proprie necessità, in corrispondenza delle righe segnalate dal commento --> # Modifica parametri

## Utilizzo ##
Una volta scaricate le librerie necessarie e scaricato il repository, per avviare lo script sarà sufficiente eseguire il comando:
```
python3 excel2textkey.py
```
Una volta selezionato il foglio di calcolo da convertire verrà generata una cartella, con lo stesso nome e nella stessa posizione del foglio di calcolo selezionato, contenente le coppie di file `txt-key`.
