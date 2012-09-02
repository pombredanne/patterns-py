#! /usr/bin/env python

'''Atomic file writing'''


class AtomicWriter(object):
    '''A file-like object context-manager that atomically replaces a file'''
    def __init__(self, path, *args, **kwargs):
        self.fout = None
        self.path = path
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.fout = open(self.path + '.tmp', *self.args, **self.kwargs)
        return self.fout

    def __exit__(self, typ, val, trace):
        # If there was no exception within this context, swap the files
        self.fout.close()
        self.fout = None
        if not val:
            import os
            os.rename(self.path + '.tmp', self.path)
        else:
            # Otherwise, re-raise the exception
            raise val
