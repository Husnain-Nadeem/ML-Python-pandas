#Name : Husnain Nadeem
#Reg no : 23-ntu-cs-1038
import pandas as pd
#create dataframe for dictionary

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Tokyo"],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print("Manual DataFrame:")
print(df)