# Write doc file to sphinx doc directory.
# Assumption: we're run from within the buildout root.
# Run us with ``bin/python update_documentation.py``.
import logging
import os

from nenslint import txt_to_rst


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
template = """
%(check)s
------------------------------------------------------------------------------

Reason
%(reason)s

Fix
%(fix)s


"""

for module in [txt_to_rst]:
    checker_class = getattr(module, 'Checker')
    outfile.write(template % dict(check=checker_class.check,
                                  reason=checker_class.reason,
                                  fix=checker_class.fix))
    logger.info("Wrote documentation for %s", module)

outfile.close()
