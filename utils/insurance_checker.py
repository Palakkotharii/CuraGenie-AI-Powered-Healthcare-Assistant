def check_insurance_coverage(treatment_name):
    # Simulated database of covered treatments
    covered_treatments = [
        "General Consultation",
        "Blood Test",
        "MRI Scan",
        "X-Ray",
        "Heart Surgery",
        "Physiotherapy",
        "COVID-19 Treatment",
        "Vaccination",
        "Cancer Treatment"
    ]

    treatment_name = treatment_name.strip().lower()

    if any(treatment_name in treatment.lower() for treatment in covered_treatments):
        return f"✅ Treatment '{treatment_name.title()}' is covered under your insurance plan."
    else:
        return f"❌ Treatment '{treatment_name.title()}' is not covered under your insurance plan."
