import json
import os

URL = "data/db.json"

data = {
    "miMovistar":{"servicios":{},
                  "usuarios":{},
                  "categorias":{}
                  }
}

def saveData(**data):
    with open(URL, "w") as archivo:
        json.dump(data, archivo, indent=4)


def loadData(**data):
    if os.path.isfile(URL):
        with open(URL, "r") as archivo:
            return json.load(archivo)
    else:
        saveData(**data)
        return data
    

saveData(**data)