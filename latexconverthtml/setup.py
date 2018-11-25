#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# Auteur: David Couronné
# Convertion automatique de LaTeX en HTML
import re

from latexconverthtml import LaTeXCommands

# Commandes sans argument à supprimer
listeCommandesClean = [LaTeXCommands.LaTeXCommand(r"\\newpage", 0),
                       LaTeXCommands.LaTeXCommand(r"\\hfill", 0),
                       LaTeXCommands.LaTeXCommand(r"\\medskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\bigskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\smallskip", 0),
                       LaTeXCommands.LaTeXCommand(r"\\setlength", 0),
                       LaTeXCommands.LaTeXCommand(r"\\Large", 0),
                       LaTeXCommands.LaTeXCommand(r"\\decofourleft", 0),
                       LaTeXCommands.LaTeXCommand(r"\\decofourright", 0),
                       ]
# Commandes de mise en page ou de glue avec un argument à supprimer
listeCommandesLayout = [LaTeXCommands.LaTeXCommand("\\thispagestyle", 1),
                        LaTeXCommands.LaTeXCommand("\\rhead", 1),
                        LaTeXCommands.LaTeXCommand("\\lhead", 1),
                        LaTeXCommands.LaTeXCommand("\\lfoot", 1),
                        LaTeXCommands.LaTeXCommand("\\rfoot", 1),
                        LaTeXCommands.LaTeXCommand("\\parindent", 1),
                        LaTeXCommands.LaTeXCommand("\\pagestyle", 1),
                        LaTeXCommands.LaTeXCommand("\\hspace", 1),
                        LaTeXCommands.LaTeXCommand("\\vspace", 1),
                        ]

# Remplacement de commandes avec un ou plusieurs arguments
listeReplace = [[LaTeXCommands.LaTeXCommand("\\textbf", 1), ["<strong>", 1, "</strong>"]],
                [LaTeXCommands.LaTeXCommand("\\emph", 1), [
                    "<em>", 1, "</em>"]],
                    [LaTeXCommands.LaTeXCommand("\\rm", 1), [
                    1]],
                    [LaTeXCommands.LaTeXCommand("\\np", 1), [
                    1]],
                ]
#Remplacement de commandes avec aucun argument ou commandes math.
listeReplaceSimple = [[LaTeXCommands.LaTeXCommand(r"\\Ouv", 0), r"(O; $\\vec{u}$, $\\vec{v}$)"],
[LaTeXCommands.LaTeXCommand(r"\\Oijk", 0), r"(O; $\\vec{i}$, $\\vec{j}$, $\\vec{k}$)"],
[LaTeXCommands.LaTeXCommand(r"\\degres",0), " &deg "],
[LaTeXCommands.LaTeXCommand(r"\\vect",0), r"\\vec"],

]