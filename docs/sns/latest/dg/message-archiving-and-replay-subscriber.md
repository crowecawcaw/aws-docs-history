# Amazon SNS message replay for FIFO

topic subscribers

Amazon SNS replay allows topic subscribers to retrieve and redeliver archived messages from
the topic data store to a subscribed endpoint.

- Messages can be replayed immediately after the subscription is created.
- A replayed message retains the same content, `MessageId`, and
  `Timestamp` as the original.
- The message includes a `Replayed` attribute to indicate that it is
  a replayed message.
- To replay only specific messages, apply a filter policy to your
  subscription.
  For more on filtering messages, see [Filter
  replayed messages](#message-archiving-and-replay-subscription-filtering "#message-archiving-and-replay-subscription-filtering").

## Create a message

replay policy using the AWS Management Console

Use this option to create a new replay policy using the AWS Management Console.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Choose a topic subscription or create a new one. To learn more about
   creating subscriptions, see [Creating a subscription to an Amazon SNS
   topic](sns-create-subscribe-endpoint-to-topic.md "sns-create-subscribe-endpoint-to-topic.md").
3. To initiate the message replay, go to the **Replay**
   drop-down and choose **Start replay**.
4. From the **Replay timeframe** modal, make the following
   selections:
   1. **Choose replay start date and time** –
      Choose the **date** (YYYY/MM/DD format) and
      **time** (24-hour hh:mm:ss format) from which
      you want to start replaying archived messages. The start time should
      be later than the beginning of the approximated archive time.
   2. **(Optional) Choose replay end date and time**
      – Choose the **date** (YYYY/MM/DD format)
      and **time** (24-hour hh:mm:ss format) when you
      want to stop replaying archived messages.
   3. Choose **Start replay**.

5. (Optional) To **stop** a message replay, go
   to the **Subscription details** page and choose
   **Stop replay** from the **Replay**
   drop-down.
6. (Optional) To **monitor** message replay
   metrics from within this workflow using CloudWatch, see [Monitor
   message replay metrics using Amazon CloudWatch](#message-archiving-and-replay-subscription-cloudwatch "#message-archiving-and-replay-subscription-cloudwatch").

**To view and edit a message replay policy**

You can perform the following actions from the **Subscription
details** page:

- To **view** the message replay status, the
  **Replay status** field displays the following
  values:
  - **Completed** – The replay has
    successfully redelivered all messages, and is now delivering newly
    published messages.
  - **In progress** – The replay is currently
    replaying the selected messages.
  - **Failed** – The replay was unable to
    complete.
  - **Pending** – The default state while the
    replay initiates.

- (Optional) To **modify** a message replay
  policy, go to the **Subscription details** page and choose
  **Start replay** from the **Replay**
  drop-down. Starting a replay will replace the existing replay.

## Add a replay policy

to the subscription using the API

To replay archived messages use the attribute `ReplayPolicy`.
`ReplayPolicy` can be used with the `Subscribe` and
`SetSubscriptionAttributes` API actions. This policy has the
following values:

- **`StartingPoint`** (Required)
  – Signals where to start replaying messages from.
- **`EndingPoint`** (Optional)
  – Signals when to stop replaying messages. If
  `EndingPoint` is omitted, then the replay will continue until
  caught up to the current time.
- **`PointType`** (Required)
  – Sets the type of starting and ending points. Currently, the
  supported value for `PointType` is `Timestamp`.

For example, to recover from a downstream failure and resend all messages for a
two hour time period on October 1, 2023, use the
`SetSubscriptionAttributes` API action to set a
`ReplayPolicy` as follows:

```
`{
 "PointType":"Timestamp",
 "StartingPoint":"2023-10-01T10:00:00.000Z",
 "EndingPoint":"2023-10-01T12:00:00.000Z"
}`
```

To replay all messages sent to the topic as of October 1, 2023, and continue
receiving all newly published messages to your topic, use the
`SetSubscriptionAttributes` API action to set a
`ReplayPolicy` on your subscription as follows:

```
`{
 "PointType":"Timestamp",
 "StartingPoint":"2023-10-01T00:00:00.000Z"
}`
```

To verify that a message has been replayed, the boolean attribute
`Replayed` is added to each replayed message.

## Add a replay policy to the subscription using

the SDK

To use an AWS SDK, you must configure it with your credentials. For
more information, see [Shared `config` and
`credentials` files](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md") in the _AWS SDKs and Tools Reference Guide_.

The following code example shows how to set the `ReplayPolicy` on a
subscription to redeliver messages from the Amazon SNS FIFO topic's archive for a 2-hour
time window on October 1st 2023.

```
// Specify the ARN of the Amazon SNS subscription to initiate the ReplayPolicy on.
String subscriptionArn =
    "arn:aws:sns:us-east-2:123456789012:MyArchiveTopic.fifo:1d2a3e9d-7f2f-447c-88ae-03f1c68294da";

// Set the ReplayPolicy to replay messages from the topic's archive
// for a 2 hour time period on October 1st 2023 between 10am and 12pm UTC.
String replayPolicy =
    "{\"PointType\":\"Timestamp\",\"StartingPoint\":\"2023-10-01T10:00:00.000Z\",\"EndingPoint\":\"2023-10-01T12:00:00.000Z\"}";

// Set the ArchivePolicy for the Amazon SNS topic
SetSubscriptionAttributesRequest request = new SetSubscriptionAttributesRequest()
    .withSubscriptionArn(subscriptionArn)
    .withAttributeName("ReplayPolicy")
    .withAttributeValue(replayPolicy);
sns.setSubscriptionAttributes(request);
```

## Understanding

the EndingPoint

When you apply a `ReplayPolicy` to an Amazon SNS subscription, the
`EndingPoint` value is optional. If no `EndingPoint` is
provided, the replay will start from the specified `StartingPoint` and
continue until it catches up to the current time, including processing any newly
published messages. Once caught up, the subscription will function as a regular
subscription, receiving new messages as they are published.

If an `EndingPoint` is specified, the service will replay messages from
the `StartingPoint` up to the `EndingPoint` and then stop.
**This action effectively pauses the
subscription.** While the subscription is paused, newly published
messages will not be delivered to the subscribed endpoint.

To resume message delivery, apply a new `ReplayPolicy` without
providing an `EndingPoint`, and set the `StartingPoint` to the
desired point in time from which to continue receiving messages. For example, to
resume a subscription from where a prior replay finished, set the new
`StartingPoint` to the previously provided
`EndingPoint`.

## Filter

replayed messages

Amazon SNS message filtering let's you control the replayed messages that Amazon SNS replays
to your subscriber endpoint. When message filtering and message archiving are both
enabled, Amazon SNS first retrieves the message from the topic’s data store, then applies
the message against the subscription’s `FilterPolicy`. The message is
delivered to the subscribed endpoint when there is a match, otherwise message is
filtered out. For more information, see [Amazon SNS subscription filter
policies](sns-subscription-filter-policies.md "sns-subscription-filter-policies.md").

## Monitor

message replay metrics using Amazon CloudWatch

You can monitor replay messages using Amazon CloudWatch using the following metrics. To be
notified of anomalies in your workloads and help avoid impact, you can configure
Amazon CloudWatch alarms on these metrics. For more details, see [Logging and monitoring in Amazon SNS](sns-logging-monitoring.md "sns-logging-monitoring.md").

| Metric                                     | Description                                                                                                                                   |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **NumberOfReplayedNotificationsDelivered** | Provides the subscriber with the aggregate number of messages replayed from the topic archive, at 1-minute resolution.                        |
| **NumberOfReplayedNotificationsFailed**    | Provides the subscriber with the aggregate number of messages replayed that failed to deliver from the topic archive, at 1-minute resolution. |
