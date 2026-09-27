

# MediaConnect router output state event
<a name="monitoring-eventbridge-events-router-output-state"></a>

AWS Elemental MediaConnect publishes this event when a router output's state changes. This includes changes to or from the following states:
+ Creating
+ Standby
+ Starting
+ Active
+ Updating
+ Stopping
+ Deleting
+ Recovering
+ Migrating
+ Error

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Output State",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerOutput:b2c3d4e5f6a1"
  ],
  "detail": {
    "previousState": "STANDBY",
    "currentState": "ACTIVE"
  }
}
```