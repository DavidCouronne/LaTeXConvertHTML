#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#Auteur: David Couronné
#Convertion automatique de LaTeX en HTML

import re


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


class LaTeXCommand:
    def __init__(self, nom, arg=1, optn=False):
        self.nom = nom
        self.arg = arg
        self.optn = optn
        if arg == 0:
            self.regex = re.compile(self.nom + r"\b")
        if arg == 1:
            self.regex = re.compile(self.nom + r"\{([\d|\w|\.|-]*)\}")

    def find(self, contenu):
        return contenu.find(self.nom)

    def findCommand(self, texte):
        index = texte.find(self.nom)
        avant = texte[:index]
        apres = texte[index+len(self.nom):]
        argOptn = ""
        listeArg = []
        if self.optn:
            if apres[0] == "[":
                i = 0
                while apres[i] != "]":
                    i = i + 1
                argOptn = apres[1:i]
                apres = apres[i+2:]
            else:
                apres = apres[1:]
        else:
            apres = apres[1:]
        argRest = self.arg
        avantManip = "{"+apres
        while argRest != 0:
            argRest = argRest - 1
            ouvert2 = apres.find("{")
            ferme1 = apres.find("}")
            if ouvert2 == -1:
                ouvert2 = ferme1
            while ouvert2 < ferme1:
                ouvert2 = apres.find("{", ferme1+1)
                ferme1 = apres.find("}", ferme1+1)
            listeArg.append(apres[:ferme1])
            apres = apres[ferme1+2:]
        longueurArgument = 0
        for argument in listeArg:
            longueurArgument = longueurArgument + len(argument)+2

        apres = avantManip[longueurArgument:]
        return index, avant, apres, argOptn, listeArg

    def cleanCommand(self, contenu):
        passe = 0
        while self.nom in contenu:
            passe = passe + 1
            index, avant, apres, argOptn, listeArg = self.findCommand(contenu)
            # print("Passe"+str(passe),apres)
            contenu = avant+apres
        return contenu

    def replaceCommand(self, contenu, listeReplace):
        while self.nom in contenu:
            index, avant, apres, argOptn, listeArg = self.findCommand(contenu)
            texte = ""
            for argument in listeReplace:
                if type(argument) is type("c"):
                    texte = texte + argument
                elif argument == 0:
                    texte = texte + "[" + argOptn + "]"
                else:
                    texte = texte + "{" + listeArg[argument-1] + "}"
            contenu = avant + texte + apres
        return contenu