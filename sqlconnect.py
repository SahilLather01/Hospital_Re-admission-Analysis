import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root_",
    database="projects"
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv("cleaned_hospital_readmission.csv")  # Make sure this file exists in your working directory

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_data (
        age FLOAT,
        time_in_hospital INT,
        n_lab_procedures INT,
        n_procedures INT,
        n_medications INT,
        n_outpatient INT,
        n_inpatient INT,
        n_emergency INT,
        medical_specialty VARCHAR(255),
        diag_1 VARCHAR(50),
        diag_2 VARCHAR(50),
        diag_3 VARCHAR(50),
        glucose_test VARCHAR(50),
        A1Ctest VARCHAR(50),
        change VARCHAR(50),
        diabetes_med VARCHAR(50),
        readmitted INT,
        total_visits INT
    )
""")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO patient_data (
            age, time_in_hospital, n_lab_procedures, n_procedures, n_medications,
            n_outpatient, n_inpatient, n_emergency, medical_specialty,
            diag_1, diag_2, diag_3, glucose_test, A1Ctest, change,
            diabetes_med, readmitted, total_visits
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        float(row['age']),
        int(row['time_in_hospital']),
        int(row['n_lab_procedures']),
        int(row['n_procedures']),
        int(row['n_medications']),
        int(row['n_outpatient']),
        int(row['n_inpatient']),
        int(row['n_emergency']),
        row['medical_specialty'],
        row['diag_1'],
        row['diag_2'],
        row['diag_3'],
        row['glucose_test'],
        row['A1Ctest'],
        row['change'],
        row['diabetes_med'],
        int(row['readmitted']),
        int(row['total_visits'])
    ))

# Commit and close
conn.commit()
print(" Patient data imported successfully into MySQL!")
conn.close()
