from collections import OrderedDict;
from datetime import datetime;

def readFile(path):
    return open(path, 'r').read();

def getFileAsArray(data):
    return data.split(' ');

def getTime():
    return (datetime.now().time().second) * 1000 + datetime.now().time().microsecond;

def findWordInFile(path, word):
    startTime = getTime();

    data = getFileAsArray(readFile(path));

    for index, value in enumerate(data):
        if str.capitalize(word) == str.capitalize(value):
            print "Found '" + word + "' at position " + str(index);

    now = getTime();
    timeTaken = now-startTime;

    print "Found word in: " + str(timeTaken) + " milliseconds";

def writeSentenceToFile(path):
    data = getFileAsArray(readFile(path));

    noDupes = list(OrderedDict.fromkeys(data));

    keys = [];
    order = [];

    for value in data:
        for indexKey, valueKey in enumerate(noDupes):
            if (value == valueKey):
                order.append(indexKey);
                key = value;
                if (key not in keys):
                    keys.append(key);

    minFile = open('sentenceMin.txt', 'w');

    for index, value in enumerate(keys):
        val = str(keys[index]);
        minFile.write(val + "|");

    minFile.write('\n');

    for index, value in enumerate(order):
        minFile.write(str(value) + ",");

    print "Condensed sentence!"

def minifyData(data):
    startTime = getTime();

    noDupes = list(OrderedDict.fromkeys(data));

    keys = [];
    order = [];

    for value in data:
        for indexKey, valueKey in enumerate(noDupes):
            if (value == valueKey):
                order.append(indexKey);
                key = value;
                if (key not in keys):
                    keys.append(key);

    minFile = open('min.txt', 'w');

    for index, value in enumerate(keys):
        val = str(keys[index]).replace('\n', '/n');
        minFile.write(val + "|");

    minFile.write("||");

    for index, value in enumerate(order):
        minFile.write(str(value) + ",");

    now = getTime();
    timeTaken = now - startTime;

    print "Text Minified in: " + str(timeTaken) + " milliseconds";

def reconstruct():
    startTime = getTime();

    minFile = open('min.txt', 'r');

    rawData = minFile.read();
    data = rawData.split("||");

    rawkeys = data[0];
    raworder = data[1];

    keys = rawkeys.split('|');
    orderArray = raworder.split('|');

    order = orderArray[1].split(',')

    fileStr = '';

    for index, value in enumerate(order):
        if value is not '':
            fileStr += keys[int(value)].replace('/n', '\n') + " ";
            fileStr.replace('/n', '\n');

    constrFile = open('constructed.txt', 'w');
    constrFile.write(fileStr);

    now = getTime();
    timeTaken = now - startTime;

    print "Re-constructed file from min.txt in: " + str(timeTaken) + " milliseconds";