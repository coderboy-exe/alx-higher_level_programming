#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        while i < len(my_list):
            if i == len(my_list):
                break
            print('{:d}'.format(my_list[i-1]))
            i -= 1
