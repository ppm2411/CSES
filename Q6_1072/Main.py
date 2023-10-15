#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1072


n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(0)
    elif i == 2:
        print(6)
    else:
        sq = i * i
        res = ((sq * (sq - 1)) // 2) - 4 * (i - 2) * (i - 1)
        print(res)