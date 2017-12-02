"""
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.
"""


def checksum(fileobject):
    sum = 0;
    for line in fileobject.readlines():
        lineNum = list(map(int, line.split()))
        sum += max(lineNum) - min(lineNum)
    return sum

file = open("inputDay2.txt")
print(checksum(file))
