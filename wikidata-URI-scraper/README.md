![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)


# wikidata-URIs-scraper

Scritto a supporto della preparazione di un vocabolario completo per l'addestramento di Annif, software per l'indicizzazione automatica per soggetto di testi; partendo da un foglio di calcolo, lo scraper automatizza la procedura lato web browser di ricerca di ogni termine, riga per riga, su Wikipedia o Wikidata. 

Per riprodurre un vocabolario strutturato secondo la forma supportata da Annif, l'URI di ogni Elemento Wikidata trovato viene copiato, per la stessa riga del foglio di calcolo, nella colonna precedente rispetto al termine ricercato.   

## Preparazione ##
Il foglio di calcolo di partenza deve essere così strutturato:

* **Colonna 1**: vuota; 
* **Colonna 2**: termine da ricercare per l'ottenimento del relativo URI 

## Utilizzo ##
Una volta scaricate le librerie necessarie e scaricato il repository, per avviare lo script sarà sufficiente eseguire il comando:
```
python3 wikipedia.py
```
Ogni termine viene ricercato su Wikipedia, se il termine ricercato coincide esattamente con il nome della voce Wikipedia, viene seguito il link che rimanda al relativo elemento Wikidata e l'URI viene copiato all'interno del foglio di calcolo tra parentesi uncinate `<` `>`

oppure

```
python3 wikidata.py
```
Ogni termine viene ricercato tramite API del servizio di riconciliazione di Wikidata, se il termine ricercato esiste e coincide, il relativo URI viene copiato all'interno del foglio di calcolo tra parentesi uncinate `<` `>`. 
