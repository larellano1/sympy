# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

## Definição dos símbolos para álgebra computacional.
x, y, r1, a1, b1, r2, a2, b2 = sp.symbols('x y r1 a1 b1 r2 a2 b2')

# Definição da função vetorial que descreve o sistema dinâmico.
dx = r1*x - a1*x*x - b1*x*y
dy = r2*y - a2*y*y - b2*y*x

# Cálculo das derivadas parciais para criação da Matriz Jacobiana.
dxdx = sp.diff(dx,x)
dxdy = sp.diff(dx,y)
dydx = sp.diff(dy,x)
dydy = sp.diff(dy,y)

# Matriz Jacobiana
J = sp.Matrix([[dxdx, dxdy],[dydx, dydy]])


# Cálculo da Matriz Jacobiana M (x, y) para parâmetros específicos.
J = J.subs([(r1,10),(a1,0.025),(b1,0.3), (r2,15),(a2,0.015),(b2,0.3)])

# Estabelecimento do conjunto S (x, y) sobre o qual a função operará.
xs = np.linspace(0,50,15)
ys = np.linspace(0,50,15)

# Criação da função vetorial F(x,y) que calcula o Jacobiano num ponto específico e multiplica pelo vetor deslocamento naquele ponto.
# Trata-se da ideia da utilização da aproximação linear para estimar as variações em cada ponto.
field = sp.lambdify([x,y], J.dot([.0001,.0001]), 'numpy')

# Função que combina os diversos valores de x com os de y, para estabelecer os diversos pontos em que a função será avaliada.
u, v = np.meshgrid(xs,ys)

# Avaliação da função nos diversos pontos.
res = field(u, v)

# Função para plotar o campo vetorial.
plt.quiver(xs, ys, res[0], res[1], color = "b")
plt.savefig("graph1.pdf", format = "pdf")
plt.show()