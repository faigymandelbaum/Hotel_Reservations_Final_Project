from data_analysis import cleaning
import pandas as pd
import an_filled as an
from sql.database_actions import create_tables_from_df


def main():
    df_hotels = pd.read_csv(an.INFO_FOLDER + '/' + an.HOTELS_INFO_FILE)
    df_hotels = cleaning.clean(df_hotels)
    create_tables_from_df(df_hotels)
    return df_hotels

if __name__ == '__main__':
    df_hotels = main() 
       