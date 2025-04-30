import pytesseract
import cv2
import numpy as np
from PIL import Image

# Uncomment and adjust if Tesseract is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def analyze_report(uploaded_file):
    try:
        # Convert the uploaded file to an OpenCV-compatible image
        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Step 1: Convert to grayscale for better clarity
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Step 2: Apply adaptive thresholding (to improve contrast)
        thresh = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31, 2
        )

        # Step 3: Denoise the image using fastNlMeansDenoising
        denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

        # Step 4: Resize the image to make the text larger (optional)
        resized = cv2.resize(denoised, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Step 5: OCR configuration for better accuracy with medical reports
        custom_config = r'--oem 3 --psm 6'  # LSTM OCR engine and single uniform block of text

        # Step 6: Perform OCR
        text = pytesseract.image_to_string(resized, config=custom_config)

        # Step 7: Clean the extracted text (strip empty lines and extra whitespace)
        cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned_text = "\n".join(cleaned_lines)

        return cleaned_text
    except Exception as e:
        return f"Error analyzing report: {str(e)}"
