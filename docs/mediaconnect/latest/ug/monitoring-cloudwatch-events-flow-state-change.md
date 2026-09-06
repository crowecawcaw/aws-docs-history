

# MediaConnect flow state change event
<a name="monitoring-cloudwatch-events-flow-state-change"></a>

AWS Elemental MediaConnect publishes this event when a flow's state has changed from or to any of the following states: Standby, Active, Updating, Deleting, Starting, Stopping, or Error. 

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Flow Status Change",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow"
  ],
  "detail": {
    "currentStatus": "STARTING",
    "previousStatus": "STANDBY"
  }
}
```