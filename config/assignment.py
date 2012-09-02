#! /usr/bin/env python

'''Idempotent configuration'''


class Plugin(object):
    '''A dummy plugin class that should accept new configuration in the
    `config` method idempotently, and also validates new configurations'''
    def __init__(self):
        self.config_ = None

    def config(self, **kwargs):
        '''This function should be idempotent, and raise exceptions if the
        configuration is invalid'''
        self.config_['foo'] = kwargs.get('foo', 'bar')
        if 'bad-key' in kwargs:
            raise KeyError('Configuration cannot contain `bad-key`')
