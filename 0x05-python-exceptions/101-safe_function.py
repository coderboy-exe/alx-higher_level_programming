#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as err:
        stderr.write("Exception: {}\n".format(err))
        return None
