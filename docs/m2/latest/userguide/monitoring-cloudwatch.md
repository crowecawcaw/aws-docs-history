AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Monitoring AWS Mainframe Modernization with Amazon CloudWatch

You can monitor AWS Mainframe Modernization using CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so that you can
access historical information and gain a better perspective on how your web application or
service is performing. You can also set alarms that watch for certain thresholds, and send
notifications or take actions when those thresholds are met. For more information, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The following tables list the metrics and dimensions for AWS Mainframe Modernization. The namespace for
these metrics is `AWS/M2`.

## Runtime Environment Metrics

| Metric                    | Description                                                                                                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPUUtilization            | The CPU utilization of instances in the environment.<br>Dimension: environmentId<br>Units: Percent<br>Valid statistics: Average, Minimum, Maximum                      |
| InboundNetworkThroughput  | Inbound network throughput of instances in the environment.<br>Dimension: environmentId<br>Units: Bytes per second<br>Valid statistics: Average, Minimum, Maximum      |
| MemoryUtilization         | The memory utilization of instances in the environment.<br>Dimension: environmentId<br>Units: Percent<br>Valid statistics: Average, Minimum, Maximum                   |
| OutboundNetworkThroughput | Outbound network throughput of the instances in the environment.<br>Dimension: environmentId<br>Units: Bytes per second<br>Valid statistics: Average, Minimum, Maximum |

## Application Metrics

| Metric                    | Description                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BatchJobCompletedCount    | The number of completed jobs during the time interval.<br>This metric is available for Rocket Software (formerly Micro Focus) and for AWS Blu Age 3.7.0 and later<br>releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Sum                                                                                                     |
| BatchJobFailedCount       | The number of failed jobs during the time interval.<br>This metric is available for Rocket Software and for AWS Blu Age 3.7.0 and later<br>releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Sum                                                                                                                               |
| JvmMemoryFree             | The amount of available memory that is not currently in use by the Java<br>Virtual Machine.<br>This metric is only available for the AWS Blu Age runtime engine. It is available for<br>AWS Blu Age 3.7.0 and later releases.<br>Dimension: applicationId<br>Units: Bytes<br>Valid statistics: Average, Minimum, Maximum                                |
| JvmMemoryMax              | The maximum amount of memory allowed for the Java Virtual Machine.<br>This metric is only available for the AWS Blu Age runtime engine. It is available for<br>AWS Blu Age 3.7.0 and later releases.<br>Dimension: applicationId<br>Units: Bytes<br>Valid statistics: Average, Minimum, Maximum                                                         |
| JvmMemoryUsed             | The amount of memory actively used by the Java Virtual Machine.<br>This metric is only available for the AWS Blu Age runtime engine. It is available for<br>AWS Blu Age 3.7.0 and later releases.<br>Dimension: applicationId<br>Units: Bytes<br>Valid statistics: Average, Minimum, Maximum                                                            |
| ProcessesActiveCount      | The active number of concurrent service execution processes that are<br>processing requests.<br>This metric is only available for the Rocket Software runtime engine.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Sum                                                                                                              |
| SessionCount              | The number of HTTP sessions for the application.<br>This metric is only available for the AWS Blu Age runtime engine. It is available for<br>AWS Blu Age 3.7.0 and later releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Average, Minimum, Maximum                                                                           |
| SharedMemoryFree          | The memory that is available for the enterprise server to store all the<br>information it needs to run transactions and jobs.<br>This metric is only available for the Rocket Software runtime engine.<br>Dimension: applicationId<br>Units: Kilobytes<br>Valid statistics: Average, Minimum, Maximum                                                   |
| SharedMemoryTotal         | The total amount of shared memory allocated for the enterprise server to store<br>all the information it needs to run transactions and jobs.<br>This metric is only available for the Rocket Software runtime engine.<br>Dimension: applicationId<br>Units: Kilobytes<br>Valid statistics: Average, Minimum, Maximum                                    |
| ThreadActiveCount         | The number of engine threads that are processing requests.<br>This metric is only available for the AWS Blu Age runtime engine. It is available for<br>AWS Blu Age 3.7.0 and later releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Average, Minimum, Maximum                                                                 |
| TransactionCompletedCount | The number of committed transactions during the time interval.<br>This metric is available for Rocket Software and for AWS Blu Age 3.7.0 and later<br>releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Sum                                                                                                                    |
| TransactionFailedCount    | The number of failed transactions during the time interval.<br>This metric is available for Rocket Software and for AWS Blu Age 3.7.0 and later<br>releases.<br>Dimension: applicationId<br>Units: Count<br>Valid statistics: Sum                                                                                                                       |
| TransactionResponseTime   | The amount of time from the moment that a user sends a request until the time<br>that the application indicates that the request has been completed.<br>This metric is available for Rocket Software and for AWS Blu Age 3.7.0 and later<br>releases.<br>Dimension: applicationId<br>Units: Milliseconds<br>Valid statistics: Average, Minimum, Maximum |

## Dimensions

| Dimension     | Description                                                            |
| ------------- | ---------------------------------------------------------------------- |
| applicationId | This dimension filters the metric to the identified application by ID. |
| environmentId | This dimension filters the metric to the identified environment by ID. |
