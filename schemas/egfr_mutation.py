CREATE_EGFR_MUTATION = """
CREATE TABLE IF NOT EXISTS egfr_mutation (
    patient_id TEXT PRIMARY KEY REFERENCES all_patients(patient_id),
    mutation_type TEXT,
    ngs_report_date DATE,
    raw_mgi TEXT
);
"""
