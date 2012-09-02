Configuration
=============
There are a number of worthy patterns with respect to configuration. Ranging
from sharing configuration options throughout a package to having an inheritance
relationship between different configurations.

Package-Wide
------------
If you want to carry package-wide configuration, it's often easiest to just
have a dictionary `config` at the top level of the package that may be
imported by modules. Typically this reads from a file, parses it and then
makes it available.

    # Import the configuration that's been read
    from mypackage import config
    
    config['foo']
    config['bar']

Assignment and Validation
-------------------------
Especially if using a system with plugins, you may want to reconfigure plugins 
on the fly. In such cases, rather than making the per-plugin configuration an 
argument to `__init__`, require that plugins implement an idempotent `config`
method that raises an exception if the configuration is invalid. In this way, 
the application making use of the plugins can verify configurations that
include information for external components.

Cascading
---------
If there are a large number of configurable components in your system, you'd
probably like to be able to configure large swaths of them easily. For this, it
can be helpful to have configurations that are chained together, and key misses
default to the parent configuration.

    # Set foo's config
    foo.config['widgets'] = 10
    
    # Set the configuration for one of foo's children
    foo['bar'].config['widgets'] = 5
    # Check 'baz' configuration
    foo['baz'].config['widgets']
    # => 10
    foo['bar'].config['widgets']
    # => 5
    
    del foo['bar'].config['widgets']
    foo['bar'].config['widgets']
    # => 10
