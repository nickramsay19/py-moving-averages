'''
    gen.py
    Created by Nicholas Ramsay

    This file generates a data.csv file with random values following a normal distribution.
'''

import random
import math

# Create a normal distribution function, both variable mean & std.dev and desired hardcoded values
nd_ms = lambda x, m, s : math.e**(-((x - m)**2)/2*(s**2)) / s * math.sqrt(2 * math.pi)
nd = lambda x : nd_ms(x, 0, 0.05)

with open('data.csv', 'w+') as file:
    
    items = [ 
                (
                    str(x) + ', ' + 
                    str(
                        math.floor(1000*nd(x))/1000 
                        + random.randint(1, 1000) / 200 # add "jitter"
                    ) + '\n'
                ) 
                for x in range(-100, 100) 
    ]

    file.writelines(items)

'''
Alternative
import numpy as np

m, s = 0, 0.05

n = np.random.normal(m, s, 200)

# then sort this list
'''