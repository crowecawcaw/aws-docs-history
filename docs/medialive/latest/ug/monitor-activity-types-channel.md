# States for channels and

multiplexes

You can monitor the states of MediaLive channels and multiplexes.

MediaLive reports the state of all channels. MediaLive turns these states into CloudWatch events
with the detailType set to `MediaLive Channel State Change`. For an example
of the JSON for these events, see [JSON
for a state change event](monitoring-cloudwatch-json-state-change.md "monitoring-cloudwatch-json-state-change.md").

The channel states are the following:

- **Creating**
- **Deleting**
- **Idle**: The channel isn't running. For information about
  charges that you accrue when a channel is idle, see [Pricing in MediaLive](pricing.md "pricing.md").
- **Recovering**: One or both pipelines in the channel failed,
  but MediaLive is restarting it.
- **Running**.
- **Starting**
- **Stopping**
- **Updating**: You changed the [channel class](class-channel-input.md "class-channel-input.md")for a channel. This state
  is captured on the console but not in [Amazon CloudWatch events](monitoring-via-cloudwatch.md "monitoring-via-cloudwatch.md").
  MediaLive reports the state of all multiplexes. MediaLive turns these states into CloudWatch events
  with the detailType set to `MediaLive Multiplex State Change`.

The multiplex states are the following:

- **Creating**
- **Deleting**
- **Idle**: The multiplex isn't running. For information about
  charges that you accrue when a multiplex is idle, see [Pricing in MediaLive](pricing.md "pricing.md").
- **Recovering**: One or both pipelines in the multiplex
  failed, but MediaLive is restarting it.
- **Running**
- **Starting**
- **Stopping**
