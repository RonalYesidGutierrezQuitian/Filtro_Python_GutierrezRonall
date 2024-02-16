import os

def filterFor(key, forFilter, **data):
    d = [element for element in data if element[key] == forFilter]
    return d


def uuid(category:str, data:list):
    firstCaracter = category[0].upper()
    lenData = len(data)
    if (lenData < 9) and (lenData > 0):
        return f"{firstCaracter}0{lenData + 1}"
    elif (lenData == 0):
        return f"{firstCaracter}01"
    else:
        return f"{firstCaracter}{lenData}"