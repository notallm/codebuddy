<h1 align = "center"><a href = "https://pypi.org/project/codebuddy/">CodeBuddy <code>v0.0.2</code></a></h1>
<h3 align = "center">stack overflow search on exception</h3>

# Overview

`codebuddy` is a tool for python programmers. On exceptions, it uses the stack overflow public api to search for top answers and returns them in a neat fashion, along with traceback information for debug information.

# Examples

## Basic Usage

``` python
from codebuddy import codebuddy

def main():
    print(7 + "3") # <= that's illegal

codebuddy(main)
```

This code returns an error, which `codebuddy` catches and gets stack overflow answers for.

```
$ python3 main.py

Traceback (most recent call last):
  File "/home/aarushgupta/fun/codebuddy/codebuddy/__init__.py", line 6, in codebuddy
    function()
  File "test.py", line 4, in bob
    print(7 + "3")
TypeError: unsupported operand type(s) for +: 'int' and 'str'

============================================================================================
Exception of type TypeError caught by CodeBuddy
============================================================================================

============================================================================================
Possible Solutions
============================================================================================

--------------------------------------------------------------------------------------------

Python TypeError: unsupported operand type(s) for +: 'int' and 'str'
    I Have been working on a project and get the following error: `TypeError: unsupported operand type(s) for +: 'int' and 'str'.`
    URL: https://stackoverflow.com/questions/29261566/python-typeerror-unsupported-operand-types-for-int-and-str

--------------------------------------------------------------------------------------------

...
```

Very neat indeed! The user also gets the description and url to the question in the results as well.

## Advanced Usage

`codebuddy` also supports arguments

``` python
from codebuddy import codebuddy

def main(number: int):
    print(number + "3") # <= that's still illegal

codebuddy(main, 1) # executes function as "main(1)"
```

# Copyright &copy; 2023 Aarush Gupta
This code is copyrighted but licensed to the public under the GNU AGPLv3 license and any later versions.
