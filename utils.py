import pandas as pd
from datetime import datetime

def preprocess(df):
    # remove missing values in the dataframe
    def remove_missing_values(df):
        # ** YOUR CODE HERE **
        dfNa = df.isna()
        df = df[dfNa['pickup_longitude'] == False]
        df = df[dfNa['pickup_latitude'] == False]
        df = df[dfNa['dropoff_longitude'] == False]
        df = df[dfNa['dropoff_latitude'] == False]
        return df

    # remove outliers in fare amount
    def remove_fare_amount_outliers(df):
        # ** YOUR CODE HERE **
        df = df[df['fare_amount'] != 0]
        return df

    # replace outliers in passenger count with the mode
    def replace_passenger_count_outliers(df):
        # ** YOUR CODE HERE **
        dfMode = max(df['passenger_count'].mode())
        df['passenger_count'] = df['passenger_count'].replace(0, dfMode)
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

        df = df[df['pickup_longitude'].between(nyc_min_longitude,nyc_max_longitude)]
        df = df[df['pickup_latitude'].between(nyc_min_latitude,nyc_max_latitude)]
        df = df[df['dropoff_longitude'].between(nyc_min_longitude,nyc_max_longitude)]
        df = df[df['dropoff_latitude'].between(nyc_min_latitude,nyc_max_latitude)]

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
        # cols = df.columns.tolist()
        # print(df.dtypes)
        # print(df)
        # print(df.pickup_datetime)
        # tt = df['pickup_datetime'].timetuple
        # df['year'] = df['pickup_datetime'].apply(lambda x: datetime.strptime(str(int(x)), '%Y'))
        # df['year'] = datetime.strptime(str(df[2]), '%Y')
        # df['month'] = datetime.strptime(str(df[2]), '%m')
        # df['day'] = datetime.strptime(str(df[2]), '%d')
        # df['day_of_week'] = datetime.date.weekday(str(df[2]))
        df['year'] = df['pickup_datetime'].dt.year
        df['month'] = df['pickup_datetime'].dt.month
        df['day'] = df.pickup_datetime.dt.day
        df['weekday'] = df.pickup_datetime.dt.weekday
        df['hour'] = df.pickup_datetime.dt.hour
        df.drop(columns=['pickup_datetime'], inplace=True)
        # print('df year', df['year'])
        # print('df month', df['month'])
        # print('df day', df['day'])
        # print('df weekday', df['weekday'])
        # print('df hour', df.hour)
        # print('df', df)

        try:
            x = df['pickup_datetime']
        except KeyError:
            print("Good job!")
        else:
            raise ValueError("Column `pickup_datetime' still exists")

        # 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
        # df['hour'] = datetime.strptime(str(df[2]), '%H')

        # asdf = df.apply(lambda x: datetime.strptime(str(int(x)), '%Y-%m-%d %H:%M:%S %Z'))
        # print(asdf)

        # asdf = datetime.strptime( , '%Y-%m-%d %H:%M:%S %Z')
        # print(asdf)

        #remove pickup_datetime column
        # df = df.drop(['pickup_datetime'])


        return df

    # function to calculate euclidean distance
    def euc_distance(lat1, long1, lat2, long2):
        return(((lat1-lat2)**2 + (long1-long2)**2)**0.5)

    # create new column for the distance travelled
    def create_pickup_dropoff_dist_features(df):
        # ** YOUR CODE HERE **
        df['travel_distance'] = euc_distance(df.pickup_latitude, df.pickup_longitude, df.dropoff_latitude, df.dropoff_longitude)

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
