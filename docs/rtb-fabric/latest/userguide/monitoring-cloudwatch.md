# Monitoring RTB Fabric with Amazon CloudWatch

You can monitor RTB Fabric using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Note

RTB Fabric CloudWatch metrics are available in the following regions only: US East (N. Virginia),
US West (Oregon), Europe (Ireland), Europe (Frankfurt), Asia Pacific (Singapore), and Asia Pacific (Tokyo).

For RTB Fabric, you can monitor request volume, latency, HTTP status codes, and infrastructure metrics
to track the performance and health of your RTB gateways and links.

The RTB Fabric service reports metrics in the `AWS/RTBFabric` namespace.
