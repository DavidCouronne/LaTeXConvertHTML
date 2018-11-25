#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#Auteur: David Couronné
#Convertion automatique de LaTeX en HTML

from latexconverthtml import LaTeX
from latexconverthtml import setup
import re

test = LaTeX.Source(r"""On admet que $f$ vérifie la relation suivante : $f'(t) + \dfrac{1}{5}f(t) = 4$.
\medskip

\begin{enumerate}
\item Déterminer les valeurs de $a$ et $b$ sachant qu'initialement, la température du four est de
$\np{1000}$~\degres C, c'est-à-dire que $f(0) = \np{1000}$.
\item  Pour la suite, on admet que, pour tout nombre réel positif $t$: 

\[f(t) = 980\text{e}^{- \frac{t}{5}} + 20.\]

\medskip

	\begin{enumerate}
		\item Déterminer la limite de $f$ lorsque $t$ tend vers $+ \infty$.
		\item Étudier les variations de $f$ sur $[0~;~+ \infty[$. 
		
En déduire son tableau de variations complet.
		\item Avec ce modèle, après combien de minutes le four peut-il être ouvert sans risque pour
 les céramiques ?
 	\end{enumerate}
\item  La température moyenne (en degré Celsius) du four entre deux instants $t_1$ et $t_2$ est donnée
par: $\dfrac{1}{t_2 - t_1}\displaystyle\int_{t_1}^{t_2} f(t)\:\text{d}t$.

	\begin{enumerate}
		\item À l'aide de la représentation graphique de $f$ ci-dessous, donner une estimation de la
température moyenne $\theta$ du four sur les $15$ premières heures de refroidissement.
		
Expliquer votre démarche.
		
\begin{center}
\psset{xunit=0.6cm,yunit=0.01cm}
\begin{pspicture}(-1,-50)(19,1100)
\multido{\n=0+1}{20}{\psline[linestyle=dashed,linewidth=0.5pt](\n,0)(\n,1100)}
\multido{\n=0+100}{11}{\psline[linestyle=dashed,linewidth=0.5pt](0,\n)(19,\n)}
\psaxes[linewidth=1.25pt,Dy=200]{->}(0,0)(0,0)(19,1100)
\psaxes[linewidth=1.25pt,Dy=200](0,0)(0,0)(19,1100)
\uput[d](16.4,-40){temps écoulé (en heure)}
\uput[r](0,1080){température (en \degres C)}
\psplot[plotpoints=3000,linewidth=1.25pt,linecolor=blue]{0}{19}{980 2.71828 0.2 x mul exp div 20 add}
\end{pspicture}
\end{center}
\medskip

		\item  Calculer la valeur exacte de cette température moyenne $\theta$ et en donner la valeur
arrondie au degré Celsius.
	\end{enumerate}
\item  Dans cette question, on s'intéresse à l'abaissement de température (en degré Celsius) du
four au cours d'une heure, soit entre deux instants $t$ et $(t + 1)$. Cet abaissement est donné
par la fonction $d$ définie, pour tout nombre réel $t$ positif, par : $d(t) = f(t) - f(t + 1)$.
	\begin{enumerate}
		\item Vérifier que. pour tout nombre réel $t$ positif: $d(t) = 980\left(1 - \text{e}^{- \frac{1}{5}}\right)\text{e}^{- \frac{t}{5}}$.
		\item Déterminer la limite de $d(t)$ lorsque $t$ tend vers $+ \infty$.
		
Quelle interprétation peut-on en donner ?
 	\end{enumerate}
\end{enumerate}

\newpage
\vspace{2cm}
\textbf{\textsc{Exercice 2} \hfill 4 points}""")


test.cleanSpace()
test.convertEnumerate()
test.collapseLines()


for command in setup.listeCommandesClean:
    test.contenu = re.sub(command.regex, "", test.contenu)

print(test.contenu)
