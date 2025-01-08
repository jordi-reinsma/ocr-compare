import pypdfium2
import pypdfium2._helpers.bitmap as bitmap
import tesserocr


def pdf2txt(input: bytes) -> str:
    try:
        pdf = pypdfium2.PdfDocument(input)
        full_text = ""
        for page in pdf:
            image: bitmap.PdfBitmap = page.render()
            full_text += tesserocr.image_to_text(image.to_pil()) + "\n"
        return full_text
    finally:
        pdf.close()
