
from sklearn import svm




if __name__ == "__main__":
    X = [[0, 0], [1, 1]]
    y = [0, 1]
    clf = svm.SVC()
    clf.fit(X, y)

    x1 = raw_input("insert value to predict: ")
    x2 = raw_input("insert value to predict: ")

    res = clf.predict([[x1, x2]])
    print res