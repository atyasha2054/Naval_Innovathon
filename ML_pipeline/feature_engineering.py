import pandas as pd

df = pd.read_csv("data/clean_traffic.csv")

features = df.groupby("ip.src").agg(
    packet_count=("frame.time_epoch", "count"),
    unique_dst_ips=("ip.dst", "nunique"),
    unique_dst_ports=("tcp.dstport", "nunique"),
    tls_handshake_events=("tls.handshake.type", lambda x: (x != -1).sum()),
    http_request_count=("http.request.uri", lambda x: (x != "NO_HTTP").sum())
).reset_index()

print(features.head())
features.to_csv("data/features.csv", index=False)
