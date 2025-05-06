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
    df = pd.read_csv('train.csv', parse_dates=['pickup_datetime'], nrows=500000, encoding="utf-16")
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
training_set, testing_set = train_test_split(df,test_size=.33) #Not tested, check this link: https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html



# keras.layers.Dense( - Keras Dense Layer Format
#     units,
#     activation=None,
#     use_bias=True,
#     kernel_initializer="glorot_uniform",
#     bias_initializer="zeros",
#     kernel_regularizer=None,
#     bias_regularizer=None,
#     activity_regularizer=None,
#     kernel_constraint=None,
#     bias_constraint=None,
#     lora_rank=None,
#     **kwargs
# )
# Build neural network in Keras
model = Sequential(
  [
    Dense(2, activation="relu", name= "hlayer1"),
    Dense(3, activation="relu", name="hlayer2"),
    Dense(4, activation="relu", name="hlayer3"),
    Dense(5, name="output")
  ]
)
# ** YOUR CODE HERE **

model.summary()


#Basic idea of what we need
hLayer1 = Dense(15, "linear")



# Compile and Train the model
# ** YOUR CODE HERE **



# Evaluate the Model (RMSE)
# ** YOUR CODE HERE **