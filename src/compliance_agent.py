from contract_parser import read_contract, extract_contract_information


# Required contract clauses
required_clauses = [
    "confidentiality",
    "insurance",
    "applicable laws",
    "delivery delay"
]


# Read contract
contract_text = read_contract()

# Extract contract information
information = extract_contract_information(contract_text)


print("VENDOR CONTRACT COMPLIANCE AGENT")
print("================================")


# Check required clauses
print("\nClause Compliance Check")
print("=======================")

for clause in required_clauses:

    if clause.lower() in contract_text.lower():

        print(clause, "-> PRESENT")

    else:

        print(clause, "-> MISSING")


# Risk analysis
print("\nCompliance Risk Analysis")
print("=======================")

risk_count = 0


if information["Delivery Period"] == "Not Found":
    print("HIGH RISK: Delivery period is missing.")
    risk_count += 1


if information["Payment Period"] == "Not Found":
    print("MEDIUM RISK: Payment terms are missing.")
    risk_count += 1


if information["Termination Notice"] == "Not Found":
    print("MEDIUM RISK: Termination notice is missing.")
    risk_count += 1


if information["Delay Notification"] == "Not Found":
    print("HIGH RISK: Delay notification clause is missing.")
    risk_count += 1


if "confidentiality" not in contract_text.lower():
    print("HIGH RISK: Confidentiality clause is missing.")
    risk_count += 1


if "insurance" not in contract_text.lower():
    print("HIGH RISK: Insurance clause is missing.")
    risk_count += 1


if "applicable laws" not in contract_text.lower():
    print("HIGH RISK: Legal compliance clause is missing.")
    risk_count += 1


if risk_count == 0:

    print("\nOverall Risk: LOW")

elif risk_count <= 2:

    print("\nOverall Risk: MEDIUM")

else:

    print("\nOverall Risk: HIGH")


print("\nCompliance analysis completed successfully!")