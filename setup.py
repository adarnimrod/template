#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='template',
    version=open('VERSION', 'r').read(),
    description='''A CLI tool for generating files from Jinja2 templates and
    environment variables.''',
    long_description=open('README.rst', 'r').read(),
    url='https://www.shore.co.il/git/template',
    author='Nimrod Adar',
    author_email='nimrod@shore.co.il',
    license='MIT',
    classifiers=[
        'Development status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
    ],
    keywords='config configuration jinja template environment',
    packages=find_packages(),
    install_requires=['Jinja2', 'PyYAML'],
    extras_require={
        'dev': ['tox'], },
    entry_points={
        'console_scripts': [
            'template=template:main'], },
)
