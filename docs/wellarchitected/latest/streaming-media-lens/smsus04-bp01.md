

# SMSUS04-BP01 Design efficient, scalable live streaming workflows
<a name="smsus04-bp01"></a>

Run live streaming workflows so that processing resources are provisioned for the duration and audience of each event, not held continuously at peak capacity. Live workloads are uniquely wasteful when left running between events or over-provisioned for a latency target the use case doesn't need, because encode and packaging resources are consumed for the whole window whether viewers are watching.

**Desired outcome:**
+ Live channels and their supporting resources run only for the scheduled event window and scale to the actual concurrent audience.
+ The latency tier for each event is chosen deliberately, so resources are spent on ultra-low latency only where the experience requires it.
+ Pipeline redundancy is applied where availability requires it, not as a blanket default that doubles resource use for every channel.

**Common anti-patterns:**
+ Leaving live encoding channels running between events, so encode compute is consumed continuously for a workflow that is idle most of the time.
+ Defaulting every event to the lowest available latency tier, incurring the extra encode and packaging overhead of ultra-low latency for content where a few seconds of delay is acceptable.
+ Provisioning standing redundant pipelines for all channels regardless of the availability requirement, so resource use is doubled even for low-stakes events.
+ Sizing live infrastructure for a theoretical peak audience rather than the expected concurrent viewers, leaving capacity powered and unused.

**Benefits of establishing this best practice:**
+ Lower encode and packaging energy, because channels consume resources only during scheduled events and at the latency tier the event requires.
+ Reduced idle capacity, because supporting components scale to real concurrent demand rather than a static peak assumption.
+ Lower delivery cost that tracks the reduction in channel runtime and provisioned redundancy.
+ Maintained resilience for events that need it, because redundancy is targeted rather than uniform.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

A live workflow differs from on-demand in that its resource cost is governed by time and concurrency rather than catalog size. An encoding channel consumes compute for every minute it runs, so the largest avoidable waste in live streaming is channels left active between events or sized for an audience that never arrives. Starting and stopping channels around the event schedule, and scaling supporting components to observed concurrency, aligns resource use with the work actually being done.

Treating ultra-low latency as a universal default is the most common way live workflows over-consume. Lower latency requires shorter segments and more frequent packaging and delivery operations, which raises the per-minute resource cost of the channel. For interactive experiences such as live auctions or sports betting, that delay is worth the cost. For a keynote or a concert stream, a few seconds of latency is imperceptible to the experience and the extra resource cost buys nothing. Choose the latency tier per event from the experience requirement, not from wanting to minimize latency everywhere.

Standing redundant pipelines protect against failure but double the resources a channel consumes for its entire run, so apply them where the availability requirement justifies the cost and rely on event-driven recovery for lower-stakes events. Energy use isn't measurable per stream, so track resource proxies, channel run-hours, encode compute hours, and provisioned redundant pipeline-hours. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps
<a name="implementation-steps"></a>

1. **Start and stop channels around the event schedule:** Automate AWS Elemental MediaLive channel start and stop against the event calendar so channels are not left running between events. Idle channel time is pure waste in a live workflow.

1. **Choose the latency tier per event:** Match the delivery latency to the experience requirement.
+ Reserve ultra-low-latency delivery (for example, Amazon Interactive Video Service (Amazon IVS) for interactive use cases) for events that genuinely need it
+ Use standard low-latency HTTP Live Streaming (HLS) or Dynamic Adaptive Streaming over HTTP (DASH) for content where a few seconds of delay is acceptable

1. **Encode live with quality-defined variable bit rate:** Configure MediaLive with quality-defined variable bit rate (QVBR) so live encodes spend bit rate according to content complexity rather than a fixed ceiling, reducing delivery bits without a perceptible quality loss.

1. **Scale supporting components to concurrency:** Drive the following with event-driven scaling tied to concurrent-viewer metrics, so supporting infrastructure tracks the actual audience rather than a peak assumption.
+ Packaging
+ Origin
+ Any real-time processing

1. **Apply pipeline redundancy selectively:** Enable standing pipeline redundancy only for events whose availability requirement justifies the doubled resource cost. For lower-stakes events, rely on automated restart and recovery instead of persistent redundancy.

1. **Measure live efficiency:** Track the following per event, and review them against the monthly account-level figures from the AWS Customer Carbon Footprint Tool to confirm changes reduce consumed resources.
+ Channel run-hours
+ Encode compute hours
+ Redundant pipeline-hours

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS03-BP01 Implement efficient encoding and delivery mechanisms](smsus03-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Live Streaming on AWS](https://aws.amazon.com/solutions/implementations/live-streaming-on-aws/)

**Related services**
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)
+ [Amazon Interactive Video Service](https://aws.amazon.com/ivs/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)