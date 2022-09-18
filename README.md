# Air_Quality

Purpose: I initially started this project with the intent of running multivariable linear regressions in python on air quality data. The goal was to predict the average air quality of a city given it's population and population density. However, after plotting the data there was much less correlation between the air quality and the features. 

Outcome: The plots in the provided png file show how little correlation was found between the air quality and the population/population density. I suspsect that with more data correlations may increase. The averages were taken over the most recent 35 datapoints provided by the API, which typically occured within the last day or so of querying the API. Perhaps with longer term averages the correlation may increase. 

Although I was unable to use this project as practice for any sort of machine learning, I learned other valueable skills in python. 

Skills Learned:
  - Pandas Dataframes
  - JSON data structures
  - Querying API's
  - Basic Plotting

Files Included:

update_data.py - This script gathers all data used for the analysis. Data is pulled from a CSV and the OpenAQ API. The file queries the API for each city in our list given in "US Cities.csv" and averages all the measurements reported to find average measurements for each city. The average values for the three paramaters of interest (O3, NO2, and PM2.5) are then saved out as CSV files to be used in analysis. 

plotting.py - This script plots the air quality data gathered against both Population and Population Densit using matplotlib. 
