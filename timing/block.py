#! /usr/bin/env python

'''My preferred alternative to timeit'''

import time

class Timer(object):
    '''A context-manager object that times blocks'''
    def __init__(self, name):
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = -time.time()
        print 'Starting %s' % self.name
        return self

    def __exit__(self, typ, val, trace):
        self.start += time.time()
        if typ:
            print '  Failed %s in %fs' % (self.name, self.start)
        else:
            print '     Ran %s in %fs' % (self.name, self.start)
