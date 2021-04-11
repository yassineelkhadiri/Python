# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab)+ ": "+ str(row["cars_per_cap"]))

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = str.upper(row["country"])


# or :cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)