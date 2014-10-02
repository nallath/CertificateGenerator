__author__ = 'jaime'

import random

class DefaultString(object):
    """ Holds a set of predefined strings of which one is randomly returned
    """

    def __init__(self,strings):
        self._strings = strings # List of strings
        self._indexToUse = -1;
        if len(strings) < 1:
            print 'ERROR: Size of strings is lower then 1'

    def getValue(self):
        if self._indexToUse == -1: # Used to always return the same (random generated) data
            self._indexToUse = random.randint(0,len(self._strings)-1)
        return self._strings[ self._indexToUse]

