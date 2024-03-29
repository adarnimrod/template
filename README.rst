Template
########

.. image:: https://git.shore.co.il/nimrod/template/badges/master/pipeline.svg
    :target: https://git.shore.co.il/nimrod/template/-/commits/master
    :alt: pipeline status

.. image:: https://img.shields.io/pypi/v/template.svg
    :target: https://pypi.org/project/template/
    :alt: Latest version on PyPI

.. image:: https://img.shields.io/pypi/l/template.svg
    :target: http://www.gnu.org/licenses/agpl-3.0.en.html
    :alt: Project license

.. image:: https://img.shields.io/pypi/dm/template.svg
    :target: https://pypistats.org/packages/template
    :alt: PyPI Stats

|

.. image:: https://img.shields.io/pypi/implementation/template.svg
    :target: https://git.shore.co.il/nimrod/template/-/pipelines/latest
    :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/pyversions/template.svg
    :target: https://git.shore.co.il/nimrod/template/-/pipelines/latest
    :alt: Supported Python versions

A CLI tool for generating files from `Jinja2 <http://jinja.pocoo.org/>`_
templates and environment variables.


Installation
------------

.. code:: shell

    pip install template[all]


This will install Template along with the dependencies for all of the filters
available with it. However, you can use narrower specifiers if you want to avoid
a specific dependency (the filters listed below include the needed specifier).
In previous releases of Template all of the dependencies were required. To not
break existing templates, for the foreseeable future those dependencies will
remain a requirement and new dependencies for specific filters will be optional.
This will change in the 0.9 release where all filter specific dependencies will
be optional. Please update your project before that happens.


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

- :code:`combine`: Merges 2 dictionaries with the 2nd overriding the 1st.
  Returns the result.
- :code:`to_yaml`: Convert to yaml (requires the :code:`yaml` package
  specifier).
- :code:`from_yaml`: Convert from yaml (requires the :code:`yaml` package
  specifier).
- :code:`to_json`: Convert to json.
- :code:`from_json`: Convert from json.
- :code:`to_toml`: Convert to toml (requires the :code:`toml` package
  specifier).
- :code:`from_toml`: Convert from toml (requires the :code:`toml` package
  specifier).
- :code:`jmespath`: Queries data using the `JMESPath <http://jmespath.org/>`_
  query language (requires the :code:`jmespath` package specifier).
- :code:`run`: Runs a command and returns the stdout, stderr and returncode
  using run_. This filter is replaced with the :code:`run` function and will
  be removed in the 0.10 release.
- :code:`ipaddress`: Returns an IPAddress object from the netaddr_ library
  (requires the :code:`netaddr` package specifier).
- :code:`ipnetwork`: Returns an IPNetwork object from the netaddr_ library
  (requires the :code:`netaddr` package specifier).
- :code:`iprange`: Returns an IPRange object from the netaddr_ library.
  (requires the :code:`netaddr` package specifier).
- :code:`ipglob`: Returns an IPGlob object from the netaddr_ library (requires
  the :code:`netaddr` package specifier).
- :code:`ipset`: Returns an IPSet object from the netaddr_ library (requires
  the :code:`netaddr` package specifier).

Example usage can be seen in :code:`tests` and for specific filters in the
docstrings in :code:`template/filters.py`.

Jinja functions
---------------

- :code:`run`: Runs a command and returns the stdout, stderr and returncode
  using run_. This function replaces the :code:`run` filter.
- :code:`readfile`: Returns the contents of a file.

Example usage can be seen in :code:`tests` and for specific filters in the
docstrings in :code:`template/functions.py`.

Testing
-------

Tests require Pipenv_ and
`Bats <https://github.com/bats-core/bats-core>`_. Run the tests with the
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

Release requires Pipenv_ and Python 3.6 or later. To bump the version run
:code:`pipenv run bumpversion major|minor|patch` to update the version and git
commit and tag the changes, then run :code:`git push --follow-tags` to push the
git commit and tag. The GitLab CI will then build and upload a release to PyPI.
To manually upload to PyPI run :code:`pipenv run build` to build the Python
package and :code:`pipenv run upload -s dist/*` to upload a signed version.

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

.. _netaddr: https://netaddr.readthedocs.io/
.. _Pipenv: https://docs.pipenv.org
.. _run: https://docs.python.org/3.6/library/subprocess.html?highlight=popen#subprocess.run
