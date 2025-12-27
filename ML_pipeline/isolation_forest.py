import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/features.csv")

X = df.drop(columns=["ip.src"])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(contamination=0.08, random_state=42)
df["if_anomaly"] = model.fit_predict(X_scaled)
df["if_score"] = model.decision_function(X_scaled)

# SAVE MODELS
joblib.dump(model, "models/iforest.pkl")
joblib.dump(scaler, "models/scaler.pkl")

df.to_csv("data/if_results.csv", index=False)
print("Isolation Forest trained & saved.")
