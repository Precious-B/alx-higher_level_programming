#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str(i) >= 'a' and str(i) <= 'z':
            str1 = chr(ord(str(i) - 32))
        else:
            str1 = str(i)
            print("{}".format(str))
