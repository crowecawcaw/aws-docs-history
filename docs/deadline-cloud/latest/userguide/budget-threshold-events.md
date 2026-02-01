# Monitor a budget with EventBridge events

Deadline Cloud sends budget-related events, using Amazon EventBridge, to your default EventBridge event bus. You
can create custom functions that receive the events and act on them to send
notifications to automatically notify users via email, Slack, or other channels when a
budget reaches predefined levels. For example, you can send SMS messages when a budget
reaches a certain threshold. These notifications help you stay on top of your spending and make
informed decisions before your budget is exhausted.

Deadline Cloud periodically aggregates usage and cost data for each render farm. Then it checks
to see if any of the budget thresholds has been crossed. If a threshold is crossed,
Deadline Cloud triggers an event to alert you so that you can take the appropriate action. An
event is triggered whenever a budget crosses one of these thresholds, specified in
percent of the budget used:

- 10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 96, 97, 98, 99, 100
  The budget usage thresholds get closer together as a budget approaches 100 percent
  usage. This frequency helps you closely monitor usage as the budget reaches its limit. You can
  also set your own budget thresholds. Deadline Cloud sends an event when usage passes your custom
  thresholds. After your budget reaches 100 percent, Deadline Cloud stops sending events. If you
  adjust your budget, Deadline Cloud sends events for your thresholds based on the new budget
  amount.

You can use the EventBridge console ([https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/")) to create rules to send the Deadline Cloud
events to the appropriate target for the event. For example, you can send the event to
an Amazon Simple Queue Service queue and from there to multiple targets, such as AWS End User Messaging
SMS or a Amazon Relational Database Service database for logging.

For examples of an EventBridge rule, see the following topics:

- [Send
  an email when events happen using Amazon EventBridge](../../../eventbridge/latest/userguide/eb-s3-object-created-tutorial.md "../../../eventbridge/latest/userguide/eb-s3-object-created-tutorial.md").
- [Creating an
  Amazon EventBridge rule that sends notifications to Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/create-eventbridge-rule.md "../../../chatbot/latest/adminguide/create-eventbridge-rule.md").
- [Getting started with
  Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").
  For more information about budget events, see the [Budget Threshold Reached event](../developerguide/events-detail-reference.md#event-detail-budget-threshold-reached "../developerguide/events-detail-reference.md#event-detail-budget-threshold-reached") in the _Deadline Cloud Developer
  Guide_.
