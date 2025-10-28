# Using Region switch in ARC with Amazon EventBridge

Using Amazon EventBridge, you can set up event-driven rules that monitor your Region switch resources in Amazon Application Recovery Controller (ARC),
and then initiate target actions that use other AWS services. For
example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic whenever a Region switch
plan completes execution.

You can create rules in Amazon EventBridge to act on the following ARC Region switch events:

- _Region switch plan execution._ The event specifies that a Region switch plan has been run (executed).
- _Region switch plan evaluation._ The event specifies that a Region switch plan evaluation has completed.
  To capture specific ARC events that you're interested in, define event-specific patterns that EventBridge can use to detect the events.
  Event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides
  the values that you're looking for.

Events are emitted on a best effort basis. They're delivered from ARC to EventBridge in near real-time
under normal operational circumstances. However, situations can arise that might delay or prevent delivery of an event.

For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md").

## Monitor a Region switch resource with EventBridge

With EventBridge, you can create rules that define actions to take when ARC emits
events for Region switch resources.

To type or copy and paste an event pattern into the EventBridge console, in the console, select to the option
**Enter my own** option. To help you determine event patterns that might be useful for you, this topic
includes [example Region switch patterns](#arc-eventbridge-examples-region-switch "#arc-eventbridge-examples-region-switch").

###### To create a rule for a resource event

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. For the AWS Region to create the rule in, choose the Region where you created the plan that
   you want to monitor events for.
3. Choose **Create rule**.
4. Enter a **Name** for the rule, and, optionally, a description.
5. For **Event bus**, leave the default value, **default**.
6. Choose **Next**.
7. For the **Build event pattern** step, for **Event source**, leave
   the default value, **AWS events**.
8. Under **Sample event**, choose **Enter my own**.
9. For **Sample events**, type or copy and paste an event pattern. For examples, see the next section.

## Example Region switch patterns

Event patterns have the same structure as the events that they match. The pattern quotes the
fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that you can use
to monitor ARC actions and resources.

The following event patterns provide examples that you might use in EventBridge for
the Region switch capability in ARC.

- _Select all events from Region switch for PlanExecution_.

```
{
    "source": [ "aws.arc-region-switch" ],
    "detail-type": [ "ARC Region switch Plan Execution" ]
}
```

- _Select all events from Region switch for PlanEvaluation_.

```
    	{
    	"source": [ "aws.arc-region-switch" ],
    	"detail-type": [ "ARC Region Switch Plan Evaluation" ]
    	}
```

The following is an example ARC event for a _Region switch plan execution_:

```
{
  	"version": "0",
  	"id": "1111111-bbbb-aaaa-cccc-dddddEXAMPLE", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/aaaaaExample"], # planArn
  	"detail": {
  		"version": "0.0.1",
  		"eventType": "ExecutionStarted",
  		"executionId": "bbbbbbEXAMPLE",
  		"executionAction": "activating/deactivating {region}",
  		"idempotencyKey": "1111111-2222-3333-4444-5555555555", # As there is a possibility of dual logging
  	}
}
```

The following is an example ARC event for a _Region switch plan step level execution_:

```
{
  	"version": "0",
  	"id": "1111111-bbbb-aaaa-cccc-dddddEXAMPLE", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/aaaaaExample"], # planArn
  	"detail": {
  		"version": "0.0.1",
  		"eventType": "StepStarted",
  		"executionId": "bbbbbbEXAMPLE",
  		"executionAction": "activating/deactivating {region}",
  		"idempotencyKey": "1111111-2222-3333-4444-5555555555", # As there is a possibility of dual logging
  		"stepDetails" : {
  			"stepName": "Routing control step",
  			"resource": ["arn:aws:route53-recovery-control::111122223333:controlpanel/abcdefghiEXAMPLE/routingcontrol/jklmnopqrsEXAMPLE"]
  		}
  	}
}
```

The following is an example ARC event for a _Region switch plan evaluation warning_.

For a Region switch plan evaluation, an event is emitted when a warning is returned. If the warning is not cleared,
an event is emitted for the warning only once every 24 hours. When the event is cleared, no further events are
emitted for that warning.

```
{
  	"version": "0",
  	"id": "05d4d2d5-9c76-bfea-72d2-d4614802adb4", # Random uuid
  	"detail-type": "ARC Region Switch Plan Execution",
  	"source": "aws.arc-region-switch",
  	"account": "111122223333",
  	"time": "2023-11-16T23:38:14Z",
  	"region": "us-east-1",
  	"resources": ["arn:aws:arc-region-switch::111122223333:plan/a2b89be4821bfd1d"],
  	"detail": {
    	"version": "0.0.1",
    	"idempotencyKey": "1111111-2222-3333-4444-5555555555",
    	"metadata": {
        "evaluationTime" : "timestamp",
        "warning" : "There is a plan evaluation warning for arn:aws:arc-region-switch::111122223333:plan/a2b89be4821bfd1d. Navigate to the Region switch console to resolve."
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
 "Resource": "arn:aws:logs:us-east-1:222222222222:log-group:/aws/events/*:*",
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

For more information about creating EventBridge rules for readiness, see [Monitor a readiness check resource with EventBridge](eventbridge-readiness.md#RCEventBridgeCreateRule "eventbridge-readiness.md#RCEventBridgeCreateRule"). 4. On the **Select target** page, choose **CloudWatch** as your
target. 5. Choose a CloudWatch log group from the drop-down menu.
