# Monitoring your metrics with CloudWatch

You can monitor Amazon Braket using Amazon CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. You view historical information generated up to 15 months ago
or search metrics that have been updated in the last 2 weeks in the Amazon CloudWatch console to gain a
better perspective on how Amazon Braket is performing. To learn more, see
[Using CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md").

###### Note

You can view the CloudWatch log streams for Amazon Braket notebooks by navigating to the
**Notebook detail** page on the Amazon SageMaker AI console. Additional
Amazon Braket notebook settings are available through the
[SageMaker console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").

###### In this section:

- [Amazon Braket metrics and dimensions](#braket-metric-dimensions "#braket-metric-dimensions")

## Amazon Braket metrics and dimensions

Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data
points that are published to CloudWatch. Every metric is characterized by a set of dimensions. To learn
more about metrics dimensions in CloudWatch, see
[CloudWatch dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension").

Amazon Braket sends the following metric data, specific to Amazon Braket, into the Amazon CloudWatch metrics:

**Quantum Task Metrics**

Metrics are available if quantum tasks exist. They are displayed under **AWS/Braket/By Device** in the CloudWatch console.

| Metric  | Description                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Count   | Number of quantum tasks.                                                                                                                  |
| Latency | This metric is emitted when a quantum task has completed. It represents the<br>total time from quantum task initialization to completion. |

**Dimensions for Quantum Task Metrics**

The quantum task metrics are published with a dimension based on the
`deviceArn` parameter, which has the form
**arn:aws:braket:::device/xxx**.
