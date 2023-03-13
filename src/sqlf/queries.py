import sqlf.database_actions 
from entities.reservation import Reservation

def get_top_agent_reservations_in_country(s_country):

    '''
    This is a function that runs a sql query to get top 10 reservations for the best agent in a country.
    The data is put into a dataframe and then made as instances of a class.

    Parameters:
    s_country(str): The country that the viewer would like to see the data on.

    Returns:
    list: a list of the reservation class instances.
    '''

    q_query = f'''SELECT TOP 10 *
    FROM Reservation r
    JOIN Guest g
    ON r.GuestId = g.GuestId
    WHERE r.agent = (SELECT TOP 1 r.agent
        FROM Reservation r
        JOIN Guest g
        ON r.GuestId = g.GuestId
        WHERE g.country = 'IRL' and r.agent != 'no agent'
        GROUP BY r.agent
        ORDER BY COUNT(r.agent) DESC) and r.GuestId = g.GuestId and g.country = '{s_country}';'''
    
    df_results = sqlf.database_actions.query(q_query)

    ls_reservations = [Reservation(row) for index, row in df_results.iterrows()]
    return ls_reservations
    

def get_reservations_and_guest_from_specific_year_within_range(n_year, n_min, n_max):

    '''
    This is a function that runs a sql query to get reservations and guest from a specific year within a range.
    The data is put into a dataframe and then made as instances of a class.

    Parameters:
    n_year(int): The year that the viewer would like to see the data on.
    n_min(int): The lowest average daily rate the viewr wants to see.
    n_max(int): Th highest average daily rate the viewer wants to see.

    Returns:
    list: a list of the reservation class instances.
    '''

    q_query = f'''SELECT *
    FROM Reservation r
    JOIN Guest g
    ON g.GuestId = r.GuestId
    WHERE YEAR(reservation_status_date) = {n_year} and adr BETWEEN {n_min} AND {n_max} and is_canceled != 1;'''

    df_results = sqlf.database_actions.query(q_query)

    ls_reservations = [Reservation(row) for index, row in df_results.iterrows()]
    return ls_reservations

def get_impact_of_number_children_on_nights_stayed():

    '''
    This is a function that runs a sql query to view the impact of number of children in a family in the nights thay stayed.

    Parameters:
    None

    Returns:
    df: a dataframe of the query result.
    '''

    q_query = '''SELECT g.children, AVG(r.stays_in_weekend_nights + r.stays_in_week_nights) AS average_nights
    FROM Reservation r
    JOIN Guest g
    ON r.GuestId = g.GuestId
    GROUP BY g.children;'''

    df_results = sqlf.database_actions.query(q_query)

    return df_results