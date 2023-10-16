#     Name = PRABHUPADA MISHRA
#     Regd. No. = 2241013159
#     Problem statement = https://cses.fi/problemset/task/1754


t = int(input())
output = []

for _ in range(t):
    a, b = map(int, input().split())
    
    if (a + b) % 3 == 0 and 2 * min(a, b) >= max(a, b):
        output.append("YES")
    else:
        output.append("NO")

print("\n".join(output))





