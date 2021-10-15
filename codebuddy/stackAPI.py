from json import loads
from requests import get

class StackAPI:
    def __init__(self) -> None:
        pass

    def search(self, query: str) -> dict:
        url = f"https://api.stackexchange.com/2.3/search?order=desc&sort=activity&tagged=python&intitle={query}&site=stackoverflow&filter=!nKzQUR30W7"
        response = get(url).text
        json = loads(response)
        top = json["items"][:5]
        return top