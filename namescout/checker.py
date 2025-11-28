import httpx

PYPI = "https://pypi.org/pypi/{}/json"
TESTPYPI = "https://test.pypi.org/pypi/{}/json"

def check_name(name: str, registry_url: str) -> str:
    """
    Returns:
        "taken", "not taken", or "error"
    """
    try:
        r = httpx.get(registry_url.format(name), timeout=3)
    except httpx.RequestError:
        return "error"

    if r.status_code == 404:
        return "not taken"

    if r.status_code == 200:
        return "taken"

    return "error"
