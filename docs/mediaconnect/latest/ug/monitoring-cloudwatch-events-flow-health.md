# MediaConnect flow health

event

AWS Elemental MediaConnect publishes flow health events after a flow health indicator state
changes.

MediaConnect publishes this event any time there is a state change to one or more of the
following flow health indicators. This event publishes the current and previous
state of the flow.

The following are flow health indicators:

- **Source state**
  - Possible states: `connected`, `receiving`,
    `disconnected`, `idle`

- **Failover switch**
  - Possible states: `true`, `false`

- **TR-101**: TR-101 is an industry standard
  technical recommendation for the monitoring of transport streams (TS). The
  following events are only published for TS based protocols.

      + **TS sync loss** is `true`
       when source payloads do not look like a valid transport
       stream.
      + **Continuity count error** is
       `true` when the source finds continuity count
       errors.
      + **Transport error** is
       `true` when the TS has the transport indicator
       set.
      + **PCR error** is `true`
       when there is a PCR discontinuity or a long gap in PCR packet
       reception.

  For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Flow Health",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2006-01-02T15:04:05Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow"
  ],
  "detail": {
    "unhealthy": true,
    "current": {
      "failover_switch": false,
      "source_state": "CONNECTED",
      "tr101": {
        "ts_sync_loss": false,
        "continuity_count_error": true,
        "transport_error": true,
        "pcr_error": true
      }
    },
    "previous": {
      "failover_switch": false,
      "source_state": "CONNECTED",
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
