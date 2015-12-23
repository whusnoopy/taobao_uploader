import sys
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)s %(message)s"))
log.addHandler(consoleHandler)
