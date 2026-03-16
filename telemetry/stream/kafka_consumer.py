from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "network-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening for telemetry events...")

for message in consumer:
    event = message.value
    print("Received event:", event)