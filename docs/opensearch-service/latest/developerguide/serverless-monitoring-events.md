# Monitoring OpenSearch Serverless events using Amazon EventBridge

Amazon OpenSearch Service integrates with Amazon EventBridge to notify you of certain events that affect your
domains. Events from AWS services are delivered to EventBridge in near real time. The same events
are also sent to [Amazon CloudWatch Events](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatchEvents.md"), the
predecessor of Amazon EventBridge. You can write rules to indicate which events are of interest to you,
and what automated actions to take when an event matches a rule. Examples of actions that you
can automatically activate include the following:

- Invoking an AWS Lambda function
- Invoking an Amazon EC2 Run Command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic or an Amazon SQS queue
  For more information, see [Get started with
  Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User
  Guide_.

## Setting up notifications

You can use [AWS User Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md")
to receive notifications when an OpenSearch Serverless event occurs. An event is an indicator of a change
in OpenSearch Serverless environment, such as when you reach the maximum limit of your OCU usage.
Amazon EventBridge receives the event and routes a notification to the AWS Management Console
Notifications Center and your chosen delivery channels. You receive a notification when an
event matches a rule that you specify.

## OpenSearch Compute Units (OCU) events

OpenSearch Serverless sends events to EventBridge when one of the following OCU-related events occur.

### OCU usage approaching maximum

limit

OpenSearch Serverless sends this event when your search or index OCU usage reaches 75% of your
capacity limit. Your OCU usage is calculated based on your configured capacity limit and
your current OCU consumption.

**Example**

The following is an example event of this type (search OCU):

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "OCU Utilization Approaching Max Limit",
  "source": "aws.aoss",
  "account": "123456789012",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": ["arn:aws:es:us-east-1:123456789012:domain/test-domain"],
  "detail": {
    "eventTime" : 1678943345789,
    "description": "Your search OCU usage is at 75% and is approaching the configured maximum limit."
  }
}
```

The following is an example event of this type (index OCU):

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "OCU Utilization Approaching Max Limit",
  "source": "aws.aoss",
  "account": "123456789012",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": ["arn:aws:es:us-east-1:123456789012:domain/test-domain"],
  "detail": {
    "eventTime" : 1678943345789,
    "description": "Your indexing OCU usage is at 75% and is approaching the configured maximum limit."
  }

```

### OCU usage reached maximum

limit

OpenSearch Serverless sends this event when your search or index OCU usage reaches 100% of your
capacity limit. Your OCU usage is calculated based on your configured capacity limit and
your current OCU consumption.

**Example**

The following is an example event of this type (search OCU):

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "OCU Utilization Reached Max Limit",
  "source": "aws.aoss",
  "account": "123456789012",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": ["arn:aws:es:us-east-1:123456789012:domain/test-domain"],
  "detail": {
    "eventTime" : 1678943345789,
    "description": "Your search OCU usage has reached the configured maximum limit."
  }
}
```

The following is an example event of this type (index OCU):

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-012345678901",
  "detail-type": "OCU Utilization Reached Max Limit",
  "source": "aws.aoss",
  "account": "123456789012",
  "time": "2016-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": ["arn:aws:es:us-east-1:123456789012:domain/test-domain"],
  "detail": {
    "eventTime" : 1678943345789,
    "description": "Your indexing OCU usage has reached the configured maximum limit."
  }
}
```
