# HLS manifest examples

The following sections provide examples of HLS origin manifests and personalized
manifests. Understanding these examples can help you configure and troubleshoot your MediaTailor
workflows.

For information about how query parameters are applied to HLS manifests and segments, see
[MediaTailor
HLS implicit session initialization](manifest-query-parameters-hls-implicit-session-initialization.md "manifest-query-parameters-hls-implicit-session-initialization.md").

## Understanding HLS playlist types

HTTP Live Streaming (HLS) uses two primary types of playlists:

Multivariant playlist

A multivariant playlist is the top-level index file that lists all
available renditions of the content. It contains references to media
playlists but does not contain any media segments itself. This playlist
allows players to select the most appropriate rendition based on network
conditions, device capabilities, or user preferences.

This playlist type is also known by several other names in various
contexts, including master playlist, master manifest, primary playlist, main
playlist, index file, or master M3U8.

In MediaTailor workflows, the multivariant playlist is the entry point for
playback requests and is where ad personalization begins.

Media playlist

A media playlist contains the actual media segment information for a
specific rendition (quality level) of the content. It includes timing
information, segment URLs, and other metadata required for playback of a
single rendition.

This playlist type is also known as media playlist, child manifest,
chunklist, media M3U8, or rendition playlist.

In MediaTailor workflows, media playlists are personalized to include both
content segments and ad segments in the proper sequence.

For more detailed information about HLS playlist types, see [HLS playlist types](hls-playlist-types.md "hls-playlist-types.md").

## HLS origin manifest examples

The following example shows an HLS multivariant playlist that AWS Elemental MediaTailor
received by HLS from the content origin.

```
#EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-INDEPENDENT-SEGMENTS
    #EXT-X-STREAM-INF:BANDWIDTH=2665726,AVERAGE-BANDWIDTH=2526299,RESOLUTION=960x540,FRAME-RATE=29.970,CODECS="avc1.640029,mp4a.40.2",SUBTITLES="subtitles"
    index_1.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=3956044,AVERAGE-BANDWIDTH=3736264,RESOLUTION=1280x720,FRAME-RATE=29.970,CODECS="avc1.640029,mp4a.40.2",SUBTITLES="subtitles"
    index_2.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=995315,AVERAGE-BANDWIDTH=951107,RESOLUTION=640x360,FRAME-RATE=29.970,CODECS="avc1.4D401E,mp4a.40.2",SUBTITLES="subtitles"
    index_3.m3u8
    #EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subtitles",NAME="caption_1",DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,LANGUAGE="eng",URI="index_4_0.m3u8"
```

In this multivariant playlist example:

- The `#EXT-X-STREAM-INF` tags define different renditions with
  varying resolutions and bitrates
- Each rendition references a media playlist (such as
  `index_1.m3u8`)
- The `#EXT-X-MEDIA` tag defines a subtitle track

The following example shows an HLS media playlist that AWS Elemental MediaTailor received by
HLS from the content origin. This example uses `EXT-X-CUE-OUT` and
`EXT-X-CUE-IN` tags to describe ad avail opportunities.

```
#EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-TARGETDURATION:7
    #EXT-X-MEDIA-SEQUENCE:8779957
    #EXTINF:6.006,
    index_1_8779957.ts?m=1566416212
    #EXTINF:6.006,
    index_1_8779958.ts?m=1566416212
    #EXTINF:5.372,
    index_1_8779959.ts?m=1566416212
    #EXT-OATCLS-SCTE35:/DAlAAAAAsvhAP/wFAXwAAAGf+/+AdLfiP4AG3dAAAEBAQAAXytxmQ==
    #EXT-X-CUE-OUT:20.020
    #EXTINF:0.634,
    index_1_8779960.ts?m=1566416212
    #EXT-X-CUE-OUT-CONT:ElapsedTime=0.634,Duration=21,SCTE35=/DAlAAAAAsvhAP/wFAXwAAAGf+/+AdLfiP4AG3dAAAEBAQAAXytxmQ==
    #EXTINF:6.006,
    index_1_8779961.ts?m=1566416212
    #EXT-X-CUE-OUT-CONT:ElapsedTime=6.640,Duration=21,SCTE35=/DAlAAAAAsvhAP/wFAXwAAAGf+/+AdLfiP4AG3dAAAEBAQAAXytxmQ==
    #EXTINF:6.006,
    index_1_8779962.ts?m=1566416212
    #EXT-X-CUE-OUT-CONT:ElapsedTime=12.646,Duration=21,SCTE35=/DAlAAAAAsvhAP/wFAXwAAAGf+/+AdLfiP4AG3dAAAEBAQAAXytxmQ==
    #EXTINF:6.006,
    index_1_8779963.ts?m=1566416212
    #EXT-X-CUE-OUT-CONT:ElapsedTime=18.652,Duration=21,SCTE35=/DAlAAAAAsvhAP/wFAXwAAAGf+/+AdLfiP4AG3dAAAEBAQAAXytxmQ==
    #EXTINF:1.368,
    index_1_8779964.ts?m=1566416212
    #EXT-X-CUE-IN
    #EXTINF:4.638,
    index_1_8779965.ts?m=1566416212
    #EXTINF:6.006,
    index_1_8779966.ts?m=1566416212
    #EXTINF:6.006,
    index_1_8779967.ts?m=1566416212
    #EXTINF:6.006,
    index_1_8779968.ts?m=1566416212
```

In this media playlist example:

- The `#EXTINF` tags specify the duration of each segment
- The `#EXT-X-CUE-OUT` tag marks the beginning of an ad break
- The `#EXT-X-CUE-OUT-CONT` tags provide information about the
  ongoing ad break
- The `#EXT-X-CUE-IN` tag marks the end of the ad break

## HLS personalized manifest

examples

The following example shows an HLS multivariant playlist that AWS Elemental MediaTailor
personalized.

```
#EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-MEDIA:LANGUAGE="eng",AUTOSELECT=YES,FORCED=NO,TYPE=SUBTITLES,URI="../../../manifest/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/3.m3u8",GROUP-ID="subtitles",DEFAULT=YES,NAME="caption_1"
    #EXT-X-INDEPENDENT-SEGMENTS
    #EXT-X-STREAM-INF:CODECS="avc1.640029,mp4a.40.2",AVERAGE-BANDWIDTH=2526299,RESOLUTION=960x540,SUBTITLES="subtitles",FRAME-RATE=29.97,BANDWIDTH=2665726
    ../../../manifest/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0.m3u8
    #EXT-X-STREAM-INF:CODECS="avc1.640029,mp4a.40.2",AVERAGE-BANDWIDTH=3736264,RESOLUTION=1280x720,SUBTITLES="subtitles",FRAME-RATE=29.97,BANDWIDTH=3956044
    ../../../manifest/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/1.m3u8
    #EXT-X-STREAM-INF:CODECS="avc1.4D401E,mp4a.40.2",AVERAGE-BANDWIDTH=951107,RESOLUTION=640x360,SUBTITLES="subtitles",FRAME-RATE=29.97,BANDWIDTH=995315
    ../../../manifest/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/2.m3u8
```

Notice how MediaTailor has modified the media playlist URLs to include session-specific
information that enables personalized ad insertion.

The following example shows a media playlist that AWS Elemental MediaTailor
personalized.

```
#EXTM3U
    #EXT-X-VERSION:6
    #EXT-X-TARGETDURATION:7
    #EXT-X-MEDIA-SEQUENCE:8779957
    #EXT-X-DISCONTINUITY-SEQUENCE:0
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779957.ts?m=1566416212
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779958.ts?m=1566416212
    #EXTINF:5.372,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779959.ts?m=1566416212
    #EXT-X-DISCONTINUITY
    #EXTINF:3.066667,
    ../../../../segment/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0/8779960
    #EXTINF:3.0,
    ../../../../segment/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0/8779961
    #EXTINF:3.0,
    ../../../../segment/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0/8779962
    #EXTINF:3.0,
    ../../../../segment/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0/8779963
    #EXTINF:2.966667,
    ../../../../segment/43f3e412052f2808dd84ea1da90e92e914edddee/external-canary-hls/ee1696a8-4f7f-4c4c-99de-9821131847e8/0/8779964
    #EXT-X-DISCONTINUITY
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779963.ts?m=1566416212
    #EXTINF:1.368,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779964.ts?m=1566416212
    #EXTINF:4.638,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779965.ts?m=1566416212
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779966.ts?m=1566416212
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779967.ts?m=1566416212
    #EXTINF:6.006,
    https://777788889999.mediapackage.us-west-2.amazonaws.com/out/v1/e309ffd02ba8498d864dcaacff7a5ad9/index_1_8779968.ts?m=1566416212
```

In this personalized media playlist example:

- MediaTailor has inserted ad segments between the content segments
- The `#EXT-X-DISCONTINUITY` tags mark the transitions between
  content and ads
- Content segments are served from the origin server (MediaPackage in this
  example)
- Ad segments are served from MediaTailor's ad segment storage

## Key differences in personalized

manifests

When MediaTailor personalizes HLS manifests, it makes several important changes:

Multivariant playlist changes

- Variant playlist URLs are rewritten to point to MediaTailor-managed URLs
  that include session information
- The order of tags may be reorganized for optimal playback

Variant playlist changes

- Ad markers (`EXT-X-CUE-OUT`, `EXT-X-CUE-IN`)
  are replaced with actual ad segments
- Discontinuity markers (`EXT-X-DISCONTINUITY`) are added
  at content/ad boundaries
- Content segment URLs are rewritten to point to the origin or
  CDN
- Ad segment URLs are added to point to MediaTailor's ad segment
  storage

Understanding these changes can help you troubleshoot issues in your MediaTailor workflows
and ensure proper configuration of your CDN and player.

## Related topics

For more information about HLS manifests and MediaTailor, see the following topics:

- [HLS playlist types](hls-playlist-types.md "hls-playlist-types.md") -
  Detailed explanation of HLS playlist types
- [Using a CDN to optimize MediaTailor ad personalization and
  content delivery](integrating-cdn.md "integrating-cdn.md") -
  Information about using a CDN with MediaTailor
- [How MediaTailor ad insertion works](what-is-flow.md "what-is-flow.md") - Overview of how
  MediaTailor ad insertion works
