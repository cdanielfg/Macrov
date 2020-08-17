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
presupuesto=0
lista = ['1.1.1','2.2.2','2.2.3']
cantidad=[1,2,3]

filtro = data[data['No. Item'].isin(lista)]
precios=filtro['Precio Unitario'].tolist()

for i in range(len(cantidad)):
    presupuesto+=cantidad[i]*precios[i]
    
print(presupuesto)


    

