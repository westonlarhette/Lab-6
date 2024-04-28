#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:19:59 2024

@author: westonlarhette
"""

"""Create a pie chart showing the relative abundances of different elements in the universe"""
import numpy as np
import matplotlib.pyplot as plt

labels = ['Hydrogen', 'Helium', 'Oxygen', 'Carbon']
# sizes is given mass fraction (ppm) spectroscopically
sizes = [739000, 240000, 10400, 4600]

plt.pie(sizes, labels=labels)
plt.title('Abundancies of Elements in the Universe via pie chart')

plt.tight_layout()
plt.show()

