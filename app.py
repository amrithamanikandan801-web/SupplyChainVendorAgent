import streamlit as st
import pandas as pd
import joblib
import sys
from pathlib import Path
from io import BytesIO

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent
SRC_DIR = PROJECT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from contract_parser import (
    read_contract,
    extract_contract_information
)

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Supply Chain Intelligence Platform",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    font-weight: 700;
}

h2 {
    font-weight: 650;
}

h3 {
    font-weight: 600;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.agent-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #dbe3ef;
    margin-top: 15px;
}

.report-box {
    background: #f8fafc;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #2563eb;
}

.small-text {
    color: #64748b;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================

shipping_file = PROJECT_DIR / "data" / "shipping_data.csv"
vendor_file = PROJECT_DIR / "data" / "vendors.csv"
model_file = PROJECT_DIR / "models" / "delay_model.pkl"

shipping = pd.read_csv(shipping_file)
vendors = pd.read_csv(vendor_file)
model = joblib.load(model_file)

# ============================================================
# SHIPPING DELAY CALCULATION
# ============================================================

shipping["delay"] = (
    shipping["actual_days"] > shipping["planned_days"]
).astype(int)

total_shipments = len(shipping)

delayed_shipments = int(
    shipping["delay"].sum()
)

on_time_shipments = (
    total_shipments - delayed_shipments
)

delay_percentage = (
    delayed_shipments / total_shipments
) * 100

# ============================================================
# VENDOR EVALUATION
# ============================================================

vendors["vendor_score"] = (
    vendors["delivery_score"] * 0.25
    + vendors["quality_score"] * 0.25
    + vendors["cost_score"] * 0.20
    + vendors["compliance_score"] * 0.30
)

vendors["vendor_score"] = vendors["vendor_score"].round(2)

# ============================================================
# CONTRACT ANALYSIS
# ============================================================

contract_text = read_contract()

contract_info = extract_contract_information(
    contract_text
)

required_clauses = [
    "confidentiality",
    "insurance",
    "applicable laws",
    "delivery delay"
]

compliance_results = []

for clause in required_clauses:

    if clause.lower() in contract_text.lower():
        status = "PRESENT"
    else:
        status = "MISSING"

    compliance_results.append({
        "Clause": clause.title(),
        "Status": status
    })

missing_clauses = sum(
    1
    for item in compliance_results
    if item["Status"] == "MISSING"
)

if missing_clauses == 0:
    compliance_risk = "LOW"

elif missing_clauses <= 2:
    compliance_risk = "MEDIUM"

else:
    compliance_risk = "HIGH"

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📦 SCIA")

st.sidebar.caption(
    "Supply Chain Intelligence Agent"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Executive Dashboard",
        "🚚 Shipment Intelligence",
        "🏢 Vendor Intelligence",
        "📄 Contract Intelligence",
        "🤖 AI Delay Prediction",
        "🧠 Supply Chain Agent",
        "📥 Reports"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("System Status")

st.sidebar.success("✓ Shipping Data Loaded")
st.sidebar.success("✓ Vendor Data Loaded")
st.sidebar.success("✓ ML Model Loaded")
st.sidebar.success("✓ Compliance Engine Active")

st.sidebar.divider()

st.sidebar.caption(
    "Supply Chain Intelligence Platform"
)

# ============================================================
# HEADER
# ============================================================

st.title(
    "📦 Supply Chain Intelligence Platform"
)

st.caption(
    "AI-assisted logistics analytics • Vendor evaluation • "
    "Procurement contract compliance"
)

st.divider()

# ============================================================
# EXECUTIVE METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Shipments",
        total_shipments
    )

with col2:
    st.metric(
        "Delayed Shipments",
        delayed_shipments
    )

with col3:
    st.metric(
        "On-Time Shipments",
        on_time_shipments
    )

with col4:
    st.metric(
        "Delay Rate",
        f"{delay_percentage:.2f}%"
    )

# ============================================================
# 1. EXECUTIVE DASHBOARD
# ============================================================

if page == "🏠 Executive Dashboard":

    st.header("Executive Dashboard")

    st.write(
        "High-level overview of logistics, vendor and "
        "contract intelligence."
    )

    st.divider()

    col1, col2 = st.columns(2)

    # Shipment chart
    with col1:

        st.subheader("🚚 Shipment Performance")

        shipment_chart = pd.DataFrame({
            "Status": [
                "Delayed",
                "On Time"
            ],
            "Shipments": [
                delayed_shipments,
                on_time_shipments
            ]
        })

        st.bar_chart(
            shipment_chart.set_index("Status")
        )

    # Vendor chart
    with col2:

        st.subheader("🏢 Vendor Scores")

        vendor_chart = vendors[
            ["vendor_name", "vendor_score"]
        ].set_index("vendor_name")

        st.bar_chart(vendor_chart)

    st.divider()

    # Delay factors
    st.subheader("📊 Operational Delay Factors")

    factor_data = pd.DataFrame({
        "Factor": [
            "Weather",
            "Traffic",
            "Warehouse Delay",
            "Customs Delay"
        ],
        "Average": [
            shipping["weather_score"].mean(),
            shipping["traffic_score"].mean(),
            shipping["warehouse_delay_hours"].mean(),
            shipping["customs_delay_hours"].mean()
        ]
    })

    factor_data["Average"] = factor_data[
        "Average"
    ].round(2)

    st.bar_chart(
        factor_data.set_index("Factor")
    )

    st.divider()

    # Contract risk
    st.subheader("📄 Contract Compliance Status")

    if compliance_risk == "LOW":

        st.success(
            "LOW COMPLIANCE RISK — Required clauses detected."
        )

    elif compliance_risk == "MEDIUM":

        st.warning(
            "MEDIUM COMPLIANCE RISK — Review required."
        )

    else:

        st.error(
            "HIGH COMPLIANCE RISK — Missing clauses detected."
        )

# ============================================================
# 2. SHIPMENT INTELLIGENCE
# ============================================================

elif page == "🚚 Shipment Intelligence":

    st.header("🚚 Shipment Intelligence")

    st.write(
        "Analyze historical logistics tracking information "
        "and identify shipment delays."
    )

    st.divider()

    st.subheader("Shipment Dataset")

    st.dataframe(
        shipping,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📈 Planned vs Actual Delivery")

    delivery_chart = shipping[
        [
            "shipment_id",
            "planned_days",
            "actual_days"
        ]
    ].set_index("shipment_id")

    st.line_chart(delivery_chart)

    st.divider()

    st.subheader("🚨 Delayed Shipments")

    delayed_data = shipping[
        shipping["delay"] == 1
    ]

    st.dataframe(
        delayed_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Operational Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Average Distance",
            f"{shipping['distance_km'].mean():.1f} km"
        )

    with col2:

        st.metric(
            "Average Warehouse Delay",
            f"{shipping['warehouse_delay_hours'].mean():.1f} hrs"
        )

    with col3:

        st.metric(
            "Average Customs Delay",
            f"{shipping['customs_delay_hours'].mean():.1f} hrs"
        )

# ============================================================
# 3. VENDOR INTELLIGENCE
# ============================================================

elif page == "🏢 Vendor Intelligence":

    st.header("🏢 Vendor Intelligence")

    st.write(
        "Evaluate vendors using delivery, quality, cost "
        "and compliance performance."
    )

    st.divider()

    vendor_display = vendors[
        [
            "vendor_id",
            "vendor_name",
            "delivery_score",
            "quality_score",
            "cost_score",
            "compliance_score",
            "vendor_score"
        ]
    ].copy()

    st.dataframe(
        vendor_display,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Vendor Score Comparison")

    vendor_chart = vendors[
        ["vendor_name", "vendor_score"]
    ].set_index("vendor_name")

    st.bar_chart(vendor_chart)

    st.divider()

    st.subheader("Selected Vendor Analysis")

    selected_vendor = st.selectbox(
        "Select Vendor",
        vendors["vendor_name"].tolist()
    )

    vendor = vendors[
        vendors["vendor_name"] == selected_vendor
    ].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Delivery",
            vendor["delivery_score"]
        )

    with col2:
        st.metric(
            "Quality",
            vendor["quality_score"]
        )

    with col3:
        st.metric(
            "Cost",
            vendor["cost_score"]
        )

    with col4:
        st.metric(
            "Compliance",
            vendor["compliance_score"]
        )

    st.info(
        f"Calculated Vendor Score: "
        f"{vendor['vendor_score']:.2f}"
    )

# ============================================================
# 4. CONTRACT INTELLIGENCE
# ============================================================

elif page == "📄 Contract Intelligence":

    st.header("📄 Procurement Contract Intelligence")

    st.write(
        "Extract contractual terms and identify "
        "potential compliance risks."
    )

    st.divider()

    # Upload
    st.subheader("📤 Upload Contract")

    uploaded_file = st.file_uploader(
        "Upload a TXT contract",
        type=["txt"]
    )

    if uploaded_file is not None:

        uploaded_text = uploaded_file.read().decode(
            "utf-8"
        )

        st.success(
            "Contract uploaded successfully."
        )

        active_contract = uploaded_text

        active_info = extract_contract_information(
            active_contract
        )

    else:

        active_contract = contract_text
        active_info = contract_info

        st.info(
            "Using the default vendor_A.txt contract."
        )

    st.divider()

    st.subheader("Extracted Contract Terms")

    contract_table = pd.DataFrame(
        list(active_info.items()),
        columns=[
            "Contract Term",
            "Value"
        ]
    )

    st.dataframe(
        contract_table,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Compliance Clause Assessment")

    active_results = []

    for clause in required_clauses:

        if clause.lower() in active_contract.lower():

            status = "PRESENT"

        else:

            status = "MISSING"

        active_results.append({
            "Clause": clause.title(),
            "Status": status
        })

    active_table = pd.DataFrame(
        active_results
    )

    st.dataframe(
        active_table,
        use_container_width=True,
        hide_index=True
    )

    active_missing = sum(
        1
        for item in active_results
        if item["Status"] == "MISSING"
    )

    st.divider()

    st.subheader("⚖️ Compliance Risk")

    if active_missing == 0:

        st.success(
            "LOW RISK — Required clauses are present."
        )

    elif active_missing <= 2:

        st.warning(
            "MEDIUM RISK — Some clauses require review."
        )

    else:

        st.error(
            "HIGH RISK — Multiple clauses are missing."
        )

    st.divider()

    st.subheader("Original Contract")

    st.text_area(
        "Contract Content",
        active_contract,
        height=300
    )

# ============================================================
# 5. AI DELAY PREDICTION
# ============================================================

elif page == "🤖 AI Delay Prediction":

    st.header("🤖 AI Shipment Delay Prediction")

    st.write(
        "Use the trained Random Forest model to estimate "
        "whether a shipment may be delayed."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        distance = st.number_input(
            "Distance (km)",
            min_value=1,
            value=800
        )

        weather = st.slider(
            "Weather Score",
            1,
            5,
            2
        )

        traffic = st.slider(
            "Traffic Score",
            1,
            5,
            5
        )

    with col2:

        warehouse_delay = st.number_input(
            "Warehouse Delay (hours)",
            min_value=0,
            value=4
        )

        customs_delay = st.number_input(
            "Customs Delay (hours)",
            min_value=0,
            value=2
        )

        planned_days = st.number_input(
            "Planned Delivery Days",
            min_value=1,
            value=3
        )

    st.divider()

    if st.button(
        "🔮 Predict Shipment Delay",
        use_container_width=True
    ):

        shipment = pd.DataFrame(
            [[
                distance,
                weather,
                traffic,
                warehouse_delay,
                customs_delay,
                planned_days
            ]],
            columns=[
                "distance_km",
                "weather_score",
                "traffic_score",
                "warehouse_delay_hours",
                "customs_delay_hours",
                "planned_days"
            ]
        )

        prediction = model.predict(
            shipment
        )

        probability = model.predict_proba(
            shipment
        )[0][1]

        st.divider()

        if prediction[0] == 1:

            st.error(
                "⚠️ PREDICTED STATUS: DELAY"
            )

        else:

            st.success(
                "✅ PREDICTED STATUS: ON TIME"
            )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Delay Probability",
                f"{probability * 100:.2f}%"
            )

        with col2:

            st.metric(
                "On-Time Probability",
                f"{(1 - probability) * 100:.2f}%"
            )

# ============================================================
# 6. SUPPLY CHAIN AGENT
# ============================================================

elif page == "🧠 Supply Chain Agent":

    st.header("🧠 Supply Chain Intelligence Agent")

    st.write(
        "Automated multi-stage analysis combining "
        "shipment intelligence, machine learning, "
        "vendor evaluation and contract compliance."
    )

    st.divider()

    st.subheader("Agent Workflow")

    st.info(
        "Shipping Data → Delay Analysis → ML Prediction → "
        "Vendor Evaluation → Contract Parsing → "
        "Compliance Analysis → Intelligence Report"
    )

    st.divider()

    if st.button(
        "🚀 Run Supply Chain Agent",
        use_container_width=True
    ):

        with st.spinner(
            "Supply Chain Agent is analyzing the system..."
        ):

            # -----------------------------------------
            # STEP 1
            # -----------------------------------------

            shipment_delay_rate = (
                shipping["delay"].mean() * 100
            )

            # -----------------------------------------
            # STEP 2
            # -----------------------------------------

            sample = pd.DataFrame(
                [[
                    800,
                    2,
                    5,
                    4,
                    2,
                    3
                ]],
                columns=[
                    "distance_km",
                    "weather_score",
                    "traffic_score",
                    "warehouse_delay_hours",
                    "customs_delay_hours",
                    "planned_days"
                ]
            )

            prediction = model.predict(
                sample
            )[0]

            prediction_probability = model.predict_proba(
                sample
            )[0][1]

            # -----------------------------------------
            # STEP 3
            # -----------------------------------------

            highest_vendor = vendors.loc[
                vendors["vendor_score"].idxmax()
            ]

            # -----------------------------------------
            # STEP 4
            # -----------------------------------------

            agent_results = pd.DataFrame({
                "Analysis Area": [
                    "Shipment Monitoring",
                    "Delay Prediction",
                    "Vendor Evaluation",
                    "Contract Parsing",
                    "Compliance Monitoring"
                ],
                "Result": [
                    f"{shipment_delay_rate:.2f}% historical delay rate",
                    "DELAY" if prediction == 1 else "ON TIME",
                    f"{highest_vendor['vendor_name']} - "
                    f"{highest_vendor['vendor_score']:.2f}",
                    "Contract terms extracted",
                    f"{compliance_risk} compliance risk"
                ]
            })

        st.success(
            "Supply Chain Agent analysis completed."
        )

        st.divider()

        st.subheader("🧠 Agent Intelligence Report")

        st.dataframe(
            agent_results,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("Key Findings")

        if shipment_delay_rate > 50:

            st.warning(
                f"Shipment analysis detected a "
                f"{shipment_delay_rate:.2f}% historical delay rate."
            )

        else:

            st.success(
                "Historical shipment delay rate is below 50%."
            )

        if prediction == 1:

            st.warning(
                f"ML model predicts DELAY for the "
                f"sample shipment with a delay probability "
                f"of {prediction_probability * 100:.2f}%."
            )

        else:

            st.success(
                f"ML model predicts ON TIME for the "
                f"sample shipment with an on-time probability "
                f"of {(1 - prediction_probability) * 100:.2f}%."
            )

        st.info(
            f"Vendor analysis calculated a score of "
            f"{highest_vendor['vendor_score']:.2f} for "
            f"{highest_vendor['vendor_name']}."
        )

        if compliance_risk == "LOW":

            st.success(
                "Contract analysis detected no missing "
                "required clauses in the current contract."
            )

        elif compliance_risk == "MEDIUM":

            st.warning(
                "Contract analysis identified clauses "
                "requiring additional review."
            )

        else:

            st.error(
                "Contract analysis identified multiple "
                "missing compliance clauses."
            )

        st.divider()

        st.subheader("Agent Summary")

        summary = f"""
SUPPLY CHAIN INTELLIGENCE REPORT

Shipment Monitoring
-------------------
Total Shipments: {total_shipments}
Delayed Shipments: {delayed_shipments}
On-Time Shipments: {on_time_shipments}
Historical Delay Rate: {shipment_delay_rate:.2f}%

Machine Learning Prediction
---------------------------
Prediction: {"DELAY" if prediction == 1 else "ON TIME"}
Delay Probability: {prediction_probability * 100:.2f}%

Vendor Evaluation
-----------------
Highest Calculated Vendor Score:
{highest_vendor['vendor_name']}
Score: {highest_vendor['vendor_score']:.2f}

Contract Compliance
-------------------
Overall Risk: {compliance_risk}
Missing Required Clauses: {missing_clauses}

SYSTEM STATUS
-------------
Supply Chain Agent Analysis Completed
"""

        st.text_area(
            "Generated Intelligence Report",
            summary,
            height=350
        )

        st.download_button(
            "📥 Download Agent Report",
            summary,
            file_name="supply_chain_intelligence_report.txt",
            mime="text/plain",
            use_container_width=True
        )

# ============================================================
# 7. REPORTS
# ============================================================

elif page == "📥 Reports":

    st.header("📥 Reports & Data Export")

    st.write(
        "Download datasets and generated analytical reports."
    )

    st.divider()

    # Shipping CSV
    st.subheader("🚚 Shipment Report")

    shipping_csv = shipping.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Shipment CSV",
        shipping_csv,
        file_name="shipment_analysis.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # Vendor CSV
    st.subheader("🏢 Vendor Evaluation Report")

    vendor_csv = vendors.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Vendor CSV",
        vendor_csv,
        file_name="vendor_evaluation.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # Contract report
    st.subheader("📄 Contract Report")

    contract_report = f"""
PROCUREMENT CONTRACT COMPLIANCE REPORT

Extracted Terms
---------------

Delivery Period:
{contract_info["Delivery Period"]}

Payment Period:
{contract_info["Payment Period"]}

Termination Notice:
{contract_info["Termination Notice"]}

Delay Notification:
{contract_info["Delay Notification"]}

Compliance Risk:
{compliance_risk}

Missing Required Clauses:
{missing_clauses}
"""

    st.download_button(
        "Download Contract Report",
        contract_report,
        file_name="contract_compliance_report.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.divider()

    # Complete report
    st.subheader("🧠 Complete Supply Chain Report")

    complete_report = f"""
SUPPLY CHAIN INTELLIGENCE PLATFORM
===================================

SHIPMENT ANALYSIS
-----------------
Total Shipments: {total_shipments}
Delayed Shipments: {delayed_shipments}
On-Time Shipments: {on_time_shipments}
Delay Rate: {delay_percentage:.2f}%

VENDOR ANALYSIS
---------------
Number of Vendors: {len(vendors)}

CONTRACT ANALYSIS
-----------------
Delivery Period: {contract_info["Delivery Period"]}
Payment Period: {contract_info["Payment Period"]}
Termination Notice: {contract_info["Termination Notice"]}
Delay Notification: {contract_info["Delay Notification"]}

COMPLIANCE
----------
Overall Risk: {compliance_risk}
Missing Clauses: {missing_clauses}

SYSTEM
------
Supply Chain Intelligence Agent
Machine Learning + Vendor Analytics +
Contract Compliance
"""

    st.download_button(
        "📥 Download Complete Report",
        complete_report,
        file_name="complete_supply_chain_report.txt",
        mime="text/plain",
        use_container_width=True
    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Supply Chain Intelligence Platform | "
    "Machine Learning • Vendor Analytics • "
    "Contract Intelligence • Automated Agent"
)