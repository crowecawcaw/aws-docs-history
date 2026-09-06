

# MediaConnect output status change event
<a name="monitoring-cloudwatch-events-output-status-change"></a>

AWS Elemental MediaConnect publishes this event when an output's status changes. The possible values are `ENABLED` and `DISABLED`.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Output Status Change",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow",
    "arn:aws:mediaconnect:us-east-1:012345678901:output:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleOutput"
  ],
  "detail": {
    "currentStatus": "DISABLED",
    "previousStatus": "ENABLED"
  }
}
```