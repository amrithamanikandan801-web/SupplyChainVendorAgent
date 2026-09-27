# AI-Driven Supply Chain Intelligence and Automated Vendor Compliance Evaluation System

An intelligent supply chain analytics platform that combines **Machine Learning, Data Analytics, Vendor Evaluation, Contract Parsing, and Compliance Risk Detection** into a single interactive system.

The project is designed to analyze shipment data, predict potential delivery delays, evaluate vendor performance, extract important procurement contract information, and identify predefined compliance risks.

---

## 📌 Project Overview

Supply chain operations involve multiple activities such as shipment tracking, vendor management, procurement, and contract compliance.

This project provides an integrated solution that helps users:

* 🚚 Analyze shipment performance
* 🤖 Predict shipment delays using Machine Learning
* 🏢 Evaluate vendor performance
* 📄 Extract important information from procurement contracts
* ⚠️ Identify potential compliance risks
* 🧠 Combine results using a Supply Chain Intelligence Agent
* 📊 View insights through an interactive Streamlit dashboard
* 📥 Generate and download analytical reports

---

## 🎯 Objectives

* Analyze historical logistics and shipment data.
* Identify delayed and on-time shipments.
* Predict shipment delays using a **Random Forest Classifier**.
* Evaluate vendors based on delivery, quality, cost, and compliance.
* Calculate weighted vendor performance scores.
* Automatically extract important contract terms.
* Detect predefined compliance-related clauses.
* Identify potential contract compliance risks.
* Integrate all modules into a Supply Chain Intelligence Agent.
* Provide an interactive dashboard for supply chain analysis.

---

## 🚀 Key Features

### 1. Shipment Intelligence

Analyzes historical shipping data and calculates:

* Total shipments
* Delayed shipments
* On-time shipments
* Delay percentage
* Shipment-level delay status

### 2. AI-Based Delay Prediction

A **Random Forest Classifier** is trained using shipment-related features such as:

* Distance
* Weather score
* Traffic score
* Warehouse delay
* Customs delay
* Planned delivery days

The model predicts whether a shipment is likely to be:

**DELAY** or **ON-TIME**

### 3. Vendor Intelligence

Vendors are evaluated using four parameters:

| Parameter        | Weight |
| ---------------- | -----: |
| Delivery Score   |    25% |
| Quality Score    |    25% |
| Cost Score       |    20% |
| Compliance Score |    30% |

The project-defined vendor score is calculated as:

```text
Vendor Score =
(0.25 × Delivery) +
(0.25 × Quality) +
(0.20 × Cost) +
(0.30 × Compliance)
```

### 4. Contract Intelligence

The system processes procurement contract text and extracts important information such as:

* Delivery period
* Payment period
* Termination notice
* Delivery delay notification period

### 5. Compliance Risk Detection

The system checks for predefined clauses including:

* Confidentiality
* Insurance
* Applicable laws and regulations
* Delivery delay notification

The project uses a simple rule-based screening approach:

```text
0 missing clauses      → LOW
1–2 missing clauses    → MEDIUM
More than 2 missing   → HIGH
```

> **Note:** This compliance classification is a project-defined screening heuristic and is not a substitute for professional legal review.

### 6. Supply Chain Intelligence Agent

The agent integrates the outputs from:

```text
Shipment Analysis
        ↓
Delay Prediction
        ↓
Vendor Evaluation
        ↓
Contract Analysis
        ↓
Compliance Detection
        ↓
Integrated Supply Chain Report
```

### 7. Interactive Streamlit Dashboard

The dashboard provides separate sections for:

* 🏠 Executive Dashboard
* 🚚 Shipment Intelligence
* 🏢 Vendor Intelligence
* 📄 Contract Intelligence
* 🤖 AI Delay Prediction
* 🧠 Supply Chain Intelligence Agent
* 📥 Reports

---

## 🛠️ Technologies Used

| Technology          | Purpose                         |
| ------------------- | ------------------------------- |
| Python              | Core development                |
| Pandas              | Data processing and analysis    |
| Scikit-learn        | Machine Learning                |
| Random Forest       | Shipment delay prediction       |
| Joblib              | Model saving and loading        |
| Regular Expressions | Contract information extraction |
| Streamlit           | Interactive dashboard           |
| Git & GitHub        | Version control                 |

---

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

---

## 📊 Dataset

The prototype uses:

* **15 shipment records**
* **8 vendor records**
* **1 sample procurement contract**

### Shipment Analysis

| Metric            | Result |
| ----------------- | -----: |
| Total Shipments   |     15 |
| Delayed Shipments |     11 |
| On-Time Shipments |      4 |
| Delay Rate        | 73.33% |

---

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for shipment delay prediction.

### Model Configuration

```text
Algorithm: Random Forest Classifier
Number of Estimators: 100
Test Size: 20%
Random State: 42
```

### Current Prototype Result

```text
Model Accuracy: 100%
```

The reported accuracy is based on the current held-out test split. Since the prototype dataset contains only 15 records, the result should **not be interpreted as evidence of general real-world performance**. A larger dataset and cross-validation would be required for reliable evaluation.

---

## 🏢 Vendor Evaluation Results

| Vendor             | Score |
| ------------------ | ----: |
| Alpha Logistics    | 88.25 |
| Beta Suppliers     | 79.25 |
| Gamma Industries   | 87.00 |
| Delta Traders      | 70.75 |
| Epsilon Exports    | 83.90 |
| Zeta Manufacturing | 81.95 |
| Omega Supplies     | 81.00 |
| Prime Logistics    | 91.45 |

---

## 📄 Contract Analysis Result

The sample procurement contract contains:

```text
Delivery Period       : 7 business days
Payment Period        : 30 days
Termination Notice    : 30 days
Delay Notification    : 24 hours
```

### Compliance Result

```text
Missing Required Clauses : 0
Overall Risk             : LOW
```

The risk level is generated using the project's predefined rule-based screening logic.

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/SupplyChainVendorAgent.git
```

### Step 2: Open the Project

Open the project in **PyCharm** or another Python IDE.

### Step 3: Install Dependencies

```bash
pip install pandas scikit-learn joblib streamlit
```

### Step 4: Run the Dashboard

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## ▶️ Running Individual Modules

### Data Preprocessing

```bash
python src/data_preprocessing.py
```

### Train Delay Prediction Model

```bash
python src/delay_prediction.py
```

### Contract Parser

```bash
python src/contract_parser.py
```

### Compliance Agent

```bash
python src/compliance_agent.py
```

### Supply Chain Intelligence Agent

```bash
python src/supply_chain_agent.py
```

---

## 🔄 System Workflow

```text
                ┌──────────────────────┐
                │   Shipment Dataset   │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Data Preprocessing   │
                └──────────┬───────────┘
                           ↓
                ┌──────────────────────┐
                │ Random Forest Model  │
                └──────────┬───────────┘
                           ↓
                  Delay Prediction
                           │
                           │
┌──────────────────────────┼─────────────────────────┐
│                          │                         │
↓                          ↓                         ↓
Vendor Data            Contract Data           Shipment Data
│                          │                         │
↓                          ↓                         ↓
Vendor Scoring        Contract Parsing       Delay Analysis
│                          │                         │
↓                          ↓                         ↓
Vendor Insights       Compliance Check        ML Prediction
└──────────────────────────┼─────────────────────────┘
                           ↓
             Supply Chain Intelligence Agent
                           ↓
                  Streamlit Dashboard
                           ↓
                  Integrated Reports
```

---

## 📸 Dashboard

The Streamlit dashboard provides:

* Executive-level shipment metrics
* Shipment delay analysis
* Vendor performance comparison
* Contract information extraction
* AI delay prediction
* Compliance risk analysis
* Integrated Supply Chain Agent results
* Downloadable reports

Add your project screenshots below:

```text
screenshots/
├── dashboard.png
├── shipment-intelligence.png
├── vendor-intelligence.png
├── contract-intelligence.png
├── delay-prediction.png
└── supply-chain-agent.png
```

---

## 🔮 Future Enhancements

The project can be extended with:

* Larger real-world shipment datasets
* Cross-validation and advanced model evaluation
* XGBoost and other ML algorithms
* Explainable AI using SHAP
* Real-time GPS tracking
* Live weather and traffic APIs
* Automated shipment alerts
* NLP/Transformer-based contract analysis
* PDF and DOCX contract support
* Database integration
* User authentication and role-based access
* Cloud deployment
* Email notifications
* Advanced supplier risk analytics

---

## ⚠️ Limitations

* The current prototype uses a small sample dataset.
* Real-time logistics APIs are not integrated.
* Contract parsing currently uses regular expressions and predefined rules.
* Compliance detection is a basic screening mechanism.
* The system does not provide legal advice.
* Shipment data is stored in CSV format.
* Authentication and role-based access are not currently implemented.

---

## 🎓 Academic Project

**Project Title:**
AI-Driven Supply Chain Intelligence and Automated Vendor Compliance Evaluation System

**Domain:**
Data Analytics, Business Analytics, Machine Learning & Supply Chain Intelligence

**Development Environment:**
PyCharm

**Application Framework:**
Streamlit

---

## 👩‍💻 Author

**Amritha Manikandan**
B.Tech – Computer Science and Business Systems (CSBS)

---

## 📜 License

This project is developed for **academic and educational purposes**.
