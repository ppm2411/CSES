#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1070

n = int(input())
if n == 1:
    print("1")
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    if n % 2 == 0:
        # If 'n' is even, we can start with even numbers and then odd numbers
        for i in range(2, n + 1, 2):
            print(i, end=" ")
        for i in range(1, n, 2):
            print(i, end=" ")
    else:
        # If 'n' is odd, we can start with odd numbers and then even numbers
        for i in range(1, n+1, 2):
            print(i, end=" ")
        for i in range(2, n + 1, 2):
            print(i, end=" ")
