import pandas as pd
import json

#Loading the CSV files from IndianCities
districts_df = pd.read_csv('IndianCities/final_districts.csv')
cities_df = pd.read_csv('IndianCities/final_cities.csv')

# Confirming the final data structure
india_data = {}

#Grouping cities by districts
cities_grouped = cities_df.groupby('District')['City'].apply(list).to_dict()

#Merging district and cities data
for _, row in districts_df.iterrows():
    state = row['State']
    district = row['District']
    try:
        population = int(row['Population'])
    except (ValueError,TypeError):
        population = 0
    district_data = {
        'name' : district,
        'population' : population,
        'cities' : cities_grouped.get(district, [])
    }
    india_data.setdefault(state, {'districts': []})['districts'].append(district_data)


#Saving the final to JSON file
with open('i_data.json', 'w') as f:
    json.dump(india_data, f, indent=2)