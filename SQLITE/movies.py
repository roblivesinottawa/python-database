import sqlite3

# create a connection object and it will connect to the database if it exists anf if not it will create it
connection = sqlite3.connect('movies.db')

# create a cursor object
cursor = connection.cursor()

# create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS Movies
	(Title TEXT, Director TEXT, Year INT)""")

# add one movie to the database
cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

# add multiple movies to the database
famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
('Back to the Future', 'Steven Spielberg', 1985),
('Moonrise Kingdom', 'Wes Anderson', 2012)]

cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)

records = cursor.execute("SELECT * FROM Movies")
print(cursor.fetchall())

for record in records:
    print(record)


# filter records
# release_year = (1985, )
# cursor.execute("SELECT * FROM Movies WHERE Year = ?", release_year)
# print(cursor.fetchall())

# save the changes to the database
connection.commit()
connection.close()