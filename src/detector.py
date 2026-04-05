import pandas as pd

def detect_leaks(df):
    alerts = []
    cost_per_hour = []

    for index, row in df.iterrows():

        # Simulated cost calculation
        cost = (row['vcpu_usage'] * 0.05) + (row['ram_usage'] * 0.02)
        cost_per_hour.append(round(cost, 2))

        # Unused VM
        if row['vcpu_usage'] < 5 and row['ram_usage'] < 10:
            alerts.append("Unused VM")

        # Overprovisioned Resource
        elif cost > 5 and row['vcpu_usage'] < 15:
            alerts.append("Overprovisioned Resource")

        # High Utilization
        elif row['vcpu_usage'] > 85:
            alerts.append("High Utilization")

        else:
            alerts.append("Normal")

    df['cost_per_hour'] = cost_per_hour
    df['alert'] = alerts

    return df