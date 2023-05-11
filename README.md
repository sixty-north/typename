# Typename

![CI](https://github.com/sixty-north/typename/actions/workflows/actions.yml/badge.svg)

The `typename` module defines a single function also called `typename` which returns the name of the
type of any object as a string.

Its purpose is purely aesthetic, to avoid unsightly constructs such as `type(obj).__name__` or the
ghastly `obj.__class__.__name__`.

# Installation

The `typename` package is available on the Python Package Index (PyPI):

[![PyPI version](https://badge.fury.io/py/typename.svg)](https://badge.fury.io/py/typename)

*Typename* should work with any version of Python 3. To install:

With `pip` from PyPI:

    pip install typename

# How to use

    >>> from typename import typename
    >>> x = 5
    >>> typename(x)
    'int'
