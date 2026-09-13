

# Working with MediaTailor Yield Optimization
<a name="yield-optimization"></a>

Yield Optimization is a feature that automatically monetizes unused ad inventory with Amazon Ads demand during server-side ad insertion (SSAI) for livestreams. At launch, Yield Optimization is available to publishers enrolled in the Amazon Publisher Services (APS) Streaming TV program, with additional demand sources coming over time. Yield Optimization turns unfilled ad breaks into revenue at zero cost to enable and with no additional infrastructure required.

Use Yield Optimization when you need to:
+ **Maximize ad revenue.** Fill remnant inventory that your primary ad decision server (ADS) leaves unfilled, capturing revenue from programmatic demand through Amazon DSP and Sponsored TV.
+ **Improve viewer experience.** Replace repetitive house ads or slate content with relevant programmatic ads during unfilled portions of ad breaks.

## How Yield Optimization fits into the MediaTailor workflow
<a name="yield-optimization-workflow"></a>

When a viewer encounters an ad break during playback, MediaTailor follows this sequence:

1. MediaTailor detects an ad break signal (SCTE marker) from the origin content.

1. MediaTailor requests ads from your primary ad decision server (ADS).

1. The primary ADS returns ads. MediaTailor calculates the remaining unfilled duration.

1. If Yield Optimization is configured, the unfilled duration exceeds the minimum threshold of 15 seconds, and sufficient personalization time remains, MediaTailor sends an OpenRTB bid request to APS. Yield Optimization supports brand safety by passing VAST ad category signals through OpenRTB bid requests. This ensures that competing or restricted ad categories are excluded from the response, preventing conflicting ads from appearing in the same break.

1. APS returns programmatic ads. MediaTailor merges them with the primary ads and enforces deduplication to ensure the same ad is not inserted more than once within a break.

1. MediaTailor returns the complete personalized ad break to the video player.

If the APS request fails or times out, MediaTailor proceeds with only the primary ADS ads. Yield Optimization always fails open. It never blocks or delays the viewer's playback experience.

## Prerequisites
<a name="yield-optimization-prerequisites"></a>

Before you enable Yield Optimization, you must:
+ **Have an active Amazon Publisher Services (APS) Streaming TV publisher account, which is required before you can enable Yield Optimization.** Use your APS Publisher ID to enable Yield Optimization in the MediaTailor console or through the API. See [Integrating with APS](yield-optimization-integrating-aps.md).
+ Have an existing MediaTailor playback configuration.
+ Have a live streaming content source with SCTE ad break markers.

## Supported content types
<a name="yield-optimization-supported-content"></a>

Yield Optimization currently supports:
+ **Live streaming** with HLS and DASH midroll ad breaks (SCTE break duration must be available).

The following are **not supported** in the current release:
+ Video-on-Demand (VOD) content
+ Preroll ad breaks
+ Prefetch workflows
+ Overlay ad requests

**Tip**  
If you are new to Yield Optimization, start with the [Quick start guide](yield-optimization-quickstart.md), then register with APS by following [Integrating with APS](yield-optimization-integrating-aps.md). To understand timing and fail-open behavior, see [How Yield Optimization works](yield-optimization-how-it-works.md).

**Topics**
+ [How Yield Optimization fits into the MediaTailor workflow](#yield-optimization-workflow)
+ [Prerequisites](#yield-optimization-prerequisites)
+ [Supported content types](#yield-optimization-supported-content)
+ [Yield Optimization quick start guide](yield-optimization-quickstart.md)
+ [Integrating with APS](yield-optimization-integrating-aps.md)
+ [How Yield Optimization works](yield-optimization-how-it-works.md)
+ [Bid construction and templating](yield-optimization-bid-construction.md)
+ [ORTB field reference](yield-optimization-ortb-reference.md)
+ [Example templates](yield-optimization-examples.md)
+ [Best practices](yield-optimization-best-practices.md)
+ [Troubleshooting and monitoring](yield-optimization-troubleshooting.md)