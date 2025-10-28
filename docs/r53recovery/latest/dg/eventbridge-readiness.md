# Using readiness check in ARC with Amazon EventBridge

Using Amazon EventBridge, you can set up event-driven rules that monitor your readiness check resources in Amazon Application Recovery Controller (ARC),
and then initiate target actions that use other AWS services. For
example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic when a readiness check status
changes from **READY** to **NOT READY**.

###### Note

ARC only publishes EventBridge events for readiness check in the US West (Oregon) (us-west-2) AWS Region.
To receive EventBridge events for readiness check, create EventBridge rules in the US West (Oregon) Region.

You can create rules in Amazon EventBridge to act on the following ARC readiness check event:

- _Readiness check readiness._ The event specifies if readiness check status changes, for example, from
  **READY** to **NOT READY**.
  To capture specific ARC events that you're interested in, define event-specific patterns that EventBridge can use to detect the events.
  Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides
  the values that you're looking for.

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time
under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md").

## Monitor a readiness check resource with EventBridge

With EventBridge, you can create rules that define actions to take when ARC emits
events for readiness check resources.

To type or copy and paste an event pattern into the EventBridge console, in the console, select to the option
**Enter my own** option. To help you determine event patterns that might be useful for you, this topic
includes [example readiness event patterns](#arc-eventbridge-examples-readiness "#arc-eventbridge-examples-readiness").

###### To create a rule for a resource event

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. For the AWS Region to create the rule in, choose US West (Oregon). This is the required Region for readiness events.
3. Choose **Create rule**.
4. Enter a **Name** for the rule, and, optionally, a description.
5. For **Event bus**, leave the default value, **default**.
6. Choose **Next**.
7. For the **Build event pattern** step, for **Event source**, leave
   the default value, **AWS events**.
8. Under **Sample event**, choose **Enter my own**.
9. For **Sample events**, type or copy and paste an event pattern. For examples, see the next section.

## Example readiness event patterns

Event patterns have the same structure
as the events that they match. The pattern quotes the fields that you want to match and provides the values that
you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that you can use
to monitor ARC actions and resources.

The following event patterns provide examples that you might use in EventBridge for
the readiness check capability in ARC.

- _Select all events from ARC readiness check_.

```
{
    "source": [
        "aws.route53-recovery-readiness"
    ]
}
```

- _Select only events related to cells_.

```
{
    "source": [
        "aws.route53-recovery-readiness"
    ],
    "detail-type": [
        "Route 53 Application Recovery Controller cell readiness status change"
    ]
}
```

- _Select only events related to a specific cell called `MyExampleCell`_.

```
{
    "source": [
        "aws.route53-recovery-readiness"
    ],
    "detail-type": [
        "Route 53 Application Recovery Controller cell readiness status change"
    ],
    "resources": [
        "arn:aws:route53-recovery-readiness::111122223333:cell/MyExampleCell"
    ]
}
```

- _Select only events when any recovery group, cell, or readiness check status becomes `NOT READY`_.

```
{
   "source":[
      "aws.route53-recovery-readiness"
   ],
   "detail-type":{
      "new-state":{
         "readiness-status":[
            "NOT_READY"
         ]
      }
   }
}
```

- _Select only events when any recovery group, cell, or readiness check becomes anything except `READY`_

```
{
   "source":[
      "aws.route53-recovery-readiness"
   ],
   "detail":{
      "new-state":{
         "readiness-status":[
            {
               "anything-but":"READY"
            }
         ]
      }
   }
}
```

The following is an example ARC event for a _recovery group readiness status change_:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller recovery group readiness status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:recovery-group/BillingApp"
    ],
    "detail": {
        "recovery-group-name": "BillingApp",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

The following is an example ARC event for a _cell readiness status change_:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller cell readiness status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:cell/PDXCell"
    ],
    "detail": {
        "cell-name": "PDXCell",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

The following is an example ARC event for a _readiness check status change_:

```
{
    "version": "0",
    "account":"111122223333",
    "detail-type":"Route 53 Application Recovery Controller readiness check status change",
    "source":"route53-recovery-readiness.amazonaws.com",
    "time":"2020-11-03T00:31:54Z",
    "id": "1234a678-1b23-c123-12fd3f456e78",
    "region": "us-west-2",
    "resources":[
        "arn:aws:route53-recovery-readiness::111122223333:readiness-check/UserTableReadinessCheck"
    ],
    "detail": {
    "readiness-check-name": "UserTableReadinessCheck",
        "previous-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        },
        "new-state": {
            "readiness-status": "READY|NOT_READY|UNKNOWN|NOT_AUTHORIZED"
        }
    }
}
```

## Specify a CloudWatch log group to use as a target

When you create an EventBridge rule, you must specify the target
where events that are matched to the rule are sent. For a list of available targets for EventBridge,
see [Targets available in the EventBridge console](../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets "../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets").
One of the targets that you can add to an EventBridge rule is an Amazon CloudWatch log group. This section describes
the requirements for adding CloudWatch log groups as targets, and provides a procedure for adding a
log group when you create a rule.

To add a CloudWatch log group as a target, you can do one of the following:

- Create a new log group
- Choose an existing log group

If you specify a new log group using the console when you create a rule, EventBridge automatically creates the
log group for you. Make sure that the log group that you use as a target for the EventBridge rule starts with `/aws/events`.
If you want to choose an existing log group, be aware that only log groups that
start with `/aws/events` appear as options in the drop-down menu. For more information, see
[Create a new log group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#Create-Log-Group")
in the _Amazon CloudWatch User Guide_.

If you create or use a CloudWatch log group to use as a target using CloudWatch operations outside of the
console, make sure that you set permissions correctly. If you use the console to add a log group to an EventBridge
rule, then the resource-based policy for the log group is updated automatically. But, if you use the
AWS Command Line Interface or an AWS SDK to specify a log group, then you must update resource-based policy for the log group.
The following example policy illustrates the permissions that you must define in a resource-based policy
for the log group:

JSON

```
`{
 "Version":"2012-10-17",

 "Statement": [
 {
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "events.amazonaws.com",
 "delivery.logs.amazonaws.com"
 ]
 },
 "Resource": "arn:aws:logs:us-east-1:`222222222222`:log-group:/aws/events/*:*",
 "Sid": "TrustEventsToStoreLogEvent"
 }
 ]
}`

```

You can't configure a resource-based policy for a log group by using the console. To add the required permissions
to a resource-based policy, use the CloudWatch [PutResourcePolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.md")
API operation. Then, you can use the [describe-resource-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-resource-policies.html") CLI command to check that your policy was applied correctly.

###### To create a rule for a resource event and specify a CloudWatch log group target

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Choose the AWS Region that you want to create the rule in.
3. Choose **Create rule** and then enter any information about that
   rule, such as the event pattern or schedule details.

For more information about creating EventBridge rules for readiness, see [Monitor a readiness check resource with EventBridge](#RCEventBridgeCreateRule "#RCEventBridgeCreateRule"). 4. On the **Select target** page, choose **CloudWatch** as your
target. 5. Choose a CloudWatch log group from the drop-down menu.
