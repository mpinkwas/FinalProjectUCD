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

df = pd.read_csv('./content/country_vaccinations_by_manufacturer.csv')
print(df)
mean = np.mean(df['total_vaccinations'])
print(mean)
median = np.median(df['total_vaccinations'])
print(median)































