# Correlate Amazon ECS application performance using application

metrics

Amazon ECS on Fargate supports collecting metrics from your applications running on Fargate
and exporting them to either Amazon CloudWatch or Amazon Managed Service for Prometheus.

You can use the collected metadata to correlate application performance data with
underlying infrastructure data, reducing the mean time to resolve the problem.

Amazon ECS uses an AWS Distro for OpenTelemetry sidecar container to collect and route your
application metrics to the destination. The Amazon ECS console experience simplifies the process
of adding this integration when creating your task definitions.

###### Topics

- [Exporting application metrics to
  Amazon CloudWatch](application-metrics-cloudwatch.md "application-metrics-cloudwatch.md")
- [Exporting application metrics to
  Amazon Managed Service for Prometheus](application-metrics-prometheus.md "application-metrics-prometheus.md")
