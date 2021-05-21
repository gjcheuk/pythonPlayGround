import psutil
from json import dumps
from confluent_kafka import Producer
from datetime import datetime
from datetime import timedelta
import sys


def fetch_cpu_load():
    try:
        return "Cpu Load is : " + str(psutil.cpu_percent(0.1)) + "%"
    except Exception as e:
        print("Error getting cpu load")
        print(str(e))


def serialize(item):
    try:
        return dumps(item, default=lambda x: x.__dict__)
    except Exception as e:
        print("Error serialising item")
        print(str(e))


def producer_setup():
    try:
        p = Producer(
            {
                'bootstrap.servers': 'localhost:9092'
            })
        return p
    except Exception as e:
        print("Error setting up Producer")
        print(str(e))


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                (msg.topic(), msg.partition(), msg.offset()))


start_time = datetime.now()
current_time = datetime.now()
while current_time - start_time < timedelta(seconds = 10):
    kafka_prod = producer_setup()
    kafka_prod.produce('mako', value=serialize(fetch_cpu_load()), callback=delivery_callback)
    kafka_prod.poll()
    current_time = datetime.now()