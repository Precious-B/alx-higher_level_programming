#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
         roman_string is None):
        return (0)
    r_data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    numbers = [r_data[x] for x in roman_string] + [0]
    rep = 0
    for n in range(len(numbers) - 1):
        if numbers[n] >= numbers[n + 1]:
            rep += numbers[n]
        else:
            rep -= numbers[n]
    return rep
