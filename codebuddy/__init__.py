from codebuddy.core import CodeBuddyCore

def codebuddy(function, arguments: list = None) -> None:
    try:
        if arguments == None:
            function()
        else:
            exec(f"function{tuple(arguments)}")
    except Exception:
        core = CodeBuddyCore(function)
        core.entry()