# How MediaPackage works

AWS Elemental MediaPackage uses just-in-time format conversion to deliver over-the-top (OTT) video from
a single source to a wide variety of playback devices or content delivery networks
(CDNs).

In the processing flow for live content, encoders send live HLS streams to MediaPackage.
MediaPackage then packages the content, formatting it in response to playback requests from
downstream devices.

The following sections describe the live processing flows.

###### Topics

- [General AWS Elemental MediaPackage live processing
  flow](what-is-flow-gen.md "what-is-flow-gen.md")
- [Live input redundancy AWS Elemental MediaPackage processing
  flow](what-is-flow-ir.md "what-is-flow-ir.md")
