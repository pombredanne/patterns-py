#! /usr/bin/env python

'''A demonstration of cascading configuration'''


class Config(object):
    '''A configuration object'''
    def __init__(self, parnt=None, **defaults):
        self.parent = parnt
        self.defaults = defaults
        self.data = {}

    def __getitem__(self, key):
        # We have to use __contains__ rather than `get` because a configuration
        # option might legitimately be set to `None`. If this is not the case
        # for you, then you might choose an alternate implementation
        if key in self.data:
            return self.data[key]
        if self.parent:
            return self.parent[key]
        return self.defaults[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def get(self, key):
        '''Get the provided key'''
        return self.__getitem__(key)

    def set(self, key, value):
        '''Set the provided key to value'''
        return self.__setitem__(key, value)

# Example usage -- parent / child relationship
parent = Config(bar=10)
child = Config(parent)

# Inherit from parent
parent['foo'] = 5
child['foo']  # 5

# Override in child
child['foo']  = 10
parent['foo'] # 5
child['foo']  # 10

# Unset a child's attribute
del child['foo']
child['foo']  # 5

# Built-in defaults
parent['bar'] # 10
child['bar']  # 10

# Missing keys
parent['baz'] # KeyError
child['baz']  # KeyError