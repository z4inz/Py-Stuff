def isValid(s):
    if len(s) % 2 != 0:
        return False
    p = {"(":")","{":"}","[":"]"}
    stack = []
    for i in s:
        if i in p.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i != p[a]:
                return False
    return stack == []
