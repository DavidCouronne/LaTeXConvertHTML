#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# Auteur: David Couronné
# Convertion automatique de LaTeX en HTML

import re

from latexconverthtml import LaTeXCommands, setup


class Source:
    def __init__(self, original=""):
        self.original = original  # On garde l'original pour développement
        self.contenu = original
        self.lines = self.contenu.splitlines()
        

    def collapseLines(self):
        """Recolle les lignes dans self.contenu"""
        self.contenu = "\n".join(self.lines)

    def cleanSpace(self):
        """Agit sur les lignes.
        Enlève les espaces en début et fin de chaque ligne"""
        new_lines = []
        for line in self.lines:
            line = line.strip()
            new_lines.append(line)
        self.lines = new_lines

    def cleanCommand(self):
        """Agit sur le contenu.
        Suprrime toutes les commandes du fichier setup.py"""
        for command in setup.listeCommandesClean:
            self.contenu = re.sub(command.regex, "", self.contenu)
            self.lines = self.contenu.splitlines()

    def convertEnumerate(self):
        """Agit sur les lignes.
        Converti les environnements enumerate en listes html"""
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

    def findPstricks(self):
        """Agit sur les lignes.
        Essaie de trouver les envir
        onnements Pstricks"""
        in_pstricks = False
        lignes_pstricks = []
        pstricks = []
        for line in self.lines:
            if in_pstricks:
                lignes_pstricks.append(line)
                if r"\end{pspicture}" in line:
                    in_pstricks = False
                    pstricks.append("\n".join(lignes_pstricks))
                    lignes_pstricks = []
            else:
                if r"\psset" in line or r"\begin{pspicture}" in line:
                    in_pstricks = True
                    lignes_pstricks.append(line)
        self.pstricks = pstricks
