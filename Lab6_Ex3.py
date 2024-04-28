#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:04:12 2024

@author: westonlarhette
"""

"""Objective: Create a histogram showing the distribution
of thermal energy in a system at different temperatures"""
import numpy as np
import matplotlib.pyplot as plt

# Define constants:
k = 1.380649e-23; # Boltzmann Constant

# Create temperature array
temps = np.array([20, 20, 20, 25, 30, 30, 35, 40, 40, 40]);

# Calculate thermal energy
U = k*temps
U = U*(6.242*10**21)

# Creating a histogram

plt.hist(U,bins=8)
plt.xlabel('Thermal Energy (milli-eV)')
plt.ylabel('Frequency of Energy State')
plt.title('Histogram of System Thermal Energy at varying temperatures')

plt.tight_layout()
plt.show()