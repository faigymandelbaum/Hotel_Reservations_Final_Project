import sqlf.database_actions 
from entities.reservation import Reservation

def get_top_agent_reservations_in_country(s_country):

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
    print (df_results)
    # ls_r = []
    # for index, row in df_results.iterrows():
    #     ls_r.append(Reservation(row))
    ls_reservations = [Reservation(row) for index, row in df_results.iterrows()]
    return ls_reservations
    

def get_reservations_and_guest_from_specific_year_within_range(n_year, n_min, n_max):

    q_query = f'''SELECT *
    FROM Reservation r
    JOIN Guest g
    ON g.GuestId = r.GuestId
    WHERE YEAR(reservation_status_date) = {n_year} and adr BETWEEN {n_min} AND {n_max} and is_canceled != 0;'''

    df_results = sqlf.database_actions.query(q_query)
    print (df_results)

    ls_reservations = [Reservation(row) for index, row in df_results.iterrows()]
    return ls_reservations

def get_impact_of_number_children_on_nights_stayed():

    q_query = '''SELECT g.children, AVG(r.stays_in_weekend_nights + r.stays_in_week_nights) AS average_nights
    FROM Reservation r
    JOIN Guest g
    ON r.GuestId = g.GuestId
    GROUP BY g.children;'''

    df_results = sqlf.database_actions.query(q_query)
    print (df_results)

    return df_results