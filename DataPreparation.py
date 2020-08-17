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
