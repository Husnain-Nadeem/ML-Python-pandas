#Name Husnain Nadeem
#Reg no 23-ntu-cs-1038
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder #python


rng = np.random.default_rng(42)
student_count = 100
marks = rng.integers(40, 101, size=(student_count, 3)).astype(float)

students = pd.DataFrame(
	marks,
	columns=["Math", "Science", "English"],
)
students.insert(0, "ID", np.arange(1, student_count + 1))

# Add missing marks so the imputation step is visible in the analysis.
students.loc[[7, 34, 81], "Math"] = np.nan
students.loc[[19, 56], "Science"] = np.nan
students.loc[92, "English"] = np.nan

mark_columns = ["Math", "Science", "English"]
for column in mark_columns:
	students[column] = students[column].fillna(students[column].mean())

students["Average"] = students[mark_columns].mean(axis=1)
students["Grade"] = pd.cut(
	students["Average"],
	bins=[-np.inf, 59.99, 79.99, np.inf],
	labels=["C", "B", "A"],
)

grade_encoder = LabelEncoder()
students["Grade Encoded"] = grade_encoder.fit_transform(students["Grade"])
students["Total Score"] = students[mark_columns].sum(axis=1)

print("Student performance data (first 10 rows):")
print(students.head(10))
print("\nMissing marks after mean imputation:")
print(students[mark_columns].isna().sum())
print("\nGrade encoding mapping:")
print(dict(zip(grade_encoder.classes_, grade_encoder.transform(grade_encoder.classes_))))

plt.figure(figsize=(8, 5))
plt.hist(students["Math"], bins=10, edgecolor="black")
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.tight_layout()

q1 = students["Total Score"].quantile(0.25)
q3 = students["Total Score"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = students[
	(students["Total Score"] < lower_bound)
	| (students["Total Score"] > upper_bound)
]

plt.figure(figsize=(8, 4))
plt.boxplot(students["Total Score"], vert=False)
plt.title("Boxplot of Total Scores")
plt.xlabel("Total Score")
plt.tight_layout()

print("\nUnusually high/low total-score students:")
if outliers.empty:
	print("None")
else:
	print(outliers[["ID", "Total Score", "Grade"]].to_string(index=False))

grade_summary = students.groupby("Grade", observed=True)["Total Score"].agg(
	Students="count",
	Mean="mean",
).sort_values("Mean", ascending=False)
print("\nPerformance summary by grade:")
print(grade_summary)
print("\nBest-performing grade:", grade_summary.index[0])

plt.show()
