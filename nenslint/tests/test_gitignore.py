from __future__ import unicode_literals
from __future__ import print_function
import unittest

from nenslint import gitignore
from nenslint.tests import helpers


class GitignoreTest(unittest.TestCase):

    def test_detects_problem1(self):
        with helpers.use_example_dir('gitignore1'):
            checker = gitignore.Checker()
            self.assertFalse(checker.looks_ok())

    def test_detects_problem2(self):
        with helpers.use_example_dir('gitignore2'):
            checker = gitignore.Checker()
            self.assertFalse(checker.looks_ok())

    def test_detects_problem3(self):
        with helpers.use_example_dir('gitignore3'):
            checker = gitignore.Checker()
            self.assertTrue(checker.looks_ok())

    def test_suggested_commands1(self):
        with helpers.use_example_dir('gitignore1'):
            checker = gitignore.Checker()
            commands = checker.suggested_commands()
            self.assertEquals(len(commands), 1)
            self.assertTrue(commands[0].startswith('curl'))

    def test_suggested_commands2(self):
        with helpers.use_example_dir('gitignore2'):
            checker = gitignore.Checker()
            commands = checker.suggested_commands()
            self.assertEquals(len(commands), 1)
            self.assertTrue(commands[0].startswith('curl'))
