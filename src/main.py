from data_analysis import cleaning
import pandas as pd
import an_filled as an
from sqlf.database_actions import create_tables_from_df
import logging
import traceback
import sqlf.queries as sq

# Loading file with a load file function, the path comes from a hardcoded file.
def load_file(s_path, s_file_name):

    '''This function loads a csv into a pandas dataframe

     args: 
      s_path (str): the path to the csv file
      s_file_name(str): csv name

     returns:
      bool
      pd.DataFrame() if loaded successfully 
          '''

    df_file = pd.DataFrame()
    if (not s_path) or (not s_file_name):
        logging.error('The file name or path came up empty. Filename: ' + s_file_name + ' Path: ' + s_path)
        return False, df_file
    s_path = s_path + '/' + s_file_name
    try:
        df_file = pd.read_csv(s_path, parse_dates=['reservation_status_date'], na_values=['none', 'Undefined', ' ', '-'])
        logging.info('File loaded successfully.')
    except:
        logging.error('cannot load hotel file: ' + s_path)
        return False, df_file

    return True, df_file

def set_up():

    worked, df_hotels = load_file(an.INFO_FOLDER, an.HOTELS_INFO_FILE)
    df_cleaned_hotels = cleaning.clean(df_hotels)
    create_tables_from_df(df_cleaned_hotels)

def get_menu_choice():

    menu = "\n1. View the best agent's top 10 reservations + guests in a specific country."
    menu +=	"\n2. View reservations + guests that were not canceled that are within a specific price range (adr) for a specific year." 
    menu +=	"\n3.  View the impact the number of children have on the number of nights." 

    choice = input(menu + "\nPlease enter 1-3 (or 0 to exit): ")
    try:
        return int(choice)
    except:
        print ('Invalid menu choice. Enter 1-6 (or 0 to exit): ')
        logging.error("Invalid menu choice.")
   

def main():

    menu_choice = None

    while menu_choice != 0:

        menu_choice = get_menu_choice()

        try: 

            if menu_choice == 1: 

                country = input('For what country would you like to find the top agent?').upper()  
                if len(country) == 3:   
                    ls_top_agent_reservations = sq.get_top_agent_reservations_in_country(country)

                for each in ls_top_agent_reservations:
                    if ls_top_agent_reservations.empty:
                        logging.error
                    print ('*' , each)


            elif menu_choice == 2: 

                year = input('Please enter the year you would like to view. ')
                min = input('What is the minimum of average daily rate you would like to view?')
                max = input('What is the maximum of average daily rate you would like to view?')
                ls_within_range_reservations = sq.get_reservations_and_guest_from_specific_year_within_range(year, min, max)
                
                for each in ls_within_range_reservations:
                    print ('*' , each)

            elif menu_choice == 3:
      
                sq.get_impact_of_number_children_on_nights_stayed()

            elif menu_choice == 0:

                print ("Ending program")

                logging.info("Ending Application!")


        except Exception as e:
            print (str(e))
            logging.error(traceback.format_exc() + '{}'.format(str(e)))



if __name__ == '__main__':
 
   main() 
       