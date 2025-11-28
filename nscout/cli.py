# in cli.py
import argparse
import sys
from .checker import check_name, PYPI, TESTPYPI

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def display(label, status):
    color = {
        "taken": RED,
        "not taken": GREEN,
        "error": YELLOW,
    }[status]
    print(f"{label:10} {color}{status}{RESET}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Package name to check")
    parser.add_argument("--version", action="store_true", help="Show nscout version")

    args = parser.parse_args()

    if args.version:
        from . import __version__
        print(__version__)
        sys.exit(0)

    pkg = args.name.strip()

    pypi_status = check_name(pkg, PYPI)
    testpypi_status = check_name(pkg, TESTPYPI)

    display("PyPI:", pypi_status)
    display("TestPyPI:", testpypi_status)

    if pypi_status == "taken":
        sys.exit(1)
