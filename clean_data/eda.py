import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("IBM_HR_Data_Enterprise.csv")

print(df.describe(include="all"))

# Attrition count
df["Attrition"].value_counts().plot(kind="bar", title="Attrition Distribution")
plt.tight_layout()
plt.savefig("attrition_distribution.png")

# Department-wise attrition
dept = df.groupby("Department")["AttritionFlag"].mean()
dept.plot(kind="bar", title="Department Attrition Rate")
plt.tight_layout()
plt.savefig("department_attrition.png")

print("EDA complete.")
