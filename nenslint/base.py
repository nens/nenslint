from __future__ import unicode_literals
from __future__ import print_function
import logging

logger = logging.getLogger(__name__)


class BaseChecker(object):
    """Base class for all checkers.

    Its goal is to document a checker's API and to enforce documentation
    through automatic documentation generation.

    In a subclass, you need to fill in the :attr:`check`, :attr:`reason` and
    :attr:`fix` attributes and implement the :meth:`looks_ok` and
    :meth:`suggested_commands` methods.

    """
    #: Question-like oneliner that tells what we're about to check.
    check = "Fill this in."
    #: Some docstring-like multi-line explanation why we want to check this
    #: and why it is important.
    #:
    #: Keep it indented in the source file, with four spaces. This helps with
    #: rendering the documentation. Look at an existing checker to see how it
    #: can be done.
    reason = "Fill this in."
    #: A textual explanation of how to fix it.
    #:
    #: For indentation rules, see :attr:`reason`.
    fix = "Fill this in."

    def __init__(self):
        """Do whatever you need to do to set it up.

        Detect whether files exists or so.
        """
        pass

    @classmethod
    def documentation(self):
        """Return documentation.

        This method is used for the sphinx documentation and for printing an
        explanation after we detected a potential problem.

        You normally don't need to overwrite this in a subclass.
        """
        result = []
        result.append('')
        result.append(self.check)
        result.append('-' * len(self.check))
        result.append('')
        result.append('Reason')
        result.append(self.reason)
        result.append('')
        result.append('Fix')
        result.append(self.fix)
        result.append('')
        return '\n'.join(result)

    def looks_ok(self):
        """Return whether we've got a potential problem.

        Implement it in a subclass.
        """
        pass

    def suggested_commands(self):
        """Return list of commands to fix the issue.

        It will be printed for easy copy/pasting.

        Implement it in a subclass.

        """
        return []
