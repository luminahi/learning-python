
import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as jsonFile:
            data = json.load(jsonFile)
    except IOError:
        print("Could not read file")
    return data

