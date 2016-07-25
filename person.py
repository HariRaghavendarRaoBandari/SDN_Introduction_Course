#! /usr/bin/env python2
"""
A program to generate a parent class and two child classes Male and Female.
"""
__author__ = "Hari Raghavendar Rao"


class Person():
    """
    The main parent class for a person.
    """
    gender = "Null"

    def get_gender():
        return gender


class Male(Person):
    """
    A child class of person which handles all Male
    """
    gender = "Male"

    def get_gender():
        return gender


class Female(Person):
    """
    A child class of person which handles all Females
    """
    gender = "Female"

    def get_gender():
        return gender

if __name__ == "__main__":

    """
    Main function
    """
