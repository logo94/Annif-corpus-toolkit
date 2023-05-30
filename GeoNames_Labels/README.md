![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)

# GeoNames Labels
Scritto a supporto della preparazione di un vocabolario completo per l'addestramento di Annif, software per l'indicizzazione automatica per soggetto di testi; partendo dagli URIs presenti nel file IT.zip liberamente scaricabile dall'authority file [GeoNames](https://download.geonames.org/export/dump/), lo script per ogni riga di un foglio di calcolo raggiunge la relativa pagina e trascrive, nella colonna successiva, l'etichetta originale disambiguata tramite riferimento geografico specifico incluso tra parentesi uncinate `<` `>`.


## Preparazione ##
Il foglio di calcolo di partenza deve essere così strutturato:

* **Colonna 1**: URI dell'elemento GeoNames da disambiguare; 
* **Colonna 2**: Etichetta originale;
* **Colonna 3**: vuota.

## Utilizzo ##
Una volta scaricate le librerie necessarie e scaricato il repository, per avviare lo script sarà sufficiente eseguire il comando:
```
python3 geonames_labels.py
```
Ogni termine viene ricercato su GeoNames, etichetta e riferimento geografico vengono copiati all'interno del foglio di calcolo secondo la forma `Luogo <Riferimento geografico>`.
