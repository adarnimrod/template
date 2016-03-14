Template
########

A CLI tool for generating files from Jinja2 templates and environment variables.

Example
-------

.. code:: shell

    $ export name='John'
    $ echo 'Hello {{ name if name is defined else 'world' }}. | template
    Hello John.


TODO
----

- Input/output detection/redirection.
- Complex data types (process environment variables, Jinja filters).
