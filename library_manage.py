#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from library.middleware import set_current_tenant 


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "multitenant.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    from django.db import connection

    args = sys.argv
    db = args[1]
    with connection.cursor() as cursor:
        set_current_tenant(db)
        del args[1]
        execute_from_command_line(args)


if __name__ == "__main__":
    main()
