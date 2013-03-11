from __future__ import unicode_literals
from __future__ import print_function
import unittest

from nenslint import base


class BaseCheckerTest(unittest.TestCase):

    def test_documentation(self):
        checker_class = base.BaseChecker  # Note: class, not instance!
        self.assertTrue('-----' in checker_class.documentation())

    def test_looks_ok(self):
        # Check whether the basic API methods exist and if they're documented.
        checker = base.BaseChecker()
        checker.looks_ok()
        self.assertTrue(checker.looks_ok.__doc__)

    def test_suggested_commands(self):
        # Check whether the basic API methods exist and if they're documented.
        checker = base.BaseChecker()
        checker.suggested_commands()
        self.assertTrue(checker.suggested_commands.__doc__)
