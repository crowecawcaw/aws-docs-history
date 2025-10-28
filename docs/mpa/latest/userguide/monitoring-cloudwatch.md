# Monitoring Multi-party approval with Amazon CloudWatch

You can monitor Multi-party approval using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

CloudWatch collects metrics that track the usage of some AWS resources.
These metrics correspond to AWS service quotas.
Tracking these metrics can help you proactively manage your quotas. For more information, see [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md") in the _Amazon CloudWatch User
Guide_.

Service quota usage metrics are in the `AWS/Usage` namespace and are collected every minute. Currently, the only metric name in this namespace that CloudWatch publishes is `ResourceCount`. This
metric is published with the dimensions `Resource`, `Service`, and
`Type`. The `Resource` dimension specifies the type of resource being tracked. For example, the `ResourceCount` metric with the dimensions
`"Service": "Multi-party approval"`, `"Type": "Resource"` and `"Resource":
 "IdentitySource"` indicates the number of `IdentitySource` resources in your account.

The following tables list the metrics and dimensions for Multi-party approval.

**Metrics**

| Metric          | Description                                                                                                                                                                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `ResourceCount` | The number of the specified resources running in your account. The resources are defined by the dimensions associated with the metric. The most useful statistic for this metric is `MAXIMUM`, which represents the maximum number of resources used during the 1-minute period. | **Dimensions** |
| Dimension       | Description                                                                                                                                                                                                                                                                      |
| ---             | ---                                                                                                                                                                                                                                                                              |
| `Service`       | The name of the AWS service containing the resource. For Multi-party approval usage metrics, the value for this dimension is `Multi-party approval`.                                                                                                                             |
| `Class`         | The class of resource that is being tracked. Multi-party approval usage metrics use this dimension with a value of `None`.                                                                                                                                                       |
| `Type`          | The type of entity that is being tracked. Currently, the only valid value for Multi-party approval is `Resource`.                                                                                                                                                                |
| `Resource`      | The type of resource that is being tracked. Currently, valid values include the following: `IdentitySource`, `ApprovalTeam`, and `ApproversPerApprovalTeam`                                                                                                                      |
