from kubernetes import client, config
from kafka import KafkaConsumer
import json

config.load_kube_config()

apps = client.AppsV1Api()

consumer = KafkaConsumer(
    "network-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Automation operator started...")

for message in consumer:
    event = message.value

    if event["latency_ms"] > 100:
        print("High latency detected. Scaling deployment.")

        body = {
            "spec": {
                "replicas": 3
            }
        }

        apps.patch_namespaced_deployment_scale(
            name="payment-service",
            namespace="default",
            body=body
        )
