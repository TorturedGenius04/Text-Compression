import utils as Utils

data = Utils.readFile("text.txt");
array = Utils.getFileAsArray(data);

Utils.findWordInFile("sentence.txt", "is"); # Task 1

Utils.writeSentenceToFile("sentence.txt"); # Task 2

Utils.minifyData(array); # Task 3
Utils.reconstruct();