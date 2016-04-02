import requests
import json

searchTermDict = {}
searchTermList = []

fileList = []

with open("keywords.json") as objectAttributes:
    data = json.load(objectAttributes)

with open("fileAttributes.json") as localDatabase:
    databaseInfo = json.load(localDatabase)


print("Pre Implementation of JSON management tools for Szism")
print("By: Austin Fell")
print("(Non-Release)")

if __name__ == "__main__":
    for i in data["SearchTerms"][0]:
        j = data["SearchTerms"][0][i]
        searchTermDict[i] = []
        searchTermList.append(i)
        for z in j:
            searchTermDict[i].append(z)

print("Now reading in partially corrupt data from local database")

for i in databaseInfo:
    for j in searchTermList:
        try:
            print("Parsing " + i + " " + j + ": " + databaseInfo[i][0][j])
        except KeyError:
            print("KEY " + j + " DOES NOT EXIST. PLEASE CHECK COMPOSITION OF fileAttributes.json")

