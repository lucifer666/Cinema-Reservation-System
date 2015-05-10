import sqlite3
from settings import *

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

with open(sql_database, "r") as f:
    connection.executescript(f.read())
    connection.commit()

with open(sql_fill_database, "r") as f:
    cursor.executescript(f.read())
    connection.commit()
