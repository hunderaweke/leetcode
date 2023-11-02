class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '[' or i =='{' or i == '(':
                stack.append(i)
            else:
                if not stack:
                    return False
                if i ==  ']' and stack[-1] == '[':
                    stack.pop()
                elif i =='}' and stack[-1] == '{':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return not stack

        return is_valid