from sys import exc_info

class CodeBuddyCore:
    def __init__(self, function) -> None:
        self.function = function

    def getExcpetionInformation(self) -> str:
        type_, value, _ = exc_info()
        raw = f"{type_.__name__}: {value}"
        searchable = raw.replace(f"{self.function.__name__}()", "x()")
        return searchable

def codebuddy(function, arguments: list = None) -> None:
    try:
        if arguments == None:
            function()
        else:
            exec(f"function{tuple(arguments)}")
    except Exception:
        core = CodeBuddyCore(function)
        core.entry()