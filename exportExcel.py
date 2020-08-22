# -*- coding: utf-8 -*-
"""
Macrov Project

Export to excel function
"""
import pandas as pd
import numpy as np

data = {'No. Item': np.random.randint(1,100,size=100).tolist(),
        'Analisis de precios unitarios': ['Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación',
                                          'Retiro','Localización','Rocería','Desmonte','Instalación'],
        'Unidad': ['Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3',
                   'm','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día',
                   'm2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3',
                   'm','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un',
                   'Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un','Día','m2',
                   'm3','m','un','Día','m2','m3','m','un','Día','m2','m3','m','un'],
        'Importe de materiales': np.random.randint(100,100000,size=100).tolist(),
        'Importe de mano de obra': np.random.randint(100,100000,size=100).tolist(),
        'Importe de equipo': np.random.randint(100,100000,size=100).tolist(),
        'Importe de auxiliares': np.random.randint(100,100000,size=100).tolist(),
        'Importe de conceptos': np.random.randint(100,100000,size=100).tolist(),
        'Precio unitario': np.random.randint(10000,900000,size=100).tolist()}
dataframe = pd.DataFrame(data, columns = ['No. Item', 'Analisis de precios unitarios', 'Unidad',
                                          'Importe de materiales', 'Importe de mano de obra',
                                          'Importe de equipo','Importe de auxiliares','Importe de conceptos',
                                          'Precio unitario'])
dataframe.to_excel('MacrovExported.xlsx',sheet_name='Presupuesto')