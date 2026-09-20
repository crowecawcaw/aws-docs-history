

# Publishing large messages with Amazon SNS
<a name="large-message-payloads"></a>

Amazon SNS supports message payloads up to 1 MiB (1,048,576 bytes) when you configure the `MaximumMessageSize` topic attribute. By default, topics accept messages up to 256 KiB. Topics with `MaximumMessageSize` set above 256 KiB support Amazon Data Firehose, Amazon SQS, and AWS Lambda subscriptions, with up to 100 total subscriptions per topic.

## How publishing large messages works
<a name="large-messages-how-it-works"></a>

You can set the `MaximumMessageSize` topic attribute to any integer value between 1,024 and 1,048,576 bytes. By default, all existing and newly created topics have a `MaximumMessageSize` of 262,144 bytes (256 KiB).

When you publish a message, Amazon SNS validates the combined size of the message body and message attributes against the topic's configured `MaximumMessageSize`. If the combined size exceeds the limit, Amazon SNS returns an `InvalidParameter` error on publish.

## Supported configuration
<a name="large-messages-supported-configuration"></a>

When you set `MaximumMessageSize` above 256 KiB, Amazon SNS supports the following configuration.

**Subscription limits**

The topic supports up to 100 total subscriptions. If you attempt to create additional subscriptions, Amazon SNS returns an `InvalidParameter` error.

**Supported endpoint types**

Topics with `MaximumMessageSize` above 256 KiB support the following endpoint types:
+ Amazon Data Firehose
+ Amazon SQS
+ AWS Lambda

Topics with `MaximumMessageSize` at 256 KiB or below also support HTTP/HTTPS, SMS, email, email-json, and mobile push (application) endpoints.

## Setting MaximumMessageSize on existing topics
<a name="large-messages-existing-topics"></a>

You can increase or decrease a topic's `MaximumMessageSize` at any time. After you change the value, Amazon SNS validates new publish requests against the updated limit.

To set `MaximumMessageSize` above 256 KiB, the topic must have 100 or fewer total subscriptions, all of which must be supported endpoint types (Amazon Data Firehose, Amazon SQS, or AWS Lambda). If the topic has unsupported endpoint types or more than 100 subscriptions, Amazon SNS returns an `InvalidParameter` error.

## Configuring your topic for large messages
<a name="large-messages-configuring"></a>

### Using the AWS Management Console
<a name="large-messages-console"></a>

**To configure your topic to publish larger messages**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/home](https://console.aws.amazon.com/sns/home).

1. In the left navigation pane, choose **Topics**.

1. Select your topic and choose **Edit**.

1. Under **Maximum message size**, set your desired limit (up to 1,024 KiB).

1. Choose **Save changes**.

### Using the AWS CLI
<a name="large-messages-cli"></a>

Set `MaximumMessageSize` when creating a new topic:

```
aws sns create-topic \
    --name my-large-message-topic \
    --attributes MaximumMessageSize=1048576
```

Replace `my-large-message-topic` with your topic name and `1048576` with your desired maximum message size in bytes.

Set `MaximumMessageSize` on an existing topic:

```
aws sns set-topic-attributes \
    --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
    --attribute-name MaximumMessageSize \
    --attribute-value 1048576
```

Replace `arn:aws:sns:us-east-1:123456789012:my-topic` with the ARN of your topic and `1048576` with your desired maximum message size in bytes.

Verify your topic's current `MaximumMessageSize`. If the attribute has not been explicitly set, it does not appear in the response, and the topic uses the default of 262,144 bytes (256 KiB).

```
aws sns get-topic-attributes \
    --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```

## Amazon SNS API reference for large messages
<a name="large-messages-api-reference"></a>

Large message support uses existing Amazon SNS APIs. You don't need new API operations.


| API | Change | 
| --- | --- | 
| CreateTopic | Accepts MaximumMessageSize in the Attributes parameter. Valid range: 1,024–1,048,576 bytes. | 
| SetTopicAttributes | Accepts MaximumMessageSize as an attribute name. | 
| GetTopicAttributes | Returns MaximumMessageSize if the attribute has been explicitly set. If not returned, the topic uses the default of 262,144 bytes (256 KiB). | 
| Publish | Validates the combined size of the message body and message attributes against the topic's MaximumMessageSize. | 
| PublishBatch | Validates the combined size of all messages in the batch (each message's body and attributes) against the topic's MaximumMessageSize. | 

## Endpoint compatibility
<a name="large-messages-endpoint-compatibility"></a>

The following list describes how Amazon SNS delivers your large messages to each supported endpoint type.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) – Amazon Data Firehose loads streaming data into data stores and analytics services. It supports records up to 1,000 KiB (1,024,000 bytes). The delivered message must stay below this limit. The limit includes Amazon SNS delivery metadata, such as the message ID and timestamp. Messages that exceed the limit fail delivery. A topic's `MaximumMessageSize` can be set up to 1,024 KiB (1,048,576 bytes). For this reason, we recommend that you set a lower `MaximumMessageSize` for topics with Firehose subscriptions. For the current record size limit, see [Amazon Data Firehose quotas](https://docs.aws.amazon.com/firehose/latest/dev/limits.html).
+ [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) – Amazon SNS can deliver a message to a subscribed Amazon SQS queue up to the Amazon SQS maximum supported message size. The queue's own `MaximumMessageSize` does not apply to messages from Amazon SNS. The Amazon SNS topic's `MaximumMessageSize` is the effective size limit for these messages.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Amazon SNS invokes AWS Lambda functions asynchronously. AWS Lambda supports asynchronous invocation payloads up to 1 MiB. No additional configuration is required for AWS Lambda subscriptions.

## Best practices
<a name="large-messages-best-practices"></a>

### Configure dead-letter queues
<a name="large-messages-bp-dlq"></a>

We recommend configuring a dead-letter queue (DLQ) on all subscriptions to handle failed message delivery. A DLQ captures messages that Amazon SNS can't successfully deliver to the subscribed endpoint, allowing you to inspect and reprocess them. For more information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md).

### Monitor with CloudWatch metrics and alarms
<a name="large-messages-bp-monitoring"></a>

Use CloudWatch metrics to monitor message delivery and set alarms on failed deliveries. The `NumberOfNotificationsFailed` metric tracks messages that Amazon SNS can't deliver to subscribed endpoints. Create a CloudWatch alarm on this metric to receive alerts when delivery failures occur. For more information, see [Monitoring Amazon SNS topics using CloudWatch](sns-monitoring-using-cloudwatch.md).

### Publishing messages larger than 1 MiB with Amazon S3
<a name="large-messages-bp-s3"></a>

To publish messages larger than 1 MiB, use the [Amazon SNS Extended Client Library for Java](https://github.com/awslabs/amazon-sns-java-extended-client-lib/) or the [Amazon SNS Extended Client Library for Python](https://github.com/awslabs/amazon-sns-python-extended-client-lib) to store payloads in Amazon S3 and publish a reference through Amazon SNS. These libraries support messages up to 2 GB and are compatible with both Standard and FIFO topics. For instructions on increasing `MaximumMessageSize` before choosing this approach, see [Configuring your topic for large messages](#large-messages-configuring).