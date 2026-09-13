

# Advertising integration
<a name="smperf07"></a>

Ad insertion affects streaming performance, viewer experience, and monetization. SSAI and CSAI have different performance characteristics. Proper ad integration maintains playback continuity while maximizing fill rate.


| SMPERF07: How do you optimize advertising integration for streaming media performance? | 
| --- | 
| [SMPERF07-BP01 Implement Server-Side Ad Insertion (SSAI) for smooth viewer experience](smperf07-bp01.md) | 
| [SMPERF07-BP02 Implement ad prefetching to optimize ad decision server performance and improve fill rates](smperf07-bp02.md) | 

## Capability intent
<a name="smperf07-intent"></a>
+ Ads are stitched into a single stream with matched resolution, bit rate, codec, and frame rate.
+ Ad insertion failures don't break content playback (timeout and fallback).
+ Ad prefetching fills inventory ahead of predictable breaks without violating targeting or expiry rules.

## Maturity levels
<a name="smperf07-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Ads are inserted client-side with no format matching. Mismatches in bit rate, codec, or audio levels are common. No timeout on ad decisioning. | 
| 2 | Emerging | SSAI is partially implemented, but ad creatives are not conditioned to match content format. Timeouts exist but fallback behavior is untested. | 
| 3 | Defined | SSAI stitches ads into a single stream with matched resolution and codec. Timeouts and fallback slate are configured. Prefetching is used for predictable breaks. | 
| 4 | Proactive | Ad creatives are transcoded to match all ABR rungs, audio normalization is enforced, and prefetch expiry controls avoid stale ad delivery. | 
| 5 | Optimized | Ad integration is fully transparent to the viewer with no measurable quality transition. Fill rate and latency are tracked per break, and decisioning failures trigger automated fallback without playback interruption. | 

## Common issues to watch for
<a name="smperf07-issues"></a>
+ Ads encoded at different bit rate, resolution, or codec than the main content causing visible transitions.
+ No timeout on ad decisioning, causing playback stalls when the ad server is slow.
+ Audio level mismatches between content and ads.
+ Prefetching without expiry controls, serving stale or irrelevant ads.