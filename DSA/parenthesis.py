def isValid(self, s) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    stack = []

    for c in s:
        match c:
            case '(':
                stack.append(c)
            case '[':
                stack.append(c)
            case '{':
                stack.append(c)
            case ')':
                if len(stack) == 0:
                    return False
                instack = stack.pop()
                if c == ')' and instack != '(':
                    return False
            case ']':
                if len(stack) == 0:
                    return False
                instack = stack.pop()
                if c == ']' and instack != '[':
                    return False
            case '}':
                if len(stack) == 0:
                    return False
                instack = stack.pop()
                if c == '}' and instack != '{':
                    return False
            case _:
                return False
    if len(stack) == 0:
        return False
    return True

