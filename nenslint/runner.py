"""
:mod:`nenslint.runner` is the main module of nenslint: it contains the actual
function (:func:`main`) that's installed by ``setup.py`` as the ``nenslint``
command.

The only thing that regularly needs to be changed in this file is the
:attr:`CHECKER_MODULE_NAMES` variable with the list of actual checks.

"""
from __future__ import print_function
from __future__ import unicode_literals
from optparse import OptionParser
import importlib  # Note: available from python 2.7 onwards.
import logging

#: List of checker module names. Each should have a ``Checker`` class that's a
#: subclass of :class:`nenslint.base.BaseChecker`. They are run in the order
#: given.
CHECKER_MODULE_NAMES = ['txt_to_rst',
                        'gitignore',
                        ]

logger = logging.getLogger(__name__)
_raw_input = raw_input  # To make tests possible.


def checker_classes():
    """Return checker classes.

    Used by :func:`main` and by the documentation generation script.

    For every checker module name in :attr:`CHECKER_MODULE_NAMES`, an import
    like ``from nenslint.[checker module name] import Checker`` is done. The
    imported checker classes (note: not instantiated yet) are returned.

    """
    classes = []
    for checker_module_name in CHECKER_MODULE_NAMES:
        module = importlib.import_module('nenslint.%s' % checker_module_name)
        classes.append(module.Checker)
    return classes


def run_actual_checkers():
    """Run the actual checking process, going through all configured checkers.

    For every checker, it calls the :meth:`nenslint.base.BaseChecker.looks_ok`
    method implemented in that checker. If it returns ``False``, it prints the
    checker's documentation (by calling
    :meth:`nenslint.base.BaseChecker.documentation`) and it then prints the
    commands suggested by
    :meth:`nenslint.base.BaseChecker.suggested_commands`.

    When no problems are detected, the next checker in line is called
    directly. If there was a problem (and thus some suggested commands were
    printed), we assume you want to go fix them right away. But we *do* ask
    if you want to continue anyway, first. This helps with stepping over false
    positives.

    """
    for checker_class in checker_classes():
        checker = checker_class()
        if checker.looks_ok():
            logger.debug("Looks ok: %s", checker.check)
            continue
        print(checker_class.documentation())
        print("Suggested commands:\n")
        for command in checker.suggested_commands():
            print(command)
        print()
        answer = _raw_input("Continue checking? [y/N] ")
        # ^^^ _raw_input is just raw_input, but with a local name to make
        # testing possible.
        if not 'y' in answer.lower():
            return


def main():
    """Function that's run as the ``nenslint`` console script.

    Basically it only parses the commandline and checks whether it should
    enable the logging in verbose or non-verbose mode. It then runs
    :func:`run_actual_checkers` that does the real work.

    """
    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="Verbose mode")
    (options, args) = parser.parse_args()
    loglevel = options.verbose and logging.DEBUG or logging.INFO
    logging.basicConfig(level=loglevel,
                        format="%(levelname)s: %(message)s")
    run_actual_checkers()
