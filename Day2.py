"""
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.
"""


def rowDiff(row):
    minimum = 10
    maximum = 0
    for num in row:
        if int(num) < minimum: minimum = int(num)
        if int(num) > maximum: maximum = int(num)
    return maximum - minimum


def allRows(fileobject):
    data = fileobject.read()
    rowList = data.split()
    print(rowList)
    rowDiffs = []
    for num in rowList:
        rowDiffs.append(rowDiff(num))
    return sum(rowDiffs)


file = open("inputDay2.txt")
print(allRows(file))
