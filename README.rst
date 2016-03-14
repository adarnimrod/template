Template
########

A CLI tool for generating files from Jinja2 templates and environment variables.

Example
-------

.. code:: shell

    $ template -h
    usage: template [-h] [-o OUTPUT] [filename]

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
    $ cat username
    John

TODO
----

- Complex data types (process environment variables, Jinja filters).
