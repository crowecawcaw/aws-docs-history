# Creating a custom event
 pattern for an EventBridge rule

You can find several predefined patterns in EventBridge for CloudFormation and Git sync events.
 This simplifies how an event pattern is created. Instead of writing your own event
 patterns, you can select field values on a form, and EventBridge generates the pattern for you.
 You can create a new rule using one of these predefined event patterns or create your
 own custom event pattern.

When a service like CloudFormation delivers an event to the default event bus, EventBridge uses
 the event pattern defined in your rule to determine if the event should be delivered to
 the rule's target(s). An event pattern matches the data in the desired CloudFormation
 events. 

Each event pattern is a JSON object that contains:


* A `source` attribute that identifies the service the event is
 coming from. For example, `aws.cloudformation` or
 `aws.codeconnections`.
* (Optional): A `detail-type` attribute that contains an array of the
 event types to match.
* (Optional): A `detail` attribute containing any other event data on
 which to match.


For example, the stack ID, the resources involved, status of various
 resources, and other data relevant to a particular type of events.
For example, the following event pattern matches against all resource status change
 events:


```
{
  "source": ["aws.cloudformation"],
  "detail-type": ["CloudFormation Resource Status Change"]
}
```
While the following event pattern uses event detail data to match only resource status
 change events where CloudFormation creates a new `AWS::S3::Bucket` or
 `AWS::SNS::Topic` resource:


```
{
  "source": ["aws.cloudformation"],
  "detail-type": ["CloudFormation Resource Status Change"],
  "detail": {
    "status-details": {
      "status": ["CREATE_COMPLETE"]
    },
    "resource-type": ["AWS::S3::Bucket", "AWS::SNS::Topic"]
  }
}
```
For more information on writing event patterns, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html") in
 the *Amazon EventBridge User Guide*.
