import json
import os
import sys

# Config

# save the file every x keys [default = 5]
saveEvery = 5

# Config Ends

def start():
    thisDict = ''
    outputFile = ''
    try:
        inputFile = sys.argv[1]
        thisDict = jsonToDict(inputFile)
    except:
        print("""
    What file do you want to translate? (Example: 'en_us.json')
        """)
        while not thisDict:
            inputFile = getInput()
            thisDict = jsonToDict(inputFile)
    try:
        outputFile = sys.argv[2]
    except:
        print("""
    What file do you want to save this as? (Example: 'output.json')
        """)
        while not outputFile:
            outputFile = getOutput()
    translateDict(thisDict, outputFile)

def getInput():
    thisFile = input('Input File: ')
    if '.' not in thisFile:
        thisFile = thisFile + '.json'
    return thisFile

def jsonToDict(thisFile):
    try:
        with open(thisFile, 'r', encoding='raw_unicode_escape') as thisJson:
            return json.loads(thisJson.read().encode('raw_unicode_escape').decode())
    except FileNotFoundError:
        print("""
    File not found
        """)
        return
    except json.decoder.JSONDecodeError:
        print("""
    This tool only works with JSON files
        """)
        return

def getOutput():
    thisFile = input('Output File: ')
    if not thisFile:
        thisFile = 'output'
    if not thisFile.endswith('.json'):
        thisFile = thisFile + '.json'
    if thisFile in os.listdir():
        print("""
    File '{}' already exists, do you want to override it? (Y/N)
        """.format(thisFile))
        while True:
            answer = input('Answer: ')
            if answer.lower() in ['y', 'yes']:
                return thisFile
            elif answer.lower() in ['n', 'no']:
                return print()
    return thisFile

def translateDict(thisDict, outputFile):
    newDict = {}
    maxLen = len(thisDict)
    print("""
    For each value, two lines are printed:
    The first line shows the default value
    The second line accepts a new value as an input
    (Pressing enter will use the default value)
    """)
    with open(outputFile, 'w+', encoding='utf-8') as thisFile:
        thisFile.write('{\n}')
    for index, (key, value) in enumerate(thisDict.items(), start=1):
        # print "[current key/total number of keys]"
        print("[{0}/{1}] {2}".format(index, maxLen, key))
        # print "key: value"
        print("Old: " + value)
        # print "key: (your new value)"
        newValue = input("New: ")
        # if the value is empty, use the default value
        if newValue:
            newDict[key] = newValue
        else:
            newDict[key] = value
        # print "newline"
        print()
        # save every x keys
        saveFile(outputFile, newDict)
    return print("Done!")

def saveFile(file, dict):
    with open(file, 'w+', encoding='utf-8') as thisFile:
        json.dump(dict, thisFile, indent=2)

if __name__ == '__main__':
    start()