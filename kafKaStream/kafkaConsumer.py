from kafka import KafkaConsumer
import json
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, database='mako')
client.create_database('mako')

consumer = KafkaConsumer(
    'mako',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for msg in consumer:
    print(msg)
#
# try:
#     while True:
#         print('Waiting for message..')
#         msg = consumer.poll(1)
#         print(msg)
#         if msg is None:
#             continue
#         if msg.error():
#             print("Consumer error: {}".format(msg.error()))
#             continue
#         json_body = [
#         {
#             "measurement": "cpu_load",
#             "tags": {
#             },
#             "fields":json.loads(msg.value())
#         }
#         ]
#         client.write_points(json_body)
# except KeyboardInterrupt:
#     sys.stderr.write('%% Aborted by user\n')
# finally:
#     consumer.close()