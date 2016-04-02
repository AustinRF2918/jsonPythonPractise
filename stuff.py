import requests
import json

dataOne = '["StartBootstrap-OnePagePortfolio", {"Attributes": ["one page", "business", "beautiful"]}]'
dataTwo = '["StartBootstrap-TwoPagePortfolio", {"Attributes": ["two page", "personal", "drab"]}]'

if __name__ == "__main__":
    loadedJSON = []
    loadedJSON.append(json.loads(dataOne))
    loadedJSON.append(json.loads(dataTwo))
    temp = loadedJSON[0]
    for i in temp[1]['Attributes']:
        print(i)

