import os
import pathlib
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python 0_run_all.py <pdfs folder 1> <pdfs folder 2> ...")
        sys.exit(1)

    FOLDERS = [pathlib.Path(folder) for folder in sys.argv[1:]]
    FILES = [folder / file for folder in FOLDERS for file in os.listdir(folder)]
    LIBS = ["easy", "pdfium", "tesseract", "vision"]
    assert all(file.suffix == ".pdf" for file in FILES)

    for lib in LIBS:
        os.system(f"mkdir -p ocr/{lib} > /dev/null")
        for i, file in enumerate(FILES, start=1):
            file_name = file.name.removesuffix(".pdf")
            print(lib, i, file_name)
            os.system(f"python 1_run_ocr.py {lib} '{file}' > 'ocr/{lib}/{file_name}.txt'")


if __name__ == "__main__":
    main()
