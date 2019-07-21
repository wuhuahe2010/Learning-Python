#-*- coding:utf -*-

from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='10.1.11.175:9292,10.1.11.176:9292,10.1.11.177:9292',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('exaple_topic', {'aaa':'bbb','tags':[{'kk1':'vv1','ll2':'334'}]})

producer.close()