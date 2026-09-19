#Name Husnain Nadeem
#Reg no 23-ntu-cs-1038
#Pakistan province analysis

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#manual data creation
provinces = pd.DataFrame({
	"Province": ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan"],
	"Population (millions)": [110.0, None, 35.5, 12.3],
	"Literacy Rate (%)": [64.7, 58.0, 55.0, None],
	"Region": ["East", "South", "North", "West"],
})

print("Original dataset:")
print(provinces)
#Dropna
provinces = provinces.dropna(subset=["Population (millions)"]).copy()
literacy_median = provinces["Literacy Rate (%)"].median()
provinces["Literacy Rate (%)"] = provinces["Literacy Rate (%)"].fillna(literacy_median)

label_encoder = LabelEncoder()
provinces["Region Label"] = label_encoder.fit_transform(provinces["Region"])
region_one_hot = pd.get_dummies(provinces["Region"], prefix="Region")
provinces = pd.concat([provinces, region_one_hot], axis=1)

print("\nCleaned and encoded dataset:")
print(provinces)
print("\nLabel encoding mapping:")
print(dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))))
print("\nMedian used for missing literacy rate:", literacy_median)

# IQR method to detect outliers in literacy rate
literacy = provinces["Literacy Rate (%)"]
q1 = literacy.quantile(0.25)
q3 = literacy.quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = provinces[
	(literacy < lower_bound) | (literacy > upper_bound)
]["Province"].tolist()

print("\nLiteracy-rate outliers:", outliers if outliers else "None")

plt.figure(figsize=(8, 5))
plt.scatter(provinces["Population (millions)"], provinces["Literacy Rate (%)"])
for _, province in provinces.iterrows():
	plt.annotate(
		province["Province"],
		(province["Population (millions)"], province["Literacy Rate (%)"]),
		xytext=(5, 5),
		textcoords="offset points",
	)
plt.title("Population vs Literacy Rate by Province")
plt.xlabel("Population (millions)")
plt.ylabel("Literacy Rate (%)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

