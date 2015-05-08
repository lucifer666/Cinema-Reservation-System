import sqlite3

class DataBase:

    def __init__(self):
        self.connection = sqlite3.connect("cinema.db")
        self.cursor = self.connection.cursor()

    def create_cinema(self):
        '''
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Movies(
                movie_id INTEGER PRIMARY KEY,
                movie_name TEXT,
                movie_rating REAL)""")
        self.connection.commit()


        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Projections(
                project_id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                movie_type TEXT,
                movie_date TEXT,
                movie_time TEXT,
                FOREIGN KEY(movie_id) REFERENCES Movies(movie_id))""")
        self.connection.commit()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reservations(
                reservations_id INTEGER PRIMARY KEY,
                username TEXT,
                projection_id INTEGER,
                row INTEGER,
                col INTEGER,
                FOREIGN KEY(projection_id) REFERENCES Projections(project_id))""")
        self.connection.commit()
        '''
    #def insert_data(self):
        """
        number_of_movies = int(input("Number of movies: "))

        while number_of_movies != 0:
                movie_name = input("Movie name: ")
                movie_rating = input("Movie rating: ")
                self.cursor.execute('''INSERT INTO Movies(movie_name, movie_rating)
                  VALUES(?,?)''', (movie_name, movie_rating))

                number_of_movies -= 1
                self.connection.commit()

        print("The data were added successfuly!")

        number_of_projections = int(input("Number of projections: "))

        while number_of_projections != 0:
                movie_id = int(input("Movie id: "))
                movie_type = input("Movie type: ")
                date = input("Date: ")
                time = input("Time: ")
                self.cursor.execute('''INSERT INTO Projections(movie_id, movie_type, movie_date, movie_time)
                  VALUES(?,?,?,?)''', (movie_id, movie_type, date, time))

                number_of_projections -= 1
                self.connection.commit()

        print("The data were added successfuly!")

        number_of_reservations = int(input("Number of reservations: "))

        while number_of_reservations != 0:
                username = input("Username: ")
                projection_id = int(input("Projection id: "))
                row = int(input("Row: "))
                col = int(input("Col: "))
                self.cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                  VALUES(?,?,?,?)''', (username, projection_id, row, col))

                number_of_reservations -= 1
                self.connection.commit()

        print("The data were added successfuly!")
        """
def main():
    database = DataBase()
    database.create_cinema()
    database.insert_data()


if __name__ == "__main__":
    main()
