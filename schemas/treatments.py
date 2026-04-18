CREATE_TREATMENTS = """
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT REFERENCES all_patients(patient_id),
    line_number INTEGER,
    drug_name TEXT,
    start_date DATE,
    end_date DATE,
    duration_days REAL,
    response TEXT,
    reason_stop TEXT
);
"""
