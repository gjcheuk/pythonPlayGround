from kafka import KafkaConsumer
import json
import sys
from influxdb import InfluxDBClient
from confluent_kafka import Consumer, KafkaError

client = InfluxDBClient(host='localhost', port=8086, database='mako')
client.create_database('mako')

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True
})
c.subscribe(['mako_new_2'])

try:
    while True:
        print('Waiting for message..')
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        json_body = [
            {
                "measurement": "cpu_load",
                "tags": {
                },
                "fields": {
                    "Float_value": json.loads(msg.value())
                }
            }
        ]
        client.write_points(json_body)
except KeyboardInterrupt:
    sys.stderr.write('%% Aborted by user\n')
finally:
    c.close()

