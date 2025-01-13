import contextlib
import importlib
import pathlib
import signal
import sys
import time
import typing


@contextlib.contextmanager
def timeout(duration: int):
    def timeout_handler(signum, frame):
        raise TimeoutError(f"timeout after {duration} seconds")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(duration)
    try:
        yield
    finally:
        signal.alarm(0)


def main():
    if len(sys.argv) < 3:
        print("Usage: python <lib> <file>")
        print("Example: python vision file.pdf")
        print("Example: python pdfium book.pdf")
        sys.exit(1)

    init_time = time.time()
    module = importlib.import_module("libs." + sys.argv[1])
    init_time = time.time() - init_time

    pdf2txt: typing.Callable[[bytes], str] = module.pdf2txt
    file = pathlib.Path(sys.argv[2]).read_bytes()

    with timeout(150):
        exec_time = time.time()
        output = pdf2txt(file)
        exec_time = time.time() - exec_time

    print(f"Init time: {init_time:.5f}s")
    print(f"Exec time: {exec_time:.5f}s")
    print(f"Text size: {len(output)}")
    print(output)


if __name__ == "__main__":
    main()
