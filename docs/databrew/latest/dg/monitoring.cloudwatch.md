# Monitoring DataBrew with Amazon CloudWatch

You can monitor DataBrew using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS Glue DataBrew reports the following metrics in the `AWS/DataBrew`
namespace.

| Metric         | Description                                                                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `SessionCount` | The total number of DataBrew sessions across the customer's account<br>Valid Dimensions: LogGroupName<br>Valid Statistic: Sum<br>Units: Count |
