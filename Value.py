__author__ = 'jaime'

class Value(object):
    """A Setting contains a single setting / variable that can be used in a template. """
    def __init__(self,name,default = None,value = None):
        self._name = name

        if default is None and value is None:
            print 'ERROR: ' + name + 'Has no default and no value!'

        self.default = default

        if value is None and default is not None:
            self._value = default.getValue()
        else:
            self._value = value

    def getName(self):
        return self._name

    def getValue(self):
        return self._value

