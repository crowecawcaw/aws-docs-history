# Integrating AWS Clean Rooms into event-driven

applications using Amazon EventBridge

You can incorporate AWS Clean Rooms into event-driven applications (EDAs) that use events that
occur in AWS Clean Rooms to communicate between application components and initiate downstream
processes. You do this by using Amazon EventBridge to route events from AWS Clean Rooms to other software
components. Amazon EventBridge is a serverless service that uses events to connect application
components together, making it easier for you to integrate AWS services like AWS Clean Rooms
into event-driven architectures without additional code and operations.

Event-driven architecture is a style of building loosely-coupled software systems that
work together by emitting and responding to events. In this model, an events represents a
change in a resource or environment.

Here's how EventBridge works with AWS Clean Rooms:

As with many AWS services, AWS Clean Rooms generates and sends events to the EventBridge default
_event bus_. An event bus is a router that receives events and routes
them to the destinations, or _targets_, that you specify. Targets can
include other AWS services, custom applications, and SaaS partner applications.

EventBridge routes events according to _rules_ you create on the event bus.
For each rule, you specify a filter, or _event pattern_, to select only
the events you want. Whenever an event is sent to the event bus, EventBridge compares it against
each rule. If the event matches the rule, EventBridge routes the event to the specified
target(s).

![AWS services send events to the EventBridge default event bus. If the event matches a rule's event pattern, EventBridge sends the event to the targets specified for that rule.](images/eventbridge-integration-how-it-works.png)
For example, suppose you want to know every time a new AWS Clean Rooms collaboration is created in
your account. You could create a rule on the default event bus. In the rule you would create
an event pattern that specified events from AWS Clean Rooms named `Collaboration
 Created`. Every time EventBridge received an event matching those properties,
it would route the event to the specified workflow.

## AWS Clean Rooms events

AWS services can send events directly to the EventBridge default event bus. In addition,
AWS CloudTrail sends events originating from numerous AWS services to EventBridge as well. These
events can include API calls, console sign ins and actions, service events, and CloudTrail
Insights. For more information, see [AWS service
events delivered via AWS CloudTrail](../../../eventbridge/latest/userguide/eb-service-event-cloudtrail.md "../../../eventbridge/latest/userguide/eb-service-event-cloudtrail.md") in the _EventBridge User Guide_.

For a full list of AWS Clean Rooms events sent to EventBridge, refer to the AWS Clean Rooms topic in the
[_EventBridge
Events Reference_](../../../eventbridge/latest/ref/welcome.md "../../../eventbridge/latest/ref/welcome.md").

| Event detail type                                                                                                                                                              | Description               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| [Collaboration Created](events-detail-reference-full.md#event-detail-collaboration-created "events-detail-reference-full.md#event-detail-collaboration-created")               | Collaboration Created     |
| [Collaboration Updated](events-detail-reference-full.md#event-detail-collaboration-updated "events-detail-reference-full.md#event-detail-collaboration-updated")               | Collaboration Updated     |
| [Membership Created](events-detail-reference-full.md#event-detail-membership-created "events-detail-reference-full.md#event-detail-membership-created")                        | Membership Created        |
| [Membership Updated](events-detail-reference-full.md#event-detail-membership-updated "events-detail-reference-full.md#event-detail-membership-updated")                        | Membership Updated        |
| [Membership Deleted](events-detail-reference-full.md#event-detail-membership-deleted "events-detail-reference-full.md#event-detail-membership-deleted")                        | Membership Deleted        |
| [Protected Query Submitted](events-detail-reference-full.md#event-detail-protected-query-submitted "events-detail-reference-full.md#event-detail-protected-query-submitted")   | Protected Query Submitted |
| [Protected Query Succeeded](events-detail-reference-full.md#event-detail-protected-query-succeeeded "events-detail-reference-full.md#event-detail-protected-query-succeeeded") | Protected Query Succeeded |
| [Protected Query Failed](events-detail-reference-full.md#event-detail-protected-query-failed "events-detail-reference-full.md#event-detail-protected-query-failed")            | Protected Query Failed    |
| [Protected Query Timed Out](events-detail-reference-full.md#event-detail-protected-query-timed-out "events-detail-reference-full.md#event-detail-protected-query-timed-out")   | Protected Query Timed Out |
| [Protected Job Submitted](events-detail-reference-full.md#event-detail-protected-job-submitted "events-detail-reference-full.md#event-detail-protected-job-submitted")         | Protected Job Submitted   |
| [Protected Job Succeeded](events-detail-reference-full.md#event-detail-protected-job-succeeded "events-detail-reference-full.md#event-detail-protected-job-succeeded")         | Protected Job Succeeded   |
| [Protected Job Failed](events-detail-reference-full.md#event-detail-protected-job-failed "events-detail-reference-full.md#event-detail-protected-job-failed")                  | Protected Job Failed      |
| [Protected Job Cancelled](events-detail-reference-full.md#event-detail-protected-job-cancelled "events-detail-reference-full.md#event-detail-protected-job-cancelled")         | Protected Job Cancelled   |

## Routing AWS Clean Rooms events using

EventBridge

To have EventBridge route AWS Clean Rooms events to a target, you must create a rule. Each rule
contains an event pattern, which EventBridge matches against each event received on the event
bus. If the event data matches the specified event pattern, EventBridge routes that event to
the rule's target(s).

For comprehensive instructions on creating event bus rules, see [Creating
rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _EventBridge User
Guide_.

### Creating event patterns that

match AWS Clean Rooms events

Each event pattern is a JSON object that contains:

- (Optional): A `source` attribute that identifies the service
  sending the event. For AWS Clean Rooms events, the source is
  `aws.cleanrooms`.
- (Optional): A `detail-type` attribute that contains an array of
  the event names to match.
- (Optional): A `detail` attribute containing any other event
  data on which to match.

For example, the following event pattern matches against all Membership Updated events
where the collaboration was deleted from AWS Clean Rooms:

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Updated"],
  "detail": {
    "status": ["COLLABORATION_DELETED"]
  }
}
```

For more information on writing event patterns, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md")
in the _EventBridge User Guide_.
