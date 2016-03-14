#!/usr/bin/env python
'''Generate files from Jinja2 templates and environment variables.'''

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from jinja2 import Template
from os import environ
from sys import stdin, stdout
import argparse
from argparse import ArgumentParser


def render(template):
    t = Template(template)
    return t.render(environ)


def main():
    parser = ArgumentParser()
    parser.add_argument('filename',
                        help='Input filename',
                        type=argparse.FileType('r'),
                        nargs='?')
    parser.add_argument('-o', '--output',
                        help='Output to filename',
                        type=argparse.FileType('w'))
    args = parser.parse_args()
    infd = args.filename if args.filename else stdin
    outfd = args.output if args.output else stdout
    print(render(infd.read()), file=outfd)

if __name__ == '__main__':
    main()
