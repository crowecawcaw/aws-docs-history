# Monitoring Rekognition with Amazon CloudWatch

With CloudWatch, you can get metrics for individual Rekognition operations or global Rekognition metrics
for your account, You can use metrics to track the health of your Rekognition-based solution
and set up alarms to notify you when one or more metrics fall outside a defined
threshold. For example, you can
see
metrics for the number of server errors that have occurred, or metrics for
the number of faces that have been detected. You can also see metrics for the number of
times a specific Rekognition operation has succeeded. To see metrics, you can use [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), [Amazon AWS Command Line Interface](../../../AmazonCloudWatch/latest/cli.md "../../../AmazonCloudWatch/latest/cli.md"), or the [CloudWatch API](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").

You can also see aggregated metrics, for a chosen period of time, by using the Rekognition console.
For more information, see [Exercise 4: See aggregated metrics
(console)](aggregated-metrics.md "aggregated-metrics.md").

## Using CloudWatch metrics for Rekognition

To use metrics, you must specify the following information:

- The
  metric dimension, or no dimension. A
  _dimension_
  is a name-value pair that helps you to uniquely identify
  a metric. Rekognition has one dimension, named _Operation_. It
  provides metrics for a specific operation. If you do not specify a
  dimension, the metric is scoped to all Rekognition operations within your
  account.
- The metric name, such as `UserErrorCount`.

You can get monitoring data for Rekognition using the AWS Management Console, the
AWS CLI, or the CloudWatch API. You can also use the CloudWatch API through one of the Amazon AWS
Software Development Kits (SDKs) or the CloudWatch API tools. The console displays a
series of graphs based on the raw data from the CloudWatch API.
Depending
on your needs, you might prefer to use either the graphs displayed in the console or
retrieved from the API.

###

The following list shows some common uses for the metrics. These are suggestions to
get you started, not a comprehensive list.

| How Do I?                                                                                             | Relevant Metrics                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How do I track the numbers of faces recognized?                                                       | Monitor the `Sum` statistic of the<br>`DetectedFaceCount` metric.                                                                                                                                                                                    |
| How do I know if my application has reached the maximum<br>number of requests per second?             | Monitor the `Sum` statistic of the<br>`ThrottledCount` metric.                                                                                                                                                                                       |
| How can I monitor the request errors?                                                                 | Use the `Sum` statistic of the<br>`UserErrorCount` metric.                                                                                                                                                                                           |
| How can I find the total number of requests?                                                          | Use the `ResponseTime` and `Data<br>Samples` statistic of the<br>`ResponseTime` metric. This<br>includes<br>any request that results in an error. If<br>you want to see only successful operation calls, use the<br>`SuccessfulRequestCount` metric. |
| How can I monitor the latency of<br>`Rekognition`<br>operation calls?                                 | Use the `ResponseTime` metric.                                                                                                                                                                                                                       |
| How can I monitor how many times `IndexFaces`<br>successfully added faces to Rekognition collections? | Monitor the `Sum` statistic with the<br>`SuccessfulRequestCount` metric and<br>`IndexFaces` operation. Use the<br>`Operation` dimension to select the operation<br>and metric.                                                                       |

You must have the appropriate CloudWatch permissions to monitor Rekognition with CloudWatch. For more information,
see [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").

## Access Rekognition metrics

The following examples show how to access Rekognition metrics using the CloudWatch console, the AWS CLI, and the CloudWatch
API.

###### To view metrics

(console)

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. Choose **Metrics**, choose the **All
   Metrics** tab, and then choose
   **Rekognition**.
3. Choose **Metrics with no dimensions**, and then choose a
   metric.

For example, choose the **DetectedFace** metric to measure how many faces have been detected. 4. Choose a value for the date range. The metric count displayed in the
graph.

###### To view metrics successful `DetectFaces` operation calls have been made over a period of

time (CLI).

- Open the AWS CLI and enter the following command:

`aws cloudwatch get-metric-statistics --metric-name
 SuccessfulRequestCount --start-time 2017-1-1T19:46:20 --end-time
 2017-1-6T19:46:57 --period 3600 --namespace AWS/Rekognition --statistics
 Sum --dimensions Name=Operation,Value=DetectFaces --region
 us-west-2`

This example shows the successful `DetectFaces` operation calls made over a period of
time. For more information, see [get-metric-statistics](../../../cli/latest/reference/get-metric-statistics.md "../../../cli/latest/reference/get-metric-statistics.md").

###### To access metrics (CloudWatch API)

- Call `GetMetricStatistics`. For more information, see the
  [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").

## Create an alarm

You can create a CloudWatch alarm that sends an Amazon Simple Notification Service (Amazon SNS) message when the alarm
changes state. An alarm watches a single metric over a time period you specify, and
performs one or more actions based on the value of the metric relative to a given
threshold over a number of time periods. The action is a notification sent to an
Amazon SNS topic or an
Amazon EC2 Auto Scaling
policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms do not invoke
actions simply because they are in a particular state. The state must have changed
and been maintained for a specified number of time periods.

###### To set an alarm (console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Create Alarm**. This launches the
   **Create Alarm Wizard**.
3. In the **Metrics with no dimensions** metric list, choose
   **Rekognition Metrics**, and then choose a metric.

For example, choose **DetectedFaceCount** to set an alarm
for a maximum number of detected faces. 4. In the **Time Range** area, select a date range value
that includes face detection operations that you have called. Choose
**Next** 5. Fill in the **Name** and
**Description**. For **Whenever**, choose
**>=**, and enter a maximum value of your
choice. 6. If you want CloudWatch to send you email when the alarm state is reached, for
**Whenever this alarm:**, choose **State is
ALARM**. To send alarms to an existing Amazon SNS topic, for
**Send notification to:**, choose an existing SNS
topic. To set the name and email addresses for a new email subscription
list, choose **Create topic** CloudWatch saves the list and
displays it in the field so you can use it to set future alarms.

###### Note

If you use **Create topic** to create a new Amazon SNS
topic,
the
email addresses must be verified before the intended
recipients receive notifications. Amazon SNS sends email only when the alarm
enters an alarm state. If this alarm state change happens before the
email addresses are verified, intended recipients do not receive a
notification. 7. Preview the alarm in the **Alarm Preview** section.
Choose **Create Alarm**.

###### To set an alarm (AWS CLI)

- Open the AWS CLI and enter the following command. Change value of the
  `alarm-actions` parameter to reference an Amazon SNS topic that
  you previously created.

`aws cloudwatch put-metric-alarm --alarm-name UserErrors
 --alarm-description "Alarm when more than 10 user errors occur"
 --metric-name UserErrorCount --namespace AWS/Rekognition --statistic
 Average --period 300 --threshold 10 --comparison-operator
 GreaterThanThreshold --evaluation-periods 2 --alarm-actions
 arn:aws:sns:us-west-2:111111111111:UserError --unit Count`

This example shows how to create an alarm for when more than 10 user errors occur within 5 minutes.
For more information, see [put-metric-alarm](../../../cli/latest/reference/put-metric-alarm.md "../../../cli/latest/reference/put-metric-alarm.md").

###### To set an alarm (CloudWatch API)

- Call `PutMetricAlarm`. For more information, see
  _[Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md")_.

## CloudWatch

metrics for Rekognition

This section contains information about the Amazon CloudWatch metrics and the _Operation_ dimension available for Amazon Rekognition.

You can also see an aggregate view of Rekognition metrics from the Rekognition console. For more information, see
[Exercise 4: See aggregated metrics
(console)](aggregated-metrics.md "aggregated-metrics.md").

### CloudWatch metrics for Rekognition

The following table summarizes the Rekognition metrics.

| Metric                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SuccessfulRequestCount  | The number of successful requests. The response code range for<br>a successful request is 200 to 299.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                                                           |
| ThrottledCount          | The number of throttled requests. Rekognition throttles a request<br>when it receives more requests than the limit of transactions<br>per second set for your account. If the limit set for your<br>account is frequently exceeded, you can request a limit<br>increase. To request an increase, see [AWS Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").<br>Unit: Count<br>Valid statistics: `Sum,Average` |
| ResponseTime            | The time in milliseconds for Rekognition to compute the response.<br>Units:<br>1. Count for `Data Samples` statistics<br>2. Milliseconds for `Average`<br>statistics<br>Valid statistics: `Data Samples,Average`<br>NoteThe `ResponseTime` metric is not included in<br>the Rekognition metric pane.                                                                                                                                                                              |
| DetectedFaceCount       | The number of faces detected with the `IndexFaces`<br>or `DetectFaces` operation.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                                                                               |
| DetectedLabelCount      | The number of labels detected with the<br>`DetectLabels` operation.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                                                                                             |
| ServerErrorCount        | The number of server errors. The response code range for a<br>server error is 500 to 599.<br>Unit: Count<br>Valid statistics: `Sum, Average`                                                                                                                                                                                                                                                                                                                                      |
| UserErrorCount          | The number of user errors (invalid parameters, invalid image,<br>no permission, etc). The response code range for a user error is<br>400 to 499.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                |
| MinInferenceUnits       | The minimum number of inference units specified during the<br>`StartProjectVersion` request.Unit:<br>CountValid statistics:<br>`Average`                                                                                                                                                                                                                                                                                                                                          |
| MaxInferenceUnits       | The maximum number of inference units specified during the<br>`StartProjectVersion` request.Unit:<br>CountValid statistics:<br>`Average`                                                                                                                                                                                                                                                                                                                                          |
| DesiredInferenceUnits   | The number of inference units to which Rekognition is scaling up or<br>down.<br>Unit: Count<br>Valid statistics: `Average`                                                                                                                                                                                                                                                                                                                                                        |
| InServiceInferenceUnits | The number of inference units that the model is using.<br>Unit: Count<br>Valid statistics: `Average`<br>It is recommended that you use the Average statistic to obtain<br>the 1 minute average of how many instances are used.                                                                                                                                                                                                                                                    |

### CloudWatch metrics for Rekognition Streaming

Rekognition also has a second namespace used for streaming operations, "Rekognition
Streaming". The following table summarizes the Rekognition Streaming metrics.

| Metric                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SuccessfulRequestCount | The number of successful requests. The response code range<br>for a successful request is 200 to 299.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                                                           |
| CallCount              | The number of specified operations performed in your<br>account.<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                                                                                                               |
| ThrottledCount         | The number of throttled requests. Rekognition throttles a<br>request when it receives more requests than the limit of<br>transactions per second set for your account. If the limit<br>set for your account is frequently exceeded, you can request<br>a limit increase. To request an increase, see [AWS Service Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").<br>Unit: Count<br>Valid statistics: `Sum,Average` |
| ServerErrorCount       | The number of server errors. The response code range for a<br>server error is 500 to 599.<br>Unit: Count<br>Valid statistics: `Sum, Average`                                                                                                                                                                                                                                                                                                                                      |
| UserErrorCount         | The number of user errors (invalid parameters, invalid<br>image, no permission, etc). The response code range for a<br>user error is 400 to 499.<br>Unit: Count<br>Valid statistics: `Sum,Average`                                                                                                                                                                                                                                                                                |
| ConcurrentSessions     | The number of concurrent sessions your account is currently<br>using.Unit: CountValid statistics:<br>`Max,Average`                                                                                                                                                                                                                                                                                                                                                                |

### CloudWatch dimension for Rekognition

To retrieve operation-specific metrics, use the `Rekognition` namespace
and provide an operation dimension.

For more information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the
_Amazon CloudWatch User Guide_.

### CloudWatch dimension for Rekognition Custom

Labels

The following table displays the CloudWatch dimensions available for use with
Rekognition Custom Labels:

| Dimension   | Description                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| ProjectName | The name of the Rekognition Custom Labels project you created with<br>`CreateProject`.                |
| VersionName | The name of the Rekognition Custom Labels project version you created<br>with `CreateProjectVersion`. |

For more information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the
_Amazon CloudWatch User Guide_.
