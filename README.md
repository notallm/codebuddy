# codebuddy
stack overflow search on exception

codebuddy is a tool for python programmers. On exceptions, it uses the stack overflow public api to search for 
top answers and returns them in a neat fashion, along with traceback information for debug information.

example: basic usage
``` python
from codebuddy import codebuddy

def main():
    print(7 + "3") # throws error

codebuddy(main) # show codebuddy the entrypoint
```

this code returns an error, which codebuddy catches and gets stack overflow answers for.

```
$ python3 main.py

Traceback (most recent call last):
  File "/home/aarushgupta/fun/codebuddy/codebuddy/__init__.py", line 6, in codebuddy
    function()
  File "main.py", line 6, in main
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

example: function argument support
``` python
from codebuddy import codebuddy

def main(number: int):
    print(number + "3")

codebuddy(main, 1) # executes as "main(1)"
```
