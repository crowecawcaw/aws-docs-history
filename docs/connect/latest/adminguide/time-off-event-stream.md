

# Time off event stream
<a name="time-off-event-stream"></a>

You can use time off events to integrate Connect Customer scheduling with external HR systems, for example, to drive leave-approval workflows. Connect Customer publishes a time off event to EventBridge each time an agent's time off request changes status, directly to your account's default event bus.

Each event uses the following source and detail-type values.
+ Source: `aws.connect`
+ Detail-type: `Amazon Connect Time Off Event`

Connect Customer emits an event when a time off request transitions to one of the following statuses, or when a published field on the request changes:

`AWAITING_APPROVAL`  
The request has been submitted and is awaiting approval.

`APPROVED`  
The request has been approved and added to the schedule.

`REJECTED`  
The request was rejected.

`CANCELLED`  
The request was cancelled.

Delivery is at-least-once, so the same event can be delivered more than once. Each event includes an `eventId` value that is stable across retries and redeliveries of the same change. Deduplicate on `eventId`. Do not deduplicate on the envelope `id` field, which EventBridge regenerates for each delivery.

The following example shows a time off event payload:

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "source": "aws.connect",
    "detail-type": "Amazon Connect Time Off Event",
    "account": "123456789012",
    "time": "2026-06-01T10:30:00Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:connect:us-west-2:123456789012:instance/instance-id",
        "arn:aws:connect:us-west-2:123456789012:instance/instance-id/agent/agent-id"
    ],
    "detail": {
        "eventId": "8960bddc-7b52-38e8-91a3-663511a85092",
        "instanceArn": "arn:aws:connect:us-west-2:123456789012:instance/instance-id",
        "timeoffId": "timeoff-id",
        "agentArn": "arn:aws:connect:us-west-2:123456789012:instance/instance-id/agent/agent-id",
        "staffingGroupArn": "arn:aws:connect:us-west-2:123456789012:instance/instance-id/staffing-group/sg-id",
        "forecastGroupArn": "arn:aws:connect:us-west-2:123456789012:instance/instance-id/forecast-group/fg-id",
        "shiftActivityArn": "arn:aws:connect:us-west-2:123456789012:instance/instance-id/opt/shift-activity/activity-id",
        "timeoffStatus": "APPROVED",
        "timeoffStartTimestamp": "2026-06-01T00:00:00.000Z",
        "timeoffEndTimestamp": "2026-06-05T23:59:59.000Z",
        "effectiveTimeOffHours": 1.5,
        "isAllDayTimeOff": false,
        "createdTimestamp": "2026-05-15T10:30:00.000Z",
        "lastUpdatedTimestamp": "2026-05-15T10:30:00.000Z"
    }
}
```

The following table describes the fields in the `detail` object of the event.


| Field | Description | 
| --- | --- | 
| `eventId` | A unique, stable identifier for the event. Use this value to deduplicate events. | 
| `instanceArn` | The ARN of the Connect Customer instance. | 
| `timeoffId` | The identifier of the time off request. | 
| `agentArn` | The ARN of the agent that the time off request is for. | 
| `staffingGroupArn` | The ARN of the staffing group. This field is omitted when the request has no staffing group. | 
| `forecastGroupArn` | The ARN of the forecast group. | 
| `shiftActivityArn` | The ARN of the shift activity. | 
| `timeoffStatus` | The status of the time off request: `AWAITING_APPROVAL`, `APPROVED`, `REJECTED`, or `CANCELLED`. | 
| `timeoffStartTimestamp` | The start of the time off period, in UTC ISO-8601 format with millisecond precision. | 
| `timeoffEndTimestamp` | The end of the time off period, in UTC ISO-8601 format with millisecond precision. | 
| `effectiveTimeOffHours` | The number of time off hours for the request. This field is omitted until the request is approved, so it doesn't appear on `AWAITING_APPROVAL` events or on requests rejected before approval. | 
| `isAllDayTimeOff` | Whether the request is for the entire day. | 
| `createdTimestamp` | When the time off request was created, in UTC ISO-8601 format with millisecond precision. | 
| `lastUpdatedTimestamp` | When the time off request was last updated, in UTC ISO-8601 format with millisecond precision. | 

The envelope `resources` array contains both the instance ARN and the agent ARN, so you can filter EventBridge rules at instance or agent granularity.