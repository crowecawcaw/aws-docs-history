# Monitor state changes for future-dated Capacity Reservations

Amazon EC2 sends an event to Amazon EventBridge when the state of a future-dated Capacity Reservation changes.

The following is example of this event. In this example, the future-dated Capacity Reservation entered
the `scheduled` state. Note the state highlighted in the
`detail-type` field.

```
{
   "version":"0",
   "id":"12345678-1234-1234-1234-123456789012",
   "detail-type":"EC2 Capacity Reservation `Scheduled`",
   "source":"aws.ec2",
   "account":"123456789012",
   "time":"yyyy-mm-ddThh:mm:ssZ",
   "region":"us-east-1",
   "resources":[
      "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-1234567890abcdefg"
   ],
   "detail":{
      "capacity-reservation-id":"cr-1234567890abcdefg",
      "state":"scheduled"
   }
}
```

The possible values for the `detail-type` field are:

- `Scheduled`
- `Active`
- `Delayed`
- `Unsupported`
- `Failed`
- `Expired`
  For more information about these states, see [View the state of a Capacity Reservation](capacity-reservations-view.md "capacity-reservations-view.md").

You can create Amazon EventBridge events that monitor for these events and then trigger specific
actions when they occur. For more information, see [Creating rules that react to
events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

To create a rule that monitors for all state change events, you can use the following
event pattern.

```
{
  "source": ["aws.ec2"],
  "detail-type": [{
    "prefix": "EC2 Capacity Reservation"
  }]
}
```

To create a rule that monitors for only specific state changes, you can use the
following event pattern.

```
{
  "source": ["aws.ec2"],
  "detail-type": [{
    "prefix": "EC2 Capacity Reservation `state`"
  }]
}
```

For example, the following event pattern monitors for events that are sent when a
future-dated Capacity Reservation enters the `active` state.

```
{
  "source": ["aws.ec2"],
  "detail-type": [{
    "prefix": "EC2 Capacity Reservation Active"
  }]
}
```
