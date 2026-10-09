class Solution:
    def isValid(self, s: str) -> bool:
        openers = []
        if len(s) == 0:
            return True


        def match(paren: str) -> str:
            match paren:
                case "}":
                    return "{"
                case "]":
                    return "["
                case ")":
                    return "("

        for char in s:
            if char == '(' or char == '{' or char == '[':
                openers.append(char)
            elif not openers or match(char) != openers.pop():
                return False
            else:
                pass
        if not openers:
            return True
        else:
            return False