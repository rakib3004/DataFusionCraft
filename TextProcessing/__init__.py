#C:\Program Files\Tesseract-OCR
from PIL import Image
import pytesseract

# Path to the Tesseract executable (update it based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_bangla_text_from_image(image_path):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image with the Bengali language
    text = pytesseract.image_to_string(image, lang='ben')

    return text

# Example usage
image_path = "page_5.png"
extracted_bangla_text = extract_bangla_text_from_image(image_path)

print("Extracted Bangla Text:")
print(extracted_bangla_text)
