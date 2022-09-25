def solve(targetText, typedText):
    lenTargetText = len(targetText)
    lenTypedText = len(typedText)
    ptrTarget = 0
    ptrTyped = 0

    while (ptrTarget < lenTargetText and ptrTyped < lenTypedText):
        if typedText[ptrTyped] == targetText[ptrTarget]:
            ptrTarget += 1
            ptrTyped += 1
        else:
            ptrTyped += 1
    if ptrTarget == lenTargetText:
        return lenTypedText - lenTargetText
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    noOfTestCases = int(input())
    dict = {}
    output = []
    for i in range(noOfTestCases):
        targetText = input()
        typedText = input()
        output.append(solve(targetText, typedText))

    count = 1
    for out in output:
        print("Case #" + str(count) + ": " + str(out))
        count += 1
