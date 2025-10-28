# IVS WHIP Publishing | Real-Time Streaming

This document explains how to use WHIP-compatible encoders like OBS to publish to IVS
real-time streaming. [WHIP](https://www.ietf.org/archive/id/draft-ietf-wish-whip-01.html "https://www.ietf.org/archive/id/draft-ietf-wish-whip-01.html")
(WebRTC-HTTP Ingestion Protocol) is an IETF draft developed to standardize WebRTC
ingestion.

WHIP enables compatibility with software like OBS, offering an alternative (to the IVS
broadcast SDK) for desktop publishing. More sophisticated streamers familiar with OBS may
prefer it for its advanced production features, such as scene transitions, audio mixing, and
overlay graphics. This provides developers with a versatile option: use the IVS web
broadcast SDK for direct browser publishing or allow streamers to use OBS on their desktop
for more powerful tools.

Also, WHIP is beneficial in situations where using the IVS broadcast SDK isn't feasible or
preferred. For example, in setups involving hardware encoders, the IVS broadcast SDK might
not be an option. However, if the encoder supports WHIP, you can still publish directly from
the encoder to IVS.

**WHIP requirements:**

- Your SDP offer must include an H.264 video track, even if you are only publishing
  audio. If the offer does not include a video track, the connection will be
  rejected.
- The global WHIP endpoint (https://global.whip.live-video.net) returns a 307
  Temporary Redirect. WHIP clients must handle 307 redirects correctly and persist
  headers in the redirected request, as required by the WHIP specification.

## OBS Guide

OBS supports WHIP as of version 30. To start, download OBS v30 or newer: [https://obsproject.com/](https://obsproject.com/ "https://obsproject.com/").

To publish to an IVS stage using OBS via WHIP, follow these steps:

1. [Generate](getting-started-distribute-tokens.md "getting-started-distribute-tokens.md") a participant token with publish capability. In WHIP
   terms, a participant token is a bearer token. By default, participant tokens
   expire in 12 hours, but you can extend the duration up to 14 days.
2. Click **Settings**. In the **Stream** section of the **Settings**
   panel, select **WHIP** from the **Service** dropdown.
3. For the **Server**, enter
   https://global.whip.live-video.net.
4. For the **Bearer Token**, enter the participant
   token that you generated in step 1.
5. Configure your video settings as you normally would, with a few
   restrictions:
   1. IVS real-time streaming supports input up to 720p at 8.5 Mbps. If you
      exceed either of these limits, your stream will be disconnected.
   2. We recommend setting your **Keyframe
      Interval** in the **Output**
      panel to 1s or 2s. A low keyframe interval allows video playback to
      start more quickly for viewers. We also recommend setting **CPU Usage Preset** to **veryfast** and **Tune** to
      **zerolatency**, to enable the lowest
      latency.
   3. Because OBS does not support simulcast, we recommend keeping your
      bitrate below 2.5 Mbps. This enables viewers on lower-bandwidth
      connections to watch.

6. Press **Start Streaming**.

**Note**: We are aware of quality issues (like
intermittent video freezing) that can occur with WHIP in OBS. These typically arise when
the broadcaster's network is unstable. We recommend testing WHIP in OBS before using it
for production live streams. Lowering your broadcast bitrate also may help reduce the
occurrence of these issues.
