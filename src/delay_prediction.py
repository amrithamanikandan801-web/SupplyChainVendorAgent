import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv("../data/shipping_data.csv")

# Create delay column
df["delay"] = 0

for i in range(len(df)):
    if df.loc[i, "actual_days"] > df.loc[i, "planned_days"]:
        df.loc[i, "delay"] = 1


# Select features
features = [
    "distance_km",
    "weather_score",
    "traffic_score",
    "warehouse_delay_hours",
    "customs_delay_hours",
    "planned_days"
]

X = df[features]
y = df["delay"]


# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create machine learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


# Test the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Supply Chain Delay Prediction")
print("=============================")

print("Model Accuracy:", accuracy)


# Save the trained model
joblib.dump(
    model,
    "../models/delay_model.pkl"
)

print("\nModel saved successfully!")