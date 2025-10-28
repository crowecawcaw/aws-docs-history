# MediaConnect source

health event

AWS Elemental MediaConnect publishes source health events after a source health indicator state
changes.

MediaConnect publishes this event any time there is a state change to one or more of the
following source health indicators. This event publishes the current and previous
state of the flow. Note that the source health event lists the affected flow and
source in the `resources` section.

The following are source health indicators:

- **Source state**
  - Possible states: `connected`, `receiving`,
    `disconnected`, `idle`

- **TR-101**: TR-101 is an industry standard
  technical recommendation for the monitoring of transport streams (TS). The
  following events are only published for TS based protocols.

      + **TS sync loss** - true when source
       payloads do not look like a valid transport stream.
      + **Continuity count error** - true
       when the source finds continuity count errors.
      + **Transport error** - true when the
       TS has the transport indicator set.
      + **PCR error** - true when there is a
       PCR discontinuity or a long gap in PCR packet reception.

  For information about subscribing to this event, see [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

The following message is an example of this event.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "MediaConnect Source Health",
  "source": "aws.mediaconnect",
  "account": "012345678901",
  "time": "2006-01-02T15:04:05Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:mediaconnect:us-east-1:012345678901:flow:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleFlow",
    "arn:aws:mediaconnect:us-east-1:012345678901:source:1-AbCdEfGhIjKlMnOp-abcdef123455:ExampleSource"
  ],
  "detail": {
    "unhealthy": true,
    "current": {
      "state": "CONNECTED",
      "tr101": {
        "ts_sync_loss": false,
        "continuity_count_error": true,
        "transport_error": true,
        "pcr_error": true
      }
    },
    "previous": {
      "state": "CONNECTED",
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
