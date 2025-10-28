# Delivering live content from AWS Elemental MediaPackage

AWS Elemental MediaPackage uses the following resources for live content:

- _Channels_ are the entry point for your live streams from upstream encoders.

For supported live inputs and codecs, see [Live supported codecs and input types](supported-inputs-live.md "supported-inputs-live.md").

- _Endpoints_ tell MediaPackage how to package outbound content. Endpoints are associated with channels and hold encryption, stream, and packaging settings.
  The following sections describe how to use these resources to manage live content in MediaPackage.

###### Topics

- [Working with channels in AWS Elemental MediaPackage](channels.md "channels.md")
- [Working with endpoints in AWS Elemental MediaPackage](endpoints.md "endpoints.md")
