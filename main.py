from magic_reservation_system import MagicReservationSystem
from show_pretty_data import PrettyData
from command_line_interface import CLI

def main():
    reservation = MagicReservationSystem()
    pretty_data = PrettyData()
    cli = CLI()

    cli.enter_name()
    cli.enter_number_of_tickets()
    pretty_data.print_show_movies()
    print(reservation.cinema_hall())
    cli.enter_movie_id()



if __name__ == "__main__":
    main()
