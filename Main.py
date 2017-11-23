import random
from Util import computeErrors
from Util import getListOfOpcode
from db import database

def filterData():
    opcodes = getListOfOpcode()

    features = []
    return features

def main():
    '''
    Now we are building the model of APK, i.e. a vector which represents
    a each single APK containing the istructions existing in all the analysed
    app
    '''
    db = database("localhost", "root", "MmscC,eh43a", "opcodes")
    n = db.getNumberOfAPK()     #total dimension of dataset
    bias = 1

    features = filterData()
    numberOfIstructions = len(features)
    singleAPK = [i for i in range(0, numberOfIstructions)] #data
    W = [1 for i in range(0, numberOfIstructions)]
    answers = db.getIsMalware()

    X = []  # Matrix containing each APK vector
    for i in range(0, n):
        X.append(singleAPK)

    # calcolo il numero d'errori
    numberOfErrors = computeErrors(n, numberOfIstructions, X, W, answers, bias)

    print numberOfErrors

    i = 1
    j = 0
    while (numberOfErrors > 0):
        j += 1
        f = 0
        for h in range(0, numberOfIstructions):
            f += (X[i][h] * W[h])
        f += bias
        print "f: %s" % f
        if (f * answers[i] <= 0):
            for h in range(0, numberOfIstructions):
                W[h] += answers[i] * X[i][h]
            print W
            bias += answers[i]
            numberOfErrors = computeErrors(n, numberOfIstructions, X, W, answers, bias)

        i += 1

        if (i > n):
            i = 1
        print "ERRORS: %s" % numberOfErrors
        break



if __name__ == "__main__":
    main()
