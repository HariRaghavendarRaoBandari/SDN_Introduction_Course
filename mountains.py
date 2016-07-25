"""
A program to play around with dictionary

"""
__author__      = "Hari Raghavendar Rao"

if __name__=="__main__":
    
    mountains = {
            "Mount Everest": 8848,
            "K2": 8611,
            "Kangchenjunga": 8586,
            "Lhoste": 8516,
            "Makalu": 8462,
            }
    print "Mountain names: ",
    for key,value in mountains.iteritems():
        print key,

    print "\nMountain Elevations: ",
    for key,value in mountains.iteritems():
        print value,
    print ""

    for key,value in mountains.iteritems():
        print ("%s is %d meters tall" % (key, value))
