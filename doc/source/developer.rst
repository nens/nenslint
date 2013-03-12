Developer documentation
=======================

The program is structured in two parts:

- A module :mod:`nenslint.runner` with the ``nenslint`` script that actually
  runs everything.

- A bunch of several other modules with each one single Checker class. Every
  checker should check one aspect, for instance whether the buildout setup is
  up to date. A single check can translate into a number of separate details
  that need to be "sub-checked", but that's ok as long as it is an
  implementation detail in the checker.

  One single check should be pretty much stand-alone and well-testable.

  See :ref:`adding-a-checker` if you want to add a new one.


Development notes
-----------------

- Every kind of check should be in its own file.

- Everything needs to be tested.

- No changes ought to be made; only print commands. This makes testing
  easy. It also makes it more clear what's happening. Making it more clear
  might not be the best reason, but the easy testing is enough to stick with
  it for the time being.

- After adding a checker, run ``bin/python update_documentation.py`` to update
  the automatically-generated sphinx checker documentation. This re-generates
  the ``checkers.rst`` sphinx file from information in the checkers' code. A
  guarantee for always up-to-date documentation!


TODO wishlist: checks that can be added
---------------------------------------

- Help with upgrade to buildout 2.x.

- Check our own version. Are we new enough?

- If we're a Django project, set up the i18n machinery.


.. _adding-a-checker:

Adding a new checker
--------------------

Adding a new checker means three things:

- Add a separate module with a class in it named ``Checker`` that subclasses
  :class:`nenslint.base.BaseChecker`.

- Of course you should add tests in the ``nenslint/tests/`` subdirectory. Look
  at the other test files to see how it's done.

- Lastly, add the new checker to the list in
  :attr:`nenslint.runner.CHECKER_MODULE_NAMES`.

Here's the documentation for :class:`nenslint.base.BaseChecker`. It tells you
the attributes you need to set and the methods that you need to implement in
your own checker.

.. autoclass:: nenslint.base.BaseChecker
   :members: check, reason, fix, looks_ok, suggested_commands, documentation
   :undoc-members:

.. todo::

   Add doc comments to the attributes.


The central module with the actual ``nenslint`` script
------------------------------------------------------

.. automodule:: nenslint.runner
   :members:
