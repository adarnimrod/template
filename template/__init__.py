#!/usr/bin/env python
'''Generate files from Jinja2 templates and environment variables.'''

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from jinja2 import Template
from os import environ
from sys import stdin


def render(template):
    t = Template(template)
    return t.render(environ)


def usage():
    raise NotImplemented


def main():
    template = stdin.read()
    print(render(template))

if __name__ == '__main__':
    main()
