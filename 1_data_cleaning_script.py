#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 2021

Author: Cecile Glt-Slmcs

Data cleaning of the dataset "data_worldbank.csv"
This dataset is the base of a work about education access around the world
"""

# Importation
import pandas as pd
import numpy as np

# importation of the dataset
filepath = 'data_worldbank.csv'
df = pd.read_csv(filepath, encoding = 'utf-8')
df.head()

# suppression of a column
df.drop('série Code', axis = 1, inplace = True)

# rename the columns
cols = ['Pays', 'Code ISO', 'Indicateurs', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
df.columns = cols

# replacing '..' by NaN to falicitate pre-processing
df.replace('..', np.nan, inplace=True)

# changing the datatype
cols = ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
for i in cols:
    df[i] = df[i].astype('float')

# suppression of the last row
df.drop([13237, 13238, 13239, 13240, 13241], inplace=True)

# creating a column with mean of the last 10 years
df['Valeurs'] = df.mean(axis=1)

# selection of the columns needed
df = df[["Pays", "Code ISO", "Indicateurs", "Valeurs"]]

# modifying the dataset
df = pd.pivot_table(df, index=['Pays', 'Code ISO'], columns= "Indicateurs", values='Valeurs', aggfunc=np.mean).reset_index()
df.head()

# creating two files
df.to_csv('data_total.csv')
df.to_excel('data_total.xlsx')
