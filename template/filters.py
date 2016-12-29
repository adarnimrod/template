#!/usr/bin/env python


def to_yaml(value):
    '''
    Converts given data structure to YAML form.
    Examples:

    >>> to_yaml([1,2,3])
    '[1, 2, 3]\\n'
    >>> to_yaml({'a': 1, 'b': 2})
    '{a: 1, b: 2}\\n'
    >>> to_yaml({1: {'a': [1,2,3]}})
    '1:\\n  a: [1, 2, 3]\\n'
    >>> to_yaml("abc")
    'abc\\n...\\n'
    '''
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
