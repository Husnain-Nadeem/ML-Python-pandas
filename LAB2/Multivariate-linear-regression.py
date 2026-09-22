import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load dataset from the same folder
df = pd.read_csv("Admission_Predict.csv")

# Check column names
print("Columns:", df.columns.tolist())

# Remove Serial Number column
if 'Serial No.' in df.columns:
    df.drop('Serial No.', axis=1, inplace=True)
elif 'Serial#' in df.columns:
    df.drop('Serial#', axis=1, inplace=True)

# Target variable
if 'Chance of Admit ' in df.columns:
    y = df['Chance of Admit ']
    df.drop('Chance of Admit ', axis=1, inplace=True)
else:
    y = df['Chance of Admit']
    df.drop('Chance of Admit', axis=1, inplace=True)

# ----------------------------
# Simple Linear Regression
# ----------------------------

simple_lr = LinearRegression()
simple_lr.fit(df[['GRE Score']], y)

plt.figure(figsize=(8, 5))
plt.scatter(
    df['GRE Score'],
    y,
    color='green',
    alpha=0.5,
    label='Actual Data'
)

plt.plot(
    df['GRE Score'],
    simple_lr.predict(df[['GRE Score']]),
    color='red',
    linewidth=3,
    label='Regression Line'
)

plt.xlabel('GRE Score')
plt.ylabel('Admission Chance')
plt.title('GRE Score vs Admission Chance')
plt.legend()
plt.show()

# ----------------------------
# Train/Test Split
# ----------------------------

x_train, x_test, y_train, y_test = train_test_split(
    df,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------
# Multivariate Linear Regression
# ----------------------------

lr = LinearRegression()
lr.fit(x_train, y_train)

# Predictions
pred = lr.predict(x_test)

# Feature Importance Plot
coefficients = lr.coef_
features = df.columns

plt.figure(figsize=(8, 5))
plt.barh(features, coefficients)
plt.xlabel('Coefficient Value (Weight)')
plt.title('Feature Importance in Multivariate Linear Regression')
plt.axvline(x=0)
plt.show()

# ----------------------------
# Model Evaluation
# ----------------------------

rmse = np.sqrt(metrics.mean_squared_error(y_test, pred))
print("RMSE:", rmse)

print("R² Score:", metrics.r2_score(y_test, pred))