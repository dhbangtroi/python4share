#!/usr/bin/env python
# coding: utf-8

# Write the function remove_pins that updates the remaining pins in a bowling alley after one throw.  Normally ten pins are grouped together in a reversed triangle, however to make it easier all pins are placed next to each other, so a row of 10 pins.
# 
# 
# The function uses two characters to represent the pins still standing 'I' and the ones that are already knocked down '.' 
# It receives two integers that represent the start to stop positions of the pins that were knocked down during one turn (include the start ánd the stop) and it receives a name of a file that contains characters that act as pins "IIIIIIIIII". The start and stop position combined are the range of pins that are knocked down.
# The function returns a string with the pins still standing ‘I’ and with the ones that rolled over ‘.’ (do not include any spaces).
# 
# Example
# 
# file = open('text.txt','w')
# file.write("IIIIIIIIII")
# file.close()
# 
# print(remove_pins(1,4,'text.txt'))
# returns "I....IIIII"

# In[12]:


def remove_pins(start,stop,file):
    fp = open(file)
    buffer = fp.readline()
    fp.close()
    pins = list(buffer)
    #print(pins)
    for i in range(start,stop+1):
        pins[i] = '.'
    pins = ''.join(pins)
    return pins
#remove_pins(1,4,'pins.txt')
#remove_pins(2,8,'pins.txt')
#remove_pins(0,0,'pins.txt')
#remove_pins(1,1,'pins.txt')


# In[1]:


#import pandas as pd
#object = pd.read_pickle('testcases.p')
#object

