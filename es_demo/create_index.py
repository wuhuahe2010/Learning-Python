#-*- coding:utf8 -*-

import logging
from elasticsearch import Elasticsearch
import http.client
import json

logging.basicConfig(
    # filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d')

#logging.info('test info')
#logging.debug('test debug')
#logging.warning('test warning')
#logging.error('test error')
#logging.critical('test critical')
# 创建es 索引
es = Elasticsearch([{'host':'10.1.241.10','port': 19210},{'host':'10.1.241.11','port': 19210},{'host':'10.1.241.12','port': 19210},{'host':'10.1.241.14','port': 19210}])
# for i in range(1,100):
#     result = es.indices.create(index='news{0}'.format(i), ignore=400)
# logging.info("create index result: {}".format(result))

logging.info("#1 获取所有index")
conn = http.client.HTTPConnection("10.1.241.11", 19210)
try:
    conn.request('GET', '/_cat/indices')
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    for index_info in data.split("\n"):
        index_info_arr = index_info.split()
        if len(index_info_arr) > 2:
            index = index_info_arr[2]
            print("Get index: [{0}]".format(index))
            print("Are you sure to delete this index: {index} [Y/N]".format(index=index))
            yesOrNo = input()
            if yesOrNo == 'Yes' or yesOrNo == 'Y' or yesOrNo == 'y' or yesOrNo is None or yesOrNo == '':
                print("delete this index: {index}......".format(index=index))
                es.indices.delete(index=index, ignore=[400, 404])
            else:
                print("not to delete this index: %s ......." % index)
except Exception as e:
    logging.error(e)
finally:
    conn.close()
