#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 22:30:31 2021

@author: cecile
"""

import pandas as pd
import numpy as np

filepath = 'data_worldbank.csv'

df = pd.read_csv(filepath, encoding = 'utf-8')
df.head()

df.drop('série Code', axis = 1, inplace = True)

cols = ['Pays', 'Code ISO', 'Indicateurs', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
df.columns = cols

df.replace('..', np.nan, inplace=True)

cols = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
for i in cols:
    df[i] = df[i].astype('float')

df.drop([13237, 13238, 13239, 13240, 13241], inplace=True)

df['Valeurs'] = df.mean(axis=1)

df = df[["Pays", "Code ISO", "Indicateurs", "Valeurs"]]

df = pd.pivot_table(df, index=['Pays', 'Code ISO'], columns= "Indicateurs", values='Valeurs', aggfunc=np.mean).reset_index()
df.head()

df.to_csv('data_total.csv')
df.to_excel('data_total.xlsx')
