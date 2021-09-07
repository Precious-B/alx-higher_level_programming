#!/usr/bin/python3
res = ""
for letter in range(122, 96, -1):
    if not letter % 2:
        res = res + letter.upper()
    else:
        res = res + letter.lower()
        print(str(res), end="")
