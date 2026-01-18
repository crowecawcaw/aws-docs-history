# Monitor an Amazon MSK Provisioned cluster

There are several ways that Amazon MSK helps you monitor the status of your Amazon MSK Provisioned cluster.

- Amazon MSK gathers Apache Kafka metrics and sends them to Amazon CloudWatch where you can view them. For more information about Apache Kafka metrics, including the ones that Amazon MSK surfaces, see [Monitoring](http://kafka.apache.org/documentation/#monitoring "http://kafka.apache.org/documentation/#monitoring") in the Apache Kafka documentation.
- You can also monitor your MSK cluster with Prometheus, an open-source monitoring
  application. For information about Prometheus, see [Overview](https://prometheus.io/docs/introduction/overview/ "https://prometheus.io/docs/introduction/overview/") in the
  Prometheus documentation. To learn how to monitor your MSK Provisioned cluster with Prometheus, see [Monitor an MSK Provisioned cluster with
  Prometheus](open-monitoring.md "open-monitoring.md").
- (Standard brokers only) Amazon MSK helps you monitor your disk storage capacity by automatically sending you storage capacity alerts when a
  Provisioned cluster is about to reach its storage capacity limit. The alerts also provide
  recommendations on the best steps to take to address detected issues. This helps you
  to identify and quickly resolve disk capacity issues before they become critical.
  Amazon MSK automatically sends these alerts to the [Amazon MSK
  console](https://console.aws.amazon.com/msk/home?region=us-east-1#/home/ "https://console.aws.amazon.com/msk/home?region=us-east-1#/home/"), Health Dashboard, Amazon EventBridge, and email contacts for your AWS account. For
  information about storage capacity alerts, see [Use Amazon MSK storage capacity alerts](cluster-alerts.md "cluster-alerts.md").

###### Topics

- [View Amazon MSK metrics using CloudWatch](cloudwatch-metrics.md "cloudwatch-metrics.md")
- [Amazon MSK metrics for monitoring Standard brokers with CloudWatch](metrics-details.md "metrics-details.md")
- [Amazon MSK metrics for monitoring Express brokers with CloudWatch](metrics-details-express.md "metrics-details-express.md")
- [Monitor an MSK Provisioned cluster with
  Prometheus](open-monitoring.md "open-monitoring.md")
- [Monitor consumer lags](consumer-lag.md "consumer-lag.md")
- [Use Amazon MSK storage capacity alerts](cluster-alerts.md "cluster-alerts.md")
