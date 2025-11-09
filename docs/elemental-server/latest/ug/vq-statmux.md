This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Statmux Rate Control

## Description

Statistical multiplexing (statmux) rate control applies only to an event created on an
AWS Elemental Server node that has the Statmux option or a combination of an AWS Elemental Server
node and a Statmux node.

The statmux controls are divided between the stream assembly of the event or profile and
several fields on the MPTS output. The event is always created on the AWS Elemental Server node.
The MPTS output is created on the AWS Elemental Server node or the Statmux node.

Statistical multiplexing is performed on the STPS channels that make up an MPTS output
when the **Rate Control Mode** of the video stream is set to
Statmux. In terms of video quality, all the controls described in the other sections of this
chapter apply, along with the following special controls.

**SPTS Channel (Event) Controls**

In the event (which is called an SPTS channel in an MPTS output) the following controls
apply:

- **Bitrate (Nominal Bitrate).**
- **Minimum Bitrate**. The bitrate allocated to a given SPTS
  channel, which will never go below this number.
- **Maximum Bitrate**. The bitrate allocated to a given SPTS
  channel, which will never exceed this number.

These settings guide the distribution of bitrate among the channels in the multiplex as
described below.

**MPTS Output Controls**

The MPTS output has the following controls:

- **Transport Stream Bitrate**: The total size of the MPTS
  output.
- **Video Allocation**: The portion of the **Transport Stream Bitrate** that is allocated to the video of all the
  SPTS channels.

These settings determine the overall bitrate "pool" that is distributed among the channels
in the multiplex as described below.

**Statmux Bitrate Allocation**

At runtime, each SPTS channel sends per-frame complexity information to the multiplexer
and receives corresponding bitrate allocations. The allocations for each frame in channel are
computed as follows.

- The **Nominal Bitrates** for all channels are scaled
  proportionately; such sum of the scaled nominal bitrates matches the Video Allocation for the
  multiplex. This is bitrate distribution if all the channels have the same complexity.
- The complexity of each channel is examined (relative to the other channels) and the
  **Nominal Bitrate** of each channel is adjusted. In this
  adjustment, the spread between the Min and Max of a given channel affects how much that
  channel's **Nominal Bitrate** is adjusted: the bigger the range,
  the bigger the adjustment.
- The **Nominal Bitrate** of each channel is adjusted again,
  if necessary, to stay within the Min and Max
  range.
- This last adjustment may result in “leftovers.” These leftovers are distributed among
  channels that did not get adjusted.
- The final bitrate allocation is sent to each SPTS channel.

## Recommendations

- **Transport Stream Bitrate**: The total size of the MPTS output;
  this number is set based on the bandwidth characteristics of the intended network.
- **Video Allocation**: This number is typically calculated
  as follows:

VA = Useable bitrate - (the maximum anticipated audio of all SPTS channels) - (the
maximum anticipated data of all SPTS channels).

where the useable bitrate is typically 95-97% of the **Transportation Stream Bitrate**.

- **Nominal** bitrate is set for each SPTS channel relative
  to other channels depending on resolution, framerate, and codec used to encode the video.
  Typically the nominal bit rate is set to a value that provides the desired video quality in
  an non-statmuxed application.
- **Minimum** bitrate sets a minimum allocation for a channel
  regardless of how low its relative complexity. A typical value for each SPTS channel is:

(Nominal) ÷ 2

The combined minimum bitrates for all channels in the multiplex is less than the
**Video Allocation (VA)**. An alert is triggered if it ever
equals or exceeds the VA.

- **Maximum** bitrate sets a maximum allocation for a
  channel, regardless of how high its relative complexity is. A typical value for each SPTS
  channel is:

Nominal x 2

The combined maximum bitrate is typically greater than the combined **Video Allocation (VA)**: if it is less than the VA, then all channels
receive their maximum allocation (they are encoded at constant bitrates).

The allocation of bitrates in the MPTS can be monitored in real time via the MPTS
Performance screen on the web interface.

## Location of Fields

**Event or Profile API**

| Location of Field on Web Interface       | Location of Tag in XML                        |
| ---------------------------------------- | --------------------------------------------- |
| Streams – Video > Advanced > Bitrate     | stream_assembly/video_description/bitrate     |
| Streams – Video > Advanced > Min Bitrate | stream_assembly/video_description/min_bitrate |
| Streams – Video > Advanced > Max Bitrate | stream_assembly/video_description/max_bitrate |

**MPTS API**

| Location of Field on Web Interface   | Location of Tag in XML |
| ------------------------------------ | ---------------------- |
| MPTS > Transportation Stream Bitrate | bitrate                |
| MPTS > Video Allocation              | video_allocation       |
