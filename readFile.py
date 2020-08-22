# -*- coding: utf-8 -*-
"""
Proyect Macrov
"""
#Main librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Load file data
data = pd.read_excel("MACRO.xlsx", shet_name=0)
data.head()
data.info()

#datat type correction

data['precio']=data['Precio Unitario'].astype('category')
data.info()

#Numeric values description
print(data.describe());

#Prices hist, from the lesser value to the mean value
a=plt.hist(data['precio'],bins=100,range=[1200,735479],align='left',rwidth=0.1)