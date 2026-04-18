CREATE_MOLECULAR = """
CREATE TABLE IF NOT EXISTS molecular_profile (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT REFERENCES patients(patient_id),
    ros1_positive INTEGER DEFAULT 0,
    alk_positive INTEGER DEFAULT 0,
    egfr_positive INTEGER DEFAULT 0,
    fusion_partner TEXT,
    ngs_report_date DATE,
    raw_mgi TEXT
);
"""
