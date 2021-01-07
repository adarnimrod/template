#!/usr/bin/env python
# pylint: disable=missing-docstring
from setuptools import setup, find_packages

setup(
    name="template",
    version="0.6.3",
    description="""A CLI tool for generating files from Jinja2 templates and
    environment variables.""",
    long_description=open("README.rst", "r").read(),
    long_description_content_type="text/x-rst",
    url="https://www.shore.co.il/git/template",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    license="AGPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: System Administrators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",  # noqa: E501 pylint: disable=line-too-long
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
    extras_require={"dev": ["pipenv"]},
    entry_points={"console_scripts": ["template=template:main"]},
)
