import sqlite3

class DataBase:
    
    def __init__(self):
        self.connection = sqlite3.connect("cinema.db")
        self.cursor = self.connection.cursor()

    def create_cinema(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies(movie_id INTEGER PRIMARY KEY,
                                movie_name TEXT,
                                movie_rating INTEGER)""") 
                                self.connection.commit()

    def insert_movies(self):
        number_of_movies = int(input("Number of movies: "))

        while number_of_movies != 0:
                name = input("Movie name: ")
                movie_rating = input("Movie rating:")
                self.cursor.execute('''INSERT INTO movies(movie_name, movie_rating)
                  VALUES(?,?)''', (name, movie_rating ))

                number_of_movies -= 1
                self.connection.commit()

        print("The data were added successfuly!")

database = DataBase()
database.insert_movies()

