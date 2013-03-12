# Write doc file to sphinx doc directory.
# Assumption: we're run from within the buildout root.
# Run us with ``bin/python update_documentation.py``.
import logging
import os
import sys

from nenslint.runner import checker_classes

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
output_filename = './doc/source/checks.rst'
if not os.path.exists(output_filename):
    logger.error("%s doesn't exist. We're run from the wrong directory?",
                 output_filename)
    sys.exit(1)

outfile = open(output_filename, 'w')
outfile.write("""Available checks
=================================

""")

for checker_class in checker_classes():
    outfile.write(checker_class.documentation())
    logger.info("Wrote documentation for %s", checker_class)

outfile.close()
