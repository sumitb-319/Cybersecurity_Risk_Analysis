import csv
import random
from datetime import datetime, timedelta

# Define constants
departments = ['HR', 'Finance', 'IT', 'Operations', 'Sales', 'Marketing']
incident_types = ['Phishing', 'Malware', 'Ransomware', 'Unauthorized Access', 'Suspicious Login']
severity_levels = ['Low', 'Medium', 'High']
resolved_options = ['Yes', 'No']

# Start date for incident generation
start_date = datetime(2025, 1, 1)

# Generate 1000 dummy records
rows = []
for _ in range(1000):
    date = start_date + timedelta(days=random.randint(0, 180))
    department = random.choice(departments)
    incident_type = random.choice(incident_types)
    severity = random.choice(severity_levels)
    time_to_resolve = round(random.uniform(1.5, 72.0), 1)  # between 1.5 to 72 hrs
    resolved = random.choice(resolved_options)

    rows.append([
        date.strftime('%Y-%m-%d'),
        department,
        incident_type,
        severity,
        time_to_resolve,
        resolved
    ])

# CSV file name
filename = "cyber_incident_data_1000.csv"

# Column headers
headers = ["Date", "Department", "Incident Type", "Severity", "Time to Resolve (hrs)", "Resolved"]

# Write to CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ File '{filename}' created with 1000 dummy records.")
