import fitz  
from PIL import Image

def pdf_to_images(pdf_path, image_folder):
    pdf_document = fitz.open(pdf_path)
    import os
    os.makedirs(image_folder, exist_ok=True)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)

        pix = page.get_pixmap()

        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        image_path = os.path.join(image_folder, f"page_{page_number + 1}.png")
        image.save(image_path, "PNG")

    pdf_document.close()

pdf_path = "Tafsir.pdf"
image_folder = "tafsir"
pdf_to_images(pdf_path, image_folder)
