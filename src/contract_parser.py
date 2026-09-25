import re
from pathlib import Path


# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Find the contract
contract_file = project_folder / "contracts" / "vendor_A.txt"


# Read the contract
def read_contract():

    with open(contract_file, "r", encoding="utf-8") as file:
        return file.read()


# Extract important information
def extract_contract_information(text):

    information = {}

    # Delivery period
    match = re.search(
        r"deliver.*?within\s+(\d+)\s+business days",
        text,
        re.IGNORECASE
    )

    if match:
        information["Delivery Period"] = match.group(1) + " business days"
    else:
        information["Delivery Period"] = "Not Found"


    # Payment period
    match = re.search(
        r"payment.*?within\s+(\d+)\s+days",
        text,
        re.IGNORECASE
    )

    if match:
        information["Payment Period"] = match.group(1) + " days"
    else:
        information["Payment Period"] = "Not Found"


    # Termination notice
    match = re.search(
        r"terminated.*?(\d+)\s+days",
        text,
        re.IGNORECASE
    )

    if match:
        information["Termination Notice"] = match.group(1) + " days"
    else:
        information["Termination Notice"] = "Not Found"


    # Delay notification
    match = re.search(
        r"notify.*?within\s+(\d+)\s+hours",
        text,
        re.IGNORECASE
    )

    if match:
        information["Delay Notification"] = match.group(1) + " hours"
    else:
        information["Delay Notification"] = "Not Found"


    return information


# Main program
print("CONTRACT PARSER")
print("================")

contract_text = read_contract()

print("\nContract loaded successfully!")

information = extract_contract_information(
    contract_text
)

print("\nExtracted Information")
print("=====================")

for key, value in information.items():

    print(key + ":", value)