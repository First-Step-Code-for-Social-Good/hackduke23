import pandas as pd

# download latest results from google sheets
results_df = pd.read_csv("https://docs.google.com/spreadsheets/d/18JH_jUX1ifjVdBcxsQUnchi5alx0JOa0LBC62lXJQe4/export?format=csv")
co2_df = pd.read_csv("https://docs.google.com/spreadsheets/d/1IAgwmM4-Cdpv8fK6TQHcoNfVHf0aXJNtMDtYEQ-q878/export?format=csv")

num_results = len(results_df)

# example of how to access a question's answer for most recent response
# print(results_df['test q 1'][num_results-1])

# 2
state = results_df['What state are you from?'][num_results-1]

# 3
zip_code = results_df['What is your zip code?'][num_results-1]








# processing

zip_c02 = co2_df[co2_df['Zip Code'] == 1001]['c02'].values[0]
print(zip_c02)