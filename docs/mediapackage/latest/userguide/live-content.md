# Delivering live content from AWS Elemental MediaPackage

AWS Elemental MediaPackage uses the following resources for live content:

- A _channel group_ is the top-level resource that consists of channels and
  origin endpoints that are associated with it and that provides predictable URLs for stream delivery.
  All channels and origin endpoints within the channel group are guaranteed to share the DNS.
- A _channel_ is the entry point for your live streams from upstream encoders.

For supported live inputs and codecs, see [Supported inputs and outputs](supported-inputs.md "supported-inputs.md").

- An _origin endpoint_ tells MediaPackage how to package outbound content. Endpoints are associated with channels and hold encryption, stream, and packaging settings.
  The following sections describe how to use these resources to manage live content in MediaPackage.

###### Topics

- [Working with channel groups in AWS Elemental MediaPackage](channel-groups.md "channel-groups.md")
- [Working with channels in AWS Elemental MediaPackage](channels.md "channels.md")
- [Working with origin endpoints in AWS Elemental MediaPackage](endpoints.md "endpoints.md")
