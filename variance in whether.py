import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
print(london_data.head())
#print(london_data.iloc[100:200])
print(len(london_data))
temp= london_data["TemperatureC"]
average_temp= np.mean(temp)
temperature_var = np.var(temp)
print(temperature_var)
temp_sd= np.std(temp)
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
mean6= np.mean(june)
mean7= np.mean(july)
sd6= np.std(june)
sd7=np.std(july)
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
 #lowest variability is December
