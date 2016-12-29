Template
########

.. image:: https://travis-ci.org/adarnimrod/template.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/template

A CLI tool for generating files from Jinja2 templates and environment
variables.

Examples
--------

.. code:: shell

    $ template -h
    usage: template [-h] [-o OUTPUT] [filename]

    A CLI tool for generating files from Jinja2 templates and environment
    variables.

    positional arguments:
      filename              Input filename

      optional arguments:
        -h, --help            show this help message and exit
          -o OUTPUT, --output OUTPUT
                                  Output to filename
    $ export name='John'
    $ echo 'Hello {{ name if name is defined else 'world' }}. | template
    Hello John.
    $ echo '{{ USER }}' > username.j2
    $ template --output username.txt username.j2
    $ cat username.txt
    John


Jinja filters
-------------

The following Jinja filters were added:

- :code:`to_yaml`: Convert to yaml.
- :code:`from_yaml`: Convert from yaml.
- :code:`to_json`: Convert to json.
- :code:`from_json`: Convert from json.
- :code:`pprint`: Pretty print variable.
- :code:`combine`: Combine 2 dictionaries.

Example usage can be seen in :code:`tests.sh`.

Testing
-------

Local tests require both a Python 2, Python 3 and Tox installed and can be run
by running :code:`tox`. Alternatively, Travis CI is used to test on multiple
versions of Python for every push.

Release
-------

Currently releases are done locally by running :code:`tox -e release` and
require Python and Tox installed. Releases with Travis CI are coming.

License
-------

This software is licensed under the AGPL 3+ license (see the :code:`LICENSE.txt`
file).

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.

TODO
----

- Fix combining dictionaries test.
- Fix Travis CI test on Python 3.2 (https://travis-ci.org/adarnimrod/template/jobs/187388235).
- Release on tagged commits to PyPI in Travis CI.
- TOML support?
