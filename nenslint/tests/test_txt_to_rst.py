from __future__ import unicode_literals
from __future__ import print_function
import unittest

from nenslint import txt_to_rst
from nenslint.tests import helpers


class TxtToRstTest(unittest.TestCase):

    def test_detects_problem(self):
        with helpers.use_example_dir('txt_to_rst1'):
            checker = txt_to_rst.Checker()
            self.assertFalse(checker.looks_ok())

    def test_suggested_commands(self):
        with helpers.use_example_dir('txt_to_rst1'):
            checker = txt_to_rst.Checker()
            commands = checker.suggested_commands()
            self.assertEquals(len(commands), 3)
            self.assertEquals(
                commands[0],
                "git mv CHANGES.txt CHANGES.rst")

    def test_detects_problem(self):
        with helpers.use_example_dir('txt_to_rst2'):
            checker = txt_to_rst.Checker()
            self.assertTrue(checker.looks_ok())

    def test_only_setuppy1(self):
        with helpers.use_example_dir('txt_to_rst3'):
            checker = txt_to_rst.Checker()
            self.assertFalse(checker.looks_ok())

    def test_only_setuppy2(self):
        with helpers.use_example_dir('txt_to_rst3'):
            checker = txt_to_rst.Checker()
            commands = checker.suggested_commands()
            self.assertEquals(
                commands,
                ["grep txt setup.py"])
