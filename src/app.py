from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from src.detector import detect_leaks

app = FastAPI()

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load sample data
def load_data():
    return pd.read_csv("data/servers_usage.csv", nrows=1000)

@app.get("/")
def home():
    return {"message": "Cloud Cost Leak Detection API Running"}

# 1. Get all resources
@app.get("/resources")
def get_resources():
    df = load_data()
    return df.to_dict(orient="records")

# 2. Detect leaks
@app.get("/detect-leaks")
def detect():
    df = load_data()
    result = detect_leaks(df)

    alerts = result[
        ['server_id', 'vcpu_usage', 'ram_usage', 'cost_per_hour', 'alert']
    ]

    return alerts.to_dict(orient="records")

# 3. Recommendations
@app.get("/recommendations")
def recommendations():
    return {
        "suggestions": [
            "Terminate unused VMs",
            "Reduce overprovisioned resources",
            "Scale down low-utilization servers",
            "Monitor high utilization instances"
        ]
    }

# 4. Potential savings
@app.get("/potential-savings")
def savings():
    df = load_data()
    result = detect_leaks(df)

    leak_count = len(result[result["alert"] != "Normal"])
    estimated_savings = leak_count * 2.5

    return {
        "leak_resources": leak_count,
        "estimated_savings_per_hour_usd": estimated_savings
    }