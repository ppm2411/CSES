#   Name = PRABHUPADA MISHRA
#   Regd. No. = 2241013159
#   Problem statement = https://cses.fi/problemset/task/1069

dna = input()
cur_ch = dna[0]
cur_c = 1
lng_ch = cur_ch
lng_c = 1

for i in range(1, len(dna)):
    nxt_ch = dna[i]

    if nxt_ch == cur_ch:
        cur_c += 1
    else:
        if cur_c > lng_c:
            lng_c = cur_c
            lng_ch = cur_ch
        cur_ch = nxt_ch
        cur_c = 1

if cur_c > lng_c:
    lng_c = cur_c
    lng_ch = cur_ch

print(lng_c)