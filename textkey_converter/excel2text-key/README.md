![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
[![en](https://img.shields.io/badge/lang-en-yellow.svg)](https://github.com/logo94/excel2text-key/blob/main/README.en.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)

# excel2text-key
Excel2text-key permette di leggere un file Excel e generare, per ogni riga compilata, una coppia di file con estensione `.txt` e `.key`.

Lo script supporta diversi formati tra cui le estensioni: `xls`, `xlsx`, `xlsm`, `xltx` e `xltm`.


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
