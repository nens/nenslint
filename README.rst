nenslint: check and update your projects
==========================================

Nenslint is both a "lint" tool that tells you what's wrong with your project's
setup *and* a helper tool that helps you fix it up.

**Goal**: make it easy to bring your project up-to-date without having to know
details about many different aspects of our project setup. Who knows
everything about buildout? i18n setup details? This script should know *and
document it*.

Usage
-----

Basic usage: call it and it'll spit out improvements it finds. Extra commands
are available for help in fixing it up.


Current status of nenslint
--------------------------

Barely started!

TODO:

- Upgrade to buildout 2.x.

- Check our own version.

- txt-to-rst switch.


Development notes
-----------------

- Every kind of check should be in its own file.

- Everything needs to be tested.

- No changes ought to be made; only print commands. This makes testing
  easy. It also makes it more clear what's happening. Making it more clear
  might not be the best reason, but the easy testing is enough to stick with
  it for the time being.

- After adding a checker, run ``bin/python update_documentation.py`` to update
  the automatically-generated sphinx checker documentation.
