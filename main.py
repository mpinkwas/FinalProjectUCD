# This is my final project on the rising house prices in Ireland
from urllib import request

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pip as pip
import requests
data_2017 = pd.read_csv('./content/PPR-2017-Dublin.csv')
data_2018 = pd.read_csv('./content/PPR-2018-Dublin.csv')
data_2019 = pd.read_csv('./content/PPR-2019-Dublin.csv')
data_all = data_2019, data_2018, data_2017
print(data_all)
data = requests.get("https://priceregister.civictech.ie/api/sales")















