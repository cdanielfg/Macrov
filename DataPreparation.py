# -*- coding: utf-8 -*-
"""
Macrov Project

data preparation
"""

#Main librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load file data
data = pd.read_excel("MACRO.xlsx", shet_name=0)

data=data.fillna(0)
budget=0
listProducts = ['1.1.1','2.2.2','2.2.3']
quantity=[1,2,3]

dataFilter = data[data['No. Item'].isin(listProducts)]
prices=dataFilter['Precio Unitario'].tolist()

for i in range(len(quantity)):
    budget+=quantity[i]*prices[i]
    
print(budget)


    

