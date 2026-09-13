

# SMPERF06-BP02 Implement ultra-low latency streaming for real-time interactive experiences
<a name="smperf06-bp02"></a>

Implement Web Real-Time Communication (WebRTC) based streaming solutions to achieve sub-second latency for interactive streaming applications that require real-time viewer engagement.

**Desired outcome:**
+ You have a streaming path with sub-second glass-to-glass latency (typically 200–500 ms) for interactive use cases such as live gaming, auctions, and virtual events.
+ Your ultra-low latency infrastructure is managed rather than built from scratch, letting the team focus on the interactive experience instead of WebRTC plumbing.
+ Your clients fall back gracefully to standard-latency streaming on devices or networks that can't sustain WebRTC.

**Common anti-patterns:**
+ Choosing WebRTC for passive broadcast use cases where Low-Latency HTTP Live Streaming (LL-HLS) or Low-Latency DASH (LL-DASH) would meet the latency requirement at lower cost.
+ Skipping fallback paths for devices or network conditions that WebRTC can't support.
+ Serving high-scale broadcasts with WebRTC only, without hybrid patterns that combine WebRTC and HTTP Live Streaming (HLS) or Dynamic Adaptive Streaming over HTTP (DASH).

**Benefits of establishing this best practice:**
+ Sub-second delivery (200-500 ms) compared to 5-30 seconds with HLS or DASH
+ Real-time viewer participation in auctions, betting, and interactive overlays
+ Consistent timing across all viewers, which is required for competitive or transactional features
+ Lower operational burden when using managed WebRTC services instead of self-hosted infrastructure
+ Adaptive bit rate and network resilience handled at the protocol layer
+ Bidirectional audio and video for use cases that need viewer-to-broadcaster communication

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

WebRTC and HLS or DASH have fundamentally different delivery models with different cost structures. HLS and DASH are HTTP pull protocols. Viewers fetch segments from content delivery network (CDN) caches, so adding a viewer costs almost nothing at the origin. WebRTC is a UDP push protocol. Each viewer holds a session on a media server. The 1,000th viewer costs the same server CPU and bandwidth as the first. That structural cost difference is why WebRTC and HLS are not interchangeable, even when both can meet a latency target. WebRTC delivers sub-second latency but at per-viewer server cost. HLS scales horizontally through CDN caches but adds 5 to 30 seconds of delay. The decision rule follows from whether sub-second delivery changes the product. A viewer chat reacting to a goal has no meaning if the chat appears before the goal is on screen. An auction bid posted at the last second doesn't land unless every viewer sees the clock at the same time. When the viewing experience depends on keeping everyone on the same moment, the per-viewer cost of WebRTC is justified. When viewers only need to watch within a few seconds of live, low-latency HLS or DASH delivers the experience without the per-session server overhead. At broadcast scale, a hybrid pattern usually wins. It uses a small WebRTC cohort for synchronized viewers and HLS delivery for the mass audience watching the same event.

### Implementation steps
<a name="implementation-steps"></a>

1. **Assess use case requirements:** Confirm the interactive use case genuinely needs sub-second latency rather than the low-latency HLS or DASH profiles covered in SMPERF06-BP01. Use cases that typically need sub-second latency include:
+ Gaming
+ Auctions
+ Shopping
+ Betting

1. **Evaluate audience scale and geography:** Size the WebRTC deployment against expected concurrent participants and their regional distribution, since scaling and routing differ from HLS.

1. **Implement Amazon Interactive Video Service (IVS) with WebRTC:** Configure IVS stages for real-time streaming with participant management, set up WebRTC ingestion from broadcasting applications, and enable adaptive bit rate streaming for network resilience.

1. **Configure client-side WebRTC integration:** Use the IVS Web Broadcast SDK for browser-based streaming, integrate the IVS Real-time Streaming SDK for mobile applications, and handle network adaptation and quality adjustments.

1. **Implement fallback mechanisms:** Configure automatic fallback to standard-latency streaming for unsupported devices and set up monitoring for connection quality and participant management.

1. **Optimize for interactive features:** Implement real-time chat and viewer participation features, configure bidirectional audio and video where needed, and set up participant moderation and management controls.

1. **Monitor performance metrics:** Track glass-to-glass latency, monitor connection success rates and quality metrics, and analyze viewer engagement and interaction patterns.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF01-BP01 Select origin technology appropriate for your workload](smperf01-bp01.html)
+ [SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency](smperf06-bp01.html)

**Related documents**
+ [Amazon IVS User Guide - Real-time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/what-is.html)
+ [Amazon IVS Web Broadcast SDK Documentation](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/broadcast-web.html)
+ [New - Deliver Interactive Real-Time Live Streams with Amazon IVS](https://aws.amazon.com/blogs/aws/new-deliver-interactive-real-time-live-streams-with-amazon-ivs/)

**Related services**
+ [Amazon Interactive Video Service (IVS)](https://aws.amazon.com/ivs/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)