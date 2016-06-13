from __future__ import unicode_literals

__author__ = "Pymatgen Development Team"
__email__ ="pymatgen@googlegroups.com"
__maintainer__ = "Shyue Ping Ong"
__maintainer_email__ ="shyuep@gmail.com"
__date__ = "May 25 2016"
__version__ = "3.6.1"


# Useful aliases for commonly used objects and modules.
# Allows from pymatgen import <class> for quick usage.

from .core import *
from .electronic_structure.core import Spin, Orbital
from .matproj.rest import MPRester
from monty.json import MontyEncoder, MontyDecoder, MSONable
