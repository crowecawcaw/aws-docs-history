

# MediaConnect flow maintenance event
<a name="monitoring-cloudwatch-events-flow-maintenance"></a>

AWS Elemental MediaConnect publishes this event when a flow's maintenance status has changed, either to or from any of the following states: 
+ **SCHEDULED** - Maintenance is scheduled for the flow.
+ **RESCHEDULED** - MediaConnect is unable to perform maintenance at the previously scheduled date and time. A new date and time has been automatically assigned by MediaConnect for this flow's maintenance.
+ **CANCELED** - Maintenance for this flow is cancelled by MediaConnect.
+ **INPROGRESS** - Maintenance has started and is currently in progress for this flow.
+ **FINISHED** - Maintenance completed successfully for this flow.
+ **FAILED** - Maintenance did not complete successfully for this flow. 

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

For information about MediaConnect maintenance, see [MediaConnect flow maintenance](https://docs.aws.amazon.com/mediaconnect/latest/ug/maintenance.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Flow Maintenance",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow"
  ],
  "detail": {
    "currentStatus": "FINISHED"
  }
}
```