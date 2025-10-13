import pytesseract
import cv2
import numpy as np
import re

def read_prescription_clean(uploaded_file):
    try:
        # -------------------- Load Image --------------------
        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # -------------------- Preprocessing --------------------
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        denoised = cv2.medianBlur(thresh, 3)
        resized = cv2.resize(denoised, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # -------------------- OCR --------------------
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(resized, config=custom_config)

        # -------------------- Clean Text --------------------
        lines = text.splitlines()
        cleaned_lines = []
        for ln in lines:
            ln = ln.strip()
            if not ln:
                continue
            ln = re.sub(r'[^A-Za-z0-9,()/\s.-]', '', ln)  # Remove strange symbols
            ln = re.sub(r'\s+', ' ', ln)  # Normalize spaces
            cleaned_lines.append(ln)
        cleaned_text = "\n".join(cleaned_lines)

        # -------------------- Extract Doctor & Specialization --------------------
        doctor, specialization = "", ""
        for i, ln in enumerate(cleaned_lines):
            if "Dr." in ln or "Dr" in ln:
                doctor = ln.split(",")[0]  # Take first part as doctor
                if i+1 < len(cleaned_lines):
                    specialization = cleaned_lines[i+1]  # Next line as specialization
                break

        # -------------------- Extract Phone --------------------
        phone_match = re.search(r'\(?\d{3}\)?\s?\d{3}-\d{4}', cleaned_text)
        phone = phone_match.group() if phone_match else ""

        # -------------------- Extract Patient --------------------
        patient_match = re.search(r'Patient[:\s]*([A-Za-z\s]+)', cleaned_text)
        patient = patient_match.group(1).strip() if patient_match else ""

        # -------------------- Extract Date --------------------
        date_match = re.search(r'Date[:\s]*([0-3]?\d\s*/\s*[0-1]?\d\s*/\s*\d{2,4})', cleaned_text)
        date = date_match.group(1).replace(" ", "") if date_match else ""

        # -------------------- Extract Medicines --------------------
        medicines_matches = re.findall(r'\d+\.\s*([A-Za-z\s]+(?:\s\d+\s?mg)?)', cleaned_text)
        medicines = [m.strip() for m in medicines_matches]

        # -------------------- Format Output Cleanly --------------------
        output = f"Doctor: {doctor}\n"
        output += f"Specialization: {specialization}\n"
        output += f"Phone: {phone}\n"
        output += f"Patient: {patient}\n"
        output += f"Date: {date}\n"
        output += "Medicines:\n"
        for idx, med in enumerate(medicines, 1):
            output += f"  {idx}. {med}\n"

        return output

    except Exception as e:
        return f"Error reading prescription: {str(e)}"
