import cv2
import numpy as np
import pytesseract
import re
from tabulate import tabulate  # pip install tabulate

def analyze_report(uploaded_file):
    try:
        # -------------------- Load Image --------------------
        file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # -------------------- Preprocess --------------------
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Improve contrast
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        gray = clahe.apply(gray)
        # Resize to improve OCR
        scale_percent = 200
        width = int(gray.shape[1] * scale_percent / 100)
        height = int(gray.shape[0] * scale_percent / 100)
        gray = cv2.resize(gray, (width, height), interpolation=cv2.INTER_LINEAR)
        # Thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # -------------------- OCR --------------------
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(thresh, config=custom_config)

        # -------------------- Clean Lines --------------------
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        cleaned_lines = []
        buffer = ''

        for line in lines:
            # Remove unwanted characters
            line = line.replace('?', '').replace('*', '').replace('q/dL', 'g/dL')
            if 'Test Result Normal Range' in line or 'BLOOD REPORT' in line:
                continue

            # Look for first numeric value (Result)
            match = re.search(r'\d+[\.,]?\d*\s*[%a-zA-Z/]*', line)
            if match:
                result = match.group()
                parts = line.split(result)
                test_name = (buffer + ' ' + parts[0]).strip() if buffer else parts[0].strip()
                normal_range = parts[1].strip() if len(parts) > 1 else ''
                cleaned_lines.append([test_name, result, normal_range])
                buffer = ''
            else:
                # Buffer multi-line test names
                buffer += ' ' + line

        # -------------------- Merge Multi-line Test Names --------------------
        merged_lines = []
        skip_next = False
        for i in range(len(cleaned_lines)):
            if skip_next:
                skip_next = False
                continue
            name = cleaned_lines[i][0]

            # Merge next lines if they do not have a numeric result
            j = i + 1
            while j < len(cleaned_lines) and not re.search(r'\d', cleaned_lines[j][1]):
                name += ' ' + cleaned_lines[j][0]
                skip_next = True
                j += 1

            merged_lines.append([name, cleaned_lines[i][1], cleaned_lines[i][2]])

        # -------------------- Output Table --------------------
        headers = ["Test", "Result", "Normal Range"]
        table = tabulate(merged_lines, headers=headers, tablefmt="grid")
        return table

    except Exception as e:
        return f"Error analyzing report: {str(e)}"
