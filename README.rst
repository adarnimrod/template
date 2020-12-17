Template
########

.. image:: https://git.shore.co.il/nimrod/template/badges/master/pipeline.svg
    :target: https://git.shore.co.il/nimrod/template/-/commits/master

A CLI tool for generating files from `Jinja2 <http://jinja.pocoo.org/>`_
templates and environment variables.

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
- :code:`to_toml`: Convert to toml.
- :code:`from_toml`: Convert from toml.
- :code:`jmespath`: Queries data using the `JMESPath <http://jmespath.org/>`_
  query language.
- :code:`run`: Runs a command and returns the stdout, stderr and returncode
  using `run
  <https://docs.python.org/3.6/library/subprocess.html?highlight=popen#subprocess.run>`_.

Example usage can be seen in :code:`tests` and for specific filters in the
docstrings in :code:`template/filters.py`.

Testing
-------

Tests require `Pipenv <https://docs.pipenv.org>`_ and `Bats
<https://github.com/bats-core/bats-core>`_. Run the tests with the
following commands:

.. code:: shell

   pipenv run lint  # Pre-commit hooks.
   pipenv run doctest  # Doc tests.
   pipenv run bats  # Bats tests.
   pipenv run check  # Twine check.

Also, GitLab CI is setup for this project so every push to this repository is
checked with all Python 2.7, Python 3.6 and later and all supported versions of
PyPy.

Release
-------

Release requires `Pipenv <https://docs.pipenv.org>`_. To bump the version run
:code:`pipenv run bumpversion major|minor|patch` to update the version and git
commit and tag. Then run :code:`pipenv run upload` to upload the new version to
PyPI and :code:`git push --follow-tags` to push the git commit and tag.

License
-------

This software is licensed under the AGPL 3+ license (see the :code:`LICENSE.txt`
file).

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/nimrod/.
