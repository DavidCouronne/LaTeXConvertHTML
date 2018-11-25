#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#Auteur: David Couronné
#Convertion automatique de LaTeX en HTML

class Source:
    def __init__(self, original=""):
        self.original = original #On garde l'original pour développement
        self.contenu = original
        self.lines = self.contenu.splitlines()

    def collapseLines(self):
        """Recolle les lignes dans self.contenu"""
        self.contenu = "\n".join(self.lines)

    def cleanSpace(self):
        """Enlève les espaces en début et fin de chaque ligne"""
        new_lines = []
        for line in self.lines:
            line = line.strip()
            new_lines.append(line)
        self.lines = new_lines

    def convertEnumerate(self):
        """Converti les environnements enumerate en listes html"""
        level_enumerate = 0
        level_item = 0
        new_lines = []

        for line in self.lines:
            if r"\begin{enumerate}" in line:
                level_enumerate = level_enumerate + 1
                if level_enumerate == 2:
                    line = r"""<ol type ="a" >"""
                else:
                    line = r"""<ol >"""
            elif r"\end{enumerate}" in line:
                level_enumerate = level_enumerate - 1
                line = r"""</li></ol>"""
            elif r"\item" in line:
                if level_item == 0:
                    line = line.replace(r"\item", "<li>")
                    level_item = level_item + 1
                else:
                    line = line.replace(r"\item", "</li><li>")
                    level_item = level_item - 1
            new_lines.append(line)
        self.lines = new_lines
