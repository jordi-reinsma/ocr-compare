import os
import pathlib
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python 0_run_all.py <pdfs folder>")
        sys.exit(1)

    FOLDER = pathlib.Path(sys.argv[1])
    FILES = [FOLDER / file for file in os.listdir(FOLDER)]
    LIBS = ["pdfium", "tesseract", "vision"]
    assert all(file.suffix == ".pdf" for file in FILES)

    for lib in LIBS:
        for i, file in enumerate(FILES, start=1):
            print(lib, i, file)
            os.system(f"mkdir -p texts_2/{lib} > /dev/null")
            os.system(f"python 1_run_ocr.py {lib} '{file}' > texts/{lib}/{i}.txt")


if __name__ == "__main__":
    main()
