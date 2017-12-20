from DB import database
import numpy as np
from sklearn import svm
import random

'''
We choose 
'''

if __name__ == "__main__":

    #pwd = raw_input("insert db password: ")
    db = database("localhost", "root", "MmscC,eh43a", "opcodes")

    # total dimension of dataset
    numberOfAPK = db.getNumberOfAPK()

    # we build the matrix containing for each row the features
    X = db.defineFeature()

    # vector containing answers i.e. value of attribute "is_malware"
    answers = db.getIsMalware()

    err_list = []
    correct_list = []
    # we run the training and testing 10 times just to test different executions
    for round in range(0, 10):
        # shuffle...
        total = []
        for i in range(0, len(X)):
            # we must shuffle X together answers...
            tmp = []
            tmp.append(X[i])
            tmp.append(answers[i])
            total.append(tmp)

        random.shuffle(total)

        # Matrix containing each APK vector and answers vector, after shuffling
        X = []
        answers = []
        for i in range(0, len(total)):
            X.append(total[i][0])
            answers.append(total[i][1])


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


        # train with svm
        clf = svm.SVC()
        classifier =clf.fit(train, train_answers)



        # test
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
        err_list.append(errors)
        correct_list.append(correct)

    print "avg errors -> " + str(np.mean(err_list)) + "," \
            " avg correct -> " + str(np.mean(correct_list))





