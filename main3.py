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

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
print("İlk hali:\n", yas)

# Tüm yas verisine uygula çünkü zaten 1:4 sütunları seçilmişti
imputer = imputer.fit(yas)
yas = imputer.transform(yas)
print("Eksik veriler doldurulduktan sonra:\n", yas)


ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print(ulke)

ohe= preprocessing.OneHotEncoder()

ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

sonuc = pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us' ])
print(sonuc)

sonuc2 = pd.DataFrame(data=yas, index=range(22), columns= ['boy', 'kilo', 'yas '])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data= cinsiyet, index=range(22), columns = ['cinsiyet'])
print(sonuc3)

#data frame birlestirmek icin 
s=pd.concat([sonuc,sonuc2], axis= 1)

print(s)

s2 = pd.concat([s,sonuc3], axis=1)


from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test= sc.fit_transform(x_test)
































