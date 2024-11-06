import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(stream=sys.stdout,)
formatter = logging.Formatter(
    '%(asctime)s, %(levelname)s,%(name)s, %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
