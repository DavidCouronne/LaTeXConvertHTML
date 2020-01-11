import os
import codecs

source = r"""\begin{pspicture}(-4,-4)(4,4)
\psgrid[gridlabels=0pt,subgriddiv=1,gridwidth=0.1pt]
\psaxes[linewidth=1pt,Dx=10,Dy=10](0,0)(-4,-4)(4,4)
\psaxes[linewidth=1.5pt,Dx=10,Dy=10]{->}(0,0)(1,1)
\uput[d](0.5,0){$\vec{u}$}\uput[l](0,0.5){$\vec{v}$}\uput[dl](0,0){O}
\uput[dr](2,0){B} \uput[dr](4,0){C}\uput[dl](-4,0){A}
\pscircle(0,0){2}\pscircle(0,0){3}\pscircle(0,0){4}
\psdots(-4,0)(2,0)(4,0)
\end{pspicture}
"""

preamble = r"""\documentclass{standalone}
\usepackage{pst-plot,pst-tree,pstricks,pst-node,pst-text}
\usepackage{pst-eucl}
\usepackage{pstricks-add}
\begin{document}

"""


rep = r"""C:\Users\couro\OneDrive\Documents\GitHub\LaTeXConvertHTML"""

name = r"test.tex"
total = preamble + source + r"\end{document}"
os.chdir(rep)
f = codecs.open(name, "w", "utf-8")
f.write(total)
f.close()

replatex = r"""C:\Program Files\MiKTeX 2.9\miktex\bin\x64\latex.exe"""

# os.system("latex " + name)
os.system("latex test.tex")
os.system("dvisvgm test")
os.rename("test.svg", "fig1.svg")
