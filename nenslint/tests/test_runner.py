from __future__ import unicode_literals
from __future__ import print_function
import mock
import unittest

from nenslint import runner
from nenslint import txt_to_rst


class MockChecker(object):
    ok = True
    check = "Am I checking something?"

    def looks_ok(self):
        return self.ok

    @classmethod
    def documentation(cls):
        return "Documentation"

    def suggested_commands(self):
        return ['command 1']


class MockNotOkChecker(MockChecker):
    ok = False


def _mock_checker_classes():
    return [MockChecker, MockNotOkChecker]


class RunnerTest(unittest.TestCase):

    def test_checker_classes(self):
        # Should return classes.
        self.assertEquals(runner.checker_classes()[0],
                          txt_to_rst.Checker)

    @mock.patch('nenslint.runner.run_actual_checkers')
    def test_main(self, mocked_method):
        # Smoke test.
        runner.main()
        self.assertTrue(mocked_method.called)

    @mock.patch('nenslint.runner.checker_classes', _mock_checker_classes)
    @mock.patch('nenslint.runner._raw_input', lambda question: 'n')
    def test_run_actual_checkers(self):
        # Smoke test.
        output = runner.run_actual_checkers()
        self.assertTrue(output is None)
