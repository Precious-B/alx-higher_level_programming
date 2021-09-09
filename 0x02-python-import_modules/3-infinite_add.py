#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    sum = 0
    if n == 0:
        print(sum)
    else:
        for i in range(1, n + 1):
            sum = sum + int(argv[i])
        print("{:d}".format(sum))
