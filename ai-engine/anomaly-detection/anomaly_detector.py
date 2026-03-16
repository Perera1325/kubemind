from kafka import KafkaConsumer
import json
import statistics

consumer = KafkaConsumer(
    "network-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

latencies = []

print("AI engine listening for telemetry events...")

for message in consumer:
    event = message.value
    latency = event["latency_ms"]

    latencies.append(latency)

    if len(latencies) > 20:
        baseline = statistics.mean(latencies)

        if latency > baseline * 2:
            print("Anomaly detected:", event)
