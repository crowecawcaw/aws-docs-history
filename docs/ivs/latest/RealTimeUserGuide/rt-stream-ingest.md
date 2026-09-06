

# IVS Stream Ingest \| Real-Time Streaming
<a name="rt-stream-ingest"></a>

As an alternative to using the IVS broadcast SDK, you can publish video to an IVS stage from a WHIP or RTMP source. This approach offers flexibility for workflows where using the SDK is not feasible or preferred, such as when publishing video from OBS Studio or a hardware encoder. Whenever possible, we recommend using the IVS broadcast SDK, as we cannot guarantee the performance or compatibility of third-party solutions with IVS.

This diagram illustrates how publishing with WHIP and RTMP works:

![Publishing with WHIP and RTMP.](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/Stream_Ingest.png)


## Supported Protocols
<a name="supported-protocols"></a>

IVS real-time streaming supports several ingest protocols:
+ RTMP and RTMPS — RTMP (Real-Time Messaging Protocol) is the industry standard for transmitting video over a network. RTMPS is the secure version of RTMP that operates over TLS.

  IVS supports multitrack video capability of E-RTMP (Enhanced RTMP). See [E-RTMP Multitrack Video](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#rtmp-multitrack) in the IVS RTMP Publishing documentation.
+ WHIP (WebRTC-HTTP Ingestion Protocol) — An IETF draft developed to standardize WebRTC ingestion.

 For detailed guidance on using these protocols, see our [RTMP](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html) and [WHIP](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/obs-whip-support.html) documentation.

## Supported Media Specifications
<a name="supported-media-specifications"></a>
+ Audio input format
  + Codec: AAC-LC for RTMP and Opus for WHIP
  + Channels: 2 (Stereo) or 1 (Mono)
  + Sample rate: 44.1 kHz or 48 kHz
  + Maximum bitrate: 160 Kbps
+ Video input format
  + Codec: H.264
  + H.264 profile: Baseline
  + IDR interval: 1 or 2 seconds
  + Frame rate: 10 to 60 FPS
  + B-frames: 0

    Note: The IVS broadcast SDK has B-frames enabled by default, but starting with version 1.25.0, it automatically disables B-frames when broadcasting to an IVS stage. For real-time streaming with other RTMP encoders, developers must disable B-frames. *If developers using other RTMP encoders do not disable B-frames, their streams will be disconnected*.
  + Resolution: Maximum: 720p. Minimum: 160p
  + Maximum bitrate: 8.5 Mbps

    Note: For single-track RTMP streams, this limit applies to that track. For multitrack video published using Enhanced RTMP, the limit applies to the combined bitrate of all video tracks.
  + Encoder configuration: We recommend using `veryfast` and `zerolatency` settings for an H.264 encoder. Also: the `sliced_threads` x264 option is included in the `zerolatency` presets, and we recommend that you disable it. For example, when using FFmpeg, your command should include: `-preset:v veryfast -tune zerolatency -x264-params sliced-threads=0`