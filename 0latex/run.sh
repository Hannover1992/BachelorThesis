#!/bin/bash

# LaTeX-Kompilierung
pdflatex thesis.tex && biber thesis && pdflatex thesis.tex && pdflatex thesis.tex

# Aufräumen: Löschen aller Dateien, die nicht die Endungen .bibtex, .tex, .pdf, oder .sh haben
find . -type f \
! \( -name "*.bib" -o -name "*.tex" -o -name "*.pdf" -o -name "*.sh" \) \
-exec rm {} +
