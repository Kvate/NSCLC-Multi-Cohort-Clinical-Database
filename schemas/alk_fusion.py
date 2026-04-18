CREATE_ALK_FUSION = """
CREATE TABLE IF NOT EXISTS alk_fusion (
    patient_id TEXT PRIMARY KEY REFERENCES all_patients(patient_id),
    fusion_partner TEXT,
    ngs_report_date DATE,
    raw_mgi TEXT
);
"""
