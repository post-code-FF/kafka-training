from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='172.18.0.2:9092',
    api_version=(2, 5, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

levels = ["info", "warning", "error"]

for i in range(20):
    event = {
        "service": "api",
        "level": random.choice(levels),
        "message": f"event number {i}"
    }

    producer.send("logs_temp", event)
    print("sent:", event)

    time.sleep(0.5)

producer.flush()
