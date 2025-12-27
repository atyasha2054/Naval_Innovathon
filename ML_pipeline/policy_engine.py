import pandas as pd

df = pd.read_csv("data/risk_scores.csv")

def explain(row):
    reasons = []
    if row["packet_count"] > 500:
        reasons.append("High traffic volume")
    if row["unique_dst_ports"] > 10:
        reasons.append("Port scanning behavior")
    if row["tls_handshake_events"] > 50:
        reasons.append("Abnormal TLS activity")
    return ", ".join(reasons)

def suggest_policy(row):
    if row["decision"] == "ALERT":
        if row["packet_count"] > 500:
            return "Apply rate limiting to source IP"
        if row["unique_dst_ports"] > 10:
            return "Block port scanning attempts"
        return "Monitor closely"
    return "Allow traffic"

df["explanation"] = df.apply(explain, axis=1)
df["recommended_policy"] = df.apply(suggest_policy, axis=1)

df.to_csv("data/policy_recommendations.csv", index=False)
print(df[["ip.src","decision","recommended_policy"]].head())
