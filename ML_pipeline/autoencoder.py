import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
import joblib
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/features.csv")

X = df.drop(columns=["ip.src"]).values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "models/ae_scaler.pkl")

X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

class AutoEncoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 8),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(8, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))

model = AutoEncoder(X_tensor.shape[1])
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(400):
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# SAVE MODEL
torch.save(model.state_dict(), "models/autoencoder.pt")

df["ae_score"] = ((reconstructed - X_tensor) ** 2).mean(dim=1).detach().numpy()
df.to_csv("data/ae_results.csv", index=False)

print("Autoencoder trained & saved.")
