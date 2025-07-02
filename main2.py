#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 16:36:27 2025

@author: erberk_uylas
"""

#kutuphanler
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#veri yukleme 

veriler = pd.read_csv("eksikveriler.csv")
print(veriler)

#veri onisleme
boy = veriler[['boy']]
print(boy)
print("")
boykilo = veriler[['boy','kilo']]
print(boykilo)
print("")

class insan:
    boy =180
    def kosmak(self,b):
        return b+ 10 

ali = insan()
print(ali.boy)
print("")
print(ali.kosmak(90))

l = [1,3,4] #ornek liste 

#eksik veriler

from sklearn.impute import SimpleImputer

imputer =SimpleImputer(missing_values=np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
print(yas)

imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas)[:,1:4]
print(yas)
