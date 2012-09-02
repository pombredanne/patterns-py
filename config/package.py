#! /usr/bin/env python

# For this exercise, imagine that this is taking place in __init__.py.
# Alternatively, this might happen at the top level of a module, but that's
# less interesting.

import json

with open('path/to/default/config') as f:
    config = json.load(f)

# Now submodules, etc. can easily refer to their own configuration
