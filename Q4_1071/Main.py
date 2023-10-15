# 
#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1071
#  

def value_finder(x, y):
    if y > x:
        if y % 2 == 0:
            val = ((y - 1) * (y - 1)) + 1 + (x - 1)
        else:
            val = (y * y) - (x - 1)
    else:
        if x % 2 == 0:
            val = ((x - 1) * (x - 1)) + 1 + (x - 1) + (x - y)
        else:
            val = (x * x) - (x - 1) - (x - y)
    print(val)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input_values = input().split()
        x = int(input_values[0])
        y = int(input_values[1])
        value_finder(x, y)