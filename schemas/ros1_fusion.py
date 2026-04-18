CREATE_ROS1_FUSION = """
CREATE TABLE IF NOT EXISTS ros1_fusion (
    patient_id TEXT PRIMARY KEY REFERENCES all_patients(patient_id),
    fusion_partner TEXT,
    ngs_report_date DATE,
    raw_mgi TEXT
);
"""
