# 🏥 Curageni : AI-Powered Healthcare Chatbot

A multi-feature Streamlit application that combines **Generative AI (Google Gemini)**, **Computer Vision (OCR)**, and **external APIs** to provide intelligent healthcare assistance — from symptom diagnosis to appointment scheduling.

---

## ✨ Features

| Feature | Description | Key Technologies |
|----------|--------------|------------------|
| 🧠 **General Diagnosis** | Analyzes user-entered or spoken symptoms to provide a safe, short diagnosis, possible causes, and general health advice. | Google Gemini-2.5-Flash, Speech Recognition |
| 📝 **Report Analyzer** | Processes medical report images using advanced preprocessing and OCR to extract laboratory test results into a structured table format. | OpenCV (cv2), pytesseract (OCR), NumPy |
| 💊 **Prescription Reader** | Extracts structured data (Doctor, Patient, Medicines, Date) from prescription images using OCR and Regex. | pytesseract (OCR), Regex |
| 🗓️ **Google Calendar Reminder** | Securely schedules doctor’s appointments and medical events directly in your Google Calendar. | Google Calendar API, OAuth 2.0 |
| 💼 **Insurance Checker** | Simulated backend logic to check if a treatment is covered under a health insurance plan. | Python (Simulated Logic) |

---

## 🛠️ Tech Stack

- **App Framework:** Streamlit  
- **Generative AI:** Google Gemini-2.5-Flash (via `google-generativeai` SDK)  
- **Computer Vision/OCR:** OpenCV, pytesseract  
- **Voice/Speech:** SpeechRecognition, pyttsx3  
- **APIs:** Google Calendar API, Google Cloud Services  
- **Utilities:** NumPy, tabulate, re  

---

## 🚀 Setup & Installation

### 1️⃣ Prerequisites
- Python **3.8+**
- **Tesseract OCR** 

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Palakkotharii/CuraGenie-AI-Powered-Healthcare-Assistant.git
cd CuraGenie-AI-Powered-Healthcare-Assistant

### 2️⃣ Run the Application
```bash
streamlit run app.py

