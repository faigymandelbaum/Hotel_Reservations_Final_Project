from enums.hotel_type import HotelType
from enums.customer_type import CustomerType
from enums.deposit_type import DepositType
from enums.meal_type import MealType
from entities.guest import Guest

class Reservation:

    def __init__(self, reservation_row):

        self.e_hotel_name = HotelType[reservation_row['hotel'].upper().replace(' ', '_')]
        self.b_reservation_is_canceled = reservation_row['is_canceled']
        self.n_lead_time = reservation_row['lead_time']
        self.n_arrival_date_week_number = reservation_row['arrival_date_week_number']
        self.n_stays_in_weekend_nights = reservation_row['stays_in_weekend_nights'] 
        self.n_stays_in_week_nights = reservation_row['stays_in_week_nights']
        self.e_meal = MealType[reservation_row['meal']]
        self.s_market_segment = reservation_row['market_segment']
        self.s_distribution_channel = reservation_row['distribution_channel']
        self.b_is_repeated_guest = reservation_row['is_repeated_guest']
        self.n_previous_cancellations = reservation_row['previous_cancellations']
        self.n_previous_bookings_not_canceled = reservation_row['previous_bookings_not_canceled']
        self.s_reserved_room_type = reservation_row['reserved_room_type']
        self.s_assigned_room_type = reservation_row['assigned_room_type']
        self.n_booking_changes = reservation_row['booking_changes']
        self.e_deposit_type = DepositType[reservation_row['deposit_type'].upper().replace(' ', '_')]
        self.s_agent_id = reservation_row['agent']
        self.s_company = reservation_row['company']
        self.n_days_in_waiting_list = reservation_row['days_in_waiting_list']
        self.e_customer_type = CustomerType[reservation_row['customer_type'].upper().replace('-', '_')]
        self.n_average_daily_rate = reservation_row['adr']
        self.n_required_car_parking_spaces = reservation_row['required_car_parking_spaces']
        self.n_total_of_special_requests = reservation_row['total_of_special_requests']
        self.s_reservation_status = reservation_row['reservation_status']
        self.dt_reservation_status_date = reservation_row['reservation_status_date']
        self.dt_arrival_date = reservation_row['arrival_date']
        self.s_direct_booking = reservation_row['direct_booking']
        self.o_guest = Guest(reservation_row)

    def __str__(self):
        # attributes = ['s_hotel_name','b_canceled_reservation', 'n_lead_time','n_arrival_week_num','n_num_weekend_nights','n_num_week_nights','s_meal_type','s_market_segment','s_distribution_channel','b_is_repeated_guest','n_previous_cancellations','n_previous_bookings_not_canceled','s_reserved_room_type','s_assigned_room_type','n_booking_changes','s_deposit_type','s_agent_id','s_company','n_days_in_waiting_list','s_customer_type','n_average_daily_rate','n_required_car_parking_spaces','n_total_of_special_requests','s_reservation_status','dt_reservation_status_date','dt_arrival_date','s_direct_booking','n_days_stayed']
        # s = ''
        # for attribute in attributes:
        #     s+=f'{attribute}: {self.attribute}\n'
        # return s

        s=''
        s+=f'Guest: {self.o_guest.__str__()}'
        s+=f'\nHotel: {self.e_hotel_name.name}'
        s+=f'\nArrival date:  {self.dt_arrival_date}'
        s+=f'\nCustomer Type:  {self.e_customer_type.name}'
        s+=f'\nMeal: {self.e_meal.name}'
        s+=f'\nTotal of Special Requests: {self.n_total_of_special_requests}'
        s+=f'\nDirect Booking: {self.s_direct_booking}'
        s+=f'\nAssigned Room Type: {self.s_assigned_room_type}'
        s+=f'\nAgent: {self.s_agent_id}'
        s+=f'\nAverage Daily Rate: {self.n_average_daily_rate}'
        return s




        