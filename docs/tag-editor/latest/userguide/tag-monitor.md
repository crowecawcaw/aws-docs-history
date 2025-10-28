# Monitor tag changes with serverless workflows and

Amazon EventBridge

Amazon EventBridge supports tag changes on AWS resources. Using this EventBridge type, you can build EventBridge
rules to match tag changes and route the events to one or more targets. For example, a
target might be an AWS Lambda function to invoke automated workflows. This topic provides a
tutorial for using Lambda to build a cost-effective serverless solution to securely process
tag changes on your AWS resources.

## Tag changes generate EventBridge events

EventBridge delivers a near real-time stream of system events that describe changes in AWS
resources. Many AWS resources support tags, which are custom, user-defined attributes
to easily organize and categorize AWS resources. Common use cases for tags are cost
allocation categorization, access-control security, and automation.

With EventBridge, you can monitor for changes to tags and track the tag state on AWS
resources. Previously, to achieve similar functionality, you might have continuously
polled APIs and orchestrated multiple calls. Now, any change to a tag including
individual service APIs, [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md"), and the [Tagging API](../../../resourcegroupstagging/latest/APIReference/index.md "../../../resourcegroupstagging/latest/APIReference/index.md") will initiate the tag change on resource event. The following
example shows a typical EventBridge event prompted by a tag change. It shows the new, updated,
or deleted tag keys, and their associated values.

```
{
  "version": "0",
  "id": "bddcf1d6-0251-35a1-aab0-adc1fb47c11c",
  "detail-type": "Tag Change on Resource",
  "source": "aws.tag",
  "account": "123456789012",
  "time": "2018-09-18T20:41:38Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ec2:us-east-1:123456789012:instance/i-0000000aaaaaaaaaa"
  ],
  "detail": {
    "changed-tag-keys": [
      "a-new-key",
      "an-updated-key",
      "a-deleted-key"
    ],
    "tags": {
      "a-new-key": "tag-value-on-new-key-just-added",
      "an-updated-key": "tag-value-was-just-changed",
      "an-unchanged-key": "tag-value-still-the-same"
    },
    "service": "ec2",
    "resource-type": "instance",
    "version": 3,
  }
}
```

All EventBridge events have the same top-level fields:

- **version** – By default, this value is
  set to `0` (zero) in all events.
- **id** – A unique value is generated for
  every event. This can be helpful in tracing events as they move through rules to
  targets and are processed.
- **detail-type** – Identifies, in
  combination with the `source` field, the fields and values that
  appear in the detail field.
- **source** – Identifies the service that
  was the source of the event. The source for tag changes is
  `aws.tag`.
- **time** – The timestamp of the
  event.
- **region** – Identifies the AWS Region
  where the event originated.
- **resources** – This JSON array contains
  Amazon Resource Names (ARNs) that identify resources that are involved in the
  event. This is the resource where tags have changed.
- **detail** – A JSON object, whose content
  is different depending on event type. For tag change on resource, the following
  detailed fields are included:
  - **changed-tag-keys** – The tag
    keys that changed by this event.
  - **service** – The service that the
    resource belongs to. In this example, the service is `ec2`,
    which is Amazon EC2.
  - **resource-type** – The type of
    resource of the service. In this example, it is an Amazon EC2
    instance.
  - **version** – The version of the
    tag set. The version starts at 1 and increments when tags are changed.
    You can use the version to verify the order of tag change events.
  - **tags** – The tags attached to
    the resource after the change.

For more information, see [Amazon EventBridge event
patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge User Guide_.

By using EventBridge, you can create rules that match specific event patterns based on the
different fields. We demonstrate how to do this in the tutorial. Also, we show how an
Amazon EC2 instance can be stopped automatically if a specified tag isn’t attached to the
instance. We use the EventBridge fields to create a pattern to match the tag events for the
instance that launches a Lambda function.

## Lambda and serverless

AWS Lambda follows the serverless paradigm to run code in the cloud. You run code only
when it’s needed, without thinking about servers. You pay only for the exact compute
time you use. Even though it’s called _serverless_, it doesn’t mean
that there are no servers. Serverless in this context means that you don’t have to
provision, configure, or manage the servers that are used to run your code. AWS does
all of that for you, so you can focus on your code. For more information about Lambda,
see the [AWS Lambda Product Overview](https://aws.amazon.com/lambda "https://aws.amazon.com/lambda").
