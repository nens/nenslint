nenslint: check and update your projects
==========================================

Nenslint is both a "lint" tool that tells you what's wrong with your project's
setup *and* a helper tool that helps you fix it up.

**Goal**: make it easy to bring your project up-to-date without having to know
details about many different aspects of our project setup. Who knows
everything about buildout? i18n setup details? This script should know *and
document it*.

**Basic usage**: call it and it'll spit out improvements it finds. Extra commands
are available for help in fixing it up. If no problems are found, nothing is
printed::

    $ nenslint

You can pass ``-v`` or ``--verbose`` to see debug output::

    $ nenslint -v
    DEBUG: Looks ok: Do we have old .txt files in the project root?
    DEBUG: Looks ok: Do we have a proper ``.gitignore`` file?

.. note::

   When you develop on nenslint, see the developer documentation in the sphinx docs.
