# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:05:26 2019

@author: d805664
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

n, c, r, i, p = sp.symbols('n c r i p')

p = c/n + c*(1 - i/n)*r

print("Fórmula para o Cálculo da Parcela no sistema SAC:\n")
sp.pprint(p)

dpdn = sp.diff(p,n)

print("Primeira derivada da parcela em função do prazo (número de parcelas):\n")
sp.pprint(dpdn)


# Cria a função vetorial para apresentação em gráfico.
y0 = sp.lambdify([n], 100*dpdn.subs([(c, 1250),(i, 1), (r, 0.0985)])/p.subs([(c, 1250),(i, 1), (r, 0.0985)]), 'numpy')

ns = np.linspace(12,361, 361-12)

y0 = y0(ns)


plt.style.use("ggplot")
plt.plot(ns,y0)
plt.title("Variação percentual do valor da parcela em função do prazo do financiamento.")
plt.axis([0,400,-4,1])