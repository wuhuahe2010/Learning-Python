# -*- coding: UTF-8 -*-
"""
测试操作Elasticsearch
"""
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from lambda_utils import *
import time

host_dev = ''
host_prod = ''

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''
region = ''
service = 'es'

index = 'reports'
doc_type = 'report'
doc_id = 'report_id'

awsauth = AWS4Auth(AWS_ACCESS_KEY, AWS_SECRET_KEY, region, service)

mapping = {
    doc_type: {
        "properties": {
            "report_id": {
                "type": "string",
                "index": "not_analyzed"
            },
            "create_time": {
                "type": "long",
                "index": "no"
            },
            "item_id": {
                "type": "string",
                "index": "not_analyzed"
            },
            "reason": {
                "type": "string",
                "index": "no"
            },
            "update_time": {
                "type": "long",
                "index": "no"
            },
            "user_id": {
                "type": "string",
                "index": "not_analyzed"
            },
            "operator": {
                "type": "string",
                "index": "not_analyzed"
            },
            "nickname": {
                "type": "string",
                "index": "not_analyzed"
            },
            "report_nickname": {
                "type": "string",
                "index": "not_analyzed"
            },
            "item_status": {
                "type": "long",
                "index": "not_analyzed"
            },
            "content_url": {
                "type": "string",
                "index": "no"
            },
            "item_create_time": {
                "type": "long",
                "index": "no"
            }
        }
    }
}


def createIndex(client):
    """
    创建索引
    :param client:
    :return: None
    """
    if not client.indices.exists(index=index):
        print(client.indices.create(index=index, body={'mappings': mapping}))
        print("索引创建成功")
    else:
        print("索引已经存在")


def deleteIndex(client):
    """
    删除索引
    :param client:
    :return: None
    """
    if client.indices.exists(index=index):
        client.indices.delete(index=index)
        print("索引删除成功")
    else:
        print("索引不存在")


def editMapping(client):
    add_mapping = {
        doc_type: {
            "properties": {
                "recommend_time": {
                    "type": "long",
                    "index": "not_analyzed"
                }
            }
        }
    }
    response = client.indices.put_mapping(doc_type=doc_type, body=add_mapping, index=index)
    print(response)


def createData(client):
    """
    创建数据
    :param client:
    :return: None
    """
    data_list = []
    # feedback_id = base62_encode(encode_id(int(1000 * time.time())))
    feedback_id = ""
    es_data = {
        "_index": index,
        "_type": doc_type,
        "_id": feedback_id,
    }
    data_list.append({'index': es_data})
    data = {}
    data['report_id'] = feedback_id
    data['create_time'] = int(1000 * time.time())
    data['item_create_time'] = int(1000 * time.time())
    data['item_id'] = feedback_id
    data['user_id'] = feedback_id
    data['nickname'] = 'love_jobs'
    data['report_nickname'] = 'love_jobs'
    data['item_status'] = 1
    data['operator'] = 'love_jobs'
    data_list.append(data)
    client.bulk(body=data_list)
    print("数据创建成功,id=", feedback_id)


def updateData(client, id):
    """
    修改数据
    :param client:
    :param id: 索引主键
    :return: None
    """
    data_list = []
    # feedback_id = base62_encode(encode_id(int(1000 * time.time()))
    feedback_id = ""
    es_data = {
        "_index": index,
        "_type": doc_type,
        "_id": id,
    }
    data_list.append({'index': es_data})
    data = {}
    data['report_id'] = id
    data['create_time'] = int(1000 * time.time())
    data['item_create_time'] = int(1000 * time.time())
    data['item_id'] = feedback_id
    data['user_id'] = feedback_id
    data['nickname'] = 'fengxin'
    data['report_nickname'] = 'fengxin'
    data['item_status'] = 1
    data['operator'] = 'fengxin'
    data_list.append(data)
    client.bulk(body=data_list)
    print("数据修改成功,id=", feedback_id)


def deleteData(client, id):
    """
    删除数据
    :param client:
    :param id: 数据主键
    :return: None
    """
    data_list = []
    metadata = {
        '_index': index,
        '_type': doc_type,
        '_id': id
    }
    data_list.append({'delete': metadata})
    client.bulk(body=data_list)
    print("数据删除成功,id=", id)


def queryData(client):
    """
    查询数据
    :param client:
    :return:None
    """
    responce = client.search(
        index=index,
        doc_type=doc_type,
        size=1000,
        body={
            'query': {
                'match': {
                    "report_id": '3JAgQ'
                }
            }
        }
    )
    print("查询结果为：", responce)


def es_handler(env):
    """
    创建链接
    :param env:环境变量
    :return: 链接
    """
    host = env == 'prod' and host_prod or host_dev
    return Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )


if __name__ == '__main__':
    # createIndex(es_handler('dev'))
    # createData(es_handler('dev'))
    # updateData(es_handler('dev'),'3JAgQ')
    # queryData(es_handler('dev'))
    # editMapping(es_handler('dev'))
    # deleteData(es_handler('dev'),'3JAgQ');
    # deleteIndex(es_handler('dev'))
    print("个人测试")