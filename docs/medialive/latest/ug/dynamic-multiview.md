

# Dynamic Multiview
<a name="dynamic-multiview"></a>

Dynamic Multiview presents multiple live video feeds to a viewer at the same time in a single encoded video stream — camera angles from one event, or several independent events arranged in a grid. The player requests a particular layout of a particular set of source feeds, and AWS Elemental MediaPackage assembles the live multiview stream on demand.

AWS Elemental MediaLive encodes each source feed once, using encoder settings that make the resulting renditions multiview compatible. MediaPackage then combines them without decoding, compositing, and re-encoding. The result is a standard HLS or DASH stream with a single video track, and audio and caption tracks for each source feed.

**Benefits**
+ **Plays on the devices you already reach.** The output is one video track in H.264 (AVC) or H.265 (HEVC), delivered over HLS or DASH. Any device that can play your existing streams can play a multiview stream — there is no custom player, no client-side compositing, and no additional SDK. A single DRM key covers every layout.
+ **Viewers keep control of audio and captions.** Every view's audio and caption tracks are carried in the manifest as selectable renditions, and a viewer switches between them without changing the visual layout.
+ **Views stay synchronized.** Sources are delivered as time-aligned segments, so all views in an assembled frame remain in sync.
+ **Encoding cost scales with sources, not combinations.** You encode one ABR stack for each feed no matter how many arrangements viewers request. Combinations are assembled at the point of delivery rather than pre-rendered.
+ **No new service to onboard.** Dynamic Multiview is a capability of MediaLive and MediaPackage, not a separate service.

**Related resources**
+ [Multiview](https://docs.aws.amazon.com/mediapackage/latest/userguide/dynamic-multiview.html) in the *AWS Elemental MediaPackage User Guide* – for creating the channel group, the multiview channel, and the playback URLs that select a layout.
+ [Creating a MediaPackage output group](opg-mediapackage.md) – for anything about the output group that is not multiview-specific.

**Topics**
+ [How it works](dynamic-multiview-how-it-works.md)
+ [Requirements](dynamic-multiview-requirements.md)
+ [Borders](dynamic-multiview-borders.md)
+ [Console setup](dynamic-multiview-console.md)
+ [Configuration reference](dynamic-multiview-reference.md)