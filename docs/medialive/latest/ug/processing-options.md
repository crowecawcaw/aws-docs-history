# Supported output features

MediaLive supports different types of processing that you can implement in different
combinations.

## Manifest decoration

You can set up an output so that its manifest is decorated with ad avail
information. Manifest decoration works on two sources of ad avail information:

- Ad avail information found in the channel input, if the input is a
  transport stream (TS)
- Ad avail information from SCTE 35 messages added to the output using
  the MediaLive schedule

Manifest decoration applies only to HLS outputs, MediaPackage outputs, and
Microsoft Smooth outputs:

- You can set up HLS outputs so that their manifests are decorated
  according to one of the following styles:
  - Adobe
  - Elemental
  - SCTE 35 enhanced

- MediaPackage outputs are always set up so that their manifests are
  decorated. The marker style is always SCTE 35 enhanced style. Keep in
  mind that if you don't actually want SCTE 35 messages in the output that
  you deliver from AWS Elemental MediaPackage, then on the AWS Elemental MediaPackage side you can set up
  the channel to remove the markers.
- You can set up Microsoft Smooth outputs so that the sparse track
  includes instructions that correspond to the original SCTE 35 message
  content.

You must set up the channel for the behavior that you want. For more
information, see [Enabling manifest decoration in the
output](enable-manifest-decoration.md "enable-manifest-decoration.md").

## Blanking and blackout

The _cue out_ and _cue
in_ instructions in SCTE 35 messages in TS inputs line up with
specific content in the video, audio, and captions streams. You can set up the
channel so that this content is blanked out in the output:

- To blank out content for ad avails, use the ad avail blanking feature.
- To blank out content for other messages, use the blackout
  feature.

For more information, see [Enabling ad avail blanking in the
output](enable-ad-avail-blanking.md "enable-ad-avail-blanking.md") and [Enabling blackout in the output](enable-blackout.md "enable-blackout.md").

## SCTE 35 passthrough

You can set up TS outputs so that all the SCTE 35 messages from the input are
passed through to the output. Or you can set up to remove these messages from
the output.

The behavior that you want must be set up in the channel. For more
information, see [Enabling SCTE 35 passthrough or
removal](scte-35-passthrough-or-removal.md "scte-35-passthrough-or-removal.md").

## Inserting SCTE 35 messages using the

schedule

You can insert SCTE 35 messages in TS outputs using the [channel schedule](x-actions-in-schedule-SCTE35.md "x-actions-in-schedule-SCTE35.md"). For example,
you can add an action in the channel schedule to insert a splice insert in the
running channel.

The main use case for this feature is to add SCTE 35 messages to the output,
when the input doesn't already include SCTE 35 messages.

For more information, see [Inserting SCTE 35 messages using the
schedule](setup-scte35-insertion.md "setup-scte35-insertion.md").
