#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:50:22 2024

@author: westonlarhette
"""

"""Objective: Create a bar chart showing the kinetic energy
of different objects with varying masses and constanty velocity"""
import numpy as np
import matplotlib.pyplot as plt

# Define NumPy array for masses of the objects in kg:
masses = np.array([3,5,7,2,8,15]);

# Assume constant velocity for all objects:
v = 10; # m/s

# Calculate kinetic energy
kinetic_energy = 0.5 * masses * v**2;

# Create bar chart
categories = ['Object 1', 'Object 2', 'Object 3', 'Object 4', 'Object 5', 'Object 6'];
plt.bar(categories,kinetic_energy)
plt.xlabel('Objects of varying mass');
plt.ylabel('Kinetic Energy (Joules)')
plt.title('Kinetic Energy for objects of varying mass at constant velocity')
plt.show()


