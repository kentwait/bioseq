from setuptools import setup

setup(
    # nxsim:
    name='bioseq',

    # Version number:
    version='0.1.2',

    # Application author details:
    author='Kent Kawashima',
    author_email='i@kentwait.com',

    # Package
    packages=['bioseq'],
    url='http://pypi.python.org/pypi/bioseq',
    license='LICENSE',
    description='Bioseq is a lightweight Python package for handling nucleotide, protein, and codon sequences.',

    # Dependent packages
    requires=[
        'numpy',
    ],

)
