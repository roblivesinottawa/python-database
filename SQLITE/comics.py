import sqlite3

connection = sqlite3.connect('comics.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Comics (Title TEXT, Director TEXT, Year INT)""")

comics = [('The Invincible Iron Man: Worlds Most Wanted Book 1', 'Matt Fraction', 2010),
            ('The Invincible Iron Man: Worlds Most Wanted Book 2', 'Matt Fraction', 2010),
            ('The Invincible Iron Man: The Five Nightmares', 'Matt Fraction', 2009)]

cursor.executemany("""INSERT INTO Comics VALUES (?,?,?)""", comics)

records = cursor.execute("SELECT * FROM Comics")
print(cursor.fetchall())

for record in records:
    print(record)

connection.commit()
connection.close()
            