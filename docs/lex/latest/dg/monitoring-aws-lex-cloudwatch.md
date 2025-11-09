End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Monitoring Amazon Lex

with Amazon CloudWatch

To track the health of your Amazon Lex bots, use Amazon CloudWatch. With CloudWatch,
you can get metrics for individual Amazon Lex operations or for global
Amazon Lex operations for your account. You can also set up CloudWatch alarms
to be notified when one or more metrics exceeds a threshold that you
define. For example, you can monitor the number of requests made to
a bot over a particular time period, view the latency of successful
requests, or raise an alarm when errors exceed a threshold.

## CloudWatch Metrics for

Amazon Lex

To get metrics for your Amazon Lex operations , you must specify
the following information:

- The metric dimension. A _dimension_
  is a set of name-value pairs that you use to identify a
  metric. Amazon Lex has three dimensions:
  - `BotAlias, BotName,
Operation`
  - `BotAlias, BotName, InputMode,
Operation`
  - `BotName, BotVersion, InputMode,
Operation`

- The metric name, such as
  `MissedUtteranceCount` or
  `RuntimeRequestCount`.

You can get metrics for Amazon Lex with the AWS Management Console, the AWS CLI,
or the CloudWatch API. You can use the CloudWatch API through one of the
Amazon AWS Software Development Kits (SDKs) or the CloudWatch API
tools. The Amazon Lex console displays graphs based on the raw data
from the CloudWatch API.

You must have the appropriate CloudWatch permissions to monitor
Amazon Lex with CloudWatch . For more information, see [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in
the _Amazon CloudWatch User Guide_.

## Viewing Amazon Lex

Metrics

View Amazon Lex metrics using the Amazon Lex console or the CloudWatch
console.

###### To view metrics (Amazon Lex console)

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. From the list of bots, choose the one whose metrics
   you want to see.
3. Choose **Monitoring**. Metrics are
   displayed in graphs.

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, choose
   **All Metrics**, and then choose
   **AWS/Lex**.
3. Choose the dimension, choose a metric name, then
   choose **Add to graph**.
4. Choose a value for the date range. The metric count
   for the selected date range is displayed in the
   graph.

## Creating an

Alarm

A CloudWatch alarm watches a single metric over a specified time
period, and performs one or more actions: sending a notification
to an Amazon Simple Notification Service (Amazon SNS) topic or Auto Scaling policy. The action or
actions are based on the value of the metric relative to a given
threshold over a number of time periods that you specify. CloudWatch
can also send you an Amazon SNS message when the alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has
persisted for the period that you specify.

###### To set an alarm

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Alarms**, and then choose
   **Create Alarm**.
3. Choose **AWS/Lex Metrics**, and then
   choose a metric.
4. For **Time Range**, choose a time
   range to monitor, and then choose
   **Next**.
5. Enter a **Name** and
   **Description**.
6. For **Whenever**, choose
   **>=**, and type a maximum
   value.
7. If you want CloudWatch to send an email when the alarm state
   is reached, in the **Actions** section,
   for **Whenever this alarm**, choose
   **State is ALARM**. For
   **Send notification to**, choose a
   mailing list or choose **New list** and
   create a new mailing list.
8. Preview the alarm in the **Alarm
   Preview** section. If you are satisfied
   with the alarm, choose **Create
   Alarm**.

## CloudWatch

Metrics for Amazon Lex Runtime

The following table describes the Amazon Lex runtime
metrics.

| Metric                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `KendraIndexAccessError`                                                                                                                | The number of times that Amazon Lex could<br>not access your Amazon Kendra index.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                     |
| `KendraLatency`                                                                                                                         | The amount of time that it takes Amazon Kendra<br>to respond to a request from the<br>`AMAZON.KendraSearchIntent`.Valid<br>dimensions for the `PostContent`<br>operation with the `Text` or<br>`Speech`<br>`InputMode`:<br>• `BotName, BotVersion,<br>Operation, InputMode`<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimensions for the<br>`PostText` operation:<br>• `BotName, BotVersion,<br>Operation`<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Milliseconds                                                                                                                                                                                                               |
| `KendraSuccess`                                                                                                                         | The number of successful requests from<br>the `AMAZON.KendraSearchIntent`<br>to your Amazon Kendra index.Valid<br>dimensions for the `PostContent`<br>operation with the `Text` or<br>`Speech`<br>`InputMode`:<br>• `BotName, BotVersion,<br>Operation, InputMode`<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimensions for the<br>`PostText` operation:<br>• `BotName, BotVersion,<br>Operation`<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                               |
| `KendraSystemErrors`                                                                                                                    | The number of times that Amazon Lex couldn't<br>query the Amazon Kendra index.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                                                                                                        |
| `KendraThrottledEvents`                                                                                                                 | The number of times Amazon Kendra throttled<br>requests from the<br>`AMAZON.KendraSearchIntent`.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                                                                                      |
| `MissedUtteranceCount`                                                                                                                  | The number of utterances that were not<br>recognized in the specified period.<br>Valid dimensions for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotVersion,<br>Operation, InputMode`<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimensions for the<br>`PostText` operation:<br>• `BotName, BotVersion,<br>Operation`<br>• `BotName, BotAlias,<br>Operation`                                                                                                                                                                                                                                                                         |
| `RuntimeConcurrency`                                                                                                                    | The number of concurrent connections in<br>the specified time period.<br>`RuntimeConcurrency` is<br>reported as a<br>`StatisticSet`.<br>Valid dimensions for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• Operation, BotName, BotVersion,<br>InputMode<br>• Operation, BotName, BotAlias,<br>InputMode<br>Valid dimensions for other<br>operations:<br>• Operation, BotName,<br>BotVersion<br>• Operation, BotName,<br>BotAlias<br>Unit: Count                                                                                                                                                                                                                   |
| `RuntimeInvalidLambdaResponses`                                                                                                         | The number of invalid AWS Lambda (Lambda)<br>responses in the specified period.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`                                                                                                                                                                                                                                                                                                                                                                      |
| `RuntimeLambdaErrors`                                                                                                                   | The number of Lambda runtime errors in<br>the specified period.Valid<br>dimension for the `PostContent`<br>operation with the `Text` or<br>`Speech``InputMode` :<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`                                                                                                                                                                                                                                                                                                                                                                                          |
| `RuntimePollyErrors`                                                                                                                    | The number of invalid Amazon Polly responses in<br>the specified period.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`                                                                                                                                                                                                                                                                                                                                                                             |
| `RuntimeRequestCount`                                                                                                                   | The number of runtime requests in the<br>specified period.<br>Valid dimensions for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotVersion,<br>Operation, InputMode`<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimensions for the<br>`PostText` operation:<br>• `BotName, BotVersion,<br>Operation`<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                             |
| `RuntimeSucessfulRequestLatency`<br>ImportantThis metric is `RuntimeSucessfulRequestLatency` and not `RuntimeSuccessfulRequestLatency`. | The latency for successful requests<br>between the time that the request was made<br>and the response was passed back.<br>Valid dimensions for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotVersion,<br>Operation, InputMode`<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimensions for the<br>`PostText` operation:<br>• `BotName, BotVersion,<br>Operation`<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Milliseconds                                                                                                                                                                                                          |
| `RuntimeSystemErrors`                                                                                                                   | The number of system errors in the<br>specified period. The response code range<br>for a system error is 500 to 599.<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                                                                  |
| `RuntimeThrottledEvents`                                                                                                                | The number of throttled requests. Amazon Lex<br>throttles a request when it receives more<br>requests than the limit of transactions per<br>second set for your account. If the limit<br>set for your account is frequently exceeded,<br>you can request a limit increase. To request<br>an increase, see [AWS Service<br>Limits](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").<br>Valid dimension for the<br>`PostContent` operation with<br>the `Text` or `Speech`<br>`InputMode`:<br>• BotName, BotAlias, Operation,<br>InputMode<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count |
| `RuntimeUserErrors`                                                                                                                     | The number of user errors in the specified<br>period. The response code range for a user<br>error is 400 to 499.<br>Valid dimension for the<br>`PostContent` operation with<br>`Text` or `Speech`<br>`InputMode`:<br>• `BotName, BotAlias,<br>Operation, InputMode`<br>Valid dimension for the<br>`PostText` operation:<br>• `BotName, BotAlias,<br>Operation`<br>Unit: Count                                                                                                                                                                                                                                                                                                                          |

Amazon Lex runtime metrics use the `AWS/Lex` namespace,
and provide metrics in the following dimensions. You can group
metrics by dimensions in the CloudWatch console:

| Dimension                                      | Description                                                                                                                                    |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `BotName, BotAlias, Operation,<br>InputMode`   | Groups metrics by the bot's alias, the<br>bot's name, the operation<br>(`PostContent`), and by whether<br>the input was text or speech.        |
| `BotName, BotVersion, Operation,<br>InputMode` | Groups metrics by the bot's name, the<br>version of the bot, the operation<br>(`PostContent`), and by whether<br>the input was text or speech. |
| `BotName, BotVersion,<br>Operation`            | Groups metrics by the bot's name, the<br>bots version, and by the operation,<br>`PostText`.                                                    |
| `BotName, BotAlias,<br>Operation`              | Groups metrics by the bot's name, the<br>bot's alias, and by the operation,<br>`PostText`.                                                     |

## CloudWatch Metrics for Amazon Lex Channel Associations

A channel association is the association between Amazon Lex and a
messaging channel, such as Facebook. The following table
describes the Amazon Lex channel association metrics.

| Metric                              | Description                                                                                                                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BotChannelAuthErrors`              | The number of authentication errors<br>returned by the messaging channel in the<br>specified time period. An authentication<br>error indicates that the secret token<br>provided during channel creation is invalid<br>or has expired. |
| `BotChannelConfigurationErrors`     | The number of configuration errors in<br>the specified period. A configuration error<br>indicates that one or more configuration<br>entries for the channel are invalid.                                                               |
| `BotChannelInboundThrottledEvents`  | The number of times that messages that<br>were sent by the messaging channel were<br>throttled by Amazon Lex in the specified period.                                                                                                  |
| `BotChannelOutboundThrottledEvents` | The number of times that outbound<br>events from Amazon Lex to the messaging channel<br>were throttled in the specified time<br>period.                                                                                                |
| `BotChannelRequestCount`            | The number of requests made on a<br>channel in the specified time period.                                                                                                                                                              |
| `BotChannelResponseCardErrors`      | The number of times that Amazon Lex could<br>not post response cards in the specified<br>period.                                                                                                                                       |
| `BotChannelSystemErrors`            | The number of internal errors that<br>occurred in Amazon Lex for a channel in the<br>specified period.                                                                                                                                 |

Amazon Lex channel association metrics use the `AWS/Lex`
namespace, and provide metrics for the following dimension. You
can group metrics by dimensions in the CloudWatch console:

| Dimension                                      | Description                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `BotAlias, BotChannelName, BotName,<br>Source` | Group metrics by the bot's alias, the<br>channel name, the bot's name, and the<br>source of traffic. |

## CloudWatch Metrics

for Conversation Logs

Amazon Lex uses the following metrics for conversation
logging:

| Metric                                 | Description                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConversationLogsAudioDeliverySuccess` | The number of audio logs successfully<br>delivered to the S3 bucket in the specified<br>time period.<br>Units: Count                                                                                                                                                                                                                                             |
| `ConversationLogsAudioDeliveryFailure` | The number of audio logs that failed to<br>be delivered to the S3 bucket in the<br>specified time period. A delivery failure<br>indicates an error with the resources<br>configured for conversation logs. Errors can<br>include insufficient IAM permissions, an<br>inaccessible AWS KMS key, or an inaccessible<br>S3 bucket.Units:<br>Count                   |
| `ConversationLogsTextDeliverySuccess`  | The number of text logs successfully<br>delivered to CloudWatch Logs in the specified time<br>period.<br>Units: Count                                                                                                                                                                                                                                            |
| `ConversationLogsTextDeliveryFailure`  | The number of text logs that failed to<br>be delivered to CloudWatch Logs in the specified time<br>period. A delivery failure indicates an<br>error with the resources configured for<br>conversation logs. Errors can include<br>insufficient IAM permissions, an<br>inaccessible AWS KMS key, or an inaccessible<br>CloudWatch Logs log group.<br>Units: Count |

Amazon Lex conversation log metrics use the `AWS/Lex`
namespace, and provide metrics for the following dimensions. You
can group metrics by dimension in the CloudWatch console.

| Dimension    | Description                            |
| ------------ | -------------------------------------- |
| `BotAlias`   | Group metrics by the bot's<br>alias.   |
| `BotName`    | Group metrics by the bot's<br>name.    |
| `BotVersion` | Group metrics by the bot's<br>version. |
