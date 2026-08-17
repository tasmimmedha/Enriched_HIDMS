"""Entry point for ``python -m hidms``."""

from hidms import __version__


def main() -> None:
    print(f"HIDMS v{__version__} — Health Intelligence & Diagnostic Monitoring System")


if __name__ == "__main__":
    main()
