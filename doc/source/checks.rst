Available checks
=================================


Do we have old .txt files in the project root?
------------------------------------------------------------------------------

Reason

    We use github, which renders ``.rst`` files as nicely formatted
    restructured text. Older projects often still have ``.txt`` files.

Fix

    To fix it, rename them. Oh, and check the ``setup.py`` file as it probably
    uses the readme and changelog in its long description.
    


