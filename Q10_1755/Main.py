#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1755

def palindrome(str):
    c = {}
    for i in str:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1

    x = 0
    y = ''
    z = ''
    w = ''

    for i,j in c.items():
        if j % 2 == 1:
            x += 1
            y = i
        v = j // 2
        z += i * v
        w = i * v + w

    if x > 1:
        return "NO SOLUTION"

    if x == 1:
        p = z + y + w
    else:
        p = z + w

    return p

a=input()
print(palindrome(a))