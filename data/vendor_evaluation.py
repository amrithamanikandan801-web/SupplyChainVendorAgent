import pandas as pd

# Load vendor data
df = pd.read_csv("../data/vendors.csv")

# Calculate vendor score
df["vendor_score"] = (
    df["delivery_score"] * 0.25
    + df["quality_score"] * 0.25
    + df["cost_score"] * 0.20
    + df["compliance_score"] * 0.30
)

# Display vendor evaluation
print("VENDOR EVALUATION")
print("==================")

for i in range(len(df)):
    print(
        df.loc[i, "vendor_id"],
        "-",
        df.loc[i, "vendor_name"],
        "- Score:",
        round(df.loc[i, "vendor_score"], 2)
    )

print("\nEvaluation completed successfully!")