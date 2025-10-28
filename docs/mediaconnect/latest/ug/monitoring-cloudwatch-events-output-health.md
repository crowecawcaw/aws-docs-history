# MediaConnect output

health event

AWS Elemental MediaConnect publishes output health events after an output health indicator state
changes.

MediaConnect publishes this event any time there is a state change to one or more of the
following output health indicators. This event publishes the current and previous
state of the flow. Note that the output health event lists the affected flow and
output in the `resources` section.

The following are output health indicators:

- **Output state**

      + Possible states: `connected`, `sending`,
       `disconnected`, `idle`

  For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Output Health",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2006-01-02T15:04:05Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow",
    "arn:aws:mediaconnect:us-east-1:012345678901:output:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleOutput"
  ],
  "detail": {
    "current": {
      "state": "CONNECTED"
    },
    "previous": {
      "state": "DISCONNECTED"
    }
  }
}
```
