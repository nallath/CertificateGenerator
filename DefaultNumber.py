__author__ = 'jaime'
import random

class DefaultNumber(object):

    def __init__(self,minValue,maxValue,decimals = 0):
        self._minValue = minValue
        self._maxValue = maxValue
        self._decimals = decimals
        self._value = -9001

    def getValue(self):
        if self._value == -9001:
            self._value = random.uniform(self._minValue, self._maxValue)
            self._value = round(self._value,self._decimals)
            if self._decimals == 0:
                self._value = int(self._value)  #Remove trailing zeros

        return self._value