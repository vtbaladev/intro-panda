import sqlite3
import pandas as pd

# data = pd.read_csv("bmi.csv", sep="\t")
# Connecting into sql database
connection = sqlite3.connect("gta.db")

# Getting data from table gta in gta database
gta_data = pd.read_sql("SELECT * FROM gta", connection)

# Ways to get data
first_5_rows = gta_data.head()
last_2_rows = gta_data.tail(2)

# Filter and Replace data
filtered_row = gta_data[gta_data["city"] == "Liberty City"]
replaced_city = gta_data.replace("Liberty City", "New York")

# Remove Data
remove_column = gta_data.drop(["city", "release_year"], axis=1)
remove_row = gta_data.iloc[1:4]

# Add new rows
row = {
    "release_year": 2021,
    "release_name": "Natural Vision Evolved",
    "city": "Los Angeles"
}
gta_data.loc[len(gta_data)] = row
print(gta_data)
