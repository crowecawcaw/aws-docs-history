# Working with channels in AWS Elemental MediaPackage

A channel is part of a channel group and represents the entry point for a content stream
into MediaPackage. After you create a channel, MediaPackage provides ingest endpoint
domains for its lifetime, regardless of any failures or upgrades that might occur.

Upstream encoders such as AWS Elemental MediaLive send content to the channel. When MediaPackage
receives a content stream, it packages the content and outputs the stream from an origin
endpoint that you create on the channel. Each incoming set of adaptive bitrate (ABR) streams
has one channel. A channel group can have multiple channels.

For supported live inputs and codecs, see [Supported inputs and outputs](supported-inputs.md "supported-inputs.md").

###### Topics

- [Creating a channel](channels-create.md "channels-create.md")
- [Viewing channel details](channels-view.md "channels-view.md")
- [Editing a channel](channels-edit.md "channels-edit.md")
- [Resetting channel history](channel-reset.md "channel-reset.md")
- [Deleting a channel](channels-delete.md "channels-delete.md")
