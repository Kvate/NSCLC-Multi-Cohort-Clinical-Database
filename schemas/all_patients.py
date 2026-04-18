CREATE_ALL_PATIENTS = """
CREATE TABLE IF NOT EXISTS all_patients (
    patient_id TEXT PRIMARY KEY,
    cohort_type TEXT CHECK(cohort_type IN ('ROS1','ALK','EGFR','WT')),
    age_at_dx INTEGER,
    sex TEXT,
    histology TEXT,
    tnm_at_dx TEXT,
    smoking_status TEXT,
    dx_year INTEGER,
    last_followup DATE,
    death_date DATE,
    death_cause TEXT
);
"""
