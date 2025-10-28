# Using AWS Elemental MediaTailor to create linear assembled

streams

AWS Elemental MediaTailor channel assembly is a manifest-only service that allows you to create linear
streaming channels using your existing video on demand (VOD) content mixed with live
content. MediaTailor never touches your content segments, which are served directly from your
origin server. Instead, MediaTailor fetches the manifests from your origin, and uses them to
assemble a live sliding manifest window that references the underlying content segments.
Channel assembly keeps track of things like the media sequence number that's necessary to
make playback smooth from asset to asset. Linear assembled streams are created with a low
running cost by using existing multi-bitrate encoded and packaged VOD content.

You can easily monetize channel assembly linear streams by inserting ad breaks in your
programs without having to condition the content with SCTE-35 markers. You can use channel
assembly with the MediaTailor ad insertion service, or any server-side ad insertion service.

To get started with channel assembly, see [Getting started with MediaTailor channel
assembly](channel-assembly-getting-started.md "channel-assembly-getting-started.md").

For information about integrating Channel Assembly with a content delivery network (CDN), see [Build MediaTailor linear channels with channel assembly and
CDN](ca-cdn-wflw.md "ca-cdn-wflw.md").

###### Topics

- [Working with source locations](channel-assembly-source-locations.md "channel-assembly-source-locations.md")
- [Working with channels](channel-assembly-channels.md "channel-assembly-channels.md")
- [Adding a program to a channel's schedule](channel-assembly-programs.md "channel-assembly-programs.md")
- [Insert personalized ads and ad
  breaks in a channel stream](channel-assembly-integrating-mediatailor-ssai.md "channel-assembly-integrating-mediatailor-ssai.md")
- [Time-shifting a channel's playback](channel-assembly-time-shift.md "channel-assembly-time-shift.md")
