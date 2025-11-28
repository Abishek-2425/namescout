
# **nscout** 
nscout is a small, fast command-line tool for inspecting package name
availability on **PyPI** and **TestPyPI**.  
It also fetches **full metadata** when a package exists — including version,
summary, authorship, license, release history, project URLs, and more.

nscout is designed to be:
- quick to use  
- informative out of the box  
- script-friendly  
- safe for automation (JSON mode, quiet mode)  
- ideal for package authors checking names before publishing

---

## ✨ Features

- Check whether a package name is **taken** or **not taken**
- Automatic metadata fetch from PyPI:
  - latest version
  - summary/description
  - author + author email
  - license
  - homepage & project URLs
  - Python requirement
  - release count
  - latest release timestamp
- Clean pretty layout for **single package** checks
- Compact table layout for **multiple packages**
- File mode (`-r file.txt`) for batch operations
- JSON mode for scripts & CI tools
- Quiet mode for log-friendly output
- In-memory caching for ultra-fast repeated lookups
- Works with both PyPI and TestPyPI

---

## 📦 Installation

```bash
pip install nscout
````

Or install locally during development:

```bash
pip install -e .
```

---

## 🚀 Usage

### **Check a single package**

```bash
nscout requests
```

Example output:

```
requests — taken
Version:        2.32.5
Summary:        Python HTTP for Humans.
Author:         Kenneth Reitz
Author Email:   me@kennethreitz.org
License:        Apache-2.0
Homepage:       https://requests.readthedocs.io
Project URL:    https://pypi.org/project/requests/
Python Req:     >=3.9
Release Count:  157
Latest Release: 2.32.5 (2025-08-18T20:46:00.542304Z)
```

---

### **Check multiple packages**

```bash
nscout requests flyn numpy
```

Output:

```
Name                 Status       Version      Summary
---------------------------------------------------------------------------
requests             taken        2.32.5       Python HTTP for Humans.
flyn                 taken        0.1.8        Natural-language to shell command conver
numpy                taken        2.3.5        Fundamental package for array computing
```

---

### **File mode**

Create a file:

```
requests
numpy
mynewpkg
```

Run:

```bash
nscout -r names.txt
```

---

### **JSON output (for CI / scripts)**

```bash
nscout --json requests
```

Example:

```json
[
  {
    "name": "requests",
    "status": "taken",
    "source": {
      "pypi": { "taken": true },
      "testpypi": { "taken": true }
    },
    "metadata": {
      "version": "2.32.5",
      "summary": "Python HTTP for Humans.",
      "author": "Kenneth Reitz",
      "author_email": "me@kennethreitz.org",
      "license": "Apache-2.0",
      "homepage": "https://requests.readthedocs.io",
      "project_url": "https://pypi.org/project/requests/",
      "project_urls": {
        "Documentation": "https://requests.readthedocs.io",
        "Homepage": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests"
      },
      "requires_python": ">=3.9",
      "requires_dist": [
        "charset_normalizer<4,>=2",
        "idna<4,>=2.5",
        "urllib3<3,>=1.21.1",
        "certifi>=2017.4.17"
      ],
      "release_count": 157,
      "latest_release": {
        "version": "2.32.5",
        "timestamp": "2025-08-18T20:46:00.542304Z"
      },
      "all_versions": [...]
    },
    "error": null
  }
]
```

---

### **Quiet mode**

Disable colors and decoration:

```bash
nscout --quiet requests flyn numpy
```

---

### **Version**

```bash
nscout --version
```

---

## 🧠 Exit Codes

| Code | Meaning                      |
| ---- | ---------------------------- |
| 0    | All names available          |
| 1    | At least one name is taken   |
| 4    | Network error / PyPI failure |

These are safe for CI pipelines.

---

## 🏗 Project Structure

```
nscout/
  checker.py    → availability & metadata logic
  cli.py        → command-line interface
  format.py     → pretty output & table layouts
  cache.py      → in-memory caching
```

---

## 🛠 Development

Install in editable mode:

```bash
pip install -e .
```

Run the CLI:

```bash
python -m nscout.cli package_name
```

---

## 📤 Publishing

```bash
python -m build
twine upload dist/*
```

---

## ⚖️ License

MIT