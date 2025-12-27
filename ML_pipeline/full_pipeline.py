import os
import subprocess

PIPELINE_STEPS = [
    "prepare_data.py",
    "feature_engineering.py",
    "isolation_forest.py",
    "autoencoder.py",
    "risk_engine.py",
    "policy_engine.py"
]

def run_pipeline():
    for step in PIPELINE_STEPS:
        print(f"Running {step}...")
        subprocess.run(["python", f"src/{step}"], check=True)

if __name__ == "__main__":
    run_pipeline()
    print("\nPipeline completed successfully.")
