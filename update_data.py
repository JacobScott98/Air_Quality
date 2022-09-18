import json
import numpy as np
import requests
import pandas as pd

#Reading csv to Pandas Dataframe
cities = pd.read_csv("US Cities.csv")

#Getting Length of Cities List
c_length,_ = cities.shape
avg_pm25 = np.zeros(100)
avg_no2 = np.zeros(100)
avg_o3 = np.zeros(100)

#Outer Loop - Querying OpenAQ API for measurements of the cities in cities
for i in range(c_length):
    lat = str(cities.iloc[i,1])
    long = str(cities.iloc[i,2])
    meas = json.loads(requests.get(f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-14T23%3A00%3A00%2B00%3A00&limit=35&page=1&offset=0&sort=desc&coordinates={lat}%2C{long}&radius=50000&country_id=US&order_by=datetime").text)

    tmp_avg_pm25 = 0
    pm25_count = 0
    tmp_avg_no2 = 0
    no2_count = 0
    tmp_avg_o3 = 0
    o3_count = 0

    if "results" in meas:
        for j in range(len(meas['results'])):
            if meas['results'][j]['parameter'] == 'pm25' and meas['results'][j]['unit'] == 'µg/m³':
                tmp_avg_pm25 = tmp_avg_pm25 + meas['results'][j]['value']
                pm25_count = pm25_count + 1
            if meas['results'][j]['parameter'] == 'no2' and meas['results'][j]['unit'] == 'ppm':
                tmp_avg_no2 = tmp_avg_no2 + meas['results'][j]['value']
                no2_count = no2_count + 1
            if meas['results'][j]['parameter'] == 'o3' and meas['results'][j]['unit'] == 'ppm':
                tmp_avg_o3 = tmp_avg_o3 + meas['results'][j]['value']
                o3_count = o3_count + 1
        if pm25_count > 0:
            avg_pm25[i] = tmp_avg_pm25 / pm25_count
        if no2_count > 0:
            avg_no2[i] = tmp_avg_no2 / no2_count
        if o3_count > 0:
            avg_o3[i] = tmp_avg_o3 / o3_count


#Saving Out Values as CSV Files
np.savetxt("Average_PM25_Scores.csv",avg_pm25,delimiter=",")
np.savetxt("Average_no2_Scores.csv",avg_no2,delimiter=",")
np.savetxt("Average_o3_Scores.csv",avg_o3,delimiter=",")
print(avg_pm25)
print(avg_no2)
print(avg_o3)
