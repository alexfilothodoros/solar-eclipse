#!/usr/bin/env python

import os

from setuptools import setup


VERSION_TEMPLATE = """
# Note that we need to fall back to the hard-coded version if either
# setuptools_scm can't be imported or setuptools_scm can't determine the
# version, so we catch the generic 'Exception'.
try:
    from setuptools_scm import get_version
    __version__ = get_version(root='..', relative_to=__file__)
except Exception:
    __version__ = '{version}'
""".lstrip()

setup(
    use_scm_version={'write_to': os.path.join('eclipse', 'version.py'),
                     'write_to_template': VERSION_TEMPLATE},

)
