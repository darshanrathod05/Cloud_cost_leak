import pandas as pd
from detector import detect_leaks

# Load dataset
df = pd.read_csv("data/servers_usage.csv", nrows=50000)

# Run detection logic
result = detect_leaks(df)

# Save output
result.to_csv("data/output_alerts.csv", index=False)

print("Leak detection completed successfully")
print(result.head())