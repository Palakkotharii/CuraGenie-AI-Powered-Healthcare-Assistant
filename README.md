# 🏥 CuraGeni : AI-Powered Healthcare Chatbot  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg)](https://streamlit.io/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Google AI](https://img.shields.io/badge/Powered%20by-Google%20Gemini-green.svg)](https://deepmind.google/)

---

### 💡 Overview  
**CuraGeni** is an AI-powered healthcare assistant built using **Streamlit**, integrating **Google Gemini (Generative AI)**, **Computer Vision (OCR)**, and **external APIs**.  
It offers a seamless healthcare experience — from **symptom diagnosis** to **appointment scheduling** — all in one application.

---

## ✨ Features  

| Feature | Description | Key Technologies |
|----------|--------------|------------------|
| 🧠 **General Diagnosis** | Analyzes user-entered or spoken symptoms to provide a safe, short diagnosis, possible causes, and general health advice. | Google Gemini-2.5-Flash, Speech Recognition |
| 📝 **Report Analyzer** | Processes medical report images using preprocessing + OCR to extract lab test results into structured tables. | OpenCV (cv2), pytesseract, NumPy |
| 💊 **Prescription Reader** | Extracts structured data (Doctor, Patient, Medicines, Date) from prescription images. | pytesseract (OCR), Regex |
| 🗓️ **Google Calendar Reminder** | Allows secure scheduling of doctor’s appointments directly to your Google Calendar. | Google Calendar API, OAuth 2.0 |
| 💼 **Insurance Checker** | Simulated backend logic to check if a treatment is covered under an insurance plan. | Python (Simulated Logic) |

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
- **Tesseract OCR** installed and added to your system path.  

### 2️⃣ Clone the Repository  
```bash
git clone https://github.com/Palakkotharii/CuraGenie-AI-Powered-Healthcare-Assistant.git
cd CuraGenie-AI-Powered-Healthcare-Assistant

3️⃣ Run the Application
streamlit run app.py

