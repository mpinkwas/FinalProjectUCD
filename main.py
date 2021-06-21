# This is my final project on the number of vaccinations per country by vaccine manufacturers.
import certifi
import jupyterlab as jupyterlab
import seaborn
import sql_connectors as con
import pandas as pd
import requests
from pandas import read_csv
import numpy as np
from pip._internal.operations import install
from sqlalchemy import create_engine, engine, false
import seaborn as sns
import csv
import pip
# importing CSV dataset (downloaded from kaggle)
df = pd.read_csv('./content/country_vaccinations_by_manufacturer.csv')
print(df)

# Finding mean and median of total vaccinations in whole data set
mean = np.mean(df['total_vaccinations'])
print(mean)
median = np.median(df['total_vaccinations'])
print(median)

# Checking for NaN in df -- none found
check_for_nan = df.isnull().values.any()
print(check_for_nan)

# Checking for duplicates -- none found
check_for_dup = df.duplicated().values.any()
print(check_for_dup)

# List of Ireland and USA
Ireland = (df[3552:3633])
print(Ireland)
USA = (df[6679:7084])
print(USA)

# Iloc of Ireland and USA
print(df.iloc[3552:3633, 2:3])
print(df.iloc[6679:7084, 2:3])

# Focusing in on Ireland's and United State's vaccinations
df_irealnd = np.array(df[3552:3633])
print(df_irealnd)
df_usa = np.array(df[6679:7084])
print(df_usa)

import requests
import json

# Ireland covid cases 2019-2020 to API
payload = {'code': 'IE'}
URL = 'https://api.statworx.com/covid'
response = requests.post(url=URL, data=json.dumps(payload))

# Convert to data frame
df_api = pd.DataFrame.from_dict(json.loads(response.text))
print(df_api)


import seaborn as sns
import jupyterlab as jpl
import ssl
import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots()
plt.show()
sns.set_theme(style="whitegrid")

covid_vaccinations = sns.load_dataset("country_by_vaccinations_by_manufacturer")

# Draw a vaccination barplot by manufaturer and total numbers vaccinated
g = sns.catplot(
    data='', kind="bar",
    x="vaccine", y="total_vaccinations", hue="Ireland, United States",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Total numbers Vaccinated", "Vaccine Developer")
g.legend.set_title("USA vs Ireland Vaccination")
ssl._create_default_https_context = ssl._create_unverified_context
tips = sns.load_dataset("tips")




