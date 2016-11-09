Template
########

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
