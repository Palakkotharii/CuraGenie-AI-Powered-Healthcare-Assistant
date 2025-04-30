import pytesseract
import cv2
import numpy as np
import re

# Uncomment and adjust if Tesseract is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_prescription(uploaded_file):
    try:
        # Convert the uploaded file to an OpenCV-compatible image
        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Step 1: Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Step 2: Apply adaptive thresholding (for better contrast even if lighting is uneven)
        thresh = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31, 2
        )

        # Step 3: Denoise the image
        denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

        # Step 4: Resize the image (scale up by 2x for better OCR accuracy)
        resized = cv2.resize(denoised, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Step 5: OCR configuration (LSTM engine + assume single uniform block)
        custom_config = r'--oem 3 --psm 6'

        # Step 6: Perform OCR
        text = pytesseract.image_to_string(resized, config=custom_config)

        # Step 7: Clean the extracted text (strip empty lines and extra spaces)
        raw_lines = text.splitlines()
        cleaned_lines = []

        for ln in raw_lines:
            ln = ln.strip()
            if not ln:
                continue

            # 1) Remove any leading non-alphanumeric characters (e.g., stray bullets, symbols)
            ln = re.sub(r'^[^A-Za-z0-9]+', '', ln)

            # 2) Remove any leading "e " (common artifact from Tesseract OCR)
            ln = re.sub(r'^e ', '', ln)

            # 3) Fix numbered lists stuck together (e.g., "2.Lisinopril" → "2. Lisinopril")
            ln = re.sub(r'^(\d+)\.(\S)', r'\1. \2', ln)

            # 4) Ensure space between drug names and dosages (e.g., "Lisinopril10" → "Lisinopril 10")
            ln = re.sub(r'(\D)(\d+)', r'\1 \2', ln)

            # 5) Replace multiple spaces with a single space
            ln = re.sub(r'\s+', ' ', ln)

            # 6) Fix phone numbers formatting
            ln = re.sub(r'\(\s*(\d{3})\s*\)\s*(\d{3})\s*-\s*(\d{4})', r'(\1) \2-\3', ln)

            # 7) Correct common OCR misreadings (like "dally" → "daily")
            ln = ln.replace("dally", "daily")

            cleaned_lines.append(ln)

        cleaned_text = "\n".join(cleaned_lines)

        return cleaned_text
    except Exception as e:
        return f"Error reading prescription: {str(e)}"
