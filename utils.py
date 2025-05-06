import pandas as pd
from datetime import datetime

def preprocess(df):
    # remove missing values in the dataframe
    def remove_missing_values(df):
        # ** YOUR CODE HERE **

        return df

    # remove outliers in fare amount
    def remove_fare_amount_outliers(df):
        # ** YOUR CODE HERE **

        return df

    # replace outliers in passenger count with the mode
    def replace_passenger_count_outliers(df):
        # ** YOUR CODE HERE **
        df['passenger_count'].replace(0, df['passenger_count'].mode(), inplace=True)
        return df

    # remove outliers in latitude and longitude
    def remove_lat_long_outliers(df):
        # range of longitude for NYC
        nyc_min_longitude = -74.05
        nyc_max_longitude = -73.75

        # range of latitude for NYC
        nyc_min_latitude = 40.63
        nyc_max_latitude = 40.85

        # only consider locations within New York City
        # ** YOUR CODE HERE **


        return df


    df = remove_missing_values(df)
    df = remove_fare_amount_outliers(df)
    df = replace_passenger_count_outliers(df)
    df = remove_lat_long_outliers(df)
    return df


def feature_engineer(df):
    # create new columns for year, month, day, day of week and hour
    def create_time_features(df):
        # ** YOUR CODE HERE **
        df['year'] = datetime.striptime(df['pickup_datetime'], format='%Y')
        df['month'] = datetime.striptime(df['pickup_datetime'], format='%m')
        df['day'] = datetime.striptime(df['pickup_datetime'], format='%d')
        df['day_of_week'] = datetime.date.weekday(df['pickup_datetime']) 
        # 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
        df['hour'] = datetime.striptime(df['pickup_datetime'], format='%H')
        #remove pickup_datetime column
        df.drop(['pickup_datetime'], inplace=True)
        return df

    # function to calculate euclidean distance
    def euc_distance(lat1, long1, lat2, long2):
        return(((lat1-lat2)**2 + (long1-long2)**2)**0.5)

    # create new column for the distance travelled
    def create_pickup_dropoff_dist_features(df):
        # ** YOUR CODE HERE **
        df['travel_distance'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], df['dropoff_latitude'], df['dropoff_longitude'])

        return df

    # create new columns for the distance away from airports
    def create_airport_dist_features(df):
        airports = {'JFK_Airport': (-73.78,40.643),
                    'Laguardia_Airport': (-73.87, 40.77),
                    'Newark_Airport' : (-74.18, 40.69)}

        # ** YOUR CODE HERE **

        df['JFK_pickup'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], airports['JFK_Airport'][0],airports['JFK_Airport'][1])

        df['LGA_pickup'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], airports['Laguardia_Airport'][0],airports['Laguardia_Airport'][1])

        df['EWR_pickup'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], airports['Newark_Airport'][0],airports['Newark_Airport'][1])

        df['JFK_dropoff'] = euc_distance(df['dropoff_latitude'], df['dropoff_longitude'], airports['JFK_Airport'][0],airports['JFK_Airport'][1])

        df['LGA_dropoff'] = euc_distance(df['dropoff_latitude'], df['dropoff_longitude'], airports['Laguardia_Airport'][0],airports['Laguardia_Airport'][1])

        df['EWR_dropoff'] = euc_distance(df['dropoff_latitude'], df['dropoff_longitude'], airports['Newark_Airport'][0],airports['Newark_Airport'][1])

        return df

    df = create_time_features(df)
    df = create_pickup_dropoff_dist_features(df)
    df = create_airport_dist_features(df)
    df = df.drop(['key'], axis=1)
    return df
