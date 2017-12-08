from DB import database
from Util import getListOfOpcode
from sklearn import svm
from copy import copy
import random
import time

def filterData(db):
    X = db.defineFeature()
    return X



if __name__ == "__main__":

    #pwd = raw_input("insert db password: ")
    db = database("localhost", "root", "MmscC,eh43a", "opcodes")
    numberOfAPK = db.getNumberOfAPK()  # total dimension of dataset



    #commonFeatures = filterData(db)
    X = filterData(db)


    answers = db.getIsMalware()

    #shuffle
    total = []
    for i in range(0, len(X)):
        tmp = []
        tmp.append(X[i])
        tmp.append(answers[i])
        total.append(tmp)

    random.shuffle(total)

    X = []
    answers = []
    for i in range(0, len(total)):
        X.append(total[i][0])
        answers.append(total[i][1])
    # Matrix containing each APK vector




    # split between train and test
    test = []
    train = []
    train_answers = []
    test_answers = []
    for i in range(1, len(X)):
        if (random.uniform(0, 1) > 0.5 or len(test) == 100):
            train.append(X[i])
            train_answers.append(answers[i])
        else:
            test.append(X[i])
            test_answers.append(answers[i])


    clf = svm.SVC()
    clf.fit(train, train_answers)


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



