# Flow notifications

Amazon AppFlow is integrated with Amazon EventBridge to publish events related to the status of a flow.
The following flow events are published to your default event bus.

- **AppFlow Start Flow Run Report**: This event is published at the start
  of a flow run.
- **AppFlow End Flow Run Report**: This event is published when a flow run
  is complete.
- **AppFlow Event Flow Report**: This event is generated every five minutes
  for an event-triggered flow, and provides a count of event triggers over the five minute
  interval.
- **AppFlow Event Flow Deactivated**: This event is generated when
  Amazon AppFlow deactivates an event-triggered flow due to a failure. The deactivation reason is
  specified in the event payload.
- **AppFlow Scheduled Flow Deactivated**: This event is generated when
  Amazon AppFlow deactivates a schedule-triggered flow due to a failure. The deactivation field is
  specified in the event payload.
  You can access these events in the EventBridge console by creating an appropriate rule. For the
  steps to create a rule, see [Creating Amazon EventBridge rules that react to
  events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

## Common fields

All event payloads include the following common fields:

**account**

The 12 digit number identifying the AWS account.

**detail-type**

The name of the event. See the preceding list of flow events for more information.

**id**

The unique value generated for every event.

**region**

The AWS region where the event originated.

**resources**

The ARNs (AWS Resource Numbers) that identify the resources involved in the event.

**source**

"aws.appflow".

**time**

The event timestamp.

**version**

The flow version. By default, this is set to 0 (zero) in all events.

## Flow event detail fields

The following fields are available as part of the flow event details:

**created-by**

The ARN of the user who created the flow.

**destination**

The details of the destination connector for the flow.

**destination-object**

The destination object chosen in the flow.

**flow-arn**

The ARN of the flow.

**flow-name**

The name of the flow selected at the time of the flow creation.

**source**

The details of the source connector for the flow.

**source-object**

The source object chosen in the flow.

**trigger-type**

The flow trigger.

The following table shows the additional event field details.

| Name of the flow event                                                        | Field                           | Description                                                                                                                                                                                                |
| ----------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AppFlow Start Flow Run Report**                                             | start-time                      | The timestamp of the start of the flow run.                                                                                                                                                                |
| **AppFlow Start Flow Run Report,**<br>**AppFlow End Flow Run Report**         | incremental-transfer-time-range | The start and end timestamps that Amazon AppFlow sent to the source application, indicating<br>the time range for the incremental record transfer. This is available only for<br>schedule-triggered flows. |
| **AppFlow Event Flow Deactivated,**<br>**AppFlow Scheduled Flow Deactivated** | deactivation-reason             | The reason for deactivation.                                                                                                                                                                               |
| **AppFlow Event Flow Deactivated**,<br>**AppFlow Scheduled Flow Deactivated** | deactivation-time               | The time at which the flow was deactivated.                                                                                                                                                                |
| **AppFlow Event Flow Report**                                                 | status-report                   | The count of event triggers received from the source, and the timestamp of the five<br>minute interval over which this count was calculated. This is available only for<br>event-triggered flows.          |
| **AppFlow End Flow Run Report**                                               | end-time                        | The timestamp of the flow run completion.                                                                                                                                                                  |
| **AppFlow End Flow Run Report**                                               | num-of-records-processed        | The number of records from the source that were processed by Amazon AppFlow.                                                                                                                               |
| **AppFlow End Flow Run Report**                                               | num-of-record-failures          | The number of records that could not be inserted into the destination.                                                                                                                                     |
| **AppFlow End Flow Run Report**                                               | data-processed                  | The volume of data (in bytes) that was processed.                                                                                                                                                          |
| **AppFlow End Flow Run Report**                                               | status                          | The status that indicates if the flow run failed or was successful.                                                                                                                                        |
| **AppFlow End Flow Run Report**                                               | error                           | The reason for flow run failure in the event of a failed flow.                                                                                                                                             |
