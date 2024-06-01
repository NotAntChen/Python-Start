def palidromeint(x: int) -> bool:
    if x<0:
        #if negative, it is not a palindrome
        return False
    elif str(x)==str(x)[::-1]:
        #if the inverse string is equal, it is a palindrome
        return True
    else:
        #all other cases like 10 or 16 is false
        return False

x = 121
print(palidromeint(x))
x = -121
print(palidromeint(x))
x = 10
print(palidromeint(x))