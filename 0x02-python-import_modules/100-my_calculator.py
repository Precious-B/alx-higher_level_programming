#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    functions = [add, sub, mul, div]
    for i, j in enumerate(ops):
        if argv[2] == j:
            print("{} {} {} = {}".format(a, j, b, functions[i](a, b)))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
