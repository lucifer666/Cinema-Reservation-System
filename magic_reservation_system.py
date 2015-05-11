import sqlite3

class MagicReservationSystem:

    def __init__(self):
         self.connection = sqlite3.connect("cinema.db")
         self.cursor = self.connection.cursor()



    def show_movies(self):
        movies = self.cursor.execute("SELECT movie_id, movie_name, movie_rating FROM Movies ORDER BY movie_rating")
        return movies


    def show_movie_projections(self, movie_id):
            projections = self.cursor.execute("SELECT projection_id, movie_date, movie_time, movie_type FROM Projections \
                WHERE movie_id = ?", (movie_id,))
            return projections

    def show_movie_projections_with_date(self, movie_id, movie_date):
        projections = self.cursor.execute("SELECT projection_id, movie_time, movie_type FROM Projections \
            WHERE movie_id = ? AND movie_date = ?", (movie_id, movie_date,))
        return projections

    def cinema_hall(self, projection_id):

        #available_spots = 0
        #available_seats = "."
        #taken_seats = "X"

        size_of_the_hall = [
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        ]

        for row, rows in enumerate(size_of_the_hall):
            for col, cols in enumerate(rows):
                if size_of_the_hall[row][col] != taken_seats:
                    available_spots += 1
        return available_spots




    #def make_reservation(self):
       # name = input("Enter your name> ")
        #tickets = int(input("Choose number of tickets> "))
        #self.pretty_data.print_show_movies()
"""
c =MagicReservationSystem()
c.cinema_hall()
"""

