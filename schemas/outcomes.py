CREATE_OUTCOMES = """
CREATE TABLE IF NOT EXISTS outcomes (
    outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT REFERENCES all_patients(patient_id),
    pfs_months REAL,
    os_months REAL,
    censoring_pfs INTEGER DEFAULT 1,
    censoring_os INTEGER DEFAULT 1,
    notes TEXT
);
"""
