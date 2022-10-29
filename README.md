# Overview

[![PyPI Version][pypi-image]][pypi-url]

This package is created to make the debug process much easier for python projects.

## Algorithm

This package imports `@debug` decorator for functions and methods, which:

1. Prints all arguments taken by function and their types.
2. Show how long is instance running in seconds.
3. Catches and prints out detailed information about all exceptions.
4. Prints out all returned values and their types.

## Usage

1. Import debug from clevdebug library: `from clevdebug import debug`
2. Add `@debug` decorator to the function or method: `@debug`
3. Run the script.

## Examples

There are several usage cases.

### Simple Example

```python
# import debug from clevdebug
from clevdebug import debug


# Debugger for function
@debug
def foob(a, b):
    return b


# Debugger for method in class
class Boof:
    @debug
    def __init__(a, b) -> None:
        pass


if __name__ == '__main__':
    boo = Boof(1, b = 2)
    foob(1, 2)
```

Output is:

```
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         20: ========================================
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         21: Calling [<class 'function'>]foo:
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         37: There are 2 arguments:
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         40:      a: [<class 'int'>] 5
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         40:      b: [<class 'int'>] 4
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         43: Running foo takes: 0.00000
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         45: Result is: [<class 'int'>]4
2022-10-29 19:27:49,521 debugger of foo                        wrapper on line         58: ========================================
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         20: ========================================
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         21: Calling [<class 'function'>]__init__:
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         37: There are 2 arguments:
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         40:         a: [<class 'int'>] 5
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         40:         b: [<class 'int'>] 4
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         43: Running __init__ takes: 0.00000
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         47: There is no return.
2022-10-29 19:27:49,521 debugger of __init__                        wrapper on line         58: ========================================
```

### Catching errors

```python
# import debug from clevdebug
from clevdebug import debug


# Debugger for function
@debug
def foob(a, b):
    return b/0


if __name__ == '__main__':
    foob(1, 2)
```

Output is:

```
2022-10-29 19:37:47,173 debugger of foob                        wrapper on line         20: ========================================
2022-10-29 19:37:47,173 debugger of foob                        wrapper on line         21: Calling [<class 'function'>]foob:
2022-10-29 19:37:47,173 debugger of foob                        wrapper on line         37: There are 2 arguments:
2022-10-29 19:37:47,173 debugger of foob                        wrapper on line         40:     a: [<class 'int'>] 1
2022-10-29 19:37:47,173 debugger of foob                        wrapper on line         40:     b: [<class 'int'>] 2
2022-10-29 19:37:47,174 debugger of foob                        wrapper on line         54: Exception type : ZeroDivisionError 
2022-10-29 19:37:47,174 debugger of foob                        wrapper on line         55: Exception message : division by zero
2022-10-29 19:37:47,174 debugger of foob                        wrapper on line         56: Stack trace : ['File : PATH/main.py , Line : 42, Name : wrapper, Message : result = func(*args, **kwargs)', 'File : /PATH/dev.py , Line : 6, Name : foob, Message : return b/0']
2022-10-29 19:37:47,174 debugger of foob                        wrapper on line         58: ========================================
```

### Do not use to class


```python
from clevdebug import debug


@debug
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    A(1, 2)
```

Output is:

```
TypeError: Only functions or methods INSIDE a class can be debugged
```

## Installation

`pip install clevdebug`

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/clevdebug
[pypi-url]: https://pypi.org/project/clevdebug

