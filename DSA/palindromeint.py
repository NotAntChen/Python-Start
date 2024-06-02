def palidromeint(x: int) -> bool:
    y = 0
    og = x
    if x<0:
        #if negative, it is not a palindrome
        return False
    elif x % 10 == 0 and x != 0:
        #if it ends in 0 and 2 or more digits it is not a palindrome
        return False
    while x > 0:
        r = x % 10
        y = y*10 + r
        x = x//10
        if y == og:
            return True
        else:
            return False

x = 121
print(palidromeint(x))
x = -121
print(palidromeint(x))
x = 10
print(palidromeint(x))
