# Telemetry Normalization

The Telemetry Normalization solution enables fleet operators to receive unified vehicle telemetry regardless of whether data originates from direct MQTT connections, AWS IoT FleetWise Edge (CAN bus), or OEM cloud-to-cloud APIs. Each source uses different signal names, units, encodings, and delivery mechanisms. The normalization pipeline produces identical output from all sources so that downstream consumers — dashboards, analytics, safety processors — work uniformly.

![Telemetry Normalization Architecture](images/telemetry-normal.png)
