"""
A program to print Histogram

"""

__author__ = 'Hari Raghavendar Rao'

import random

if __name__=="__main__":

    # Generates random numbers
    gen_no = []
    for x in xrange(1001):
        gen_no.append(int(random.gauss(5, 2)))

    # Finds the frequency of numbers
    normalized = dict((i, gen_no.count(i)) for i in gen_no)

    # Prints histogram
    for key, value in normalized.iteritems():
        if key > -1 and key < 11:
            print str(key) + ":\t" + (value/10) * "*"
