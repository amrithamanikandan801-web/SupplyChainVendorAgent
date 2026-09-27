Sure 👍 You mean remove the **horizontal lines / separator lines** from the README. Here is the clean version without those lines:

# AI-Driven Supply Chain Intelligence and Automated Vendor Compliance Evaluation System

## 📌 Overview

The **AI-Driven Supply Chain Intelligence and Automated Vendor Compliance Evaluation System** is a Python-based project that integrates **Machine Learning, Data Analytics, Vendor Evaluation, Contract Analysis, and Compliance Risk Detection** into a single platform.

The system analyzes shipment data to identify delays and predict future shipment delays using a **Random Forest Classifier**. It also evaluates vendor performance using a weighted scoring method and analyzes procurement contracts to extract important terms and identify predefined compliance risks.

An interactive **Streamlit dashboard** is provided to visualize the results and generate consolidated supply chain reports.

## 🎯 Objectives

* Analyze historical shipment and logistics data.
* Identify delayed and on-time shipments.
* Predict shipment delays using Machine Learning.
* Evaluate vendors based on delivery, quality, cost, and compliance.
* Extract important information from procurement contracts.
* Detect predefined compliance-related clauses.
* Identify potential compliance risks.
* Integrate all results through a Supply Chain Intelligence Agent.
* Provide an interactive dashboard for analysis and reporting.

## 🚀 Features

### 🚚 Shipment Delay Prediction

Uses a **Random Forest Classifier** to predict whether a shipment is likely to be delayed.

### 🏢 Vendor Evaluation

Calculates vendor performance using:

* Delivery Score – 25%
* Quality Score – 25%
* Cost Score – 20%
* Compliance Score – 30%

### 📄 Contract Analysis

Extracts important contract information such as:

* Delivery period
* Payment period
* Termination notice
* Delay notification period

### ⚠️ Compliance Risk Detection

Checks predefined contract clauses including:

* Confidentiality
* Insurance
* Applicable laws and regulations
* Delivery delay notification

### 🧠 Supply Chain Intelligence Agent

Combines **Shipment Analysis, Delay Prediction, Vendor Evaluation, Contract Analysis, and Compliance Detection** into a consolidated supply chain report.

### 📊 Streamlit Dashboard

Provides an interactive interface for viewing project results and performing supply chain analysis.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Random Forest
* Joblib
* Regular Expressions (Regex)
* Streamlit
* Git & GitHub

## 📂 Project Structure

```text
SupplyChainVendorAgent/
│
├── app.py
│
├── data/
│   ├── shipping_data.csv
│   ├── vendors.csv
│   └── vendor_evaluation.py
│
├── contracts/
│   └── vendor_A.txt
│
├── models/
│   └── delay_model.pkl
│
└── src/
    ├── data_preprocessing.py
    ├── delay_prediction.py
    ├── contract_parser.py
    ├── compliance_agent.py
    └── supply_chain_agent.py
```

## 📊 Project Results

### Shipment Analysis

* **Total Shipments:** 15
* **Delayed Shipments:** 11
* **On-Time Shipments:** 4
* **Delay Rate:** 73.33%

### Machine Learning

* **Algorithm:** Random Forest Classifier
* **Number of Estimators:** 100
* **Test Size:** 20%
* **Model Accuracy:** 100% on the current held-out test split

> The current dataset contains only 15 records, so this accuracy result is suitable for the prototype but does not establish real-world model performance.

### Contract Analysis

The sample contract contains:

* Delivery Period: **7 business days**
* Payment Period: **30 days**
* Termination Notice: **30 days**
* Delay Notification: **24 hours**

### Compliance Analysis

* **Missing Required Clauses:** 0
* **Project-defined Compliance Risk:** LOW

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/SupplyChainVendorAgent.git
```

### 2. Open the Project

Open the project in **PyCharm**.

### 3. Install Required Packages

```bash
pip install pandas scikit-learn joblib streamlit
```

### 4. Run the Application

```bash
streamlit run app.py
```

The Streamlit dashboard will open in your browser.

## 🔄 System Workflow

```text
Shipment Data
      ↓
Data Preprocessing
      ↓
Shipment Delay Analysis
      ↓
Random Forest Prediction
      ↓
Vendor Evaluation
      ↓
Contract Parsing
      ↓
Compliance Risk Detection
      ↓
Supply Chain Intelligence Agent
      ↓
Streamlit Dashboard
      ↓
Reports
```

## 🔮 Future Enhancements

* Larger real-world datasets
* Advanced Machine Learning models
* Cross-validation
* Explainable AI
* Real-time GPS tracking
* Weather and traffic API integration
* NLP/Transformer-based contract analysis
* PDF/DOCX contract support
* Database integration
* User authentication
* Cloud deployment
* Automated email alerts

## ⚠️ Limitations

* Uses a small prototype dataset.
* Real-time logistics data is not currently integrated.
* Contract analysis uses Regex and predefined rules.
* Compliance detection is a basic screening mechanism and is **not legal advice**.
* Data is currently stored using CSV and TXT files.


