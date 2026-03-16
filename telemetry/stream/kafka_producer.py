from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    event = {
        "service": "payment-service",
        "latency_ms": 42,
        "timestamp": time.time()
    }

    producer.send("network-events", event)
    print("Sent event:", event)

    time.sleep(2)