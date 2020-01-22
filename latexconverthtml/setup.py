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
                       LaTeXCommands.LaTeXCommand(r"\\large", 0),
                       LaTeXCommands.LaTeXCommand(r"\\decofourleft", 0),
                       LaTeXCommands.LaTeXCommand(r"\\decofourright", 0),
                       ]
# Commandes de mise en page ou de glue avec un argument à supprimer
listeCommandesLayout = [LaTeXCommands.LaTeXCommand(r"\\thispagestyle", 1),
                        LaTeXCommands.LaTeXCommand(r"\\rhead", 1),
                        LaTeXCommands.LaTeXCommand(r"\\lhead", 1),
                        LaTeXCommands.LaTeXCommand(r"\\lfoot", 1),
                        LaTeXCommands.LaTeXCommand(r"\\rfoot", 1),
                        LaTeXCommands.LaTeXCommand(r"\\parindent", 1),
                        LaTeXCommands.LaTeXCommand(r"\\pagestyle", 1),
                        LaTeXCommands.LaTeXCommand(r"\\hspace", 1),
                        LaTeXCommands.LaTeXCommand(r"\\vspace", 1),
                        ]

# Remplacement de commandes avec un ou plusieurs arguments
listeReplace = [[LaTeXCommands.LaTeXCommand(r"\\textbf", 1), ["<strong>", 1, "</strong>"]],
                [LaTeXCommands.LaTeXCommand(r"\\emph", 1),
                 ["<em>", 1, "</em>"]
                 ],
                [LaTeXCommands.LaTeXCommand(r"\\rm", 1), [
                    1]],
                [LaTeXCommands.LaTeXCommand(r"\\np", 1), [
                    1]],
                [LaTeXCommands.LaTeXCommand(r"\\textsc", 1), [
                    1]],
                ]
# Remplacement de commandes avec aucun argument ou commandes math.
listeReplaceSimple = [[LaTeXCommands.LaTeXCommand(r"\\Ouv", 0), r"(O; $\\vec{u}$, $\\vec{v}$)"],
                      [LaTeXCommands.LaTeXCommand(
                          r"\\Oijk", 0), r"(O; $\\vec{i}$, $\\vec{j}$, $\\vec{k}$)"],
                      [LaTeXCommands.LaTeXCommand(r"\\degres", 0), " &deg "],
                      [LaTeXCommands.LaTeXCommand(r"\\vect", 0), r"\\vec"],
                      [LaTeXCommands.LaTeXCommand(r"\\og", 0), " &laquo "],
                      [LaTeXCommands.LaTeXCommand(r"\\fg", 0), " &raquo "],

                      ]

# Remplacement sans regex
listeReplaceText = [["\\,\\%", "  &#37 "],
                    ["\n\n", "<br>\n\n"],
                    ["\\begin{center}", """<div class="text-center">\n"""],
                    ["\\end{center}", "</div>\n"],
                    ["~", ""],
                    ["\\begin{flushleft}", ""],
                    ["\\end{flushleft}", ""]

                    ]
