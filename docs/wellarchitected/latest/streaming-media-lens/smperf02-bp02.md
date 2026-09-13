

# SMPERF02-BP02 Use specialized media transport and acceleration protocols
<a name="smperf02-bp02"></a>

Use specialized transport protocols for media contribution to reduce

packet loss and latency over unreliable networks.

**Desired outcome:**
+ You have contribution feeds carried over UDP-based reliable transport protocols tuned for the network type, not Real-Time Messaging Protocol (RTMP) over best-effort TCP.
+ Your contribution path has redundancy (multiple internet service providers (ISPs), bonded cellular, Direct Connect) so a single network fault doesn't take the stream off air.
+ You observe transport-level metrics (packet loss, round-trip time (RTT), retransmissions) in real time and fail over automatically when thresholds are exceeded.

**Common anti-patterns:**
+ Using RTMP for mission-critical contribution over the public internet without a fallback protocol.
+ Running SRT or RIST in production with encryption and authentication disabled.
+ Monitoring only bit rate while ignoring round-trip time, packet loss, and retransmission counts that predict outages.

**Benefits of establishing this best practice:**
+ Lower contribution latency from protocols designed for real-time media
+ Fewer dropped frames through forward error correction and retransmission
+ More efficient use of available bandwidth on constrained paths
+ Stable ingest over public internet or cellular with ARQ-based recovery
+ Ability to contribute from field locations without dedicated fiber

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Contribution and distribution have different transport characteristics. Contribution carries a few high-quality feeds from the field to the origin. Distribution fans those feeds out to viewers through CDNs. The viewer-side is solved by HTTP over TCP and caches, which is why HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH) dominate that layer.

The contribution side has different constraints:
+ One feed
+ Low latency required
+ Unreliable network in the field
+ No chance to pull from cache if a packet is lost

That is the space where UDP-based protocols like Secure Reliable Transport (SRT), Reliable Internet Stream Transport (RIST), and Real-time Transport Protocol (RTP) belong. RTMP persists in contribution mostly because ingest endpoints still accept it, not because its TCP foundation fits the problem.

Within UDP-based contribution, protocol choice comes down to the loss pattern on the network. Random loss responds well to forward error correction (FEC), which adds a fixed overhead and recovers without retransmission. Burst loss exhausts a fixed FEC budget quickly. Automatic repeat request (ARQ) recovers only the packets that actually went missing. Managed networks tend toward predictable random loss and favor FEC. Public internet paths show more bursty behavior and favor ARQ-based protocols like SRT.

### Implementation steps
<a name="implementation-steps"></a>

1. **Evaluate network conditions and contribution requirements:** Assess the network environment and determine transport needs.

1. **Select appropriate transport protocol:** Use SRT for general-purpose low-latency streaming, RIST for professional broadcast workflows, or RTP for real-time media transport with RTP Control Protocol (RTCP) for control.

1. **Configure error correction mechanisms:** Use ARQ for public networks and FEC for managed networks.

1. **Implement Direct Connect:** Set up dedicated connectivity for sustained, high-visibility events.

1. **Set up redundant connectivity:** Use bonded cellular, satellite, or multiple ISPs for resilience.

1. **Configure AWS Elemental MediaConnect:** Establish secure, reliable transport for contribution feeds.

1. **Monitor transport quality metrics:** Track network performance and transport reliability.

1. **Establish failover procedures:** Define processes for handling transport interruptions.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF02-BP01 Start with the highest quality source reasonably obtainable](smperf02-bp01.html)
+ [SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency](smperf06-bp01.html)

**Related documents**
+ [AWS Elemental MediaConnect User
+ [Direct Connect Resiliency

**Related services**
+ [AWS Elemental MediaConnect](https://aws.amazon.com/mediaconnect/)
+ [Direct Connect](https://aws.amazon.com/directconnect/)
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)