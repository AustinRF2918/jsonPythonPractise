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

class jsonWriter:
    searchTermDict = {}
    searchTermList = []
    fileList = []
    databasePath = ""
    readingPath = ""

    def __init__(self, keywordsJSON, localDatabaseJSON, debugMode):
        with open(keywordsJSON) as objectAttributes:
            self.data = json.load(objectAttributes)
            self.readingPath = keywordsJSON
        with open(localDatabaseJSON) as localDatabase:
            self.databaseInfo = json.load(localDatabase)
            self.databasePath = localDatabaseJSON

        for i in self.data["SearchTerms"][0]:
            j = self.data["SearchTerms"][0][i]
            self.searchTermDict[i] = []
            self.searchTermList.append(i)
            for z in j:
                self.searchTermDict[i].append(z)

        if debugMode is True:
            print(self.searchTermDict)

    def showKeys(self):
        print(self.searchTermList)

    def showParsed(self):
        for i in self.databaseInfo:
            for j in self.searchTermList:
                try:
                    print("Parsing " + i + " " + j + ": " + self.databaseInfo[i][0][j])
                except KeyError:
                    print("Key " + j + " does not exist. please check composition of fileAttributes.json")

    def addData(self, additionalData):
        #stolen from http://stackoverflow.com/questions/15415709/update-json-file

        innerTempDict = {}

        print("Entering data for: " + additionalData)
        for i in self.searchTermList:
            print("Data: " + i)
            temp = input()
            innerTempDict[i] = temp

        tempDict = {}
        tempDict[additionalData] = [innerTempDict]


        with open(self.databasePath, "a") as json_file:
            json_file.write("{}\n".format(json.dumps(tempDict))[1:-1])

        f = open(self.databasePath, "r")
        contents = f.readlines()
        f.close()

        contents.insert(0, "{\n" + contents[len(contents) - 1])
        contents.pop()

        f = open(self.databasePath, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()




print("Pre Implementation of JSON management tools for Szism")
print("By: Austin Fell")

dataAddition = jsonWriter("keywords.json", "fileAttributes.json", False)
dataAddition.addData("StartBootstrap-Yomother")
