#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1618


def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

a=int(input())
print(count_trailing_zeros(a))