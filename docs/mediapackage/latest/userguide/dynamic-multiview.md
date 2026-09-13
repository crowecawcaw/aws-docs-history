

# Dynamic Multiview in AWS Elemental MediaPackage
<a name="dynamic-multiview"></a>

Dynamic Multiview is a server-side capability that composes multiple live video sources into a single encoded video stream. Content providers can deliver multi-angle, multi-game, and personalized viewing experiences as standard HLS and DASH streams playable on most modern consumer devices, televisions, and set top boxes without custom player development.

Dynamic Multiview provides the following benefits:
+ **Plays on the devices you already reach.** The output is one video track in H.264 (AVC) or H.265 (HEVC), delivered over HLS or DASH. Any device that can play your existing streams can play a multiview stream — there is no custom player, no client-side compositing, and no additional SDK. A single DRM key covers every layout.
+ **Viewers keep control of audio and captions.** Every view's audio and caption tracks are carried in the manifest as selectable renditions, and a viewer switches between them without changing the visual layout.
+ **Views stay synchronized.** Sources are delivered as time-aligned segments, so all views in an assembled frame remain in sync.
+ **Encoding cost scales with sources, not combinations.** You encode one ABR stack for each feed no matter how many arrangements viewers request. Combinations are assembled at the point of delivery rather than pre-rendered.

Dynamic Multiview is a capability of AWS Elemental MediaLive and MediaPackage. MediaLive encodes each source as its own channel with encoding constraints that make the output combinable downstream. These feeds are ingested into MediaPackage as individual source channels, and MediaPackage assembles them into whatever layout a viewer requests, on demand.

## MediaPackage multiview channels
<a name="dynamic-multiview-channels"></a>

On MediaPackage, a multiview workflow uses two kinds of channels:
+ **Source channels** — ordinary CMAF channels, each receiving one camera angle or event from your encoder. Each source provides the content for one view in the assembled layout.
+ **A multiview channel** — a channel with an input type of `MULTIVIEW`. It receives no ingest of its own. Instead it declares which source channels it can use, and which layouts viewers can request. You create origin endpoints on the multiview channel, and viewers play back from those endpoints.

In this guide, a **source** is a channel that feeds content into the multiview channel, and a **view** is one region of the composited frame. Each view is normally filled by a source; if that source is unavailable, the view shows black.

All source channels and the multiview channel must be in the same channel group. For more information about channel groups, see [Working with channel groups in AWS Elemental MediaPackage](channel-groups.md).

![Architecture diagram with three columns: MediaLive, MediaPackage channel group, and CDN/Viewers. In MediaLive, four encoder sources (A, B, C, D) each feed a MediaPackage source channel (Channel A, B, C, D) in the channel group. Each source channel is also delivered on its own through the CDN to viewers as a single-view stream (A, B, C, and D). A multiview channel in the same channel group reads the segments of the source channels and performs dynamic multiview generation, producing combined outputs delivered through the CDN — shown as a two-up layout (A and B), a primary-plus-two layout (a large A with B and C), and a 2×2 grid (A, B, C, D).](https://docs.aws.amazon.com/mediapackage/latest/userguide/images/dynamic-multiview-architecture.png)


## Layouts
<a name="dynamic-multiview-layouts"></a>

A layout defines how many views are composited and how they are arranged. Each layout accepts an exact number of sources.


**Dynamic Multiview layouts**  

| Layout | Views | Arrangement | View sizes | 
| --- | --- | --- | --- | 
| 2EH | 2 | Two views side by side in the middle of the frame, with full-width bars above and below | Equal | 
| 3EL | 3 | One view in the left column, with black bars above and below it, beside two stacked views on the right | Equal | 
| 4E | 4 | Four equal views in a 2×2 grid | Equal | 
| 2PL | 2 | One large primary view on the left, one smaller view on the right, with full-width bars above and below | Primary is twice the width and height of the secondary | 
| 3PL | 3 | One large primary view on the left, two stacked views on the right, with full-width bars above and below | Primary is twice the width and height of each secondary | 
| 4PL | 4 | One large primary view on the left, with black bars above and below it, and three stacked views on the right | Primary is twice the width and height of each secondary | 

![Diagram of the six Dynamic Multiview layouts, each drawn as a 16:9 frame with black padding shaded. 2EH: two equal views (V1, V2) side by side, with full-width black bars above and below. 3EL: a tall view (V1) in the left column, with black bars above and below it, and two stacked views (V2, V3) filling the right column. 4E: four equal views (V1, V2, V3, V4) in a 2×2 grid with no padding. 2PL: a large primary view (V1) on the left and one smaller view (V2) on the right, with black fill above and below the smaller view. 3PL: a large primary view (V1) on the left and two stacked smaller views (V2, V3) on the right, with full-width black bars above and below. 4PL: a large primary view (V1) on the left, with black bars above and below it, and three stacked smaller views (V2, V3, V4) on the right.](https://docs.aws.amazon.com/mediapackage/latest/userguide/images/dynamic-multiview-layouts.png)


In `2PL`, `3PL`, and `4PL`, one view is larger than the others. This large primary view is `V1`, filled by the first source you list; the remaining sources fill the smaller views (`V2`, `V3`, and `V4`) in the order you list them.

### Black areas in the assembled frame
<a name="dynamic-multiview-black-areas"></a>

An assembled multiview frame contains black in two places, from two different causes:
+ **Layout padding.** Every layout except `4E` places synthetic black fill around the views so the combined frame keeps a standard 16:9 aspect ratio. `4E` composites its four views edge to edge with no padding.
+ **Per-view borders.** MediaLive adds a black border to each participating encode so that video compression artifacts from one view cannot bleed into its neighbor. MediaPackage does not trim these, so the black a viewer sees *between* two views is the sum of the two adjacent borders, while the outer edge of the frame shows only one. Border thickness is proportional to rendition size and is configured in MediaLive. For more information about configuring border thickness, see [Dynamic Multiview: Borders](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-borders.html) in the MediaLive user guide.

## Requirements
<a name="dynamic-multiview-requirements"></a>

**Encoder.** Source feeds must be encoded by AWS Elemental MediaLive. Multiview compositing relies on encoder output that only MediaLive produces; third-party encoders are not supported. MediaLive's encoder-side requirements are documented in the MediaLive user guide. Configure those first; this guide covers the MediaPackage side.
+ Overall requirements and validation: see [Dynamic Multiview: Requirements and Limitations](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-requirements.html).
+ Per-output encoder settings and dimension rules: see [Dynamic Multiview: MediaLive Configuration Reference](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-reference.html).
+ Borders: see [Dynamic Multiview: Borders](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-borders.html).

**Source channels.** Each source channel must:
+ use the **CMAF** input type
+ be in the same channel group as the multiview channel
+ not itself be a `MULTIVIEW` channel
+ use the **epoch-locked** output locking mode

**The multiview channel** must also be epoch-locked. Output locking mode is fixed when a channel is created, so existing non-epoch-locked CMAF channels cannot be used as multiview sources (see [Output locking mode](cmaf-ingest.md#output-locking-mode)). Input type is likewise immutable after creation: you cannot convert a CMAF channel into a multiview channel.

**Codecs.** Participating sources must be H.264 (AVC) or H.265 (HEVC). Both codecs can exist in the same workflow, but MediaPackage combines only sources encoded with the **same** codec — you can't combine an AVC source and an HEVC source in the same multiview. Frame rates must match across the sources you combine. AV1 is not supported for multiview.

**HLS child manifest URL encoding.** On multiview endpoints, the `UrlEncodeChildManifest` setting on each HLS manifest defaults to `true`, and you should keep it set to `true`. Multiview requires this for HLS playback: it URL-encodes the `aws.multiview` query string that MediaPackage embeds in the child manifest URLs, so that HLS players request the child manifests correctly. Setting it to `false` (the previous default) causes HLS playback to fail on players that request the child manifest URL as-is.

## Set up a multiview workflow
<a name="dynamic-multiview-setup"></a>

1. **Create the source channels.** Create one CMAF, epoch-locked channel per camera angle or event and point your MediaLive channel at its ingest endpoints. See [Creating a channel in AWS Elemental MediaPackage](channels-create.md).

1. **Create the multiview channel.** Create a channel with an input type of `MULTIVIEW` and a multiview configuration that declares:
   + `AvailableSources` — the names of the source channels, in the same channel group, that the multiview channel can use.
   + `AvailableLayouts` — the layouts that viewers may request. At least one.

   ```
   aws mediapackagev2 create-channel \
     --channel-group-name exampleChannelGroup \
     --channel-name exampleMultiviewChannel \
     --input-type MULTIVIEW \
     --multiview-configuration '{
         "AvailableSources": ["cam1", "cam2", "cam3", "cam4"],
         "AvailableLayouts": ["LAYOUT_4E", "LAYOUT_3PL", "LAYOUT_2EH"]
     }'
   ```

   The multiview channel is added to each source channel's `AttachedMultiviewChannels` property. This field is read-only, and a source channel cannot be deleted while a multiview channel still lists it as an available source. To delete a source channel, first remove it from the multiview channel's `AvailableSources`.

1. **Create an origin endpoint** on the multiview channel, as described in [Creating an origin endpoint](endpoints-create.md). Multiview endpoints serve HLS from CMAF or TS containers, and DASH from CMAF containers.

For an end-to-end walkthrough of creating channels and endpoints in MediaPackage, see [Getting started with AWS Elemental MediaPackage](getting-started.md).

## Request a multiview stream
<a name="dynamic-multiview-playback"></a>

Viewers select a view arrangement by adding the `aws.multiview` query parameter to the playback URL:

```
aws.multiview=layout:<layout>;sources:<source1>,<source2>,...
```
+ `layout` — one of the layouts declared in the channel's `AvailableLayouts`.
+ `sources` — a comma-separated list of source channel names. The number of sources must exactly match the layout's view count.

The order of `sources` determines which view each source fills: the first source you list appears in `V1`, the second in `V2`, the third in `V3`, and the fourth in `V4`, as labeled in the layout diagrams in [Layouts](#dynamic-multiview-layouts). MediaPackage never reorders the list, so two requests that name the same sources in a different order are different streams and produce different manifests.

**Layout values in the playback URL omit the `LAYOUT_` prefix.** A channel configured with `LAYOUT_4E` is played back with `layout:4E`; the prefixed form `layout:LAYOUT_4E` is rejected.

The parameter must be URL-encoded in the playback URL:

```
https://<egress-domain>/out/v1/exampleChannelGroup/exampleMultiviewChannel/hls/index.m3u8?aws.multiview=layout%3A4E%3Bsources%3Acam1%2Ccam2%2Ccam3%2Ccam4
```

MediaPackage propagates the parameter into the child manifest and segment URLs it emits, so a player only needs to add it to the top-level manifest request.

The same source channel may appear more than once in `sources`.

## Audio, captions, and source loss
<a name="dynamic-multiview-audio-captions"></a>

MediaPackage carries an audio track and a caption track for each source channel included in the multiview, as selectable renditions in the manifest, so a viewer can switch audio or captions without changing the visual layout. Supported captions are WebVTT and TTML.

When a source is unavailable, MediaPackage keeps the stream continuous by substituting for the missing content: black video for that source's view, silent audio for its audio track, and empty captions for its caption track.

Manifest filtering is supported on multiview endpoints, including language pruning and bitrate capping. For more information, see [Manifest filtering](manifest-filtering.md).

## Identify a view's audio and captions
<a name="dynamic-multiview-identify-audio-captions"></a>

MediaPackage labels the audio and caption renditions in a stitched manifest so that you, or a player, can tell which view each rendition belongs to. The label comes from the name you give the track in MediaLive, so name each audio and caption track that participates in the multiview.

**Name the tracks in MediaLive.** In your MediaLive channel:
+ For audio, set the **Stream Name** on each audio description — for example, `English` or `Spanish`.
+ For captions, set the **Language description** on each caption description. Caption descriptions don't have a stream name; the **Language description** is the equivalent field.

The view prefix that MediaPackage adds makes each rendition name unique, even when two source channels use the same track name. Choose names that describe the content — the language, for example — so that a viewer can tell the renditions apart. For the MediaLive output requirements, see [Dynamic Multiview: Requirements and Limitations](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-requirements.html). For where these fields appear in the MediaLive console, see [How Dynamic Multiview works](https://docs.aws.amazon.com/medialive/latest/ug/dynamic-multiview-how-it-works.html), both in the MediaLive user guide.

**HLS.** MediaPackage prefixes the name you set with the view position and uses the result as the `NAME` attribute on the `EXT-X-MEDIA` tag. An audio track whose stream name is `English`, filling the first view, appears as `View1_English`:

```
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",NAME="View1_English",URI="..."
```

Captions follow the same pattern, using the language description. A caption track whose language description is `English` and that belongs to the second view appears as `View2_English` on its `TYPE=SUBTITLES` tag. To find a view's audio or captions in an HLS manifest, look for the `View` prefix on the `NAME` attribute.

**DASH.** MediaPackage puts the same view-prefixed name in the `Label` element of the audio or subtitle adaptation set — for example `View1_English` — mirroring the HLS `NAME`. Each audio and subtitle adaptation set also carries a `Viewpoint` descriptor whose value identifies the view — `View1`, `View2`, and so on. This value matches the corresponding view's video, so a player can associate a track with its view programmatically, independent of the label text.

In both formats, the view number matches the order in which you listed the source channels in the `sources` parameter of your request: the first source is `View1`, the second is `View2`, and so on. For more information, see [Request a multiview stream](#dynamic-multiview-playback).

## Ad signaling (SCTE-35)
<a name="dynamic-multiview-ad-signaling"></a>

Dynamic Multiview supports full-screen ad replacement signaled by SCTE-35 from the primary view. MediaPackage processes SCTE-35 messages from the primary view only. SCTE-35 messages delivered inside segments are not supported. For more information about SCTE-35 handling in MediaPackage, see [SCTE-35 message options in AWS Elemental MediaPackage](scte.md).

## CDN caching
<a name="dynamic-multiview-cdn-caching"></a>

Because the view arrangement lives in the query string, each distinct combination of layout and source order is a distinct object. Configure your CDN to include the `aws.multiview` query parameter in the cache key, so that viewers requesting different arrangements are not served each other's content. If you expect many combinations, consider constraining the arrangements your application offers, so that your CDN cache stays effective.

## Constraints
<a name="dynamic-multiview-constraints"></a>

**Playback and manifests**
+ Low-latency HLS is not supported.
+ Microsoft Smooth Streaming is not supported, and a multiview endpoint cannot use the ISM container.
+ Harvest jobs and live-to-VOD are not supported on multiview endpoints.
+ Time-shifted playback is not supported: the `start` and `end` parameters, clip start time, the startover window, and `EXT-X-START` cannot be used.
+ Time delay is supported up to a maximum of 24 hours.
+ The manifest window cannot exceed 900 seconds (15 minutes).
+ I-frame-only playlists and trickplay tracks are not supported.

**Content protection**
+ A single DRM key covers every view and every layout. Per-view DRM keys are not supported.

  For more information about encryption and DRM, see [Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md).

**Channel operations**
+ Input switching based on MQCS and MQCS publishing in CMSD are not available on multiview channels.