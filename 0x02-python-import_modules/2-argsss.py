#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    print('{:d}'.format(len(args)), end=' ')
    for i in range(len(args)):
        if (len(args) == 0):
            print('arguments.')

        elif (len(args) == 1):
            print('argument: ', end='\n')
            print('1: {:s}'.format(argv[i]))

        else:
            print('arguments:', end='\n')


        print('{:d}: {:s}'.format(i + 1, (argv[i + 1])), end='\n')
