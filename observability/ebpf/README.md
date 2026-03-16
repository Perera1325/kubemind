eBPF Observability Module

This module captures low-level network communication between microservices
running inside Kubernetes clusters.

Using eBPF probes attached to the Linux kernel networking stack,
the platform detects TCP connections, measures latency, and tracks
service-to-service traffic patterns.

These metrics allow the AI engine to identify microservice anti-patterns
such as chatty services or high-latency dependencies.
