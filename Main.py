import random
from Util import computeErrors


def main():

    n = 10000
    bias = 1
    numberOfIstructions = 100

    x = [i for i in range(0, numberOfIstructions)]
    W = [1 for i in range(0, numberOfIstructions)]
    Y = [(random.randrange(-1, 2, 2)) for i in range(0, n)]
    print Y
    X = []
    for i in range(0, n):
        X.append(x)

    # calcolo il numero d'errori
    numberOfErrors = computeErrors(n, numberOfIstructions, X, W, Y, bias)

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
        if (f * Y[i] <= 0):
            for h in range(0, numberOfIstructions):
                W[h] += Y[i] * X[i][h]
            print W
            bias += Y[i]
            numberOfErrors = computeErrors(n, numberOfIstructions, X, W, Y, bias)

        i += 1

        if (i > n):
            i = 1
        print "ERRORS: %s" % numberOfErrors


if __name__ == "__main__":
    main()
