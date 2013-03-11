from __future__ import unicode_literals
from __future__ import print_function
import logging
import os


logger = logging.getLogger(__name__)


class Checker(object):
    check = "Do we have old .txt files in the project root?"
    reason = """
    We use github, which renders ``.rst`` files as nicely formatted
    restructured text. Older projects often still have ``.txt`` files."""
    fix = """
    To fix it, rename them. Oh, and check the ``setup.py`` file as it probably
    uses the readme and changelog in its long description.
    """

    def __init__(self):
        self.txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
        self.txt_files.sort()

    def looks_ok(self):
        """Return whether we've got a potential problem."""
        if self.txt_files:
            return False
        if os.path.exists('setup.py'):
            if '.txt' in open('setup.py').read():
                return False
        return True

    def suggested_commands(self):
        commands = []
        basenames = [f[:-4] for f in self.txt_files]
        for basename in basenames:
            commands.append("git mv %(basename)s.txt %(basename)s.rst" % {
                    'basename': basename})
        commands.append("grep txt setup.py")
        return commands
