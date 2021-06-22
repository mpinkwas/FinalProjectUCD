# This is my final project on the number of vaccinations per country by vaccine manufacturers.
import pandas as pd
import requests
import json
import seaborn as sns
import ssl
import matplotlib.pyplot as plt
import numpy as np
ssl._create_default_https_context = ssl._create_unverified_context

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

# looping through all data
for index, row in df.iterrows():
    print(index, ': ', row['location'], 'has', row['total_vaccinations'])

# List of Ireland and USA
Ireland = (df[3552:3633])
print(Ireland)
USA = (df[6679:7084])
print(USA)

# Merging Ireland and USA
result = pd.merge(Ireland,
                 USA[['vaccine', 'location', 'total_vaccinations']],
                 on='vaccine')
result.head()

# Iloc of Ireland and USA
print(df.iloc[3552:3633, 2:3])
print(df.iloc[6679:7084, 2:3])

# Focusing in on Ireland's and United State's vaccinations
df_ireland = np.array(df[3552:3633])
print(df_ireland)
df_usa = np.array(df[6679:7084])
print(df_usa)

# Ireland covid cases 2019-2020 to API
payload = {'code': 'IE'}
URL = 'https://api.statworx.com/covid'
response = requests.post(url=URL, data=json.dumps(payload))

# Convert to data frame
df_api = pd.DataFrame.from_dict(json.loads(response.text))
print(df_api)

#Bar graph added for Ireland data
fig,ax = plt.subplots()
sns.set_theme(style="whitegrid")

ax = sns.barplot(x="total_vaccinations", y="vaccine", data=Ireland)
plt.show()

#Bar graph added for USA data
fig,ax = plt.subplots()
sns.set_theme(style="whitegrid")

ax = sns.barplot(x="total_vaccinations", y="vaccine", data=USA)
plt.show()

