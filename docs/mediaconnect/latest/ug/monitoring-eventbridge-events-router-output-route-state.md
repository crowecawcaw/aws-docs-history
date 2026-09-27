

# MediaConnect router output route state event
<a name="monitoring-eventbridge-events-router-output-route-state"></a>

AWS Elemental MediaConnect publishes this event when the router input that is routed to a router output changes. This includes when a router input is first routed to the output, replaced with a different router input, or unrouted.

For the corresponding event on the router input side, see [Router input route state event](monitoring-eventbridge-events-router-input-route-state.md).

The `change` field indicates what happened:
+ **ROUTED** – A router input is routed to the router output, including when it replaces a previously routed input.
+ **UNROUTED** – The router input was disconnected and the router output has no routed input.

The event also contains the following fields:
+ **previousRouterInputArn** – The ARN of the router input that was previously routed to the router output, or `null` if there was none.
+ **currentRouterInputArn** – The ARN of the router input that is currently routed to the router output, or `null` if the router output has no routed input.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Output Route State",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerOutput:b2c3d4e5f6a1"
  ],
  "detail": {
    "change": "ROUTED",
    "previousRouterInputArn": "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:c3d4e5f6a1b2",
    "currentRouterInputArn": "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:a1b2c3d4e5f6"
  }
}
```