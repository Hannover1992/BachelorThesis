#!/bin/bash

# LaTeX-Kompilierung
pdflatex 00thesis.tex && biber 00thesis && pdflatex 00thesis.tex && pdflatex 00thesis.tex

# Aufräumen: Löschen aller Dateien, die nicht die Endungen .bibtex, .tex, .pdf, oder .sh haben
find . -type f \
! \( -name "*.bib" -o -name "*.tex" -o -name "*.pdf" -o -name "*.sh" \) \
-exec rm {} +
