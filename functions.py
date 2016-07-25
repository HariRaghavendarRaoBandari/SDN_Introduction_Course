#! /usr/bin/env python2
"""
 A program to try out the python functions
"""
__author__ = "Hari Raghavendar Rao Bandari"


def concatenate_two_strings():
    """
    A function which accepts two string as input and later
    it concatenate two input string then prints out concatenated string.
    """
    string1 = raw_input("Enter 1st string: ")
    string2 = raw_input("Enter 2nd string: ")
    print string1 + string2


def even_or_odd():
    """
    A function which accepts an integer number input and prints out whether input integer is even or odd
    """
    integer = int(raw_input("Enter the integer number: "))

    if integer % 2 == 0:
        print "Entered integer is even"
    elif integer % 2 == 1:
        print "Entered integer is odd"
    else:
        print "Entered input is not an integer number"


def division_by_zero():
    """
    A function uses try/except to catch the exceptions when we perform division_by_zero operation
    """
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print "Oops! Division by zero error found "


if __name__ == "__main__":
    """
    Main function
    """
    concatenate_two_strings()
    even_or_odd()
    division_by_zero()
