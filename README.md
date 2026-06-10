# DarkCodeFactory

## Kurzbeschreibung

Streamlit-App zur BMI-Berechnung.

## Voraussetzungen

- Python 3.13

## Installation

```bash
pip install -r requirements.txt
```

## Start

```bash
streamlit run app/main.py
```

## Projektstruktur

```text
DarkCodeFactory/
+-- app/
|   +-- main.py
+-- README.md
+-- requirements.txt
```

## Aktuelle Funktionen

- Eingabe von Koerpergroesse in Zentimetern
- Eingabe von Gewicht in Kilogramm
- BMI-Berechnung per Button
- Anzeige des berechneten BMI
- Einordnung in BMI-Kategorien
- Farbige Rueckmeldung je nach Kategorie

## Naechste moegliche Ausbaustufen

- Validierung und Hinweise fuer realistische Eingaben erweitern
- Erklaertexte zu BMI-Kategorien ergaenzen
- Verlauf mehrerer Berechnungen anzeigen
- Optionale Speicherung oder Export der Ergebnisse
- Tests fuer die BMI-Berechnungslogik ergaenzen
