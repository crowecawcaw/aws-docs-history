# HLS playlist types

HTTP Live Streaming (HLS) uses two primary types of playlists: multivariant playlists and media playlists. Understanding the difference between these playlist types is essential for configuring and troubleshooting MediaTailor workflows.

Multivariant playlist

A multivariant playlist is the top-level index file in an HLS streaming workflow that lists all available renditions of the content. It contains references to media playlists but does not contain any media segments itself. The multivariant playlist allows players to select the most appropriate rendition based on network conditions, device capabilities, or user preferences.

This playlist type is also known by several other names in various contexts:

- Master playlist (deprecated term)
- Master manifest (common industry term)
- Primary playlist
- Main playlist
- Index file
- Master M3U8

In MediaTailor workflows, the multivariant playlist is the entry point for playback requests and is where ad personalization begins.

###### Example Multivariant playlist example

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-INDEPENDENT-SEGMENTS
#EXT-X-STREAM-INF:BANDWIDTH=2665726,AVERAGE-BANDWIDTH=2526299,RESOLUTION=960x540,CODECS="avc1.640029,mp4a.40.2",SUBTITLES="subtitles"
index_1.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=4786126,AVERAGE-BANDWIDTH=4547599,RESOLUTION=1280x720,CODECS="avc1.640029,mp4a.40.2",SUBTITLES="subtitles"
index_2.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=8171787,AVERAGE-BANDWIDTH=7768157,RESOLUTION=1920x1080,CODECS="avc1.640029,mp4a.40.2",SUBTITLES="subtitles"
index_3.m3u8
```

Media playlist

A media playlist contains the actual media segment information for a specific rendition (quality level) of the content. It includes timing information, segment URLs, and other metadata required for playback of a single rendition. Each media playlist represents a different combination of resolution, bitrate, and other characteristics.

This playlist type is also known by several other names:

- Variant playlist
- Child manifest (common industry term)
- Chunklist
- Media M3U8
- Rendition playlist

In MediaTailor workflows, media playlists are personalized to include both content segments and ad segments in the proper sequence.

###### Example Media playlist example

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:6
#EXT-X-MEDIA-SEQUENCE:123456
#EXT-X-DISCONTINUITY-SEQUENCE:0
#EXTINF:6.0,
segment123456.ts
#EXTINF:6.0,
segment123457.ts
#EXT-X-DISCONTINUITY
#EXTINF:5.0,
ad-segment1.ts
#EXTINF:5.0,
ad-segment2.ts
#EXT-X-DISCONTINUITY
#EXTINF:6.0,
segment123458.ts
```

###### Note

Both multivariant and media playlists are text-based files that use the `.m3u8` extension. The terminology for these files varies across different documentation and contexts, but the fundamental roles remain the same in the HLS streaming architecture.

When configuring MediaTailor, you typically provide the URL to the multivariant playlist in your content origin. MediaTailor then handles the personalization of both the multivariant playlist and the media playlists to insert ads according to your configuration.

For more information about HLS playlist specifications, see the [HTTP Live Streaming RFC](https://datatracker.ietf.org/doc/html/rfc8216 "https://datatracker.ietf.org/doc/html/rfc8216").
