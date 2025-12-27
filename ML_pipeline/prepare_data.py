import pandas as pd

# Read CSV safely (handles malformed rows)
df = pd.read_csv(
    "data/traffic.csv",
    engine="python",
    on_bad_lines="skip"
)

# Fill missing values safely
df["http.request.uri"] = df["http.request.uri"].fillna("NO_HTTP")
df["tls.handshake.type"] = df["tls.handshake.type"].fillna(-1)
df["tcp.srcport"] = df["tcp.srcport"].fillna(-1)
df["tcp.dstport"] = df["tcp.dstport"].fillna(-1)
df["ip.src"] = df["ip.src"].fillna("UNKNOWN")
df["ip.dst"] = df["ip.dst"].fillna("UNKNOWN")

print("Cleaned dataset shape:", df.shape)
print(df.head())

df.to_csv("data/clean_traffic.csv", index=False)
