import pandas as pd

# download latest results from google sheets
results_df = pd.read_csv("https://docs.google.com/spreadsheets/d/18JH_jUX1ifjVdBcxsQUnchi5alx0JOa0LBC62lXJQe4/export?format=csv")
state_co2_df = pd.read_csv("state_co2.csv")
vehicle_emmisions_by_year = pd.read_csv("vehicle_emissions_by_year.csv")  # gallons per mile
co2_by_electrical_grid = pd.read_csv("co2_by_electrical_grid.csv")  # lbs per mWh   

num_results = len(results_df)

# example of how to access a question's answer for most recent response
# print(results_df['test q 1'][num_results-1])

# 2
state = results_df['What state are you from?'][num_results-1]

# 3
car_year = results_df['What year was your car manufactured?'][num_results-1]

# how many miles do you drive per year?
miles_per_year = results_df['How many miles do you drive per year?'][num_results-1]

# processing

state_c02 = state_co2_df[state_co2_df['state'] == 'AK']['co2'].values[0]


print(state_c02)