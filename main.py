import matplotlib
matplotlib.use("TkAgg")

print('more imports')
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
print('more imports')
from sklearn.metrics import mean_squared_error

from utils import preprocess, feature_engineer

try:
    print("Reading in the dataset.")
    df = pd.read_csv('train.csv', parse_dates=['pickup_datetime'], nrows=500000)
except:
    print("""
      Dataset not found in your computer.
      Please follow the instructions to download the dataset.
      """)
    quit()


# Perform preprocessing and feature engineering
df = preprocess(df)
df = feature_engineer(df)

# Scale the features
df_prescaled = df.copy()
df_scaled = df.drop(['fare_amount'], axis=1)
df_scaled = scale(df_scaled)
cols = df.columns.tolist()
cols.remove('fare_amount')
df_scaled = pd.DataFrame(df_scaled, columns=cols, index=df.index)
df_scaled = pd.concat([df_scaled, df['fare_amount']], axis=1)
df = df_scaled.copy()



# Split the dataframe into a training and testing set
# ** YOUR CODE HERE **



# Build neural network in Keras
model = Sequential()
# ** YOUR CODE HERE **



# Compile and Train the model
# ** YOUR CODE HERE **



# Evaluate the Model (RMSE)
# ** YOUR CODE HERE **