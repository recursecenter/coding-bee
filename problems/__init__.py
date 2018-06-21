from . import easy
from . import medium
from . import hard

__all__ = ['EASY', 'MEDIUM', 'HARD']

# problem definitions - these are auto-populated below and contain:
# <fn_name: str> -> <definition: str>
EASY = {}
MEDIUM = {}
HARD = {}

NAME_TO_FN = {}

# auto-populate the problem definitions
_MODULES = (('easy', easy, EASY), ('med', medium, MEDIUM), ('hard', hard, HARD))

for prefix, module, defs in _MODULES:
    names = [name for name in dir(module) if name.startswith(prefix + '_')]
    for name in names:
        fn = getattr(module, name)
        doc = fn.__doc__.strip()
        defs[name] = doc
        NAME_TO_FN[name] = fn
