import random

def loadCards(filename, shuffle=True):
    if filename.endswith(".txt"):
        fi = open(filename, 'r')
        finame = filename.replace('.txt','')
    else:
        fi = open(filename + '.txt', 'r')
        finame = filename
    print("Loading " + finame + ". . .", end=' ')
    array = []
    for i in fi:
        current = i.replace('\n', '')
        array.append(current)
    print("   [DONE]") 
    if shuffle:
        random.shuffle(array)   
    return array
