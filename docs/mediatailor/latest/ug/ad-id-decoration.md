# Ad ID decoration

AWS Elemental MediaTailor performs server side ad stitching when transitioning from content to ad
breaks. MediaTailor can condition the manifest with metadata associated with the ads that have
been stitched. Doing so can provide the following benefits:

- _Video start time_ (VST) improves
- MediaTailor can support a hybrid model of server side ad insertion and server guided ad
  insertion
- Server side sessions can build playback timelines with ad position markers
- For client side sessions that already build playback timelines with the MediaTailor API,
  session VST improves, as the session does not rely on calling the tracking API to
  build the timeline
- It's possible to leverage MediaTailor for server side ad insertion as well as client
  side rendered ads displayed in-scene. This way, a player's software development kit
  (SDK) doesn't need to have a separate integration to call ad serving entities
  directly for client-side ads. MediaTailor can vend the ads through the manifest and the
  client-side tracking API.
  There are standards for associating each creative ad asset with a unique identifier. This
  association allows advertisers, agencies, vendors, and publishers to relate a creative ad
  asset across their independent workflows. As metrics and monitoring of streams continue to
  improve and more distributors utilize server-based insertion architectures, the need arises
  to accurately communicate the identifiers assigned to individual creative assets within an
  interleaved/stitched presentation, such as within the personalized manifest.

###### Topics

- [Enabling ad ID signaling for sessions](ad-id-session-state.md "ad-id-session-state.md")
- [Manifests and ad metadata insertion](ad-id-manifest.md "ad-id-manifest.md")
- [Ad Decision Server (ADS) interactions](ad-id-ads-interactions.md "ad-id-ads-interactions.md")
- [Client-side tracking API](ad-id-client-side-tracking-api.md "ad-id-client-side-tracking-api.md")
