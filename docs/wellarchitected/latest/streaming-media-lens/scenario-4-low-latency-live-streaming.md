

# Low-latency live streaming
<a name="scenario-4-low-latency-live-streaming"></a>

There are use cases where the overall latency (often referred to as glass-to-glass latency) of the video delivery is of critical importance. Examples include simulcast with terrestrial TV, and betting or auction platforms. While specialized workflows can deliver low latency streaming (for example, WebRTC based transmission) they can be difficult to scale for high-viewership events. Therefore, it's desirable to use existing streaming workflows and optimize them to reduce overall latency as much as practicable.

Choice of contribution codec and transport protocols both impact latency. If ample bandwidth and redundant network pathing is available, contribution through JPEG-XS over ST-2110 can deliver high-quality contribution with measurable latency reductions over typical AVC or HEVC on TS contribution. In situations where the needed bandwidth isn't available, it's possible to tune AVC and HEVC encodes in favor of latency, and optimize ARQ-based transport to minimize the amount of buffering required for error recovery.

Distribution encoding can also be optimized to reduce overall latency. Services that offer advanced encoding configurations, like AWS Elemental MediaLive, give the user the kind of fine-grained control needed to achieve the desired outcome.

Recent developments in both the HLS and DASH standards provide mechanisms for greatly reducing latency between origin and player, yet maintaining the scalability HTTP-based delivery is known for. Dynamic packagers supporting these newer HLS and DASH features can significantly reduce overall playback latency for live workflows.

## Reference architecture
<a name="scenario-4-reference-architecture"></a>

![Low-latency live streaming architecture with a production facility containing two redundant Elemental Live contribution encoders connected through two AWS Direct Connect links into an AWS Region. Within the region, two Availability Zones each contain a MediaConnect ingest service and a MediaLive ABR encoder pipeline. Both pipelines output to a MediaPackage origin service using LL-HLS for origination, which delivers through a CloudFront CDN to player devices.](https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/images/image4.png)


1. Two contribution encoders take the incoming signal and convert it to JPEG-XS for low-latency, visually lossless compression. The encoders send their output as SMPTE 2110-22 through redundant dedicated links (Direct Connect) to ingest receivers in two Availability Zones (AZs).

1. The Ingest receiver (for example, AWS Elemental MediaConnect) receives the contribution feed and converts it to an uncompressed format to send through Cloud Digital Interface (CDI).

1. The ABR encoders (for example, AWS Elemental MediaLive) receive the CDI input and create the ABR outputs using encoding settings optimized for latency reduction, outputting to an origin and packaging service.

1. The origin packager generates the low-latency manifests (e.g. LL-HLS in AWS Elemental MediaPackage v2) for delivery through CDN and ultimately to players as usual.

1. Supported players retrieve the partial HLS segments as quickly as they are made available. Unsupported players are expected to ignore the partial segments per the HLS specification.

## Configuration notes
<a name="scenario-4-configuration-notes"></a>
+ If sufficient bandwidth and redundant pathing isn't available from production site to the cloud, consider using traditional TS contribution with encode parameters optimized for lower latency. ARQ-based protocols like Zixi or SRT can be configured with reduced minimum latency depending on the overall round-trip time (RTT) between production site and cloud ingest. Review this [blog post](https://aws.amazon.com/blogs/media/how-to-configure-a-low-latency-hls-workflow-using-aws-media-services/) for an example LL-HLS workflow using AWS Media Services.
+ For a fully managed, complete solution, Amazon IVS Low-Latency can deliver latency between 2-5 seconds when used with a supported player.
+ For smaller size audiences, a connection-based delivery system utilizing WebRTC can deliver video at low latency, but it does not scale to millions of viewers as HTTP based streaming can. For example, IVS Real-Time Streaming can deliver with latency as low as 300ms for up to 25,000 concurrent viewers.
+ It is important to verify that your CDN caching settings are suitable for low latency delivery. For example, HLS manifests will need a shorter TTL than would normally be used. Amazon IVS low-latency includes built-in CDN functionality that is tuned for delivery of low-latency video.