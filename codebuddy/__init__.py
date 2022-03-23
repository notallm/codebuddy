from codebuddy.core import CodeBuddyCore

from typing import Any

def codebuddy(function, *arguments: Any) -> None:
    try:
        function(*arguments)
    except Exception:
        core = CodeBuddyCore(function)
        core.entry()