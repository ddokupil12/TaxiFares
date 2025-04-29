import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import preprocess

# load first 500k entries of dataset
df = pd.read_csv('train.csv', parse_dates=['pickup_datetime'], nrows=500000)

# print the first 5 rows of the dataset
# ** YOUR CODE HERE **



# display histogram for fares and passenger count
# ** YOUR CODE HERE **




# statistical summary of dataset
# ** YOUR CODE HERE **




# print the number of missing values for each variable
# ** YOUR CODE HERE **