

# Monitoring Amazon IVS Chat
<a name="chat-health"></a>

You can monitor Amazon Interactive Video Service (IVS) Chat resources using Amazon CloudWatch. CloudWatch collects and processes raw data from Amazon IVS Chat into readable, near real-time metrics. These statistics are kept for 15 months, so you can gain a historical perspective on how your web application or service performs. You can set alarms for certain thresholds and send notifications or take actions when those thresholds are met. For details, see the [CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

## Access CloudWatch Metrics
<a name="chat-health-cloudwatch-metrics"></a>

Amazon CloudWatch collects and processes raw data from Amazon IVS Chat into readable, near-real-time metrics. These statistics are kept for 15 months, so you can gain a historical perspective on how your web application or service performs. You can set alarms for certain thresholds and send notifications or take actions when those thresholds are met. For details, see the [CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

Note that CloudWatch metrics are rolled up over time. Resolution effectively decreases as the metrics age. Here is the schedule:
+ 60-second metrics are available for 15 days.
+ 5-minute metrics are available for 63 days.
+ 1-hour metrics are available for 455 days (15 months).

For current information on data retention, search for "retention period" in [Amazon CloudWatch FAQs](https://aws.amazon.com/cloudwatch/faqs/).

### CloudWatch Console Instructions
<a name="chat-health-cloudwatch-metrics-console"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the side navigation, expand the **Metrics** dropdown, then select **All metrics**.

1. On the **Browse** tab, using the unlabeled dropdown at the left, select your “home” region, where your channel(s) was(were) created. For more on regions, see [Global Solution, Regional Control](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/what-is.html#what-is-aws). For a list of supported regions, see the [Amazon IVS page](https://docs.aws.amazon.com/general/latest/gr/ivs.html) in the *AWS General Reference*.

1. At the bottom of the **Browse** tab, select the **IVSChat** namespace.

1. Do one of the following:

   1. In the search bar, enter your resource ID (part of the ARN, `arn:::ivschat:room/<resource id>`).

      Then select **IVSChat**.

   1. If **IVSChat** appears as a selectable service under **AWS Namespaces**, select it. It will be listed if you use Amazon IVSChat and it is sending metrics to Amazon CloudWatch. (If **IVSChat** is not listed, you do not have any Amazon IVSChat metrics.)

      Then choose a *dimension* grouping as desired; available dimensions are listed in [CloudWatch Metrics](#chat-health-cloudwatch-metrics-chat) below.

1. Choose metrics to add to the graph. Available metrics are listed in [CloudWatch Metrics](#chat-health-cloudwatch-metrics-chat) below.

You also can access your chat session’s CloudWatch chart from the chat session’s details page, by selecting the **View in CloudWatch** button.

### CLI Instructions
<a name="chat-health-cloudwatch-metrics-cli"></a>

You also can access the metrics using the AWS CLI. This requires that you first download and configure the CLI on your machine. For details, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

Then, to access Amazon IVS low-latency chat metrics using the AWS CLI:
+ At a command prompt, run: 

  ```
  aws cloudwatch list-metrics --namespace AWS/IVSChat
  ```

For more information, see [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the *Amazon CloudWatch User Guide*.

## CloudWatch Metrics: IVS Chat
<a name="chat-health-cloudwatch-metrics-chat"></a>

Amazon IVS Chat provides the following metrics in the **AWS/IVSChat** namespace.


| Metric | Dimensions | Description | 
| --- | --- | --- | 
| `ConcurrentChatConnections` | None | The total number of concurrent connections in a chat room (reported max per minute). This is useful to understand when customers approach their limit for concurrent chat connections in a region.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `Deliveries` | Action | The number of deliveries of messaging requests made of a specific action type to chat connections across all your rooms in a region.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `InvocationErrors` | `Uri` | The number of invocation errors of a specific message review handler across all your rooms in a region. An invocation error occurs when the message review handler cannot be invoked.<br />Invocation errors occur when Amazon IVS Chat cannot invoke a handler. This may happen if the handler associated with a room no longer exists or times out, or if its resource policy does not allow the service to invoke it.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `LogDestinationAccessDeniedError` | `LoggingConfiguration` | The number of access-denied errors of a log destination across all your rooms in a region.<br />These errors occur when Amazon IVS Chat cannot access the destination resource you specified in the logging configuration. This may happen if the destination resource policy does not allow the service to put records.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `LogDestinationErrors` | `LoggingConfiguration` | The number of all errors of a log destination across all your rooms in a region.<br />This is an aggregated metric which includes all types of errors that occur when Amazon IVS Chat fails to deliver logs to the destination resource you specified in the logging configuration.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `LogDestinationResourceNotFoundErrors` | `LoggingConfiguration` | The number of resource-not-found errors of a log destination across all your rooms in a region.<br />These errors occur when Amazon IVS Chat cannot deliver logs to a destination resource you specified in a logging configuration because the resource does not exist. This may happen if the destination resource associated with a logging configuration no longer exists.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `MessagingDeliveries` | None | The number of deliveries of messaging requests to chat connections across all your rooms in a region.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `MessagingRequests` | None | The number of messaging requests made across all your rooms in a region.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `Requests` | Action | The number of requests made of a specific action type across all your rooms in a region.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 
| `ResponseValidationErrors` | `Uri` | The number of response-validation errors of a specific message review handler across all your rooms in a region. A response-validation error occurs when the response from the message review handler is invalid. This may mean that the response could not be parsed or fails validation checks; e.g., an invalid review result or response values that are too long.<br />Unit: Count<br />Valid statistics: Sum, Average, Maximum, Minimum | 