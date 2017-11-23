from Util import computeErrors
from Util import getListOfOpcode
from db import database

def filterData(db):
    opcodes = getListOfOpcode()
    features = db.defineFeature(opcodes)
    return features


def main():
    '''
    Now we are building the model of APK, i.e. a vector which represents
    a each single APK containing the istructions existing in all the analysed
    app
    '''
    pwd = raw_input("insert db password: ")
    db = database("localhost", "root", pwd, "opcodes")
    numberOfAPK = db.getNumberOfAPK()     #total dimension of dataset
    bias = 1

    commonFeatures = filterData(db)

    X = []  # Matrix containing each APK vector
    for i in range(1, numberOfAPK + 1):
        frequencyVector = db.getSingleAPKfrequency(commonFeatures, i)
        print len(frequencyVector)
        X.append(frequencyVector)

    numberOfIstructions = len(commonFeatures)
    W = [1 for i in range(0, numberOfIstructions)]
    answers = db.getIsMalware()


    # compute the number of errors
    numberOfErrors = computeErrors(numberOfAPK, numberOfIstructions, X, W, answers, bias)

    print numberOfErrors # Why this is 0?????????????????????????

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
            numberOfErrors = computeErrors(numberOfAPK, numberOfIstructions, X, W, answers, bias)

        i += 1

        if (i > numberOfAPK):
            i = 1
        print "ERRORS: %s" % numberOfErrors
        break



if __name__ == "__main__":
    main()
