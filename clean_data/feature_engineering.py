import pandas as pd

df = pd.read_csv("IBM_HR_Data_Enterprise.csv")

# Example engineered feature
df["HighIncomeFlag"] = (df["MonthlyIncome"] > df["MonthlyIncome"].median()).astype(int)

# Attrition rate by department
summary = df.groupby("Department")["AttritionFlag"].mean().reset_index()

print(summary.head())

df.to_csv("IBM_HR_Data_Featured.csv", index=False)
