# Amazon SNS message archiving for

FIFO topic owners

Message archiving provides the ability to archive a single copy of all messages
published to your topic. You can store published messages within your topic by enabling
the message archive policy on the topic, which enables message archiving for all
subscriptions linked to that topic. Messages can be archived for a minimum of one day to
a maximum of 365 days.

Additional charges apply when setting an archive policy. For pricing information, see
[Amazon SNS pricing](https://aws.amazon.com/sns/pricing/ "https://aws.amazon.com/sns/pricing/").

## Create a message

archive policy using the AWS Management Console

Use this option to create a new message archive policy using the
AWS Management Console.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Choose a topic or create a new one. To learn more about creating topics,
   see [Creating an Amazon SNS topic](sns-create-topic.md "sns-create-topic.md").

###### Note

Amazon SNS message archiving and replay is only available for
application-to-application (A2A) FIFO topics. 3. On the **Edit topic** page, expand the **Archive
policy** section. 4. Enable the **Archive policy** feature, and enter the
**number of days** for which you want to archive
messages in the topic. 5. Choose **Save changes**.

**To view, edit, and deactivate a message archiving topic
policy**

- On the **Topic details** page, the **Retention
  policy** displays the status of the archive policy, including
  the number of days for which it is set. Select the **Archive
  policy** tab to view the following message archive
  details:
  - **Status** – The archive and replay status
    appears as **active** when an archive policy is
    applied. The archive and replay status appears as
    **inactive** when the archive policy is set to
    an empty JSON object.
  - **Message retention period** – The
    specified number of days for message retention.
  - **Archive start date** – The date from
    which subscribers can replay messages.
  - **JSON preview** – The JSON preview of the
    archive policy.

- (Optional) To **edit** an archive policy, go
  to the topic summary page and choose **Edit**.
- (Optional) To **deactivate** an archive
  policy, go to the topic summary page and choose **Edit**.
  Deactivate the **Archive Policy** and choose **Save
  changes**.
- (Optional) To **delete** a topic with an
  archive policy, you must first deactivate the archive policy as previously
  described.

###### Important

To avoid accidental message deletions, you can not delete a topic with
an active message archive policy. The topic's message archive policy
must be deactivated before the topic can be deleted. When you deactivate
a message archive policy, Amazon SNS deletes all of the archived messages.
When deleting a topic, subscriptions are removed, and any messages in
transit may not be delivered.

## Create a message archive

policy using the API

To create a message archive policy using the API, you need to add the attribute
`ArchivePolicy` to your topic. You can set an
`ArchivePolicy` using the API actions `CreateTopic` and
`SetTopicAttributes`. `ArchivePolicy` has a single value,
`MessageRetentionPeriod`, which represents the number of days Amazon SNS
retains messages. To activate message archiving for your topic, set the
`MessageRetentionPeriod` to an integer value greater than zero. For
example, to retain messages in your archive for 30 days, set the
`ArchivePolicy` to:

```
`{
 "ArchivePolicy": {
 "MessageRetentionPeriod": "30"
 }
}`
```

To disable message archiving for your topic, and clear the archive, unset the
`ArchivePolicy`, as follows:

```
`{}`
```

## Create a message archive

policy using the SDK

To use an AWS SDK, you must configure it with your credentials. For
more information, see [Shared `config` and
`credentials` files](../../../sdkref/latest/guide/file-format.md "../../../sdkref/latest/guide/file-format.md") in the _AWS SDKs and Tools Reference Guide_.

The following code example shows how to set the `ArchivePolicy` for an
Amazon SNS topic to retain all messages published to the topic for 30 days.

```
// Specify the ARN of the Amazon SNS topic to set the ArchivePolicy for.
String topicArn =
    "arn:aws:sns:us-east-2:123456789012:MyArchiveTopic.fifo";

// Set the MessageRetentionPeriod to 30 days for the ArchivePolicy.
String archivePolicy =
    "{\"MessageRetentionPeriod\":\"30\"}";

// Set the ArchivePolicy for the Amazon SNS topic
SetTopicAttributesRequest request = new SetTopicAttributesRequest()
    .withTopicArn(topicArn)
    .withAttributeName("ArchivePolicy")
    .withAttributeValue(archivePolicy);
sns.setTopicAttributes(request);
```

## Create a message archive

policy using CloudFormation

To create an archive policy using CloudFormation see [`AWS::SNS::Topic`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md") in the
_AWS CloudFormation User Guide_.

## Grant access to an

encrypted archive

Before a subscriber can begin replaying messages from an encrypted topic, you must
complete the following steps. Because past messages are replayed, Amazon SNS needs to be
provisioned `Decrypt` access to the KMS key that was used to encrypt
the messages in the archive.

1. When you encrypt messages with a KMS key and store them within the
   topic, you must grant Amazon SNS the ability to decrypt these messages via Key
   Policy. For more, see [Grant
   decrypt permissions to Amazon SNS](#message-archiving-and-replay-topic-decrypt-permissions "#message-archiving-and-replay-topic-decrypt-permissions").
2. Enable AWS KMS for Amazon SNS. For more, see [Configuring AWS KMS permissions](sns-key-management.md#sns-what-permissions-for-sse "sns-key-management.md#sns-what-permissions-for-sse").

###### Important

When you add the new sections to your KMS key policy, do not change any
existing sections in the policy. If encryption is enabled on a topic, and the
KMS key is disabled or deleted, or the KMS key policy is not correctly
configured for Amazon SNS, Amazon SNS cannot replay messages to your subscribers.

### Grant

decrypt permissions to Amazon SNS

In order for Amazon SNS to access encrypted messages from within your topic’s
archive and replay them to subscribed endpoints, you must enable the Amazon SNS
service principle to decrypt these messages.

The following is an example policy that is required to allow the Amazon SNS service
principal to decrypt stored messages during a replay of historical messages from
within your topic.

```
{
    "Sid": "Allow SNS to decrypt archived messages",
    "Effect": "Allow",
    "Principal": {
        "Service": "sns.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*"
}
```

## Monitor message

archive metrics using Amazon CloudWatch

You can monitor archived messages using Amazon CloudWatch using the following metrics. To
be notified of anomalies in your workloads and help avoid impact, you can configure
Amazon CloudWatch alarms on these metrics. For more details, see [Logging and monitoring in Amazon SNS](sns-logging-monitoring.md "sns-logging-monitoring.md").

| Metric                                  | Description                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **ApproximateNumberOfMessagesArchived** | Provides the topic owner with the aggregate number of messages<br>archived in the topic archive, at 60-minute resolution.                      |
| **ApproximateNumberOfBytesArchived**    | Provides the topic owner with the aggregate number of bytes<br>archived, across all messages in the topic archive, at 60-minute<br>resolution. |
| **NumberOfMessagesArchiveProcessing**   | Provides the topic owner with the number of messages saved to<br>the topic archive during the interval in 1-minute<br>resolution.              |
| **NumberOfBytesArchiveProcessing**      | Provides the topic owner with the aggregate number of bytes<br>saved to the topic archive during the interval in 1-minute<br>resolution.       |

The `GetTopicAttributes` API has a `BeginningArchiveTime`
property, which represents the oldest timestamp at which a subscriber can start a
replay. The following represents a sample response for this API action:

```
{
 "ArchivePolicy": {
    "MessageRetentionPeriod": "`<integer>`"
  },
  "BeginningArchiveTime": "`<timestamp>`",
  ...
}
```
