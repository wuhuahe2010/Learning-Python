#-*- conding:utf8 -*-
import logging
import logging.config

logging.config.fileConfig('logging.conf',disable_existing_loggers=False)

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')