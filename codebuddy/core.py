from sys import exc_info
from traceback import format_exc

from html import unescape

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
        error = f"{type_.__name__}: {searchable}"
        userInformation = f"Exception caught by CodeBuddy: {type_.__name__}"
        print(traceback)
        print("=" * len(userInformation) + "\n")
        print(userInformation)
        print("-" * len(userInformation))
        print("\nStack Overflow search results:\n")
        for indice in range(len(results)):
            result = results[indice]
            title = result["title"]
            description = result["body_markdown"]
            if ". " in description:
                description = description.split(". ")[0]
            else:
                description = description.split("\n")[0]
            title = unescape(title)
            description = unescape(description)
            url = result["link"]
            print(f"{indice + 1}. {title}")
            print(f"   {description}")
            print(f"   URL to question: {url}")
            if indice + 1 < len(results):
                print()