import re

# import sys
# import time
import pypdfium2 as pdfium

# init_time = time.time()
SPACES = re.compile(r"\s+")
# init_time = time.time() - init_time


def pdf2txt(input: bytes) -> str:
    pdf = pdfium.PdfDocument(input)
    full_text = ""
    for page in pdf:
        text = page.get_textpage().get_text_bounded()
        full_text += SPACES.sub(" ", text) + "\n"
    return full_text


# def main():
#     if len(sys.argv) < 2:
#         print('Usage: python pypdfium2/main.py <file>')
#         sys.exit(1)

#     file_name = sys.argv[1]
#     with open(file_name, 'rb') as f:
#         input = f.read()

#     exec_time = time.time()
#     output = pdf2txt(input)
#     exec_time = time.time() - exec_time

#     print(f'Init time: {init_time:.5f}s')
#     print(f'Exec time: {exec_time:.5f}s')
#     print('Text size:', len(output))


# if __name__ == '__main__':
#     main()
