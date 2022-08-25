#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    print('{:d}'.format(len(args)), end=' ')
    if (len(args) == 0):
        print('arguments.')
    elif (len(args) == 1):
        print('argument:')
        print('1: {:s}'.format(argv[1]))

    else:
        print('arguments:')

    for i in range(1, len(args)):
        print('{:d}: {:s}'.format(i + 1, (argv[i + 1])), end='\n')
