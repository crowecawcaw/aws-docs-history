# Viewing input thumbnails

MediaLive can generate thumbnails for the video from inputs in your channels. The thumbnail
provides a visual verification that the content contains video. You can view the thumbnails
for each channel on the MediaLive console. You can also use one of the AWS APIs to work with
thumbnails programmatically.

**How thumbnails are generated**

When you have enabled thumbnails in a channel and the channel is
running, MediaLive generates a JPEG thumbnail every 2 seconds. The thumbnail
exists for only 2 seconds, until it gets replaced by the next thumbnail.
Each input has its own thumbnail, which means that MediaLive generates one
thumbnail for a single-pipeline channel, and two thumbnails for a
standard channel.

As soon as the thumbnail is generated, MediaLive displays it on the
console, in the channel details page. It also makes the thumbnail
available as binary data. You can use an AWS API to work with the
binary data programmatically.

**Encryption of the thumbnail**

MediaLive always encrypts each thumbnail as it is created.

###### Topics

- [Enabling thumbnails in a channel](thumbnails-enable.md "thumbnails-enable.md")
- [Viewing thumbnails on the
  console](thumbnails-view.md "thumbnails-view.md")
- [Retrieving thumbnails
  programmatically](thumbnails-work-cli.md "thumbnails-work-cli.md")
- [Limit on thumbnails in MediaLive](thumbnail-limits.md "thumbnail-limits.md")
