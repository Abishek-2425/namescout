import argparse
import sys
import json

from .checker import check_name, PYPI, TESTPYPI
from . import __version__

# Colors for terminal output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def display(label, status):
    color = {
        "taken": RED,
        "not taken": GREEN,
        "error": YELLOW,
    }.get(status, YELLOW)

    print(f"{label:10} {color}{status}{RESET}")


def main():
    parser = argparse.ArgumentParser(description="Check if package names are available on PyPI/TestPyPI.")

    # Version flag — works without requiring name(s)
    parser.add_argument(
        "--version",
        action="version",
        version=f"nscout {__version__}"
    )

    # Optional output modes
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON."
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress colored output (useful for scripts)."
    )

    # One or many package names
    parser.add_argument(
        "names",
        nargs="+",
        help="One or more package names to check."
    )

    args = parser.parse_args()

    results = {}

    # Process each package name
    for name in args.names:
        pkg = name.strip()
        pypi_status = check_name(pkg, PYPI)
        testpypi_status = check_name(pkg, TESTPYPI)

        results[pkg] = {
            "pypi": pypi_status,
            "testpypi": testpypi_status
        }

        if not args.json and not args.quiet:
            print(f"\nChecking: {pkg}")
            display("PyPI:", pypi_status)
            display("TestPyPI:", testpypi_status)

    # JSON output mode
    if args.json:
        print(json.dumps(results, indent=2))
    
    # Exit code logic
    for pkg, info in results.items():
        if info["pypi"] == "taken":
            sys.exit(1)
        if info["pypi"] == "error" or info["testpypi"] == "error":
            sys.exit(4)

    # All good
    sys.exit(0)
