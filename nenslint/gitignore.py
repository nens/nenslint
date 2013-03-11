from __future__ import unicode_literals
from __future__ import print_function
import logging
import os
import urllib

from nenslint.base import BaseChecker

logger = logging.getLogger(__name__)

GITIGNORE_URL = ('https://raw.github.com/lizardsystem/nensskel/master/'
                 'nensskel/templates/library/+dot+gitignore_tmpl')


class Checker(BaseChecker):
    check = "Do we have a proper ``.gitignore`` file?"
    reason = """
    A proper ``.gitignore`` file prevents us from accidentally committing files
    that shouldn't be committed. Mentally going through ``git status`` and
    filtering out items that are OK is *work* and we don't want that. And it
    is too easy to miss files you should add.

    Something always changes in the setup over time, so a ``.gitignore``
    that was once good, can now be missing items.
    """
    fix = """
    To fix it, grab the latest version from
    %s
    and copy the contents to your ``.gitignore``.
    """ % GITIGNORE_URL

    def __init__(self):
        self.have_gitignore = os.path.exists('.gitignore')

    def _desired_lines(self):
        lines = urllib.urlopen(GITIGNORE_URL).readlines()
        lines = [line.strip() for line in lines
                 if not line.startswith('#')]
        lines = [line for line in lines if line]
        return lines

    def looks_ok(self):
        """Return whether we've got a potential problem."""
        if not self.have_gitignore:
            logger.warn(".gitignore file missing")
            return False
        # Check contents. This brutally downloads a URL.
        lines = open('.gitignore').readlines()
        lines = [line.strip() for line in lines
                 if not line.startswith('#')]
        missing = []
        for desired_line in self._desired_lines():
            if desired_line not in lines:
                logger.debug("Missing .gitignore line: %s", desired_line)
                missing.append(desired_line)
        if missing:
            logger.warn("%s desired lines were missing from .gitignore",
                        len(missing))
            return False
        return True

    def suggested_commands(self):
        command = "curl %s -o .gitignore" % GITIGNORE_URL
        return [command]
