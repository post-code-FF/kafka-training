from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "logs_temp",
    bootstrap_servers='172.18.0.2:9092',
    group_id='log-processor',
    auto_offset_reset='earliest',
    api_version=(2, 5, 0),
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for msg in consumer:
    print("received:", msg.value)
