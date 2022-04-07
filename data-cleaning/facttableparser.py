import csv
import pandas as pd

countries = ["Argentina", "Canada", "United States", "Mexico", "Nigeria", "Mali", "Niger", "Ethiopia", "Pakistan"]
human_development_index = { "Argentina":     [0.788, 0.812, 0.817, 0.821, 0.821, 0.829, 0.835, 0.836, 0.840, 0.839, 0.843, 0.842, 0.843, 0.845, 0.845, 0.845],
                            "Canada":        [0.894, 0.898, 0.896, 0.898, 0.898, 0.901, 0.903, 0.906, 0.913, 0.918, 0.921, 0.923, 0.926, 0.928, 0.929, 0.929],
                            "United States": [0.900, 0.903, 0.906, 0.911, 0.912, 0.916, 0.919, 0.920, 0.918, 0.920, 0.921, 0.922, 0.924, 0.925, 0.926, 0.926],
                            "Mexico":        [0.737, 0.745, 0.746, 0.748, 0.748, 0.748, 0.755, 0.759, 0.756, 0.761, 0.766, 0.768, 0.771, 0.776, 0.779, 0.779],
                            "Nigeria":       [0.465, 0.473, 0.478, 0.484, 0.490, 0.482, 0.492, 0.500, 0.519, 0.523, 0.526, 0.526, 0.531, 0.534, 0.539, 0.539],
                            "Mali":          [0.367, 0.376, 0.371, 0.394, 0.401, 0.408, 0.413, 0.413, 0.413, 0.419, 0.417, 0.422, 0.427, 0.431, 0.434, 0.434],
                            "Niger":         [0.294, 0.300, 0.306, 0.314, 0.321, 0.331, 0.338, 0.350, 0.357, 0.365, 0.372, 0.378, 0.386, 0.391, 0.394, 0.394],
                            "Ethiopia":      [0.355, 0.371, 0.386, 0.403, 0.411, 0.421, 0.432, 0.438, 0.447, 0.455, 0.462, 0.467, 0.474, 0.478, 0.485, 0.485],
                            "Pakistan":      [0.486, 0.492, 0.496, 0.503, 0.508, 0.512, 0.516, 0.519, 0.523, 0.530, 0.536, 0.542, 0.550, 0.552, 0.557, 0.557]}
quality_of_life_index =   { "Argentina":     [  None,   None,   None,   None,   None,   None,   None,  32.58,  72.53,  81.12,  77.01, 138.48, 139.59, 131.85, 122.49, 115.31],
                            "Canada":        [  None,   None,   None,   None,   None,   None,   None, 164.99, 186.03, 178.29, 177.63, 177.23, 167.18, 173.90, 170.32, 163.47],
                            "United States": [  None,   None,   None,   None,   None,   None,   None, 140.62, 199.56, 195.55, 192.49, 183.96, 179.73, 180.56, 179.20, 172.11],
                            "Mexico":        [  None,   None,   None,   None,   None,   None,   None,  60.31,  87.94,  83.47,  84.97, 137.01, 129.06, 126.42, 123.48, 118.55],
                            "Nigeria":       [  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   2.99,   None,   None,   None,   None,  55.65],
                            "Mali":          [  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                            "Niger":         [  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                            "Ethiopia":      [  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None],
                            "Pakistan":      [  None,   None,   None,   None,   None,   None,   None,  -3.05,   7.67,  22.32,  21.82,  93.99,  93.41, 100.35, 123.48, 105.44]}

month_data = pd.read_csv("../parsedDataset/parsedMonth.csv")
country_data = pd.read_csv("../parsedDataset/parsedCountry.csv")
event_data = pd.read_csv("../parsedDataset/parsedEvents.csv", sep=";", parse_dates=True)
education_data = pd.read_csv("../parsedDataset/parsedEducation.csv")
health_data = pd.read_csv("../parsedDataset/parsedHealth.csv")
population_data = pd.read_csv("../parsedDataset/parsedPopulation.csv")
life_data = pd.read_csv("../parsedDataset/parsedQualityOfLife.csv")


df = pd.DataFrame(columns=['id', 'country', 'month', 'education', 'event', 'health', 'population', 'quality_of_life', 'human_development_index', 'quality_of_life_index'])
counter = 0

for country in countries:
    for month_info in month_data.iloc():
       counter += 1
       country_id = country_data[(country_data['year'] == month_info['year']) & (country_data['name'] == country)].iloc[0].id
       month_id = month_info['id']
       education_id = education_data[(education_data['year'] == month_info['year']) & (education_data['country'] == country)].iloc[0].id
       event_id = event_data[(event_data['country'] == country) & (event_data['start_date'].str.slice(0, 4) == str(month_info['year']))].iloc[0].id if len(event_data[(event_data['country'] == country) & (event_data['start_date'].str.slice(0, 4) == str(month_info['year']))].index) > 0 else None
       health_id = health_data[(health_data['year'] == month_info['year']) & (health_data['country'] == country)].iloc[0].id if len(health_data[(health_data['year'] == month_info['year']) & (health_data['country'] == country)].index) > 0 else None
       population_id = population_data[(population_data['year'] == month_info['year']) & (population_data['country'] == country)].iloc[0].id if len(population_data[(population_data['year'] == month_info['year']) & (population_data['country'] == country)].index) > 0 else None
       life_id = life_data[(life_data['year'] == month_info['year']) & (life_data['country'] == country)].iloc[0].id

       newDf = pd.DataFrame({'id': [counter],
       'country': [country_id],
       'month': [month_id],
       'education': [education_id],
       'event': [event_id],
       'health': [health_id],
       'population': [population_id],
       'quality_of_life': [life_id],
       'human_development_index': [human_development_index[country][month_info['year']-2005]],
       'quality_of_life_index': [quality_of_life_index[country][month_info['year']-2005]]})

       df = pd.concat([df, newDf], ignore_index = True)

event_data = event_data.drop(['country'], axis=1)
education_data = education_data.drop(columns=['year', 'country'])
health_data = health_data.drop(columns=['year', 'country'])
population_data = population_data.drop(columns=['year', 'country'])
life_data = life_data.drop(columns=['year', 'country'])

df.to_csv('../parsedDataset/parsedFactTable.csv')
event_data.to_csv('../parsedDataset/parsedEvents.csv', sep=';')
education_data.to_csv('../parsedDataset/parsedEducation.csv')
health_data.to_csv('../parsedDataset/parsedHealth.csv')
population_data.to_csv('../parsedDataset/parsedPopulation.csv')
life_data.to_csv('../parsedDataset/parsedQualityOfLife.csv')