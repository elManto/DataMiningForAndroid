def computeErrors(n, numberOfIstructions, X, W, Y, bias):
    numberOfErrors = 0
    for i in range(0, n):
        sum = 0
        for j in range(0, numberOfIstructions):
            sum += X[i][j] * W[j]
            sum = sum
        if ((sum + bias) * Y[i] <= 0):
            numberOfErrors += 1
    return numberOfErrors


def getListOfOpcode():
    with open("./opcode.txt", "r") as f:
        opcode = f.readlines()
    f.closed
    return [op[:-1] for op in opcode]
