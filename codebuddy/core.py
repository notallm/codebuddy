from sys import exc_info
from traceback import format_exc

from html import unescape

from os import get_terminal_size

from codebuddy.helper import *
from codebuddy.stackAPI import StackAPI

class CodeBuddyCore:
    def __init__(self, function) -> None:
        self.function = function

    def getExcpetionInformation(self) -> str:
        type_, value, _ = exc_info()
        searchable = str(value).replace(f"{self.function.__name__}()", "")
        return type_, searchable, format_exc()

    def entry(self) -> None:
        type_, searchable, traceback = self.getExcpetionInformation()
        filteredSearch = filterExceptionInformation(searchable)
        api = StackAPI()
        results = api.search(filteredSearch)
        # formatting results
        width = get_terminal_size().columns
        alert = f"""\
{'=' * width}
Exception of type {type_.__name__} caught by CodeBuddy
{'=' * width}

{'=' * width}
Possible Solutions
{'=' * width}
"""
        print(traceback)
        print(alert)
        print("-" * width)
        for indice in range(len(results)):
            result = results[indice]
            title = result["title"]
            description = result["body_markdown"]
            if ". " in description:
                description = description.split(". ")[0]
            else:
                description = description.split("\n")[0]
            title = unescape(title)
            description = unescape(description).replace("\n", " ")
            url = result["link"]
            solution = f"""
{title}
    {description}
    URL: {url}
"""
            print(solution)
            print("-" * width)