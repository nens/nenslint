from __future__ import unicode_literals
from __future__ import print_function
import mock
import unittest

from nenslint import runner
from nenslint import txt_to_rst


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
