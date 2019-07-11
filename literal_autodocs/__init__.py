# Copyright (c) 2019 Patricio Cubillos and contributors.
# literal_autodocs is open-source software under GNU GPL3 license (see LICENSE).

from .autodocs import * 
from . import VERSION as ver


__all__ = autodocs.__all__
__version__ = f"{ver.LADS_VER}.{ver.LADS_MIN}.{ver.LADS_REV}"


# Clean up top-level namespace--delete everything that isn't in __all__
# or is a magic attribute, and that isn't a submodule of this package
for varname in dir():
    if not ((varname.startswith('__') and varname.endswith('__')) or
            varname in __all__ ):
        del locals()[varname]
del(varname)

