# Amazon IVS Multitrack Video: Setup Guide

This document is focused on customers that integrate Amazon IVS APIs and SDKs into their applications.

## Adopting Multitrack Video Streaming

To adopt multitrack video, there are two required [channel](../LowLatencyAPIReference/API_Channel.md "../LowLatencyAPIReference/API_Channel.md") configurations and a recommended [thumbnail configuration](../LowLatencyAPIReference/API_ThumbnailConfiguration.md "../LowLatencyAPIReference/API_ThumbnailConfiguration.md").

### Required: Configure Channel ContainerFormat

Multitrack video may configure the broadcast software to use advanced codecs (e.g., HEVC), which are not compatible with MPEG2 Transport Stream (TS) files. Before using multitrack video, you must set `Channel.ContainerFormat` to `FRAGMENTED_MP4`.

Changing the `ContainerFormat` value changes the format of media files for both live distribution and S3 recordings (if enabled). You may need to update third-party player applications or downstream workflows that depend on the media container format.

### Required: Configure Channel MultitrackInputConfiguration

Broadcast software tools that support IVS multitrack video are required to implement automatic stream configuration through the GetClientConfiguration API operation. For broadcast-software integration details, see the [Multitrack Video Broadcast Software Integration Guide](multitrack-video-sw-integration.md "multitrack-video-sw-integration.md").

Channels with multitrack inputs have a more dynamic ABR ladder (on a per-channel and streaming-session basis) that is optimized for the creator’s setup, the network environment, and the IVS control plane. When content creators start streaming with their software (e.g., OBS Studio), the client collects and sends to GetClientConfiguration the following information:

- The creator’s preferences, including display/canvas resolution, maximum aggregate bitrate, reserved encoder sessions/bandwidth, and framerate.
- The creator's hardware/OS metadata, including GPU model, GPU memory, GPU driver version, OS version, CPU model, and system memory.

A server-side algorithm scores and ranks the configurations, to deliver a configuration that:

- Optimizes the viewer experience (highest resolution, framerate, bitrate, and number of renditions).
- Is safely supported by the streamer’s setup.
- Obeys limits configured by the `MultitrackInputConfiguration` channel property.

Finally, the broadcast software applies the configuration and starts sending multiple video tracks using the [enhanced RTMP](https://veovera.org/docs/enhanced/enhanced-rtmp-v2 "https://veovera.org/docs/enhanced/enhanced-rtmp-v2") protocol.

To adopt multitrack video, you must configure `Channel.MultitrackInputConfiguration` and the sub-properties specified in [MultitrackInputConfiguration](../LowLatencyAPIReference/API_MultitrackInputConfiguration.md "../LowLatencyAPIReference/API_MultitrackInputConfiguration.md").

- To balance cost and quality, determine the correct value for `Channel.MultitrackInputConfiguration.MaximumResolution`, to set a maximum input resolution on a per-channel basis. When the broadcast client calls GetClientConfiguration, this field determines the resolution of the largest possible input track. If any client sends a different number of tracks, or the per-track resolution, framerate, codec, or bitrate do not match the GetClientConfiguration response, the client will be disconnected.
- To provide your broadcasters with flexibility in adoption, configure `Channel.MultitrackInputConfiguration.Policy` to `allow` or `require` broadcast clients to connect with multitrack input. When the client connects using RTMP, this field determines if the broadcaster is allowed or required to send multitrack video. You can choose to make it simpler for broadcasters to slowly adopt multitrack video flexibility (with `allow`) or require broadcasters to use multitrack clients to optimize for lower cost (with `require`).

### Recommended: Review and Update ThumbnailConfiguration

If you enable thumbnailing for multitrack-enabled channels, a multitrack client is connected, and you do not specify a `resolution`, thumbnails for all input tracks are recorded. To control costs, you may want to specify a specific rendition.

The paths for the highest quality path are at the same relative locations for multitrack-input and single-track input streams. The thumbnails for additional tracks are recorded to an `additional_thumbnails` sub-key. We recommend that you use the metadata JSON file written to S3, to identify the appropriate thumbnail paths.

## Broadcaster System and Environmental Requirements

Broadcast clients that support IVS multitrack video are required to implement the GetClientConfiguration API operation, to automatically configure broadcaster stream settings. In the real world, limitations include older GPUs, poor first-mile networks, specific user settings, contention of GPU resources, and limited platform codec support. When faced with these limitations, automatic stream configuration should fall back gradually and sensibly; for example:

- Vary the aggregate bitrate between 10.2 Mbps (5 renditions) and 1.5 Mbps (2 renditions).
- Vary the highest quality track’s maximum resolution from 1080p (4 or 5 renditions) down to 480p (2 renditions).
- Vary the number of renditions between 5 (1080p, 720p, 480p, 360p, 160p) and 2 (480p, 360p).
- Vary the selection of renditions across an expansive set of supported resolutions (1080p, 720p, 540p, 480p, 360p, 240p, and 160p).
- Vary the bitrates of individual renditions from 6 Mbps (e.g., 1080p60 AVC) down to 200 Kbps (e.g., 160p AVC).
- Vary the framerate between high (60, 50, or 48 fps) and standard (30, 25, or 24 fps).
- Vary the video codec to balance safety/viewer support and codec efficiency (H.264/AVC and H.265/HEVC).
- Vary the scaler algorithm to balance GPU resources (e.g., Lanczos, bicubic, and bilinear).
- Vary video-encoding settings (including codec profile, encoder preset, look-ahead window, psycho visual AQ, and number of B-frames), depending on the GPU vendor and driver version.

The following table provides our recommendations in terms of hardware, software, and environmental configuration:

| Use Case                     | FULL_HD Streaming                                                                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| GPU and driver version       | NVIDIA GeForce 900-series or newer with NVIDIA driver 545.92 or newer<br>AMD Radeon RX 6000/7000 Series or newer with AMD Adrenalin 24.4.1 minimum |
| Display                      | 1920x1080 at 60fps                                                                                                                                 |
| Sustained upstream bandwidth | 12 Mbps                                                                                                                                            |
| Operating system             | Windows 10 or Windows 11                                                                                                                           |
| Broadcast software           | OBS Studio v30.2 (or newer)                                                                                                                        |
