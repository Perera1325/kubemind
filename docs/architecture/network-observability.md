Network Observability Layer

The platform uses eBPF probes to capture microservice communication at the
kernel level. This provides deep visibility into network flows without
modifying application code.

Captured telemetry includes service-to-service traffic, connection frequency,
and request latency. The collected data is streamed into the telemetry
pipeline where anomaly detection models analyze communication patterns.
