"""Defines a single function which returns the name of the type of any object as a string.

Its purpose is purely aesthetic, to avoid unsightly constructs such as `type(obj).__name__` or the
ghastly `obj.__class__.__name__`.
"""

__version__ = "1.0.4"
__version_info__ = tuple(__version__.split('.'))


def typename(obj) -> str:
    """The name of the type of an object."""
    return type(obj).__name__

