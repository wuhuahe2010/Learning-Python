#-*- coding:utf8 -*-

from elasticsearch import Elasticsearch
import logging.handlers
import json
from kafka import KafkaProducer

file_handler = logging.handlers.RotatingFileHandler(filename='read_alterts.log', mode='a',encoding='utf-8')

logging.basicConfig(
                    #filename="read_alterts.log",
                    #filemode='w',
                    handlers=[file_handler],
                    level=logging.INFO,
                    format='%(asctime)s|%(levelname)s|%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

producer = KafkaProducer(bootstrap_servers='10.1.11.175:9292,10.1.11.176:9292,10.1.11.177:9292',value_serializer=lambda v: json.dumps(v).encode('utf-8'))


es = Elasticsearch(['http://10.1.11.176:19210', 'http://10.1.11.177:19210'])


def get_source(page):
    """
    获取es存储的记录
    :param page:
    :return:
    """
    records = page['hits']['hits']
    for record in records:
        #jsonStr = json.dumps(record['_source'])
        logging.info(isinstance(record['_source'], dict))


def get_source_and_send_to_kafka(page, producer, topic):
    """
    获取es存储的记录
    :param page:
    :return:
    """
    records = page['hits']['hits']
    for record in records:
        #jsonStr = json.dumps(record['_source'])
        logging.info(json.dumps(record['_source']))
        producer.send(topic, record['_source'])

page = es.search(
    index='alert', doc_type='base', scroll='2m', search_type='query_then_fetch',size=1000,
    body={
        "query":{
            "match_all":{}
        }
    }
)


sid = page['_scroll_id']
scroll_size = page['hits']['total']
#get_source(page)
get_source_and_send_to_kafka(page, producer, 'alert_example_xuwy')


while(scroll_size > 0):
    logging.info('Scrolling...')
    page = es.scroll(scroll_id= sid, scroll = '2m')
    # logging.info(page)
    sid = page['_scroll_id']
    scroll_size = len(page['hits']['hits'])
    print('scroll size:', str(scroll_size))
    get_source_and_send_to_kafka(page, producer, 'alert_example_xuwy')