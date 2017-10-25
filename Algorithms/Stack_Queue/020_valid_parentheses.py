'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == "(":
                stack.append(")")
            elif x == "[":
                stack.append("]")
            elif x == "{":
                stack.append("}")
            elif len(stack) == 0 or stack.pop() != x:
                return False
        return len(stack) == 0
