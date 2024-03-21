#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:36:26 2024

@author: westonlarhette
"""
"""Plot the functions of e^x and x^3.6 over the range 2<=x<=7. Add legends. Then
make a semilog plot of the two functions. Finally make a log log plot of both"""
import numpy as np
x_values = np.linspace(2,7,500)

f1 = np.exp(x_values);
f2 = x_values**3.6;

# Import Matplotlib
import matplotlib.pyplot as plt

#Create linear plot
plt.subplot(1,3,1)
plt.plot(x_values,f1,label='$e^x$')
plt.plot(x_values,f2, label = '$x^{3.6}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Plot')
plt.legend()

# Create semilog plot
plt.subplot(1,3,2)
plt.semilogy(x_values,f1, label = 'Linearized $e^x$')
plt.semilogy(x_values,f2, label = 'Linearized $x^{3.6}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Semilog Plot')
plt.legend(fontsize = '8',loc='upper left')

# Create loglog plot
plt.subplot(1,3,3)
plt.loglog(x_values,f1, label = 'Loglog $e^x$')
plt.loglog(x_values,f2, label = 'Loglog $x^{3.6}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Loglog plot')
plt.legend(fontsize = '8', loc = 'upper left')

# Adjust layout and show plots
plt.tight_layout()
plt.show()

""" End of program"""