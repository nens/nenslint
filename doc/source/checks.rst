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
    



Do we have a proper ``.gitignore`` file?
------------------------------------------------------------------------------

Reason

    A proper ``.gitignore`` file prevents us from accidentally committing files
    that shouldn't be committed. Mentally going through ``git status`` and
    filtering out items that are OK is *work* and we don't want that. And it
    is too easy to miss files you should add.

    Something always changes in the setup over time, so a ``.gitignore``
    that was once good, can now be missing items.
    

Fix

    To fix it, grab the latest version from
    https://raw.github.com/lizardsystem/nensskel/master/nensskel/templates/library/+dot+gitignore_tmpl
    and copy the contents to your ``.gitignore``.
    


