# This is my final project on house prices in Ireland from the years 2017, and 2019
import sql_connectors as con
import matplotlib.pyplot as plt
import pandas as pd
import requests
from pandas import read_csv
import numpy as np
from sqlalchemy import create_engine
import seaborn as sns

data_2017 = pd.read_csv('./content/PPR-2017-Dublin1.csv'
                        , header=0
                        , usecols=["Date of Sale (dd/mm/yyyy)", "Postal Code", "Price Euro"])
data_2019 = pd.read_csv('./content/PPR-2019-Dublin1.csv'
                        , header=0
                        , usecols=["Date of Sale (dd/mm/yyyy)", "Postal Code", "Price Euro"])

#print(type(data_2017))
#print(type(data_2019))
#print(data_2019, data_2017)
print(data_2019)
print(data_2017)
data_2017.replace(to_replace = np.nan, value = 'Dublin 36')
print(data_2017)

import sqlite3 as sqlite
import sql as sql
import sqlalchemy as sqla
import _sqlite3 as sqlite3
engine_1 = create_engine('sqlite:///PPR-2017-Dublin.csv')
engine_2 = create_engine('sqlite:///PPR-2019-Dublin.csv')
con_1 = engine_1.connect
con_2 = engine_2.connect































