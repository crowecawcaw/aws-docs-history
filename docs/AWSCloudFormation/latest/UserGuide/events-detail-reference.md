# CloudFormation events detail reference

All events from AWS services have a common set of fields containing metadata about
 the event, such as the AWS service that's the source of the event, the time the event
 was generated, the account and region in which the event took place, and others. For
 definitions of these general fields, see [AWS service event metadata](https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html "https://docs.aws.amazon.com/eventbridge/latest/ref/events-structure.html") in the *AWS Events Reference*. 

In addition, each event has a `detail` field that contains data specific to
 that particular event. The reference below defines the detail fields for the various
 CloudFormation events.

When using EventBridge to select and manage CloudFormation events, it's useful to keep the
 following in mind:


* The `source` field specifies the event source.


For example, `aws.cloudformation` or
 `aws.codeconnections`.
* The `detail-type` field specifies the event type. 


For example, `CloudFormation Resource Status Change` or
 `CloudFormation Drift Detection Status Change`.
* The `detail` field contains the data that is specific to that
 particular event. 


For example, the stack ID, the resources involved, status of various
 resources, and other data relevant to a particular type of events.
For information on constructing event patterns that enable rules to match CloudFormation
 events, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html") in
 the *Amazon EventBridge User Guide*.

For more information on events and how EventBridge processes them, see [EventBridge
 events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html") in the *Amazon EventBridge User Guide*.

###### Topics

* [Resource Status Change event
 detail](event-detail-resource-status-change.md "event-detail-resource-status-change.md")
* [Stack Status Change event
 detail](event-detail-stack-status-change.md "event-detail-stack-status-change.md")
* [Drift Detection Status
 Change event detail](event-detail-stack-drift-detection-change.md "event-detail-stack-drift-detection-change.md")
* [StackSet Status Change event
 detail](event-detail-stackset-status-change.md "event-detail-stackset-status-change.md")
* [StackSet Stack
 Instance Status Change event detail](event-detail-stackset-stack-instance-status-change.md "event-detail-stackset-stack-instance-status-change.md")
* [StackSet Operation
 Status Change event detail](event-detail-stackset-operation-status-change.md "event-detail-stackset-operation-status-change.md")
* [Repository Sync Status
 Change event detail](event-detail-respository-sync-status-change.md "event-detail-respository-sync-status-change.md")
* [Resource Sync Status
 Change event detail](event-detail-resource-sync-status-change.md "event-detail-resource-sync-status-change.md")
