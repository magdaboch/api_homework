import sys


if sys.version_info <  (3, 6):
    raise SystemError('Must use Python 3.6 or greater')