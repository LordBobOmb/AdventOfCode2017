"""
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.
"""


def checksum(lines):
    sum = 0;
    for line in lines:
        lineNum = list(map(int, line.split()))
        sum += max(lineNum) - min(lineNum)
    return sum

def evenlyDivisibleSum(line):
    sum = 0;
    for line in lines:
        lineNum = list(map(int, line.split()))
        for num1 in lineNum:
            for num2 in lineNum:
                if (num1 > num2 and num1 % num2 == 0): sum += int(num1 / num2)
    return sum

file = open("inputDay2.txt")
lines = file.readlines()
print(checksum(lines))
print(evenlyDivisibleSum(lines))
