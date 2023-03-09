
class Guest:

    def __init__(self, reservation_row):

        self.n_adults = reservation_row['adults']
        self.n_children = int(reservation_row['children'])
        self.n_babies = reservation_row['babies']
        self.s_country = reservation_row['country']

    def __str__(self):

        return f'Guest information:\nAdults: {self.n_adults}\nChildren: {self.n_children}\nBabies: {self.n_babies}\nCountry: {self.s_country}'