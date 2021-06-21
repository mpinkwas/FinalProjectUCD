# This is my final project on the number of vaccinations per country by vaccine manufacturers.
import sql_connectors as con
import matplotlib.pyplot as plt
import pandas as pd
import requests
from pandas import read_csv
import numpy as np
from sqlalchemy import create_engine
import seaborn as sns
import csv


#importing CSV dataset (downloaded from kaggle)
df = pd.read_csv('./content/country_vaccinations_by_manufacturer.csv')
print(df)

#Finding mean and median of total vaccinations in whole data set
mean = np.mean(df['total_vaccinations'])
print(mean)
median = np.median(df['total_vaccinations'])
print(median)

#Checking for NaN in df -- none found
check_for_nan = df.isnull().values.any()
print (check_for_nan)

#Checking for duplicates -- none found
check_for_dup = df.duplicated().values.any()
print(check_for_dup)

# Focusing in on Ireland's vaccinations
df_irealnd = np.array(df[3552:3633])
print(df_irealnd)


































