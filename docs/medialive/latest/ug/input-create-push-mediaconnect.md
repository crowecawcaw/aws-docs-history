

# Setting up a MediaConnect input

This section describes how to create a MediaConnect input. With a MediaConnect input, the service provider pushes content through AWS Elemental MediaConnect to MediaLive. (From the point of view of MediaLive, the upstream system is MediaConnect. The upstream system is not the service provider.) 

To perform this setup, you must work with an AWS Elemental MediaConnect user.

This input type supports JPEG XS (TR-07) video. If you plan to ingest JPEG XS, see [Supported codecs by input type](inputs-supported-codecs-by-input-type.md) for the supported codecs and [Completing the settings – JPEG XS (TR-07)](input-specification.md#input-specification-jpegxs) for how to complete the channel's input specification.

**Topics**
+ [Set up AWS Elemental MediaConnect](setup-emx-flows.md)
+ [Create a MediaConnect input](setup-input-emx.md)
+ [Result of this procedure](setup-result-emx.md)