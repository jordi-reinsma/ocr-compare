import easyocr
import pypdfium2
import pypdfium2._helpers.bitmap as bitmap


ocr = easyocr.Reader(["pt"])


def pdf2txt(input: bytes) -> str:
    try:
        pdf = pypdfium2.PdfDocument(input)
        full_text = ""
        for page in pdf:
            image: bitmap.PdfBitmap = page.render()
            text: list[str] = ocr.readtext(image.to_numpy(), detail=0)
            full_text += " ".join(text) + "\n"
        return full_text
    finally:
        pdf.close()
