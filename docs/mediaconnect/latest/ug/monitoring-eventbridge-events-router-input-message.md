

# MediaConnect router input message event
<a name="monitoring-eventbridge-events-router-input-message"></a>

AWS Elemental MediaConnect publishes a router input message event when a router input message is set or cleared. The event indicates whether the message is currently active, and contains an error code and a message that describes the issue. These messages are visible on the MediaConnect console, or by using the `get-router-input` AWS Command Line Interface (AWS CLI) command. For more information about the `get-router-input` command, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/mediaconnect/get-router-input.html).

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Input Message",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:a1b2c3d4e5f6"
  ],
  "detail": {
    "active": true,
    "code": "StreamError",
    "message": "Stream Error: Timeout. Please investigate the router input."
  }
}
```