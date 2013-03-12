"""
Main module of nenslint: it contains the actual function (:func:`main`) that's
installed by ``setup.py`` as the ``nenslint`` command.

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


def main():
    """Function that's run as the ``nenslint`` console script.
    """
    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="Verbose mode")
    (options, args) = parser.parse_args()
    loglevel = options.verbose and logging.DEBUG or logging.INFO
    logging.basicConfig(level=loglevel,
                        format="%(levelname)s: %(message)s")
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
        answer = raw_input("Continue checking? [y/N] ")
        if not 'y' in answer.lower():
            return
