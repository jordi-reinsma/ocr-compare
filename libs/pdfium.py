import re
import pypdfium2

SPACES = re.compile(r"\s+")


def clean_text(text: str) -> str:
    # TODO: não sei como melhorar ):
    text = SPACES.sub(" ", text)
    return "".join(c for c in text if c.isprintable())


def pdf2txt(input: bytes) -> str:
    try:
        pdf = pypdfium2.PdfDocument(input)
        full_text = ""
        for page in pdf:
            text = page.get_textpage().get_text_bounded()
            full_text += clean_text(text) + "\n"
        return full_text
    finally:
        pdf.close()
