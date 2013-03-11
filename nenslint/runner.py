from __future__ import print_function
from __future__ import unicode_literals
from optparse import OptionParser
import logging
import os

from nenslint import txt_to_rst


logger = logging.getLogger(__name__)


def main():
    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="Verbose mode")
    (options, args) = parser.parse_args()
    loglevel = options.verbose and logging.DEBUG or logging.INFO
    logging.basicConfig(level=loglevel,
                        format="%(levelname)s: %(message)s")
    for module in [txt_to_rst]:
        checker = getattr(module, 'Checker')()
        if checker.looks_ok():
            logger.debug("Looks ok: %s", checker.check)
            continue
        logger.warn("Potential problem: %s", checker.check)
        print("Suggested commands:\n")
        for command in checker.suggested_commands():
            print(command)
        print()
