import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import preprocess


# load first 500k entries of dataset
df = pd.read_csv('train.csv', parse_dates=[2], nrows=500000, encoding='utf-16')


print(df)


# print the first 5 rows of the dataset
# ** YOUR CODE HERE **

print(df.head())

# display histogram for fares and passenger count
# ** YOUR CODE HERE **

x = df.hist(column='passenger_count')
plt.show()

# statistical summary of dataset
# ** YOUR CODE HERE **

df.describe()

print(df.describe())

# print the number of missing values for each variable
# ** YOUR CODE HERE **
for col in df.columns:
    n_nan = df[col].isna().sum()
    n_zero = df[col].eq(0).sum() if pd.api.types.is_numeric_dtype(df[col]) else "N/A"
    print(f"{col}: NaN={n_nan}, Zero={n_zero}")

for col in df.columns:
    n_nan = df[col].isna().sum()
    n_zero = df[col].eq(0).sum() if pd.api.types.is_numeric_dtype(df[col]) else "N/A"
    print(f"{col}: NaN={n_nan}, Zero={n_zero}")


