import importlib
import sys
import time
from typing import Callable


def main():
    if len(sys.argv) < 3:
        print("Usage: python <lib> <file>")
        print("Example: python vision file.pdf")
        sys.exit(1)

    init_time = time.time()
    module = importlib.import_module("libs." + sys.argv[1])
    init_time = time.time() - init_time

    file_name = sys.argv[2]
    with open(file_name, "rb") as f:
        input = f.read()

    pdf2txt: Callable[[bytes], str] = module.pdf2txt

    exec_time = time.time()
    output = pdf2txt(input)
    exec_time = time.time() - exec_time

    print(f"Init time: {init_time:.5f}s")
    print(f"Exec time: {exec_time:.5f}s")
    print(f"Text size: {len(output)}")
    print(output)


if __name__ == "__main__":
    main()
