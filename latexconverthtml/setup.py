#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# Auteur: David Couronné
# Convertion automatique de LaTeX en HTML
import re

from latexconverthtml import LaTeXCommands

# Commandes à supprimer
listeCommandesClean = [LaTeXCommands.LaTeXCommand(r"\\newpage", 0),
                       LaTeXCommands.LaTeXCommand(r"\\hfill", 0),
                       LaTeXCommands.LaTeXCommand(r"\\medskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\vspace", 1),
                       LaTeXCommands.LaTeXCommand(r"\\bigskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\smallskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\hspace", 1),
                       LaTeXCommands.LaTeXCommand(r"\\setlength", 0),
                       LaTeXCommands.LaTeXCommand(r"\\parindent", 1),
                       LaTeXCommands.LaTeXCommand(r"\\pagestyle", 1),
                       LaTeXCommands.LaTeXCommand(r"\\rhead", 1),
                       LaTeXCommands.LaTeXCommand(r"\\Large", 0),
                       LaTeXCommands.LaTeXCommand(r"\\thispagestyle", 1)
                       ]
