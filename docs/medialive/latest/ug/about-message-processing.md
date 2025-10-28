# About message processing

SCTE 35 messages are messages that can be included in a source MPEG-2 transport stream
(TS). SCTE-104 messages are messages that can be included in source content from
SMPTE 2110 stream or
an AWS Elemental Link hardware device. SCTE-104 messages are automatically
converted into SCTE 35 messages as soon as MediaLive ingests the input.

###### Note

To use the ad avail features of MediaLive, you should be familiar with the SCTE 35
standard and optionally with the SCTE-67 standard. You should also be familiar with
how the input that you are encoding implements those standards.

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

**Support for SCTE 35 on the input side**

On the input side of a MediaLive channel, SCTE 35 messages can appear only in inputs
containing MPEG-2 transport streams (TS). You can set up a channel so that if an input
includes these messages, the messages are either processed during ingest (passed
through) or ignored.

**Support for SCTE 35 on the output side**

On the output side of a MediaLive channel, if you set up to pass through the input (rather
than remove it), then you can set up each output so that the SCTE 35 messages from the
input are turned into cueing information that is appropriate for that output type. This
cueing information can be in the form of one or both of the following:

- SCTE 35 messages in a TS output
- Manifest (or sparse track) decoration
  You set up each output separately, so that you can set up some outputs to include
  cueing information and some to exclude it.

As an adjunct to the ad avail information, you can also set up the outputs to blank
out the video, audio, and captions within the cueing information.

###### Topics

- [Supported features by input type](input-processing-options.md "input-processing-options.md")
- [Supported output features](processing-options.md "processing-options.md")
- [Processing features – default
  behavior](processing-options-default.md "processing-options-default.md")
- [Scope of processing by feature](scope-by-feature.md "scope-by-feature.md")
- [Supported features by
  output type](processing-applicability-by-output-type.md "processing-applicability-by-output-type.md")
