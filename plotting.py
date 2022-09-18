
import matplotlib.pyplot as plt
import pandas as pd

cities = pd.read_csv("US Cities.csv")
no2 = pd.read_csv("Average_no2_Scores.csv")
o3 = pd.read_csv("Average_o3_Scores.csv")
pm25 = pd.read_csv("Average_PM25_Scores.csv")

y_labels = ["PM25 (µg/m³)","o3 (ppm)","no2 (ppm)"]
x_labels = ["Population", "Population Density"]
data = [pm25,o3,no2]

fig, axs = plt.subplots(2,3)
for i in range(2):
    for j in range(3):
        axs[i,j].scatter(cities.iloc[:,i+3],data[j])
        axs[i,j].set_xlabel(x_labels[i])
        axs[i,j].set_ylabel(y_labels[j])

fig.set_size_inches(18.5, 10.5)
plt.suptitle("Pollutants in Top 100 US Cities")
plt.savefig('Pollutants.png')
plt.show()


