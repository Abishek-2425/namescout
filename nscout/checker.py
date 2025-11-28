import httpx

PYPI = "https://pypi.org/pypi/{}/json"
TESTPYPI = "https://test.pypi.org/pypi/{}/json"


def check_name(name: str, registry_url: str) -> str:
    """
    Check package availability on PyPI or TestPyPI.

    Returns one of the following strings:
        - "taken"
        - "not taken"
        - "error"  (network problems, timeouts, server errors)
    """

    url = registry_url.format(name)

    try:
        response = httpx.get(url, timeout=3)

    except httpx.TimeoutException:
        return "error"   # timeout
    except httpx.RequestError:
        return "error"   # DNS / connection failure

    # Package not found → available
    if response.status_code == 404:
        return "not taken"

    # Package exists
    if response.status_code == 200:
        return "taken"

    # Server errors (PyPI unreachable or down)
    if 500 <= response.status_code < 600:
        return "error"

    # Anything unexpected
    return "error"
