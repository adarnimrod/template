#!/usr/bin/env python
# pylint: disable=missing-docstring
from setuptools import setup, find_packages
from template import __doc__ as description

setup(
    name="template",
    version="0.6.6",
    description=description,
    long_description=open("README.rst", "r").read(),
    long_description_content_type="text/x-rst",
    url="https://git.shore.co.il/nimrod/template",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    license="AGPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",  # noqa: E501 pylint: disable=line-too-long
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    keywords="config configuration jinja template environment",
    packages=find_packages(),
    install_requires=[
        "Jinja2",
        "PyYAML",
        "jmespath",
        "toml",
        "subprocess32>=3.5.0;python_version<'3.5'",
    ],
    extras_require={
        "all": [
            "jmespath",
            "netaddr",
            "PyYAML",
            "toml",
        ],
        "dev": ["pipenv"],
        "jmespath": ["jmespath"],
        "netaddr": ["netaddr"],
        "toml": ["toml"],
        "yaml": ["PyYAML"],
    },
    entry_points={"console_scripts": ["template=template:main"]},
)
