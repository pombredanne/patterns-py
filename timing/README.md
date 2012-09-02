Timing
=====

BlockTimer
----------
If you'd like to time lots of small little blocks, I personally prefer this to
`timeit`:

    with Timer('benchmark 1'):
        # Do a bunch of time-intensive stuff
