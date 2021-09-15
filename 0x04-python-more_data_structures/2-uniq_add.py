#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_n = 0
    for x in set(my_list):
        sum_n += x
    return (sum_n)
