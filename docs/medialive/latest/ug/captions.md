# Including captions in a channel

You can set up the MediaLive channel to extract captions when it ingests the source, and to
include those captions in the output in either the same or a different format. You can include
several captions in the output. For example, you can include captions for several languages. You
can take a source captions asset and convert it to one format in one output and to another
format in a different output.

You perform the setup for captions in your AWS Elemental MediaLive channel.

By default, AWS Elemental MediaLive does not ingest any captions (not even captionsa that are embedded in
the video). You must explicitly identify the captions to ingest and the captions to
output.

###### Note

The information in this captions section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md"). It
also assumes that you have started creating a channel, including associating an input with the
channel.

###### Topics

- [Captions features supported in a
  channel](captions-supported-features.md "captions-supported-features.md")
- [Typical scenarios for handling captions](typical-scenarios.md "typical-scenarios.md")
- [Create captions selectors in the
  inputs](identify-captions-in-the-input.md "identify-captions-in-the-input.md")
- [Plan captions for the outputs](planning-captions-in-the-outputs.md "planning-captions-in-the-outputs.md")
- [Match formats to categories](match-categories-captions.md "match-categories-captions.md")
- [Create captions encodes](create-captions-encodes.md "create-captions-encodes.md")
- [Examples of handling captions in MediaLive](examples.md "examples.md")
