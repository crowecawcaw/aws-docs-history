Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Monitoring Amazon Fraud Detector with Amazon CloudWatch

You can monitor Amazon Fraud Detector using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Topics

- [Using CloudWatch Metrics for Amazon Fraud Detector.](#using-metrics "#using-metrics")
- [Amazon Fraud Detector Metrics](#YourService-metrics "#YourService-metrics")

## Using CloudWatch Metrics for Amazon Fraud Detector.

To use metrics, you must specify the following information:

- The metric namespace. A _namespace_ is a CloudWatch container Amazon Fraud Detector uses to publish its metrics into.
  If you are using the CloudWatch [ListMetrics](../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md "../../../AmazonCloudWatch/latest/APIReference/API_ListMetrics.md") API or the [list-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metrics.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-metrics.html") command to view the metrics for Amazon Fraud Detector, specify `AWS/FraudDetector` for the namespace.
- The metric dimension. A _dimension_ is
  a name-value pair that helps you to uniquely identify a metric, for example, `DetectorId` can be a dimension name. Specifying a metric dimension is optional.
- The metric name, such as `GetEventPrediction`.

You can get monitoring data for Amazon Fraud Detector by using the AWS Management Console, the AWS CLI,
or the CloudWatch API. You can also use the CloudWatch API through one of the Amazon AWS
Software Development Kits (SDKs) or the CloudWatch API tools. The console displays a
series of graphs based on the raw data from the CloudWatch API. Depending on your needs,
you might prefer to use either the graphs displayed in the console or retrieved from
the API.

###

The following list shows some common uses for the metrics. These are suggestions to
get you started, not a comprehensive list.

| How Do I?                                                          | Relevant Metrics                                                                      |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| How do I track the number of predictions that have been performed? | Monitor the `GetEventPrediction` metric.                                              |
| How can I monitor `GetEventPrediction` errors?                     | Use the `GetEventPrediction5xxError` and the<br>`GetEventPrediction4xxError` metrics. |
| How can I monitor the latency of<br>`GetEventPrediction` calls?    | Use the `GetEventPredictionLatency` metric.                                           |

You must have the appropriate CloudWatch permissions to monitor Amazon Fraud Detector with CloudWatch. For more information,
see [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").

### Access Amazon Fraud Detector Metrics

The following steps show how to access Amazon Fraud Detector metrics using the CloudWatch console.

###### To view metrics

(console)

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. Choose **Metrics**, choose the **All
   Metrics** tab, and then choose
   **Fraud Detector**.
3. Choose the metric dimension.
4. Choose the desired metric from the list, and choose a time period for the graph.

### Create an Alarm

You can create a CloudWatch alarm that sends an Amazon Simple Notification Service (Amazon SNS) message when the alarm
changes state. An alarm watches a single metric over a time period that you specify.
It performs one or more actions based on the value of the metric relative to a given
threshold over a number of time periods. The action is a notification sent to an
Amazon SNS topic or an Auto Scaling policy.

Alarms invoke actions for sustained state changes only. CloudWatch alarms don't invoke
actions simply because they are in a particular state. The state must have changed
and have been maintained for a specified number of time periods.

###### To set an alarm (console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and choose **Create
   Alarm**. This opens the **Create Alarm
   Wizard**.
3. Choose **Select metric**.
4. In the **All metrics** tab, choose **Fraud Detector**.
5. Choose **By Detector ID**, and then choose the **GetEventPrediction** metric.
6. Choose the **Graphed metrics** tab.
7. For **Statistic**, choose **Sum**.
8. Choose **Select metric**.
9. For **Conditions**, choose **Static** for **Threshold type** and **Greater** for **Whenever…**, and then enter a maximum value of your choice. Choose **Next**.
10. To send alarms to an existing Amazon SNS topic, for
    **Send notification to:**, choose an existing SNS
    topic. To set the name and email addresses for a new email subscription
    list, choose **New list**. CloudWatch saves the list and
    displays it in the field so you can use it to set future alarms.

###### Note

If you use **New list** to create a new Amazon SNS topic,
the email addresses must be verified before the intended recipients
receive notifications. Amazon SNS sends email only when the alarm enters an
alarm state. If this alarm state change happens before the email
addresses are verified, intended recipients don't receive a
notification. 11. Choose **Next**. Add a name and optional description for your alarm. Choose **Next**. 12. Choose **Create Alarm**.

## Amazon Fraud Detector Metrics

Amazon Fraud Detector sends the following metrics to CloudWatch. All metrics support these statistics: `Average`, `Minimum`, `Maximum`, `Sum`.

| Metric                                                     | Description                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GetEventPrediction`                                       | The number of GetEventPrediction API requests.<br>Valid Dimensions: `DetectorID`                                                                                                                                                                                      |
| `GetEventPredictionLatency`                                | The interval of time taken to respond to a client request from the GetEventPrediction request.<br>Valid Dimensions: `DetectorID`<br>Unit: Milliseconds                                                                                                                |
| `GetEventPrediction4XXError`                               | The number of GetEventPrediction requests where Amazon Fraud Detector returned a 4xx HTTP response code. For each 4xx response, 1 is sent.<br>Valid Dimensions: `DetectorID`                                                                                          |
| `GetEventPrediction5XXError`                               | The number of GetEventPrediction requests where Amazon Fraud Detector returned a 5xx HTTP response code. For each 5xx response, 1 is sent.<br>Valid Dimensions: `DetectorID`                                                                                          |
| `Prediction`                                               | The number of predictions. 1 is sent if successful.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`                                                                                                                                                            |
| `PredictionLatency`                                        | The interval of time taken for a prediction operation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`<br>Unit: Milliseconds                                                                                                                                   |
| `PredictionError`                                          | The number of predictions where Amazon Fraud Detector encountered an error. 1 is sent if an error is encountered.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`                                                                                              |
| `VariableUsed`                                             | The number of GetEventPrediction requests where the variable was used as part of the evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `VariableName`                                                                                               |
| `VariableDefaultReturned`                                  | The number of GetEventPrediction requests where the variable was not present as part of the Event Attributes and therefore the default value for the variable was used during evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `VariableName`      |
| `RuleNotEvaluated`                                         | The number of GetEventPrediction requests where the rule was not evaluated because a prior rule matched.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `RuleID`                                                                                             |
| `RuleEvaluateTrue`                                         | The number of GetEventPrediction requests where the rule triggered as True and the rule outcome was returned.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `RuleID`                                                                                        |
| `RuleEvaluateFalse`                                        | The number of GetEventPrediction requests where the rule evaluated to False.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `RuleID`                                                                                                                         |
| `RuleEvaluateError`                                        | The number of GetEventPrediction requests where the rule evaluates in error<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `RuleID`                                                                                                                          |
| `OutcomeReturned`                                          | The number of GetEventPrediction calls where the specified outcome was returned.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `OutcomeName`                                                                                                                |
| `ModelInvocation (Amazon SageMaker model endpoint)`        | The number of GetEventPrediction requests where the SageMaker model endpoint was invoked as part of the evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelEndpoint`                                                                           |
| `ModelInvocationError (Amazon SageMaker model endpoint)`   | The number of GetEventPrediction requests where the invoked SageMaker model endpoint returned an error during evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelEndpoint`                                                                     |
| `ModelInvocationLatency (Amazon SageMaker model endpoint)` | The interval of time taken by the Imported Model to respond as viewed from Amazon Fraud Detector. This interval includes only the model invocation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelEndpoint`<br>Unit: Milliseconds                     |
| `ModelInvocation`                                          | The number of GetEventPrediction requests where the model was invoked as part of the evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelType`, `ModelID`                                                                                       |
| `ModelInvocationError`                                     | The number of GetEventPrediction requests where the Amazon Fraud Detector model returned an error during evaluation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelType`, `ModelID`                                                                   |
| `ModelInvocationLatency`                                   | The interval of time taken by the Amazon Fraud Detector Model to respond as viewed from Amazon Fraud Detector. This interval includes only the model invocation.<br>Valid Dimensions: `DetectorID`, `DetectorVersionID`, `ModelType`, `ModelID`<br>Unit: Milliseconds |
