from __future__ import unicode_literals
from __future__ import print_function
import logging
import os
import urllib

from nenslint.base import BaseChecker

logger = logging.getLogger(__name__)

BOOTSTRAP_URL = ('https://raw.github.com/lizardsystem/nensskel/master/'
                 'nensskel/templates/library/bootstrap.py')


class Checker(BaseChecker):
    check = "Is the buildout setup already upgraded to 2.x?"
    reason = """
    Buildout 2.x has a couple of very handy improvements. And it is
    quicker. So we need to upgrade.
    """
    fix = """
    To fix it, grab the latest ``bootstrap.py`` from
    %s
    and (until the KGS contains the right versions) add two version pins
    to your ``buildout.cfg``'s ``[version]`` part:

    zc.buildout = 2.0.1
    zc.recipe.egg = 2.0.0a3

    Some changes you need to make to your ``[buildout]`` part:

    - Remove the ``buildout-versions`` extension, it is now included in
      buildout.

    - Add ``socket-timeout = 1`` to prevent buildout from waiting a long time.

    - Add ``show-picked-versions = true``, this enables buildout's own picked
      version printing mechanism.

    - Remove ``prefer-final = true`` and ``unzip = true``, these are now the
      defaults anyway.

    The ``[console_scripts]`` part needs an extra ``dependent-scripts = true``
    setting, this lets buildout install the scripts of the dependencies.

    """ % BOOTSTRAP_URL

    def __init__(self):
        if os.path.exists('development.cfg'):
            self.buildout_filename = 'development.cfg'
        else:
            self.buildout_filename = 'buildout.cfg'
        if not os.path.exists(self.buildout_filename):
            sys.exit("%s doesn't exist" % self.buildout_filename)
        self.buildout_lines = [line.strip() for line in
                               open(self.buildout_filename).readlines()
                               if not line.startswith('#')]

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
        command = "curl %s -o bootstrap.py" % BOOTSTRAP_URL
        return [command]
