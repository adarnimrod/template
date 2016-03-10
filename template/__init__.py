#!/usr/bin/env python
'''Generate files from Jinja2 templates and environment variables.'''

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from jinja2 import FileSystemLoader, DictLoader
from jinja2.environment import Environment
from os import environ
from sys import stdin, argv


def render(template):
    env = Environment()
    return env.from_string(template).render(environ)

def usage():
    raise NotImplemented

def main():
    template=stdin.read()
    print(render(template))

if __name__ == '__main__':
    main()
