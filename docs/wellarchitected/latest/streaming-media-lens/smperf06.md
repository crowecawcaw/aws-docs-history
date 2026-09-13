

# Latency optimization
<a name="smperf06"></a>

Live streaming latency affects viewer engagement, especially for interactive content and live events. Reducing latency requires coordinated optimization across encoding, packaging, delivery, and player layers, and involves trade-offs with quality and reliability.


| SMPERF06: What tradeoffs have you made to lower live glass-to-glass latency? | 
| --- | 
| [SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency](smperf06-bp01.md) | 
| [SMPERF06-BP02 Implement ultra-low latency streaming for real-time interactive experiences](smperf06-bp02.md) | 

## Capability intent
<a name="smperf06-intent"></a>
+ Latency targets are set per use case and balanced against quality and reliability requirements.
+ Optimization spans all layers (encoder, packager, CDN, and player buffer) rather than targeting one in isolation.
+ Ultra-low-latency delivery is reserved for interactive use cases where sub-second matters.
+ Graceful fallback to standard latency is available for unsupported clients or degraded networks.

## Maturity levels
<a name="smperf06-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Latency isn't measured or targeted. Default segment durations and player buffer settings are used without tuning. | 
| 2 | Emerging | The team has reduced segment length in one layer but has not coordinated changes across encoder, CDN, and player. No fallback exists for unsupported clients. | 
| 3 | Defined | Latency targets are set per use case, optimization spans all layers, and a fallback path exists for clients that can't support low-latency protocols. | 
| 4 | Proactive | Glass-to-glass latency is measured across all stages, protocol selection matches the interactivity requirement, and ultra-low-latency is reserved for use cases that need it. | 
| 5 | Optimized | Latency budgets are allocated per layer and tracked continuously. The system adapts segment size and buffer targets dynamically based on network conditions while maintaining graceful degradation. | 

## Common issues to watch for
<a name="smperf06-issues"></a>
+ Reducing segment length without matching changes in other layers.
+ Chasing latency numbers without researching whether viewers notice the difference.
+ WebRTC deployed for passive broadcast where low-latency HLS would suffice.
+ No fallback path for devices that don't support the chosen low-latency protocol.