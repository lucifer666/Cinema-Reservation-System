from magic_reservation_system import MagicReservationSystem
from show_pretty_data import PrettyData

class CLI:

    def __init__(self):
        self.pretty_data = PrettyData()

    def enter_name(self):
        name = input("Enter your name> ")
        return name

    def enter_number_of_tickets(self):
        number_of_tickets = int(input("Choose number of tickets> "))
        return number_of_tickets

    def enter_movie_id(self):
       movie_id = int(input("Choose movie> "))
       self.pretty_data.print_show_movie_projections(movie_id)


