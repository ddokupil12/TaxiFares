import matplotlib
matplotlib.use("TkAgg")

print('more imports')
from keras.models import Sequential
from keras.layers import Dense
from keras import Model
from keras.optimizers import Adam
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
print('more imports')
from sklearn.metrics import mean_squared_error
from utils import preprocess, feature_engineer

import sys
from argparse import ArgumentParser

print(sys.argv)
# epoch (1, 20)
# Layer density (list of integers)
# Test size (0, 1)

parser = ArgumentParser()
parser.add_argument("-e", help="number of epochs")
parser.add_argument("-t", help="Test size (int between 0 and 1 exclusive)")
parser.add_argument("-h1", help="Defaults to len(df.columns)")
parser.add_argument("-h2", help="Defaults to 128")
parser.add_argument("-h3", help="Defaults to 72")
parser.add_argument("-h4", help="Defaults to 16")
parser.add_argument("-lr", help="Learning rate")

args = parser.parse_args()

try:
    print("Reading in the dataset.")
    df = pd.read_csv('train.csv', parse_dates=['pickup_datetime'], nrows=500000, encoding="utf-16")
except:
    print("""
      Dataset not found in your computer.
      Please follow the instructions to download the dataset.
      """)
    quit()


# print('pickup_datetime', df.pickup_datetime)

# Perform preprocessing and feature engineering
# print('df types', df.dtypes)
df = preprocess(df)
# print('preprocess', df)
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

numEpochs = int(args.e) if args.e else 10
testSize = float(args.t) if args.t else .33
h1units = int(args.h1) if args.h1 else len(df.columns)
h2units = int(args.h2) if args.h2 else 128
h3units = int(args.h3) if args.h3 else 72
h4units = int(args.h4) if args.h4 else 16
lr = int(args.lr) if args.lr else None

print("Epochs:", numEpochs)
print("test size:", testSize)
print("h1", h1units)
print("h2", h2units)
print("h3", h3units)
print("h4", h4units)
print("lr", lr)



# Split the dataframe into a training and testing set
# ** YOUR CODE HERE **
training_set, testing_set = train_test_split(df,test_size=testSize) #Not tested, check this link: https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html



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
    Dense(h1units, activation="relu", name= "hlayer1"),
    Dense(h2units, activation="relu", name="hlayer2"),
    Dense(h3units, activation="relu", name="hlayer3"),
    Dense(h4units, activation="relu", name="hlayer4"),
    Dense(1, name="output")
  ]
)
# ** YOUR CODE HERE **

model.summary()

optim = Adam(learning_rate=lr) if lr else Adam()


# Compile and Train the model
# ** YOUR CODE HERE **

# 1) Use Keras' compile method
model.compile(optimizer="Adam", loss="mean_squared_error", metrics=["root_mean_squared_error"])

# 2) Use Keras' fit method to train the model
input_ = training_set.drop(columns='fare_amount')
labels = training_set['fare_amount']
model.fit(epochs=numEpochs, x=input_, y=labels)

# 3) Calculate loss using MSE

# Evaluate the Model (RMSE)
# ** YOUR CODE HERE **
# Testing
# Evaluate the Model (RMSE)

# Use the testing set to make predictions
test_input = testing_set.drop(columns='fare_amount')  # Features from the testing set
test_labels = testing_set['fare_amount']  # True fare amounts for comparison

# Predict fares using the trained model
predicted_fares = model.predict(test_input)

# Evaluate the model's performance on the testing set
mse_test = mean_squared_error(test_labels, predicted_fares)
rmse_test = np.sqrt(mse_test)

print(f"Mean Squared Error (MSE) on Testing Set: {mse_test}")
print(f"Root Mean Squared Error (RMSE) on Testing Set: {rmse_test}")

results = f"==========\nEpoch #: {numEpochs} \nTest Size: {testSize} \nLayer 1: {h1units} \nLayer 2: {h2units} \nLayer 3: {h3units}\nMSE: {mse_test}\nRMSE: {rmse_test}\n"

print(results)

with open("results.txt", "a") as file:
    file.write(results)