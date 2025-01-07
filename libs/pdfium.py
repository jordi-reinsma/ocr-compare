import re
import pypdfium2 as pdfium

SPACES = re.compile(r"\s+")


def pdf2txt(input: bytes) -> str:
    pdf = pdfium.PdfDocument(input)
    full_text = ""
    for page in pdf:
        text = page.get_textpage().get_text_bounded()
        full_text += SPACES.sub(" ", text) + "\n"
    full_text = "".join(c for c in full_text if c.isprintable())
    return full_text
