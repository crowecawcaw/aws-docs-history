# Enabling ad avail blanking in the

output

In a MediaLive channel, you can enable ad avail blanking to blank out the content for an
SCTE 35 message that is considered an ad avail (as defined by the ad avail mode in [Getting ready: Set
the ad avail mode](getting-ready-set-the-ad-avail-mode.md "getting-ready-set-the-ad-avail-mode.md")).

A similar feature is [blackout](enable-blackout.md "enable-blackout.md").

Blanking involves the following processing:

- Replace the video content associated with this event with an image that you
  specify or is with a black image.
- Remove the audio that is associated with this event.
- Remove the captions that are associated with this event.
  **Comparison to Manifest Decoration and
  Passthrough**

Ad avail blanking applies to all outputs. You cannot choose to blank out for some
outputs (for example, the HLS output) and not blank out for others (for example, the
Microsoft Smooth output). It is an all-or-nothing decision.

Manifest decoration and passthrough have a smaller scope: they apply only to outputs
that support these features.

###### Important

Be careful not to get into the following situation:

- You do _not_ do passthrough.
- You do _not_ do manifest decoration in a
  specific output (because they are not supported or because you choose not
  to).
- You do implement blanking
  In this situation, there will be no markers for where the blanked content occurs.
  The only way to identify where this blanking is occurring will be to look for the
  IDR i-frames that identify where the SCTE 35 message used to be.

###### Topics

- [Enabling blanking](procedure-to-enable-ad-avail-blanking.md "procedure-to-enable-ad-avail-blanking.md")
- [Triggers for ad avail
  blanking](triggers-for-ad-avail-blanking.md "triggers-for-ad-avail-blanking.md")
- [Ad avail blanking restriction
  flags](ad-avail-blanking-restriction-flags.md "ad-avail-blanking-restriction-flags.md")
