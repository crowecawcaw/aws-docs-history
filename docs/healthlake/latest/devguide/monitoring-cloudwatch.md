# Monitoring HealthLake metrics using Amazon CloudWatch

You can monitor HealthLake using Amazon CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so you can use that
historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds, and send notifications or
take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Note

Metrics are reported for all [native HealthLake
actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

The following tables list HealthLake metrics and dimensions reported to CloudWatch. Each is presented
as a frequency count for a user-specified data range.

The following HealthLake metrics are reported to CloudWatch.

| HealthLake metrics reported to CloudWatch | Metric                                                                                                                                                                                                                      | Description |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Call Count                                | The number of calls to APIs. This can be reported for the account or a<br>specified data store.<br>Units: Count<br>Valid Statistics: Sum, Count<br>Dimensions: Operation, datastore ID, data store type                     |
| Successful Requests                       | The number of successful API requests.<br>Units: Count<br>Valid Statistics: Sum, Average<br>Dimensions: Operation, data store ID, data store type                                                                           |
| User Errors                               | The number of requests that failed due to user error.<br>Units: Count<br>Valid Statistics: Sum, Average<br>Dimensions: Operation, data store ID, data store type                                                            |
| Server Errors                             | The number of requests that failed due to server error.<br>Units: Count<br>Valid Statistics: Sum, Average<br>Dimensions: Operation, data store ID, data store type                                                          |
| Throttled Requests                        | The number of requests that have been throttled. This metric is not included<br>in user or server errors counts.<br>Units: Count<br>Valid Statistics: Sum, Average<br>Dimensions: Operation, data store ID, data store type |
| Latency                                   | The time it took in milliseconds to process the user request.<br>Unit: Milliseconds<br>Valid statistics: Minimum, Maximum, Average<br>Dimensions: Operation, data store ID, data store type                                 |

The following HealthLake dimensions are reported to CloudWatch.

| HealthLake Dimensions reported to CloudWatch | Dimension                                  | Description |
| -------------------------------------------- | ------------------------------------------ | ----------- |
| Operation                                    | The API operation used in the request      |
| DataStoreID                                  | The data store ID used in the request      |
| DataStoreType                                | The type of data store used in the request |

You can get metrics for HealthLake with the AWS Management Console, the AWS CLI, or the CloudWatch
API. You can use the CloudWatch API through one of the Amazon AWS Software Development Kits
(SDKs) or the CloudWatch API tools. The HealthLake console displays graphs based on the raw data from
the CloudWatch API.

You must have the appropriate CloudWatch permissions to monitor HealthLake with CloudWatch. For
more information, see [Identity and access management for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md")in the _Amazon CloudWatch User Guide_.

## Viewing HealthLake metrics

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Metrics**, choose **All Metrics**, and then
   choose **AWS/HealthLake**.
3. Choose the dimension, choose a metric name, then choose **Add to
   graph**.
4. Choose a value for the date range. The metric count for the selected date range is
   displayed in the graph.

## Creating an alarm using CloudWatch

A CloudWatch alarm watches a single metric over a specified time period, and performs one
or more actions: sending a notification to an Amazon Simple Notification Service (SNS)
topic or Auto Scaling policy. The action or actions are based on the value of the metric
relative to a given threshold over a number of time periods that you specify. CloudWatch can
also send you an SNS message when the alarm changes state.

###### Note

CloudWatch alarms invoke actions only when the state changes and has persisted for the
period you specify.

###### To view metrics (CloudWatch console)

1. Sign in to the [CloudWatch
   console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Alarms**, and then choose **Create
   Alarm**.
3. Choose **AWS/HealthLake**, and then choose a metric.
4. For **Time Range**, choose a time range to monitor, and then choose
   **Next**.
5. Enter a **Name** and **Description**.
6. For Whenever, choose **>=**, and type a maximum value.
7. If you want CloudWatch to send an email when the alarm state is reached, in the Actions
   section, for Whenever this alarm, choose State is **ALARM**. For Send
   notification to, choose a mailing list or choose **New list** and create
   a new mailing list.
8. Preview the alarm in the Alarm Preview section. If you are satisfied with the alarm,
   choose **Create Alarm**.
