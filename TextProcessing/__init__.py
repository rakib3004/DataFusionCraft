from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

def extract_bangla_text_from_image(image_path):
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image, lang='ben')

    return text

image_path = "page_180.png"
extracted_bangla_text = extract_bangla_text_from_image(image_path)

print("Extracted Bangla Text:")
print(extracted_bangla_text)
