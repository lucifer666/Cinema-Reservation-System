import sys
import sqlite3

class MagicReservationSystem:

    def __init__(self):
         self.connection = sqlite3.connect("cinema.db")
         self.cursor = self.connection.cursor()

    def show_movies(self):
        movies = self.cursor.execute("SELECT movie_id, movie_name, movie_rating FROM Movies ORDER BY movie_rating")
        return movies


    def show_movie_projections(self, movie_id):
            projections = self.cursor.execute("SELECT projection_id, movie_date, movie_time, movie_type FROM Projections WHERE movie_id = ?", (movie_id,))
            return projections

    def show_movie_projections(self, movie_id, movie_date):
        projections = self.cursor.execute("SELECT projection_id, movie_time, movie_type FROM Projections WHERE movie_id = ?, movie_date = ?", (movie_id,movie_date,))
        return projections




