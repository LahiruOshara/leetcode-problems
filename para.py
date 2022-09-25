def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    dict = {'(': ')', '{': '}', '[': ']'}
    for p in s:
        if p == '{' or p == '(' or p == '[':
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if popped in dict:
                if dict[popped] == p:
                    return True
                else:
                    return False
            else:
                return False
    else:
        if len(stack) == 0:
            return True
        return False

if __name__ == "__main__":
    s = ['(',')','{','}','}','{']
    print(isValid(s))