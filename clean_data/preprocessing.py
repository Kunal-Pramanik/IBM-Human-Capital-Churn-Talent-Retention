import pandas as pd

df = pd.read_csv("IBM_HR_Data_Enterprise.csv")

print("Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Save verified dataset
df.to_csv("IBM_HR_Data_Enterprise_Clean.csv", index=False)
print("Clean dataset exported.")
