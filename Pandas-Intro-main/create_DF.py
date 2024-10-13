import pandas as pd

# Creating the DataFrame
column = ["Mariya", "Batman", "Spongebob"]
titled_columns = {
    "name": column,
    "height": [1.67, 1.90, 0.25],
    "weight": [54, 100, 1]
}
data = pd.DataFrame(titled_columns)

# Selecting values from DataFrame
select_column = data["weight"][1]
select_row = data.iloc[1]["weight"]

# Manipulating DataFrame Values
data["bmi"] = data["weight"]/(data["height"]**2)

# Save dataframe into a file
data.to_csv("bmi.csv", index=False, sep="\t")

print(data)
