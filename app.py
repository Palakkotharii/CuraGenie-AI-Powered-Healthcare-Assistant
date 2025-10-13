import streamlit as st
from utils.gemini_api import gemini_ask
from utils.voice_utils import listen_to_user, speak_response
from utils.report_analyzer import analyze_report
from utils.prescription_reader import read_prescription_clean as read_prescription

from utils.google_calendar_real import create_real_calendar_event  # updated real calendar import
from utils.insurance_checker import check_insurance_coverage


# Streamlit page setup
st.set_page_config(page_title="Healthcare AI Chatbot", page_icon="🏥")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose Feature", [
    "General Diagnosis", 
    "Report Analyzer", 
    "Prescription Reader", 
    "Google Calendar Reminder",
    "Insurance Coverage Checker"
])

# General Diagnosis Page
if app_mode == "General Diagnosis":
    st.title("🏥 AI-Powered Healthcare Chatbot")
    st.write("Enter your symptoms or speak to get a general diagnosis.")

    user_symptoms = st.text_area("📝 Enter your symptoms:")

    if st.button("🧠 Diagnose from Text"):
        if user_symptoms:
            with st.spinner("Analyzing your symptoms..."):
                diagnosis = gemini_ask(f"I have these symptoms: {user_symptoms}. What could be the possible diagnosis?")
                st.success(diagnosis)
        else:
            st.warning("Please enter some symptoms.")

    if st.button("🎙️ Speak Symptoms"):
        with st.spinner("Listening..."):
            symptoms = listen_to_user()
            if symptoms:
                st.text(f"You said: {symptoms}")
                diagnosis = gemini_ask(f"I have these symptoms: {symptoms}. What could be the possible diagnosis?")
                st.success(diagnosis)
                speak_response(diagnosis)
            else:
                st.warning("Sorry, I didn't catch that. Please try again.")

# Report Analyzer Page
elif app_mode == "Report Analyzer":
    st.title("📝 Report Analyzer")
    uploaded_report = st.file_uploader("Upload your Medical Report (Image)", type=["png", "jpg", "jpeg"])
    if uploaded_report:
        with st.spinner("Analyzing report..."):
            report_text = analyze_report(uploaded_report)
            st.text_area("Extracted Report Text:", report_text, height=300)

# Prescription Reader Page
elif app_mode == "Prescription Reader":
    st.title("💊 Prescription Reader")
    uploaded_prescription = st.file_uploader("Upload your Prescription (Image)", type=["png", "jpg", "jpeg"])
    if uploaded_prescription:
        with st.spinner("Reading prescription..."):
            prescription_text = read_prescription(uploaded_prescription)
            st.text_area("Extracted Prescription Text:", prescription_text, height=300)

# Google Calendar Reminder Page (Real Google Calendar API)
elif app_mode == "Google Calendar Reminder":
    st.title("🗓️ Set a Doctor's Appointment Reminder (Real Google Calendar)")
    event_title = st.text_input("Event Title", "Doctor Appointment")
    event_date = st.date_input("Appointment Date")
    event_time = st.time_input("Appointment Time")

    if st.button("📅 Create Google Calendar Event"):
        with st.spinner("Creating real calendar event..."):
            result = create_real_calendar_event(event_title, event_date, event_time)
            st.success(result)

# Insurance Coverage Checker Page
elif app_mode == "Insurance Coverage Checker":
    st.title("💼 Insurance Coverage Checker")
    treatment = st.text_input("Enter the treatment name:")

    if st.button("🔍 Check Insurance Coverage"):
        with st.spinner("Checking coverage..."):
            result = check_insurance_coverage(treatment)
            st.success(result)
