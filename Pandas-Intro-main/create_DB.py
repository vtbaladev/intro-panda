import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE gta (release_year integet, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

cursor.executemany("INSERT INTO gta values(?, ?, ?)", release_list)

# Print all database rows
for row in cursor.execute("SELECT * FROM gta"):
    print(row)

# Print specific rows
print("---------------------------------")
cursor.execute("SELECT * FROM gta WHERE city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

# Create new Table cities and populate with data
print("---------------------------------")
cursor.execute("CREATE TABLE cities (gta_city text, real_city text)")
cursor.execute("INSERT INTO cities VALUES (?, ?)", ("Liberty City", "New York"))
cursor.execute("SELECT * FROM cities WHERE gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

# Manipulate DataBase
print("---------------------------------")
for i in gta_search:
    adjusted = [cities_search[0][1] if value == cities_search[0][0] else value for value in i]
    print(adjusted)

connection.commit()
connection.close()
