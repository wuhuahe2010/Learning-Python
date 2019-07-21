#-*- conding:utf8 -*-
import argparse
import logging

parser = argparse.ArgumentParser(description="logger_example01")
parser.add_argument("-l", "--log", help="the loglevel", default='DEBUG')

args = parser.parse_args()

loglevel = args.log
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(level=numeric_level)
logging.info("an info log")
logging.error("an error log ")
logging.critical("an critical log")
logging.warning("an warning log")
# logging.warn("an warn log")
logging.debug("an debug log")

#############################
