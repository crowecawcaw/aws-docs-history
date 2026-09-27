

# MediaConnect router input failover event
<a name="monitoring-eventbridge-events-router-input-failover"></a>

AWS Elemental MediaConnect publishes this event for a router input that uses the `FAILOVER` input type when the active source changes.

The event contains the following fields:
+ **failoverMode** – The failover mode of the router input, either `PRIMARY_SECONDARY` or `NO_PRIORITY`.
+ **currentSourceIndex** – The zero-based index of the source that is currently in use, either `0` or `1`.
+ **previousSourceIndex** – The zero-based index of the source that was previously in use. This field is absent when MediaConnect has not previously reported an active source for this router input, such as after the router input starts.
+ **primarySourceIndex** – The zero-based index of the primary source. This field is omitted when `failoverMode` is `NO_PRIORITY`.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Input Failover",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:a1b2c3d4e5f6"
  ],
  "detail": {
    "failoverMode": "PRIMARY_SECONDARY",
    "currentSourceIndex": 0,
    "previousSourceIndex": 1,
    "primarySourceIndex": 0
  }
}
```