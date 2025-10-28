# Monitoring Amazon AppFlow with Amazon CloudWatch

You can monitor your Amazon AppFlow flows by using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can
access historical information and gain a better perspective on how your flows are performing. You
can also set alarms that watch for certain thresholds, and send notifications or take actions when
those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The Amazon AppFlow service reports the following metrics in the `AWS/AppFlow`
namespace.

| Metric                          | Description                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `FlowExecutionsStarted`         | The number of flow runs started.                                                                                                                                                                                                                                                            |
| `FlowExecutionsFailed`          | The number of failed flow runs.                                                                                                                                                                                                                                                             |
| `FlowExecutionsSucceeded`       | The number of successful flow runs.                                                                                                                                                                                                                                                         |
| `FlowExecutionTime`             | The interval, in milliseconds, between the time the flow starts and the time it finishes.                                                                                                                                                                                                   |
| `FlowExecutionRecordsProcessed` | The number of records that Amazon AppFlow attempted to transfer for the flow run. This metric counts all records that Amazon AppFlow processed internally. The processed records include those that transferred successfully and those that failed to transfer because the flow run failed. | The following dimensions are supported for the Amazon AppFlow metrics. |
| Dimension                       | Description                                                                                                                                                                                                                                                                                 |
| ---                             | ---                                                                                                                                                                                                                                                                                         |
| `FlowName`                      | The name that you assigned to the flow.                                                                                                                                                                                                                                                     |
