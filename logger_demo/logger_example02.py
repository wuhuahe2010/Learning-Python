#-*- conding:utf8 -*-
import logging
#logging.basicConfig(filename="logger_example02.log",level=logging.DEBUG)
#logging.basicConfig(filename="logger_example02.log", filemode='w', level=logging.DEBUG)
logging.basicConfig(filename="logger_example02.log",
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s|%(levelname)s|%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.info("an info log")
logging.error("an error log ")
logging.critical("an critical log")
logging.warning("an warning log")
# logging.warn("an warn log")
logging.debug("an debug log")