# Managing Deadline Cloud events using Amazon EventBridge

Amazon EventBridge is a serverless service that uses events to connect application
 components together, making it easier for you to build scalable event-driven applications.
 Event-driven architecture is a style of building loosely-coupled software systems that work
 together by emitting and responding to events. Events represent a change in a resource or
 environment. 

Here's how it works:

As with many AWS services, Deadline Cloud generates and sends events to the EventBridge default event bus. (The default event bus is automatically provisioned in
 every AWS account.) An event bus is a router that receives events and
 delivers them to zero or more destinations, or *targets*. Rules you
 specify for the event bus evaluate events as they arrive. Each rule checks whether an event
 matches the rule's *event pattern*. If the event does match, the event
 bus sends the event to the specified target(s).


![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge sends the event to the targets specified for that rule.](images/eventbridge-integration-how-it-works.png)
###### Topics

* [Deadline Cloud events](#supported-events "#supported-events")
* [Delivering Deadline Cloud events using EventBridge rules](#eventbridge-using-events-rules "#eventbridge-using-events-rules")
* [Deadline Cloud events detail reference](events-detail-reference.md "events-detail-reference.md")

## Deadline Cloud events


Deadline Cloud sends the following events to the default EventBridge event bus
 automatically. Events that match a rule's event pattern are delivered to the specified
 targets on a  [best-effort basis](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level"). Events might be delivered out of order.


For more information, see [EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html")
 in the *Amazon EventBridge User Guide.*




| Event detail type | Description |
| --- | --- |
| [Budget Threshold Reached](events-detail-reference.md#event-detail-budget-threshold-reached "events-detail-reference.md#event-detail-budget-threshold-reached") | Sent when a queue reaches a percentage of its assigned budget. |
| [Job Lifecycle Status Change](events-detail-reference.md#event-detail-job-lifecycle-status-change "events-detail-reference.md#event-detail-job-lifecycle-status-change") |  Sent when there is a change to the lifecycle status of a job. |
| [Job Run Status Change](events-detail-reference.md#event-detail-job-run-status-change "events-detail-reference.md#event-detail-job-run-status-change") | Sent when the overall status of the tasks in a job changes. |
| [Step Lifecycle Status Change](events-detail-reference.md#event-detail-step-lifecycle-status-change "events-detail-reference.md#event-detail-step-lifecycle-status-change") | Sent when there is a change to the lifecycle status of a step in a job. |
| [Step Run Status Change](events-detail-reference.md#event-detail-step-run-status-change "events-detail-reference.md#event-detail-step-run-status-change") | Sent when the overall status of the tasks in a step changes. |
| [Task Run Status Change](events-detail-reference.md#event-detail-task-run-status-change "events-detail-reference.md#event-detail-task-run-status-change") | Sent when the status of a task changes. | ## Delivering Deadline Cloud events using EventBridge rules To have the EventBridge default event bus send Deadline Cloud events to a target, you must create a rule. Each rule contains an event pattern, which EventBridge matches against each event received on the event bus. If the event data matches the specified event pattern, EventBridge delivers that event to the rule's target(s). For comprehensive instructions on creating event bus rules, see [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html") in the *EventBridge User Guide*. ### Creating event patterns that match Deadline Cloud events Each event pattern is a JSON object that contains: <br>• A `source` attribute that identifies the service sending the event. For Deadline Cloud events, the source is `aws.deadline`. <br>• (Optional): A `detail-type` attribute that contains an array of the event types to match. <br>• (Optional): A `detail` attribute containing any other event data on which to match. For example, the following event pattern matches against all Fleet Size Recommendation Change events for the specified `farmId` for Deadline Cloud: ``` { "source": ["aws.deadline"], "detail-type": ["Fleet Size Recommendation Change"], "detail": { "farmId": "farm-12345678900000000000000000000000" } } ``` For more information on writing event patterns, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html") in the *EventBridge User Guide*.
