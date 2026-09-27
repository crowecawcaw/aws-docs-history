

# MediaConnect router output health event
<a name="monitoring-eventbridge-events-router-output-health"></a>

AWS Elemental MediaConnect publishes router output health events after a router output health indicator state changes.

MediaConnect publishes this event any time there is a state change to one or more of the following router output health indicators. This event publishes the current and previous state of the router output.

The following are router output health indicators:
+ **state** – The connection state of the router output destination.
  + Possible states: `CONNECTED`, `SENDING`, `DISCONNECTED`, `IDLE`

The event also includes the `outputType` field, which indicates the type of the router output.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Output Health",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerOutput:b2c3d4e5f6a1"
  ],
  "detail": {
    "current": {
      "state": "CONNECTED"
    },
    "previous": {
      "state": "DISCONNECTED"
    },
    "outputType": "STANDARD"
  }
}
```