

# MediaConnect router input health event
<a name="monitoring-eventbridge-events-router-input-health"></a>

AWS Elemental MediaConnect publishes router input health events after a router input health indicator state changes.

MediaConnect publishes this event any time there is a state change to one or more of the following router input health indicators. This event publishes the current and previous state of the router input.

The following are router input health indicators:
+ **state** – The connection state of the router input source.
  + Possible states: `CONNECTED`, `RECEIVING`, `DISCONNECTED`, `IDLE`
+ **isBitrateZero** – true when the bitrate of the router input is currently zero.
+ **TR-101** – TR-101 is an industry standard technical recommendation for the monitoring of transport streams (TS). The following indicators are only published for TS based protocols.
  + **TS sync loss** – true when source payloads do not look like a valid transport stream.
  + **Continuity count error** – true when the source finds continuity count errors.
  + **Transport error** – true when the TS has the transport indicator set.
  + **PCR error** – true when there is a PCR discontinuity or a long gap in PCR packet reception.

The `unhealthy` field is true when one or more of these indicators shows that the health of the router input is impacted.

The event also includes the `inputType` field, which indicates the type of the router input.

For information about subscribing to this event, see [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Router Input Health",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2026-05-03T18:37:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:routerInput:a1b2c3d4e5f6"
  ],
  "detail": {
    "unhealthy": true,
    "inputType": "MEDIALIVE_CHANNEL",
    "current": {
      "state": "CONNECTED",
      "isBitrateZero": false,
      "tr101": {
        "ts_sync_loss": false,
        "continuity_count_error": true,
        "transport_error": false,
        "pcr_error": false
      }
    },
    "previous": {
      "state": "CONNECTED",
      "isBitrateZero": false,
      "tr101": {
        "ts_sync_loss": false,
        "continuity_count_error": false,
        "transport_error": false,
        "pcr_error": false
      }
    }
  }
}
```