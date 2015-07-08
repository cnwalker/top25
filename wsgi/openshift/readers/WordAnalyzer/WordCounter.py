import os, string, StemFinder

def get_irregulars():
#Creates a dictionary of irregular conjugations
#The os pathing is to make sure file reading works on openshift/django
    iDict = {}
    irreg = open(os.path.join(os.path.dirname(__file__), 'irregular.txt'), 'r')
    for line in irreg.readlines():
        curline = map(lambda x: x.strip(), line.split(','))
        iDict[curline[0]] = curline[1]
    return iDict

def remove_punctuation(text):
#Uses the string module to completely remove punctuation from input string
    return text.translate(string.maketrans("",""), string.punctuation)

def combine_stems(input_dict):
#An analyzed dictionary with stems
    stemmedDict = {}
    #all_words.txt is a file that holds all the words in the English language
    all_words = map(lambda x: x.strip(), open(os.path.join(os.path.dirname(__file__), "all_words.txt"), 'r').readlines())
    irregulars = get_irregulars()
    for key in input_dict.keys():
        stem_key = StemFinder.getStem(key, all_words, irregulars)
        if stem_key in stemmedDict:
            stemmedDict[stem_key] += input_dict[key]
        else:
            stemmedDict[stem_key] = input_dict[key]
        input_dict.pop(key)
    return stemmedDict
              
def combine_words(filename):
#Reads in a given file and takes note of unique words
    Dict = {}
    raw = open(filename, 'r')
    for line in raw.readlines():
        line = remove_punctuation(line.strip()).lower().split()
        if line != []:
            for word in line:
                if Dict.get(word) == None:
                    Dict[word] = 1
                else:
                    Dict[word] += 1
    return Dict

def analyzeStems(filename):
    return combine_stems(combine_words(filename))

def listify(inDict):
    outList = []
    for key in sorted(inDict, key=lambda x: -1*inDict[x]):
        outList.append([key, inDict[key]])
    return outList
                       
    
