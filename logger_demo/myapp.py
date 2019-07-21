#-*- conding:utf8 -*-

import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    logging.info('Start')
    logging.warning('%s before you %s', 'Look', 'Leap!')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
