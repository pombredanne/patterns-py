Files
=====

AtomicWriter
------------
Bursts of file access are amenable to using a context manager to ensure that 
files are written atomically. Processes can get interrupted in the middle of
writes, and if a file has to maintain a format, it's not unlikely that it can
become corrupted. To solve this, a new file is opened, written, and upon the
completion of that write operation, renamed to be the original path. In this
way, the content of the original file has been overwritten without any risk of
corruption:

    with AtomicWriter('some/path/of/mine', 'w+') as f:
        # This implicitly creates a file 'some/path/of/mine.tmp'
        f.write('foo')
        f.write('bar')
    
    # After this context is left, 'some/path/of/mine.tmp' replaces the original
    # and the file has been written

LockedWriter / LockedReader
---------------------------
You may also want to apply filesystem-based locks to ensure that no two 
processes are using a file at the same time. For this, there are any number of 
external file locking libraries, each of which merits a context manager.

    with LockedWriter('some/path/of/mine', 'w+') as f:
        # Wait until I'm the only process trying to read it
        ...
    
    # Once this context is exited, other processes may use this file
    
    with LockedReader('some/other/path') as f:
        # I now have exclusive access to this file. No one is reading or writing
        ...
