import pandas as pd

# download latest results from google sheets
results_df = pd.read_csv("https://docs.google.com/spreadsheets/d/18JH_jUX1ifjVdBcxsQUnchi5alx0JOa0LBC62lXJQe4/export?format=csv")
state_co2_df = pd.read_csv("state_co2.csv")

num_results = len(results_df)

# example of how to access a question's answer for most recent response
# print(results_df['test q 1'][num_results-1])

# 2
state = results_df['What state are you from?'][num_results-1]



# processing

state_c02 = state_co2_df[state_co2_df['state'] == 'AK']['co2'].values[0]
print(state_c02)