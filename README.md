The `typename` module defines a single function also called typename which returns the name of the
type of any object as a string:

    >>> x = 5
    >>> typename(x)
    'int'

Its purpose is purely aesthetic, to avoid unsightly constructs such as `type(obj).__name__` or the
ghastly `obj.__class__.__name__`.
