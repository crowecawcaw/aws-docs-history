# Metrics published by log anomaly detectors

CloudWatch Logs publishes the **AnomalyCount** metric to CloudWatch metrics. This
metric is published to the `AWS/Logs` namespace.

The **AnomalyCount** metric is published with the following
dimensions:

- **LogAnomalyDetector**– The name of the
  anomaly detector
- **LogAnomalyPriority**– The priority level
  of the anomaly
