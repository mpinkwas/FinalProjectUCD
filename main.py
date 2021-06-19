# This is my final project on the rising house prices in Ireland
from urllib import request

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pip as pip
import requests
data_all = pd.read_csv('./content/PPR-ALL.csv')
print(data_all.info)
data = requests.get("https://priceregister.civictech.ie/api/sales")















