# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:33:11 2021

@author: nidac
"""

liste = [[1,2,3],[4,5,6],[7,8,9]]
myFlatten = [num for sublist in liste for num in sublist]
print(myFlatten)