def solve(length, string):
    out = [0] * length
    out[0] = 1
    for i in range(1, length):
        if string[i] > string[i - 1]:
            out[i] = out[i - 1] + 1
        else:
            out[i] = 1
    return out

if __name__ == "__main__":
    noOfTestCases = int(input())
    dict = {}
    output = []
    for i in range(noOfTestCases):
        length = int(input())
        string = input()
        output.append(solve(length, string))

    count = 1
    for out in output:
        listToStr = ' '.join(map(str, out))
        print("Case #" + str(count) + ": " + listToStr)
        count += 1