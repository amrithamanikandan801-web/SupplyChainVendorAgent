import pandas as pd
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the CSV file
csv_file = project_folder / "data" / "shipping_data.csv"

# Load the dataset
df = pd.read_csv(csv_file)

# Create delay column
df["delay"] = 0

for i in range(len(df)):
    if df.loc[i, "actual_days"] > df.loc[i, "planned_days"]:
        df.loc[i, "delay"] = 1

print("Shipping Dataset")
print("================")

print(df)

print("\nDelay Distribution")
print("==================")

print(df["delay"].value_counts())