import pandas as pd

df_if = pd.read_csv("data/if_results.csv")
df_ae = pd.read_csv("data/ae_results.csv")[["ip.src","ae_score"]]

df = df_if.merge(df_ae, on="ip.src")

df["risk_score"] = (
    (df["if_anomaly"] == -1).astype(int) * 0.6 +
    (df["ae_score"] > df["ae_score"].quantile(0.9)).astype(int) * 0.4
)

df["decision"] = df["risk_score"].apply(
    lambda x: "ALERT" if x >= 0.6 else "ALLOW"
)

df.to_csv("data/risk_scores.csv", index=False)
print(df[["ip.src","risk_score","decision"]].head())
