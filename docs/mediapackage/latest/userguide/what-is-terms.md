# AWS Elemental MediaPackage concepts and terminology

The following are AWS Elemental MediaPackage concepts and terms to be familiar with.

**Channel group**

A _channel group_ is the top-level resource that consists of channels and
origin endpoints that are associated with it and that provides predictable URLs for stream delivery.
All channels and origin endpoints within the channel group are guaranteed to share the DNS.

**Channel**

A _channel_ represents the entry point for a
content stream into MediaPackage. Upstream encoders such as AWS Elemental MediaLive send
content to the channel. When MediaPackage receives a content stream, it
packages the content and outputs the stream from an endpoint that you
create on the channel. There's one channel for each incoming set of
adaptive bitrate (ABR) streams.

**Endpoint**

An _endpoint_ is part of a channel and represents
the packaging aspect of MediaPackage. When you create an endpoint on a channel,
you indicate what streaming format, packaging parameters, and features
the output stream will use. Downstream devices request content from the
endpoint. A channel can have multiple endpoints.

**Just-in-time packaging**

MediaPackage performs _just-in-time packaging_ (JITP). When a
playback device requests content, MediaPackage dynamically customizes the live
video streams and creates a manifest in a format that's compatible with the
requesting device.

**Origination service**

MediaPackage is considered an _origination service_ because
it's the point of distribution for media content delivery.

**Packager**

A _packager_ prepares output streams for access by
different types of players. The packager type specifies the streaming format
that MediaPackage delivers from the endpoint (either Apple HLS, DASH-ISO, Microsoft
Smooth Streaming, or Common Media Application Format [CMAF]). Additional
packager settings include buffer and update durations and manifest tag
handling instructions.

A packager is a part of an origin endpoint. Each endpoint must have one,
and only one, packager. To use different packager types for the same
content, create multiple endpoints on the channel.

**Source Content**

_Source contents_ are live streams and video files that
MediaPackage ingests.

- For live video, source content comes from an upstream encoder,
  such as AWS Elemental MediaLive. MediaPackage supports HLS source content.

**Stream**

A _stream_ refers to the content input and output of
MediaPackage.

For live workflows, an upstream encoder sends a live
stream as an input to MediaPackage to the channel. When a downstream device
requests playback of the content, MediaPackage dynamically packages the stream
(including specifying the packager type, adding encryption, and configuring
track outputs) and delivers it to the requesting device as an output of the
endpoint. An endpoint can produce multiple streams.

**Track**

_Tracks_ make up the output content stream. MediaPackage
includes selected video, audio, and subtitles or captions tracks in the
output stream. The stream delivers the tracks to the player (either directly
or through a CDN), and the player plays back the tracks based on player
logic or network conditions (such as available bandwidth).
