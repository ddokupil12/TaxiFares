import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import preprocess


# load first 500k entries of dataset
df = pd.read_csv('train.csv', parse_dates=[2], nrows=500000, encoding='latin1')

# print the first 5 rows of the dataset
# ** YOUR CODE HERE **

print(df.head(5))

# display histogram for fares and passenger count
# ** YOUR CODE HERE **



# statistical summary of dataset
# ** YOUR CODE HERE **




# print the number of missing values for each variable
# ** YOUR CODE HERE **