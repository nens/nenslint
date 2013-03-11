"""Testing helpers
"""
from __future__ import unicode_literals
from __future__ import print_function
import contextlib
import os

import pkg_resources


# The chdir context manager is partially copied from
# http://code.activestate.com/recipes/576620-changedirectory-context-manager/

@contextlib.contextmanager
def use_example_dir(test_subdir):
    """A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.

    """
    target = pkg_resources.resource_filename('nenslint.tests', test_subdir)
    assert(os.path.exists(target))
    prev_cwd = os.getcwd()
    os.chdir(target)
    try:
        yield
    finally:
        os.chdir(prev_cwd)
