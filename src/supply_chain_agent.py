import pandas as pd
import joblib

from contract_parser import read_contract, extract_contract_information


print("=" * 60)
print("        SUPPLY CHAIN VENDOR INTELLIGENCE AGENT")
print("=" * 60)


# --------------------------------------------------
# 1. SHIPPING DELAY ANALYSIS
# --------------------------------------------------

print("\n1. SHIPPING DELAY ANALYSIS")
print("--------------------------")

shipping_data = pd.read_csv("../data/shipping_data.csv")

shipping_data["delay"] = 0

for i in range(len(shipping_data)):
    if shipping_data.loc[i, "actual_days"] > shipping_data.loc[i, "planned_days"]:
        shipping_data.loc[i, "delay"] = 1


total_shipments = len(shipping_data)
delayed_shipments = shipping_data["delay"].sum()

delay_percentage = (delayed_shipments / total_shipments) * 100

print("Total Shipments:", total_shipments)
print("Delayed Shipments:", delayed_shipments)
print("Delay Percentage:", round(delay_percentage, 2), "%")


# --------------------------------------------------
# 2. LOAD MACHINE LEARNING MODEL
# --------------------------------------------------

print("\n2. DELAY PREDICTION MODEL")
print("-------------------------")

model = joblib.load("../models/delay_model.pkl")

print("Random Forest Model Loaded Successfully")


# Example shipment
new_shipment = [[
    800,     # distance
    2,       # weather score
    5,       # traffic score
    4,       # warehouse delay
    2,       # customs delay
    3        # planned days
]]

prediction = model.predict(new_shipment)

if prediction[0] == 1:
    print("Predicted Result: DELAY")
else:
    print("Predicted Result: ON TIME")


# --------------------------------------------------
# 3. VENDOR EVALUATION
# --------------------------------------------------

print("\n3. VENDOR EVALUATION")
print("--------------------")

vendors = pd.read_csv("../data/vendors.csv")

vendors["vendor_score"] = (
    vendors["delivery_score"] * 0.25
    + vendors["quality_score"] * 0.25
    + vendors["cost_score"] * 0.20
    + vendors["compliance_score"] * 0.30
)

for i in range(len(vendors)):

    print(
        vendors.loc[i, "vendor_id"],
        "-",
        vendors.loc[i, "vendor_name"],
        "- Score:",
        round(vendors.loc[i, "vendor_score"], 2)
    )


# --------------------------------------------------
# 4. CONTRACT ANALYSIS
# --------------------------------------------------

print("\n4. CONTRACT ANALYSIS")
print("--------------------")

contract_text = read_contract()

contract_information = extract_contract_information(
    contract_text
)

for key, value in contract_information.items():

    print(key + ":", value)


# --------------------------------------------------
# 5. COMPLIANCE ANALYSIS
# --------------------------------------------------

print("\n5. COMPLIANCE RISK ANALYSIS")
print("---------------------------")

required_clauses = [
    "confidentiality",
    "insurance",
    "applicable laws",
    "delivery delay"
]

risk_count = 0

for clause in required_clauses:

    if clause.lower() in contract_text.lower():

        print(clause, "-> PRESENT")

    else:

        print(clause, "-> MISSING")

        risk_count += 1


if risk_count == 0:

    overall_risk = "LOW"

elif risk_count <= 2:

    overall_risk = "MEDIUM"

else:

    overall_risk = "HIGH"


print("\nOverall Compliance Risk:", overall_risk)


# --------------------------------------------------
# 6. FINAL AGENT REPORT
# --------------------------------------------------

print("\n" + "=" * 60)
print("                 FINAL AGENT REPORT")
print("=" * 60)

print("Total Shipments:", total_shipments)
print("Delayed Shipments:", delayed_shipments)
print("Delay Percentage:", round(delay_percentage, 2), "%")

print("Predicted Shipment Status:",
      "DELAY" if prediction[0] == 1 else "ON TIME")

print("Contract Compliance Risk:", overall_risk)

print("\nVendor Scores:")

for i in range(len(vendors)):

    print(
        vendors.loc[i, "vendor_name"],
        "->",
        round(vendors.loc[i, "vendor_score"], 2)
    )


print("\nSupply Chain Intelligence Analysis Completed!")