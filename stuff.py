import requests
import json

class jsonParser:
    searchTermDict = {}
    searchTermList = []

    fileList = []
    def __init__(self, keywordsJSON, localDatabaseJSON, debugMode):
        with open(keywordsJSON) as objectAttributes:
            self.data = json.load(objectAttributes)
        with open(localDatabaseJSON) as localDatabase:
            self.databaseInfo = json.load(localDatabase)

        for i in self.data["SearchTerms"][0]:
            j = self.data["SearchTerms"][0][i]
            self.searchTermDict[i] = []
            self.searchTermList.append(i)
            for z in j:
                self.searchTermDict[i].append(z)

        if debugMode is True:
            print(self.searchTermDict)

    def showParsed(self):
        for i in self.databaseInfo:
            for j in self.searchTermList:
                try:
                    print("Parsing " + i + " " + j + ": " + self.databaseInfo[i][0][j])
                except KeyError:
                    print("Key " + j + " does not exist. please check composition of fileAttributes.json")

    def printSearchTerms(self):
        print(self.searchTermList)

    def findWithAtrributes(self, attributeList):
        tempDict = {}
        tempDict2 = {}

        for i in self.databaseInfo:
            tempDict[i] = self.databaseInfo[i]
            tempDict2[i] = self.databaseInfo[i]

        tempKeys = tempDict.keys()

        for i in attributeList:
            for j in i.keys():
                if j not in self.searchTermList:
                    print("You searched for a term that was not in the term list.")
                    break

        for i in tempKeys: #go through all our possible files
            for j in attributeList: #go through all the entered data
                for z in j.keys():
                    if j[z] != tempDict[i][0][z]:
                        if i in tempDict2:
                            del tempDict2[i]

        return tempDict2

    def scrapeKeys(self, fwaObject):
        tempKeys = []
        for i in fwaObject.keys():
            tempKeys.append(i)
        return tempKeys


print("Pre Implementation of JSON management tools for Szism")
print("By: Austin Fell")

dataObject = jsonParser("keywords.json", "fileAttributes.json", False)
z = dataObject.findWithAtrributes([{"SinglePage" : "Multi Page"}, {"Beautiful" : "No"}])
print(dataObject.scrapeKeys(z))
