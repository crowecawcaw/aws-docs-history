

# MediaConnect router input source metadata changed event
<a name="monitoring-eventbridge-events-router-input-source-metadata"></a>

AWS Elemental MediaConnect publishes this event when the metadata for a router input's source changes. The event detail contains the `metadataChangeTime` field, which is the time of the most recent change to the source metadata.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Input Source Metadata Changed",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:a1b2c3d4e5f6"
  ],
  "detail": {
    "metadataChangeTime": "2026-05-03T18:37:24Z"
  }
}
```