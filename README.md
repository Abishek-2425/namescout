
## **nscout**

A small command-line tool for checking whether a package name is already taken on **PyPI** and **TestPyPI**.
It queries PyPI’s public JSON endpoints and reports the results in a simple, readable format.

---

## **Features**

* Checks availability on both PyPI and TestPyPI
* Supports checking **multiple package names** at once
* Optional **JSON output** for scripts and CI (`--json`)
* Optional **quiet mode** for clean automation (`--quiet`)
* Predictable **exit codes** for automation workflows
* Minimal dependencies, very fast
* Works on Python 3.10+

---

## **Installation**

From PyPI:

```bash
pip install nscout
````

For local development:

```bash
pip install -e .
```

---

## **Usage**

### Check a single package

```bash
nscout requests
```

### Check multiple names

```bash
nscout requests flask numpy
```

### JSON output (script/CI-friendly)

```bash
nscout requests flask --json
```

Output:

```json
{
  "requests": { "pypi": "taken", "testpypi": "taken" },
  "flask": { "pypi": "taken", "testpypi": "taken" }
}
```

### Quiet mode

```bash
nscout requests --quiet
```

Produces minimal output without colors.

### Version

```bash
nscout --version
```

---

## **Exit Codes**

These are useful in CI or automation:

| Code | Meaning                            |
| ---- | ---------------------------------- |
| 0    | All names available                |
| 1    | Name taken on PyPI                 |
| 2–3  | (reserved for future expansion)    |
| 4    | Network/server error during lookup |

---

## **Why this tool exists**

PyPI doesn’t have a dedicated “is this name available?” endpoint.
This tool performs a lightweight check against PyPI’s JSON metadata URLs:

* If the endpoint returns **404**, the name is **not taken**
* A **200** means the name is already published
* Any network or server issue is reported as `"error"`

This keeps the tool fast, predictable, and convenient during package creation or CI validation.

---

## **Development**

Run directly from source:

```bash
python -m nscout <package-name>
```

Project layout:

```
nscout/
├── nscout/
│   ├── checker.py      # core logic
│   ├── cli.py          # command line interface
│   └── __init__.py
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## **Notes**

nscout stays intentionally small and focused. The project aims to make early package development smoother—especially when reserving names, validating builds, or wiring CI checks.

Contributions are welcome, as long as they preserve the tool’s simplicity and intention.

---

**Powered by Python, fueled by caffeine, guided by late-night curiosity.☕🚀**