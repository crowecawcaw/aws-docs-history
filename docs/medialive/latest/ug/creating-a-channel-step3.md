# Complete general settings

The **General settings** section in the **Create
channel** page lets you configure global settings and global
features:

- Global _settings_ set behavior that applies
  to all inputs or all outputs in the channel. You can't configure the behavior
  differently for different inputs or outputs.
- Global _features_ set up features that are
  optional but that apply globally to all outputs if they are enabled.

###### To complete the general settings

1. On the **Create channel** page, choose **General
   settings**.
2. In the **General channel settings** section, set the global
   settings and optional features as needed. For information about each setting or
   feature, see the topics at the end of this procedure.
3. When you have finished working with these fields, go to the [next step](creating-a-channel-step4.md "creating-a-channel-step4.md").

## Avail blanking

Optional feature. You can set this to blank out the output video during ad avails.
For more information, see [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md").

## Avail configuration

Optional feature. You can modify the way that MediaLive handles SCTE-35 ad avail
messages, or you can keep the default behavior. For information about the default
behavior and how to modify that behavior, see [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md").

## Blackout slate

Optional feature. You can black out the output video as specified by program
metadata, if that metadata is present in the input. For more information, see [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md").

## Feature activations

Optional features. You can enable the input prepare feature for input switching.
For more information, see [Preparing inputs in
AWS Elemental MediaLive](feature-prepare-input.md "feature-prepare-input.md").

## Global configuration

Global configuration settings. In this section, complete the first three fields as
appropriate. For details about each field, choose the **Info** link
next to the field.

## Global configuration – input loss

behavior

Global configuration settings. The **Input Loss
Behavior** fields control how MediaLive handles input
loss. You can customize the handling. For more information, see
[Handling loss of video input](feature-input-loss.md "feature-input-loss.md").

## Motion graphics configuration

Optional feature. You can enable the motion graphics overlay feature. For more
information, see [Working with motion graphics
overlays](feature-mgi.md "feature-mgi.md").

## Nielsen configuration

Optional feature. You can configure a MediaLive channel to convert Nielsen watermarks
to ID3 metadata. For more information see [Converting Nielsen watermarks to ID3](feature-nielsen-id3.md "feature-nielsen-id3.md").

## Timecode configuration

Global configuration settings. This section lets you specify the timecode for the
output. For more information about configuring the timecode, see [Working with timecodes and timestamps](timecode.md "timecode.md").

## Logging

Optional feature. You can enable logging of activity on this individual channel.
For detailed information about this feature, see [Monitoring a channel using
Amazon CloudWatch Logs](monitoring-with-logs.md "monitoring-with-logs.md").

To enable logging, choose a log level other than **DISABLED**.
The levels are listed from least to most verbose.

To disable logging, choose **DISABLED**.
