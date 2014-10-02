__author__ = 'jaime'

class Value(object):
    """A Setting contains a single setting / variable that can be used in a template. """
    def __init__(self,name,default,value = None):
        self._name = name
        self.default = default
        if value is None:
            self._value = default.getValue()
        else:
            self._value = value

    def getName(self):
        return self._name

    def getValue(self):
        return self._value

