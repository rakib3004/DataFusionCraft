import fitz  # PyMuPDF
from PIL import Image

def pdf_to_images(pdf_path, image_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create the output folder if it doesn't exist
    import os
    os.makedirs(image_folder, exist_ok=True)

    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document.load_page(page_number)

        # Convert the page to a Pix object
        pix = page.get_pixmap()

        # Create an Image object from the Pix
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image to the output folder
        image_path = os.path.join(image_folder, f"page_{page_number + 1}.png")
        image.save(image_path, "PNG")

    # Close the PDF document
    pdf_document.close()

# Example usage
pdf_path = "Tafsir.pdf"
image_folder = "tafsir"
pdf_to_images(pdf_path, image_folder)
