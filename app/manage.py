#!/usr/bin/env python
from sys import argv
from os  import environ


def main() -> None:
    # Run administrative tasks
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.settings')

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(argv)


if __name__ == '__main__':
    main()