#!/bin/bash

echo "Creating kubemind telemetry topics..."

kafka-topics.sh --create \
--topic network-events \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1

kafka-topics.sh --create \
--topic service-metrics \
--bootstrap-server localhost:9092 \
--partitions 3 \
--replication-factor 1

echo "Topics created successfully."