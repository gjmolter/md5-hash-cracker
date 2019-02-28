#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from itertools import permutations
import itertools

hash_to_crack = raw_input("INSERT THE MD5 HASH TO BE CRACKED: ")

def testHash(combination):
    for testString in combination:
        print testString
        if hashlib.md5(testString).hexdigest() == hash_to_crack:
            print("THE HASH '%s' HAS BEEN CRACKED!\nTHE ORIGINAL STRING IS = '%s'") % (hash_to_crack, testString)
            return True
    return False

# Only testing strings up to 15 characters. Change it here if you want bigger strings (will take a long time to calculate, though)
for x in range(1, 16):
    print "Starting to test strings with %d characters: " % (x)

    # Only testing a-z and 1-9. Add extra characters to this array to have them tested. (Once again, it will take more time to calculate strings)
    combinacao = ["".join(a) for a in itertools.product(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], repeat=x)]

    if (testHash(combinacao)):
        break
    else:
        print "The script could not crack the hash. Maybe try adding more testable characters or increase the number of characters"
