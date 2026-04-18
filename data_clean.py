import pandas as pd
import numpy as np

#loading the dataset 
df = pd.read_csv(r"E:\Maroof Python\project_1\Indian_Employee_Data.csv")
print(df.head())

#checking the missing values
print("Missing values in each column")
print(df.isnull().sum())


df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Performance_Rating'] = df['Performance_Rating'].fillna(df['Performance_Rating'].median())

df.replace([np.inf, -np.inf],np.nan, inplace=True)
df.fillna(df.select_dtypes(include=[np.number]).mean(), inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)

#replace negative salaries
df["Salary"]= np.where(df["Salary"] <0 ,df["Salary"].mean(), df["Salary"])
salary_mean= df["Salary"].mean()
salary_std= df["Salary"].std()
lower_bound= salary_mean - (3* salary_std)
upper_bound= salary_mean + (3* salary_std)

df= df[(df["Salary"]>=lower_bound) & df["Salary"]<=upper_bound]

df.to_csv('cleaned_indian_employee_data.csv',index=False)
print("data cleaning completed, saved as cleaned_indian_employee_data.csv")