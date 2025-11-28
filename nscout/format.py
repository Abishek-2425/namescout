# nscout/format.py

# -------------------------------------------------------------------
# Color helpers (quiet mode removes all ANSI sequences)
# -------------------------------------------------------------------

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def colorize(text: str, color: str, quiet: bool) -> str:
    if quiet:
        return text
    return f"{color}{text}{RESET}"


# -------------------------------------------------------------------
# Pretty output for a *single* package
# -------------------------------------------------------------------
def print_single(result: dict, quiet: bool):
    name = result["name"]
    status = result["status"]

    # Determine colored status label
    if status == "taken":
        status_str = colorize("taken", RED, quiet)
    elif status == "not_taken":
        status_str = colorize("not taken", GREEN, quiet)
    else:
        status_str = colorize("error", YELLOW, quiet)

    print(f"\n{name} — {status_str}")

    if status == "taken" and result["metadata"]:
        m = result["metadata"]

        print(f"Version:        {m['version']}")
        print(f"Summary:        {m['summary'] or '—'}")
        print(f"Author:         {m['author'] or '—'}")
        print(f"Author Email:   {m['author_email'] or '—'}")
        print(f"License:        {m['license'] or '—'}")
        print(f"Homepage:       {m['homepage'] or '—'}")
        print(f"Project URL:    {m['project_url'] or '—'}")
        print(f"Python Req:     {m['requires_python'] or '—'}")
        print(f"Release Count:  {m['release_count']}")

        if m["latest_release"]:
            ts = m["latest_release"]["timestamp"]
            print(f"Latest Release: {m['latest_release']['version']} ({ts})")


# -------------------------------------------------------------------
# Table output for *multiple* packages  (aligned & color-safe)
# -------------------------------------------------------------------
def print_multi(results: list, quiet: bool):
    NAME_W = 20
    STATUS_W = 12
    VERSION_W = 12

    print(f"\n{'Name':{NAME_W}} {'Status':{STATUS_W}} {'Version':{VERSION_W}} Summary")
    print("-" * (NAME_W + STATUS_W + VERSION_W + 10 + 20))

    for result in results:
        name = result["name"]

        # Raw status (used for width calc)
        raw_status = (
            "taken" if result["status"] == "taken"
            else "not taken" if result["status"] == "not_taken"
            else "error"
        )

        padded_status = f"{raw_status:{STATUS_W}}"

        # Colorize after padding
        if result["status"] == "taken":
            status_str = colorize(padded_status, RED, quiet)
        elif result["status"] == "not_taken":
            status_str = colorize(padded_status, GREEN, quiet)
        else:
            status_str = colorize(padded_status, YELLOW, quiet)

        version = result["metadata"]["version"] if result["metadata"] else "—"
        summary = result["metadata"]["summary"] if result["metadata"] else "—"

        print(
            f"{name:{NAME_W}} "
            f"{status_str} "
            f"{version:{VERSION_W}} "
            f"{summary[:40]}"
        )
