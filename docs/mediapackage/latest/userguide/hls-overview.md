# HLS and LL-HLS in AWS Elemental MediaPackage

MediaPackage supports HTTP Live Streaming (HLS) and Low-Latency HLS (LL-HLS) for delivering content to a wide range of devices, particularly Apple devices and browsers. HLS is one of the most widely supported adaptive bitrate streaming protocols, while LL-HLS extends the standard HLS protocol to provide reduced latency for near real-time streaming experiences.

## HLS and LL-HLS features and capabilities

When using HLS or LL-HLS in MediaPackage, you can take advantage of the following features:

- **Container types**: HLS and LL-HLS support both TS and CMAF container types, providing flexibility for different use cases.
- **Program date/time**: MediaPackage can insert `EXT-X-PROGRAM-DATE-TIME` tags at configurable intervals, enabling features like viewer seek in the playback timeline and time display on the player.
- **Start tag**: MediaPackage supports adding `EXT-X-START` tags to control where playback begins in the manifest.
- **I-frame only streams**: MediaPackage can include additional I-frame only streams to enable player functionality like fast forward and rewind.
- **Audio rendition groups**: For TS containers, MediaPackage can group all audio tracks into a single rendition group, allowing all other tracks to be used with any audio rendition.
- **SCTE-35 ad markers**: MediaPackage supports signaling ad markers in
  HLS manifests using Daterange format or SCTE-35 enhanced CUE
  tags.
- **Encryption**: HLS supports AES-128 and Sample AES encryption methods with FairPlay (Sample AES only) and Clear Key AES-128 (AES-128 only) DRM systems.

## HLS manifest structure

An HLS manifest is a text-based M3U8 playlist that describes the available media segments and their characteristics. HLS uses a hierarchical structure with two types of playlists:

- **Multivariant playlist**: Contains information about the available variants (different bitrates and resolutions) and references to the media playlists.
- **Media playlist**: Contains references to the actual media segments for a specific variant.

Key tags in HLS manifests include:

- **EXT-X-STREAM-INF**: Describes a variant stream
  in the multivariant playlist.
- **EXT-X-MEDIA**: Describes alternative renditions
  such as audio or subtitles.
- **EXTINF**: Specifies the duration of a media
  segment.
- **EXT-X-PROGRAM-DATE-TIME**: Associates a segment
  with an absolute date and time.
- **EXT-X-KEY**: Specifies how to decrypt encrypted
  segments.
- **EXT-X-SESSION-KEY**: Provides encryption key
  information in the multivariant playlist to enable client key pre-fetching for
  DRM-protected content.
- **EXT-X-DATERANGE**: Signals ad markers and
  program transition events.

LL-HLS extends the standard HLS protocol with additional tags and features to reduce latency:

- **EXT-X-PART**: Identifies partial segments that can be delivered before a complete segment is available.
- **EXT-X-PRELOAD-HINT**: Provides hints to the player about upcoming content.
- **EXT-X-SERVER-CONTROL**: Specifies server parameters for low-latency streaming.

## Differences between HLS and LL-HLS

While HLS and LL-HLS share many features, there are important differences to consider:

- **Latency**: Standard HLS typically has latency of 18-30 seconds, while LL-HLS can achieve latency as low as 3-5 seconds.
- **Program date/time**: Program date/time (PDT) is optional for standard HLS but required for LL-HLS.
- **Segment delivery**: LL-HLS delivers partial segments to reduce latency, while standard HLS delivers complete segments.
- **Player compatibility**: LL-HLS requires players that specifically support the low-latency extensions.

When choosing between HLS and LL-HLS, consider your latency requirements, player compatibility, and the importance of features like trick play (fast forward/rewind).

## HLS and LL-HLS use cases

Consider using HLS or LL-HLS endpoints in the following scenarios:

- Delivering content to Apple devices (iPhone, iPad, Apple TV) and browsers
- Implementing low-latency streaming for live events or interactive experiences (LL-HLS)
- Supporting DRM-protected content with FairPlay or AES-128 encryption
- Creating multi-protocol streaming workflows that need to include HLS alongside other formats
- Enabling advanced playback features like fast forward and rewind with I-frame only streams

For information about creating HLS or LL-HLS endpoints, see [Create an HLS or LL-HLS
manifest](endpoints-create.md#hls-llhls-manifest "endpoints-create.md#hls-llhls-manifest").
