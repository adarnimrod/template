#!/usr/bin/env python
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


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
    '''
    Converts given data structure to JSON form.
    Examples:

    >>> to_json([1,2,3])
    '[1, 2, 3]'
    >>> to_json({'b':2})
    '{"b": 2}'
    >>> to_json(2)
    '2'
    >>> to_json({1: {'a': [1,2,3]}})
    '{"1": {"a": [1, 2, 3]}}'
    '''
    from json import dumps
    return dumps(value)


def from_json(value):
    '''
    Returns native data structure from the given JSON string.
    Examples:

    >>> from_json('[1, 2, 3]')
    [1, 2, 3]
    >>> from_json('"a"')
    u'a'
    >>> from_json('{"1": {"a": [1, 2, 3]}}')
    {u'1': {u'a': [1, 2, 3]}}
    '''
    from json import loads
    return loads(value)


def from_yaml(value):
    '''
    Returns native data structure from the given YAML string.
    Examples:

    >>> from_yaml('a')
    'a'
    >>> from_yaml('[1, 2, 3]')
    [1, 2, 3]
    >>> from_yaml('{"1": {"a": [1, 2, 3]}}')
    {'1': {'a': [1, 2, 3]}}
    '''
    from yaml import safe_load
    return safe_load(value)


def pprint(value):
    '''
    Returns a pretty string representation of the data structure given.
    Examples:
    >>> pprint(1)
    '1'
    >>> pprint([{'first_name': 'John', 'last_name': 'Doe'}, {'first_name': 'Jane', 'last_name': 'Doe'}])  # noqa: E501
    "[{'first_name': 'John', 'last_name': 'Doe'},\\n {'first_name': 'Jane', 'last_name': 'Doe'}]"
    '''
    from pprint import pformat
    return pformat(value)


def combine(default, override):
    '''
    Returns a combined dictionary of the 2 dictionaries given (with the 2nd
    overriding the 1st).
    Examples:
    >>> combined = combine({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    >>> 'a' in combined
    True
    >>> 'c' in combined
    True
    >>> combined['b'] == 3
    True
    '''
    combined = default.copy()
    combined.update(override)
    return combined
