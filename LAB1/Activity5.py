# #Name Husnain Nadeem
# #Reg no 23-ntu-cs-1038
# Multi-format Data Loading & Visualization Challenge
# You are provided with three small files:
# students.csv (contains names and marks)
# attendance.json (contains student names with attendance %)
# extra.xlsx (contains bonus marks per student)
# Task:
# Load all three files into Pandas DataFrames.
# Merge them into a single DataFrame with columns: Name, Marks, Attendance, Bonus.
# Create a scatter plot of Marks vs Attendance and highlight students with attendance < 70%.
# Apply one-hot encoding on Name.

import pandas as pd
import matplotlib.pyplot as plt

# Load files
students = pd.read_csv("student.csv")
attendance = pd.read_json("attendance.json")
extra = pd.read_excel("extra.xlsx")

# Merge DataFrames
df = students.merge(attendance, on="Name")
df = df.merge(extra, on="Name")

print("Merged DataFrame:")
print(df)

# Identify students with attendance below 70%
low_attendance = df["Attendance"] < 70

# Scatter Plot
plt.figure(figsize=(8, 5))

# Students with attendance >= 70%
plt.scatter(
    df.loc[~low_attendance, "Marks"],
    df.loc[~low_attendance, "Attendance"],
    label="Attendance >= 70%"
)

# Highlight students with attendance < 70%
plt.scatter(
    df.loc[low_attendance, "Marks"],
    df.loc[low_attendance, "Attendance"],
    marker="x",
    s=100,
    label="Attendance < 70%"
)

plt.xlabel("Marks")
plt.ylabel("Attendance (%)")
plt.title("Marks vs Attendance")
plt.legend()
plt.grid(True)
plt.show()

# One-Hot Encoding on Name
encoded_df = pd.get_dummies(df, columns=["Name"])

print("\nOne-Hot Encoded DataFrame:")
print(encoded_df)