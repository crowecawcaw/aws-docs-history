

# Integrating AWS Clean Rooms into event-driven applications using Amazon EventBridge
<a name="eventbridge-integration-full"></a>

You can incorporate AWS Clean Rooms into event-driven applications (EDAs) that use events that occur in AWS Clean Rooms to communicate between application components and initiate downstream processes. You do this by using Amazon EventBridge to route events from AWS Clean Rooms to other software components. Amazon EventBridge is a serverless service that uses events to connect application components together, making it easier for you to integrate AWS services like AWS Clean Rooms into event-driven architectures without additional code and operations.

Event-driven architecture is a style of building loosely-coupled software systems that work together by emitting and responding to events. In this model, an events represents a change in a resource or environment.

Here's how EventBridge works with AWS Clean Rooms:

As with many AWS services, AWS Clean Rooms generates and sends events to the EventBridge default *event bus*. An event bus is a router that receives events and routes them to the destinations, or *targets*, that you specify. Targets can include other AWS services, custom applications, and SaaS partner applications. 

EventBridge routes events according to *rules* you create on the event bus. For each rule, you specify a filter, or *event pattern*, to select only the events you want. Whenever an event is sent to the event bus, EventBridge compares it against each rule. If the event matches the rule, EventBridge routes the event to the specified target(s).

![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge sends the event to the targets specified for that rule.](http://docs.aws.amazon.com/clean-rooms/latest/userguide/images/eventbridge-integration-how-it-works.png)


For example, suppose you want to know every time a new AWS Clean Rooms collaboration is created in your account. You could create a rule on the default event bus. In the rule you would create an event pattern that specified events from AWS Clean Rooms named **Collaboration Created**. Every time EventBridge received an event matching those properties, it would route the event to the specified workflow.

## AWS Clean Rooms events
<a name="eventbridge-service-events-full"></a>

AWS services can send events directly to the EventBridge default event bus. In addition, AWS CloudTrail sends events originating from numerous AWS services to EventBridge as well. These events can include API calls, console sign ins and actions, service events, and CloudTrail Insights. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *EventBridge User Guide*. 

For a full list of AWS Clean Rooms events sent to EventBridge, refer to the AWS Clean Rooms topic in the [*EventBridge Events Reference*](https://docs.aws.amazon.com/eventbridge/latest/ref/welcome.html).


| Event detail type | Description | 
| --- | --- | 
| [Analysis Template Created](events-detail-reference-full.md#event-detail-analysis-template-created) | The Analysis Template owner and all active members of the collaboration are notified when an Analysis Template is Created. | 
| [Analysis Template Updated](events-detail-reference-full.md#event-detail-analysis-template-updated) | The Analysis Template owner and all active members of the collaboration that have visibility into the update are notified when an Analysis Template is Updated. | 
| [Analysis Template Deleted](events-detail-reference-full.md#event-detail-analysis-template-deleted) | The Analysis Template owner and all active members of the collaboration are notified when an Analysis Template is Deleted. | 
| [Collaboration Created](events-detail-reference-full.md#event-detail-collaboration-created) | The **Collaboration** owner is notified when a **Collaboration** is **Created**. | 
| [Collaboration Updated](events-detail-reference-full.md#event-detail-collaboration-updated) | The **Collaboration** owner and all active members of the collaboration that have visibility into the update are notified when a **Collaboration** is **Updated**. | 
| [Collaboration Change Request Created](events-detail-reference-full.md#event-detail-collaboration-change-request-created) | The Collaboration owner and all active members of the collaboration are notified when a Collaboration Change Request is Created. | 
| [Collaboration Change Request Approved](events-detail-reference-full.md#event-detail-collaboration-change-request-approved) | The Collaboration owner and all active members of the collaboration are notified when a Collaboration Change Request is Approved. | 
| [Collaboration Change Request Cancelled](events-detail-reference-full.md#event-detail-collaboration-change-request-cancelled) | The Collaboration owner and all active members of the collaboration are notified when a Collaboration Change Request is Cancelled. | 
| [Collaboration Change Request Committed](events-detail-reference-full.md#event-detail-collaboration-change-request-committed) | The Collaboration owner and all active members of the collaboration are notified when a Collaboration Change Request is Committed. | 
| [Configured Table Association Created](events-detail-reference-full.md#event-detail-configured-table-association-created) | The Configured Table Association owner and all active members of the collaboration are notified when a Configured Table Association is Created. | 
| [Configured Table Association Updated](events-detail-reference-full.md#event-detail-configured-table-association-updated) | The Configured Table Association owner and all active members of the collaboration that have visibility into the update are notified when a Configured Table Association is Updated. | 
| [Configured Table Association Deleted](events-detail-reference-full.md#event-detail-configured-table-association-deleted) | The Configured Table Association owner and all active members of the collaboration are notified when a Configured Table Association is Deleted. | 
| [Configured Table Association Analysis Rule Created](events-detail-reference-full.md#event-detail-configured-table-association-analysis-rule-created) | The Configured Table Association Analysis Rule owner and all active members of the collaboration are notified when a Configured Table Association Analysis Rule is Created. | 
| [Configured Table Association Analysis Rule Updated](events-detail-reference-full.md#event-detail-configured-table-association-analysis-rule-updated) | The Configured Table Association Analysis Rule owner and all active members of the collaboration that have visibility into the update are notified when a Configured Table Association Analysis Rule is Updated. | 
| [Configured Table Association Analysis Rule Deleted](events-detail-reference-full.md#event-detail-configured-table-association-analysis-rule-deleted) | The Configured Table Association Analysis Rule owner and all active members of the collaboration are notified when a Configured Table Association Analysis Rule is Deleted. | 
| [Id Mapping Table Created](events-detail-reference-full.md#event-detail-id-mapping-table-created) | The Id Mapping Table owner and all active members of the collaboration are notified when an Id Mapping Table is Created. | 
| [Id Mapping Table Updated](events-detail-reference-full.md#event-detail-id-mapping-table-updated) | The Id Mapping Table owner and all active members of the collaboration that have visibility into the update are notified when an Id Mapping Table is Updated. | 
| [Id Mapping Table Deleted](events-detail-reference-full.md#event-detail-id-mapping-table-deleted) | The Id Mapping Table owner and all active members of the collaboration are notified when an Id Mapping Table is Deleted. | 
| [Id Namespace Association Created](events-detail-reference-full.md#event-detail-id-namespace-association-created) | The Id Namespace Association owner and all active members of the collaboration are notified when an Id Namespace Association is Created. | 
| [Id Namespace Association Updated](events-detail-reference-full.md#event-detail-id-namespace-association-updated) | The Id Namespace Association owner and all active members of the collaboration that have visibility into the update are notified when an Id Namespace Association is Updated. | 
| [Id Namespace Association Deleted](events-detail-reference-full.md#event-detail-id-namespace-association-deleted) | The Id Namespace Association owner and all active members of the collaboration are notified when an Id Namespace Association is Deleted. | 
| [Invited To Collaboration](events-detail-reference-full.md#event-detail-invited-to-collaboration) | The invited member is notified when they are invited to a Collaboration. | 
| [Membership Created](events-detail-reference-full.md#event-detail-membership-created) | The Membership owner and all active members of the collaboration are notified when a Membership is Created. | 
| [Membership Updated](events-detail-reference-full.md#event-detail-membership-updated) | The Membership owner is notified when a Membership is Updated, unless the membership was removed from the collaboration in which case all active members of the collaboration are notified. | 
| [Membership Deleted](events-detail-reference-full.md#event-detail-membership-deleted) | The Membership owner and all active members of the collaboration are notified when a Membership is Deleted. | 
| [Protected Job Submitted](events-detail-reference-full.md#event-detail-protected-job-submitted) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job is Submitted. | 
| [Protected Job Started](events-detail-reference-full.md#event-detail-protected-job-started) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job is Started. | 
| [Protected Job Cancelling](events-detail-reference-full.md#event-detail-protected-job-cancelling) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job is Cancelling. | 
| [Protected Job Cancelled](events-detail-reference-full.md#event-detail-protected-job-cancelled) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job is Cancelled. | 
| [Protected Job Succeeded](events-detail-reference-full.md#event-detail-protected-job-succeeded) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job has Succeeded. | 
| [Protected Job Failed](events-detail-reference-full.md#event-detail-protected-job-failed) | The Job Runner, Job Payer and Results Receiver of a Protected Job are notified when the Protected Job has Failed. | 
| [Protected Query Submitted](events-detail-reference-full.md#event-detail-protected-query-submitted) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query is Submitted. | 
| [Protected Query Started](events-detail-reference-full.md#event-detail-protected-query-started) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query is Started. | 
| [Protected Query Cancelling](events-detail-reference-full.md#event-detail-protected-query-cancelling) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query is Cancelling. | 
| [Protected Query Cancelled](events-detail-reference-full.md#event-detail-protected-query-cancelled) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query is Cancelled. | 
| [Protected Query Succeeded](events-detail-reference-full.md#event-detail-protected-query-succeeded) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query has Succeeded. | 
| [Protected Query Failed](events-detail-reference-full.md#event-detail-protected-query-failed) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query has Failed. | 
| [Protected Query Timed Out](events-detail-reference-full.md#event-detail-protected-query-timed-out) | The Query Runner, Query Payer and Results Receiver(s) of a Protected Query are notified when the Protected Query has Timed Out. | 

## Routing AWS Clean Rooms events using EventBridge
<a name="eventbridge-using-events-rules-full"></a>

To have EventBridge route AWS Clean Rooms events to a target, you must create a rule. Each rule contains an event pattern, which EventBridge matches against each event received on the event bus. If the event data matches the specified event pattern, EventBridge routes that event to the rule's target(s).

For comprehensive instructions on creating event bus rules, see [Creating rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *EventBridge User Guide*.

### Creating event patterns that match AWS Clean Rooms events
<a name="eventbridge-using-events-rules-patterns-full"></a>

Each event pattern is a JSON object that contains:
+ (Optional): A `source` attribute that identifies the service sending the event. For AWS Clean Rooms events, the source is `aws.cleanrooms`.
+ (Optional): A `detail-type` attribute that contains an array of the event names to match.
+ (Optional): A `detail` attribute containing any other event data on which to match.

For example, the following event pattern matches against all Id Namespace Association Updated events where the collaboration was deleted from AWS Clean Rooms:

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Updated"],
  "detail": {
    "status": ["COLLABORATION_DELETED"]
  }
}
```

For more information on writing event patterns, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *EventBridge User Guide*.