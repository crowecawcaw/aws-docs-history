# Frame capture output

In a Frame capture output, MediaLive supports SCTE 35 features as follows:

- Passthrough of the SCTE 35 messages – Not applicable.
- Manifest decoration – Not supported because these outputs don't
  have manifests.
- Blanking and blackout – Applicable. Content in the output is
  blanked or blacked out if the features are enabled at the channel
  level.
  A Frame capture output doesn't support passthrough of the SCTE 35 messages.
  However, if blanking or blackout is enabled (at the channel level), then content
  that falls between the start and stop of the blackout is blanked or blacked out,
  even though no SCTE 35 messages are present.
