class Solution(object):
    def isValid(self, s):
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
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            if len(stack) == 0:
                return True
            return False