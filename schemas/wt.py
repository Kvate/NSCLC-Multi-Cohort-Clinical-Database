CREATE_WT = """
CREATE TABLE IF NOT EXISTS wt (
    patient_id TEXT PRIMARY KEY REFERENCES all_patients(patient_id),
    notes TEXT,
    ngs_report_date DATE,
    raw_mgi TEXT
);
"""
