#-*- coding:utf8 -*-

from kafka import KafkaConsumer

consumer = KafkaConsumer('alert_example_xuwy', bootstrap_servers='10.1.11.175:9292,10.1.11.176:9292,10.1.11.177:9292',
                         group_id='consumer00001',auto_offset_reset='earliest')

for msg in consumer:
    print(msg)