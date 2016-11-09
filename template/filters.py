#!/usr/bin/env python


def to_yaml(value):
    from yaml import safe_dump
    return safe_dump(value)


def to_json(value):
    from json import dumps
    return dumps(value)


def from_json(value):
    from json import loads
    return loads(value)


def from_yaml(value):
    from yaml import safe_load
    return safe_load(value)


def pprint(value):
    from pprint import pformat
    return pformat(value)


def combine(default, override):
    combined = default.copy()
    combined.update(override)
    return combined
