# Amazon RDS event notification tags and

attributes

When Amazon RDS sends an event notification to Amazon Simple Notification Service (SNS) or Amazon EventBridge, the notification
contains message attributes and event tags. RDS sends the message attributes separately
along with the message, while the event tags are in the body of the message. Use the message
attributes and the Amazon RDS tags to add metadata to your resources. You can modify these tags
with your own notations about the DB instances. For more information about tagging Amazon RDS resources, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").

By default, the Amazon SNS and Amazon EventBridge receives every message sent to them. SNS and EventBridge can
filter the message and send the notifications to the preferred communication mode, such as
an email, a text message, or a call to an HTTP endpoint.

###### Note

The notification sent in an email or a text message will not have event tags.

The following table shows the message attributes for RDS events sent to the topic
subscriber.

| Amazon RDS event attribute | Description                                                                                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| EventID                    | Identifier for the RDS event message, for example,<br>RDS-EVENT-0006.                                                            |
| Resource                   | The ARN identifier for the resource emitting the event, for example,<br>`arn:aws:rds:ap-southeast-2:123456789012:db:database-1`. |

The RDS tags provide data about the resource that was affected by the service event. RDS
adds the current state of the tags in the message body when the notification is sent to SNS
or EventBridge.

For more information about filtering message attributes for SNS, see [Amazon SNS message filtering](../../../sns/latest/dg/sns-message-filtering.md "../../../sns/latest/dg/sns-message-filtering.md") in the
_Amazon Simple Notification Service Developer Guide_.

For more information about filtering event tags for EventBridge, see [Comparison operators for use in event patterns in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md "../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md") in the _Amazon
EventBridge User Guide_.

For more information about filtering payload-based tags for SNS, see [Introducing payload-based message filtering for Amazon SNS](https://aws.amazon.com/blogs/compute/introducing-payload-based-message-filtering-for-amazon-sns/ "https://aws.amazon.com/blogs/compute/introducing-payload-based-message-filtering-for-amazon-sns/")
