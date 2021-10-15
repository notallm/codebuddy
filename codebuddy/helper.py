def filterExceptionInformation(information: str) -> str:
    filter = ["takes"]
    for item in filter:
        information = information.replace(item, "")
    information = " ".join(information.split()) # removes extra whitespaces
    return information