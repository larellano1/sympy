# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:42:22 2019

@author: d805664
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

plt.ion()
 
## This code refreshs the hole plot every time.
x = []
y = []
y2 = []
for x_ in np.linspace(0,4*np.pi,100):
    y_ = np.sin(x_)
    y2_ = np.sin(x_+np.pi/4)
    x.append(x_)
    y.append(y_)
    y2.append(y2_)    
    plt.plot(x,y, linewidth = 1.5, color='r')   
    plt.plot(x,y2, linewidth = 1.5, color='b')
    plt.title("Animated Plot")
    plt.legend(["Sin(x)", "Sin(x+pi/4)"])    
    plt.axis([0,4*np.pi,-1,1])
    plt.draw()
    plt.show()
    plt.pause(0.01)
    plt.clf()
    
