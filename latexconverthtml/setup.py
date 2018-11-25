#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#Auteur: David Couronné
#Convertion automatique de LaTeX en HTML
from latexconverthtml import LaTeX
import re

listeCommandesClean = [LaTeX.LaTeXCommand(r"\\newpage",0),
    LaTeX.LaTeXCommand(r"\\hfill",0),
    LaTeX.LaTeXCommand(r"\\medskip",0),
    LaTeX.LaTeXCommand(r"\\vspace",1)]
re_vspace = r"\\vspace\{([\d|\w|\.|-]*)\}"
re_hfill = r"\b\\hfill\b"
re_newpage = r"\\newpage\b"

newpage = LaTeX.LaTeXCommand(r"\\newpage",0)