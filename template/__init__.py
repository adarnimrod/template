#!/usr/bin/env python
# pylint: disable=import-error
"""A CLI tool for generating files from Jinja2 templates and environment
variables."""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)  # pylint: disable=duplicate-code
from os import environ
import sys
import argparse
from argparse import ArgumentParser
import template.filters

# I ignore import errors here and fail on them later in the main function so
# the module can be imported by the setup.py with jinja missing so the
# docstring can be used as the package description.
try:
    from jinja2 import Environment
except ImportError:
    pass


__version__ = "0.6.5"


def render(template_string):
    """Render the template."""
    env = Environment(autoescape=True)
    # Add all functions in template.filters as Jinja filters.
    # pylint: disable=invalid-name
    for tf in filter(lambda x: not x.startswith("_"), dir(template.filters)):
        env.filters[tf] = getattr(template.filters, tf)
    t = env.from_string(template_string)
    return t.render(environ)


def main():
    """Main entrypoint."""
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "filename",
        help="Input filename",
        type=argparse.FileType("r"),
        nargs="?",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output to filename",
        type=argparse.FileType("w"),
    )
    args = parser.parse_args()
    infd = args.filename if args.filename else sys.stdin
    outfd = args.output if args.output else sys.stdout
    print(render(infd.read()), file=outfd)


if __name__ == "__main__":
    if "Environment" not in dir():
        print(
            "Failed to import jinja2, is the package installed?",
            file=sys.stderr,
        )
        sys.exit(2)
    main()
