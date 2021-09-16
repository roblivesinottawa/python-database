import sqlite3 

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users 
(user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email TEXT)""")

users = [('Steve', 'Rogers', 'steve@gmail.com'),
        ('Tony', 'Stark', 'tony@gmail.com'),
        ('Bruce', 'Banner', 'bruce@gmail.com'),
        ('Peter', 'Parker', 'peter@gmail.com'),
        ('Natasha', 'Romanov', 'natasha@gmail.com')]

cursor.executemany("INSERT INTO Users (first_name, last_name, email) VALUES (?,?,?)", users)

cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())


connection.commit()
connection.close()