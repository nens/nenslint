Developer documentation
=======================

Current status of nenslint
--------------------------

Barely started!

TODO:

- Help with upgrade to buildout 2.x.

- Check our own version. Are we new enough?


Development notes
-----------------

- Every kind of check should be in its own file.

- Everything needs to be tested.

- No changes ought to be made; only print commands. This makes testing
  easy. It also makes it more clear what's happening. Making it more clear
  might not be the best reason, but the easy testing is enough to stick with
  it for the time being.


Documentation
-------------

After adding a checker, run ``bin/python update_documentation.py`` to update
the automatically-generated sphinx checker documentation.

This re-generates the ``checkers.rst`` sphinx file from the information in the
checkers' code. A guarantee for always up-to-date documentation!


Adding a new checker
--------------------

Adding a new checker means adding a separate module with a class named
``Checker`` that subclasses :class:`nenslint.base.BaseChecker`.

.. autoclass:: nenslint.base.BaseChecker
   :members: check, reason, fix, looks_ok, suggested_commands, documentation
   :undoc-members:
