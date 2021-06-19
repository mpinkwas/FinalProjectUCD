# This is my final project on house prices in Ireland from the years 2017, 2018 and 2019
import matplotlib.pyplot as plt
import pandas as pd
import requests
from pandas import read_csv
import numpy as np

data_2017 = pd.read_csv('./content/PPR-2017-Dublin.csv'
                        , header=0
                        , usecols=["Date of Sale (dd/mm/yyyy)", "Postal Code", "Price (�)"])
data_2018 = pd.read_csv('./content/PPR-2018-Dublin.csv'
                        , header=0
                        , usecols=["Date of Sale (dd/mm/yyyy)", "Postal Code", "Price (�)"])
data_2019 = pd.read_csv('./content/PPR-2019-Dublin.csv'
                        , header=0
                        , usecols=["Date of Sale (dd/mm/yyyy)", "Postal Code", "Price (�)"])

#print(type(data_2017))
#print(type(data_2018))
#print(type(data_2019))
#print(data_2019, data_2018, data_2017)
print(data_2019)
print(data_2018)
print(data_2017)































