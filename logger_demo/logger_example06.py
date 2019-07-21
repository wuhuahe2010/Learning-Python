#-*- condig:utf8 -*-
import logging.config
import yaml
import logging.handlers

with open('logging.yaml','r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('simpleExample')
logger.info('Example logging.....')
# 每隔 1000 Byte 划分一个日志文件，备份文件为 3 个
#file_handler = logging.handlers.RotatingFileHandler("test.log", mode="w", maxBytes=1000, backupCount=3, encoding="utf-8")
# 每隔 1小时 划分一个日志文件，interval 是时间间隔，备份文件为 10 个
#handler2 = logging.handlers.TimedRotatingFileHandler("test.log", when="H", interval=1, backupCount=10)
for i in range(10000):
    logger.info('Example logging:%d', i)