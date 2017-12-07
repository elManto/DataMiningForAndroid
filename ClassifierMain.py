from DB import database
from Util import getListOfOpcode
from sklearn import svm
from copy import copy
import random
import time

def filterData(db):
    opcodes = getListOfOpcode()
    features = db.defineFeature(opcodes)
    return features



if __name__ == "__main__":

    pwd = raw_input("insert db password: ")
    db = database("localhost", "root", pwd, "opcodes")
    numberOfAPK = db.getNumberOfAPK()  # total dimension of dataset



    #commonFeatures = filterData(db)
    commonFeatures = filterData(db)

    print "common features"
    print commonFeatures

    time.sleep(30)

    print "Before loop"
    X = []  # Matrix containing each APK vector
    for i in range(1, numberOfAPK + 1):
        print "apk number %s" % i
        frequencyVector = db.getSingleAPKfrequency(commonFeatures, i)
        print len(frequencyVector)
        X.append(frequencyVector)

    answers = db.getIsMalware()
    for i in range(0, len(answers)):
        if answers[i] == 0:
            print "%s --> 0" % i
    # split between train and test
    test = []
    train = []
    train_answers = []
    test_answers = []
    for i in range(1, len(X)):
        if (random.uniform(0, 1) > 0.5):
            train.append(X[i])
            train_answers.append(answers[i])
        else:
            test.append(X[i])
            test_answers.append(answers[i])




    clf = svm.SVC()
    clf.fit(train, train_answers)


    counter = 500
    false = 0
    res = clf.predict(test)
    print res
    correct = 0
    errors = 0
    for i in range(0, len(res)):
        if res[i] == test_answers[i]:
            correct += 1
        else:
            errors += 1

    print "errors -> " + str(errors) + ", correct -> " + str(correct)



