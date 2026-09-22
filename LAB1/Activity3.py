# #name Husnain nadeem
# #Reg no 23-ntu-cs-1038
# COVID-19 Dataset Exploration
# Load the online dataset:
# https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv
# Tasks:
# Extract only Pakistan’s data.
# Handle missing values (if any) properly.
# Plot a line chart showing cases over time.
# Find the day with the highest confirmed cases.
# Detect any outliers in daily cases using a boxplot.

import pandas as pd
import matplotlib.pyplot as plt
online_csv_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv'
# Load the dataset
df_covid = pd.read_csv(online_csv_url)
# Extract only Pakistan's data
df_pakistan = df_covid[df_covid['Country/Region'] == 'Pakistan']
# Handle missing values (if any) by filling them with 0
df_pakistan.fillna(0, inplace=True)
# Convert 'Date' column to datetime format
df_pakistan['Date'] = pd.to_datetime(df_pakistan['Date'])
# Plot a line chart showing confirmed cases over time
plt.figure(figsize=(12, 6))
plt.plot(df_pakistan['Date'], df_pakistan['Confirmed'], marker='o', linestyle='-')
plt.title('COVID-19 Confirmed Cases in Pakistan Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
# Find the day with the highest confirmed cases
max_cases_day = df_pakistan.loc[df_pakistan['Confirmed'].idxmax()]
print(f"The day with the highest confirmed cases in Pakistan is {max_cases_day['Date'].date()} with {max_cases_day['Confirmed']} cases.")
# Detect any outliers in daily cases using a boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(df_pakistan['Confirmed'], vert=False)
plt.title('Boxplot of Daily Confirmed Cases in Pakistan')
plt.xlabel('Confirmed Cases')
plt.grid()
plt.show()