
import pandas as pd
import numpy as np
import csv
import an_filled as an
import logging
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
import plotly.express as px

logging.basicConfig(filename= an.LOG_FILE,
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def clean(df_hotels):

    # Converting is_canceled column into bool column.
    try:
        df_hotels.is_canceled = df_hotels.is_canceled.map(lambda val: False if val == 0 else True)
        logging.info("column 'is_canceled' converted to bool type.")
        df_hotels.is_canceled.dtypes

    except:
        logging.error("Could not convert column 'is_canceled' to bool type")

    try:   
        df_hotels['arrival_date'] = df_hotels.apply(lambda row : str(row.arrival_date_year) + '/' + str(row.arrival_date_month) + '/' + str(row.arrival_date_day_of_month), axis=1)
        df_hotels['arrival_date'] = pd.to_datetime(df_hotels.arrival_date, format='%Y/%B/%d')
        df_hotels.arrival_date.dtypes
        logging.info("column 'arrival_date' converted to datetime.")

    except Exception as e:
        logging.error(e) 

    # Droping columns: 'arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month' 
    df_hotels.drop(['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'], axis=1, inplace = True)

    # creating a column 'hotel_booking' that has a 'yes' for bookings that weren't done through the agent or a company, and 'no' for the rest.
    try:   
        df_hotels['direct_booking'] = df_hotels.apply(lambda row : 'yes' if pd.isnull(row['agent']) and pd.isnull(row['company']) else 'no', axis=1)
        logging.info("column 'direct_booking' created.")

    except Exception as e:
        logging.error(e)

    # Filling missing values in country column with the country of the row before.
    df_hotels['country'].fillna(method='bfill', inplace= True)

    # Filling missing values in children column with the mean of the column.
    df_hotels['children'].fillna(statistics.mode(df_hotels['children']), inplace=True)

    # Filling missing values in agent column with a string.
    df_hotels['agent'].fillna('no agent', inplace=True)

    # Filling missing values in company column with a string.
    df_hotels['company'].fillna('no company', inplace=True)

    # Filling missing values in meal column with 'SC' that calls a no meal package.
    df_hotels['meal'].fillna('SC', inplace=True)

    # Filling missing values in market_segment column with the value in the row before.
    df_hotels['market_segment'].fillna(method='bfill', inplace=True)

    # Filling missing values in distribution_channel column with the value in the row before.
    df_hotels['distribution_channel'].fillna(method='bfill', inplace=True)

    # Converting is_repeated_guest column into bool column.
    try:
        df_hotels.is_repeated_guest = df_hotels.is_repeated_guest.map(lambda val: False if val == 0 else True)
        logging.info("column 'is_repeated_guest' converted to bool type.")
        df_hotels.is_canceled.dtypes

    except:
        logging.error("Could not convert column 'is_repeated_guest' to bool type")

    return df_hotels    