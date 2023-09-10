import pandas as pd
from io import StringIO
import requests

g_co2_per_bottle = 0.1825  # lbs of co2

# download latest results from google sheets
# response = requests.get("https://docs.google.com/spreadsheets/d/1lkhS5Cd32grN9zt36ejl-ndQSt3yKEx1aLhh-eBPBtk/")
# csv_data = StringIO(response.text)
# survey_results_df = pd.read_csv(csv_data, on_bad_lines='skip')

survey_results_df = pd.read_csv("https://docs.google.com/spreadsheets/d/1lkhS5Cd32grN9zt36ejl-ndQSt3yKEx1aLhh-eBPBtk/export?format=csv")
state_co2_df = pd.read_csv("state_co2.csv")
vehicle_emmisions_by_year = pd.read_csv("vehicle_emmisions_by_year.csv")  # gallons per mile
co2_by_electrical_grid = pd.read_csv("co2_by_electrical_grid.csv")  # lbs per mWh   
co2_by_food = pd.read_csv("co2_by_food.csv")  # lbs co2 per lb product

num_results = len(survey_results_df)


# 1
state = survey_results_df['What state are you from?'][num_results-1]

# # 2
foods = survey_results_df['What food products make up your diet?'][num_results-2]
foods = foods.split(", ")
total_food_co2 = 0
for food in foods:
    total_food_co2 += co2_by_food["Total_emissions"][co2_by_food["Food product"] == food].values[0]

print(total_food_co2)


# # 3
transportation = survey_results_df['How do you get around?'][num_results-1]

# # 4
car_year = survey_results_df['If you drive what year was your car made?'][num_results-1]

# # 5
miles_per_year = survey_results_df['If you drive how many miles a year on average?'][num_results-1]

# # 6
housing = survey_results_df['What is your housing situation?'][num_results-1]

# #7
water = survey_results_df['Do you [mostly] drink from a refillable Water Bottle or drink bottled water?'][num_results-1]

# processing
#test
print(survey_results_df["What food products make up your diet?"][num_results-1])

# this_users_state_co2_emmissions = state_co2_df["avg_co2"][state_co2_df["state"] == state]
