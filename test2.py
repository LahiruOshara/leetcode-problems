from re import X
from textwrap import fill


def solve(number):
    numberStr = list(str(number))
    sum = 0
    minPlcae = -1
    
    for i in numberStr:
        sum += int(i)
    
    fillerDigit = 9 - (sum % 9)
    if fillerDigit == 9:
        fillerDigit = 0

    if fillerDigit == 0:
        numberStr.insert(1, str(0))
        return ''.join(numberStr)

    place = -1
    for i in range(len(numberStr)):
        if int(numberStr[i]) > fillerDigit:
            place = i
            break
    if place == -1:
        numberStr.append(str(fillerDigit))
    else:
        numberStr.insert(place, str(fillerDigit))
    return ''.join(numberStr)

if __name__ == "__main__":
    noOfTestCases = int(input())
    dict = {}
    output = []
    for i in range(noOfTestCases):
        number = int(input())
        output.append(solve(number))

    count = 1
    for out in output:
        print("Case #" + str(count) + ": " + out)
        count += 1