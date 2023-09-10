import pandas as pd

g_co2_per_bottle = 0.1825  # lbs of co2
lbs_of_food_consumed_per_year = 2000

survey_results_df = pd.read_csv("https://docs.google.com/spreadsheets/d/1lkhS5Cd32grN9zt36ejl-ndQSt3yKEx1aLhh-eBPBtk/export?format=csv")
state_co2_df = pd.read_csv("state_co2.csv")
vehicle_emmisions_by_year = pd.read_csv("vehicle_emmisions_by_year.csv")  # gallons per mile
co2_by_electrical_grid = pd.read_csv("co2_by_electrical_grid.csv")  # lbs per mWh   
co2_by_food = pd.read_csv("co2_by_food.csv")  # lbs co2 per lb product

num_results = len(survey_results_df)

# electricty efficienty used for calculating housing emissions
state = survey_results_df['What state are you from?'][num_results-1]
user_state_emissions = state_co2_df["avg_co2"][state_co2_df["state"] == state]
user_state_electricity = co2_by_electrical_grid["lb/mwh"][co2_by_electrical_grid["state"] == state].values[0]

# food emissions
foods = survey_results_df['What food products make up your diet?'][num_results-1] 
foods = foods.split(", ")
foods_co2 = 0 #calc
for food in foods:
    try:
        foods_co2 += co2_by_food["Total_emissions"][co2_by_food["Food product"] == food].values[0]  #TODO: troubleshoot "IndexError: index 0 is out of bounds for axis 0 with size 0" that happens on some runs
    except:
        pass
foods_co2 = round(foods_co2 * lbs_of_food_consumed_per_year)

# used for calculating car emissions
car_year = survey_results_df['If you drive what year was your car made?'][num_results-1]

# car emissions
miles_per_year = survey_results_df['If you drive how many miles a year on average?'][num_results-1]
if miles_per_year == "0-1000":
    miles_per_year = 500
elif miles_per_year == "1000-15,000":
    miles_per_year = 8000
elif miles_per_year == "I do not drive":
    miles_per_year = 0
else:
    miles_per_year = 20000

car_ch4 = miles_per_year * vehicle_emmisions_by_year["ch4"][vehicle_emmisions_by_year["year"] == car_year].values[0]
car_n2o = miles_per_year * vehicle_emmisions_by_year["n2o"][vehicle_emmisions_by_year["year"] == car_year].values[0]
car_emissions = round(car_ch4 + car_n2o)

# housing emissions
housing = survey_results_df['What is your housing situation?'][num_results-1]
if housing == "Student Dorm":
    housing_electricity_usage = 1  #megawatt hours (mwh)
if housing == "Apartment":
    housing_electricity_usage = 3  #mwh
if housing == "House":
    housing_electricity_usage = 13  #mwh

housing_emmisions = round(user_state_electricity * housing_electricity_usage)

# water emissions
water = survey_results_df['Do you mostly drink from a refillable Water Bottle or drink bottled water?'][num_results-1]
if water == "Refillable Bottle":
    water_emissions = 0
else:
    water_emissions = round(156 * g_co2_per_bottle)  # 156 bottles per year

total_emissions = foods_co2 + car_emissions + housing_emmisions + water_emissions

with open("results_data.txt", "w") as file:
    file.write(str(total_emissions))
    file.write("\n")
    file.write(str(foods_co2))
    file.write("\n")
    file.write(str(car_emissions))
    file.write("\n")
    file.write(str(housing_emmisions))
    file.write("\n")
    file.write(str(water_emissions))