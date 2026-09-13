

# Live streaming
<a name="scenario-2-live-streaming"></a>

Live video streaming is core to many exciting events, news, and interactive experiences. It is used extensively in social media, sporting events, corporate streaming, e-sports, broadcast TV, and IoT and security camera applications. Because of the real-time nature of live content, special considerations must be taken when architecting live streaming solutions. As with other streaming media workflows, the fundamental architecture components include ingest, processing, origination, and delivery.

One of the unique challenges of live video streaming is that the value of the content being streamed decreases exponentially as time passes from the *live* point. For example, many people might want to watch a sporting event live, but the number of viewers who watch the event hours or days after it takes place tends to decrease as time goes on. Distributors only have one chance to get a live event right, and don't have the luxury of asking viewers to come back later when issues are resolved. As such, it is critically important to verify that live streaming workflows are optimized for reliability and performance.

The cloud is uniquely suited to handling these challenges, with its regional diversity, availability, and elastic scalability. By decoupling the various services involved in live streaming, reliable and high-performing workflows can be built that are cost effective and can scale elastically to handle variations in demand or in live stream counts. It also allows flexibility to include value added services, such as machine learning technologies to perform actions such as automated closed caption and subtitle generation or content tagging and indexing. This type of redundancy, scalability, and developer flexibility isn't possible with monolithic on-premises live streaming applications. The following diagram illustrates a sample live streaming workflow using redundant sources and a Multi-AZ architecture.

## Reference architecture
<a name="scenario-2-reference-architecture"></a>

![Live streaming architecture with a production facility containing two redundant Elemental Live contribution encoders sending feeds into an AWS Region. Within the region, two Availability Zones each contain a MediaConnect ingest service and a MediaLive ABR encoder pipeline. Both pipelines feed into a MediaPackage origin service for origination, which delivers through a CloudFront CDN to player devices.](https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/images/image2.png)


## Configuration notes
<a name="scenario-2-configuration-notes"></a>

1. The Live Stream source encodes a contribution feed at a high quality level (compressed, but at a higher bit rate than will be distributed to viewers). Two contribution encoders are run in parallel for resiliency. When possible, dual network pathing is recommended. Use of embedded timecode is recommended to allow for synchronization of the ABR encoders downstream.

1. The contribution feeds are delivered through a resilient protocol like SRT, Zixi, SMPTE 2022-1 (RTP\+FEC), or 2022-7 (packet merge) to the AWS cloud for ingest. Where possible, dedicated network pathing through Direct Connect can provide dedicated network capacity and deterministic routing for the content streams without traversing public internet segments. A service like AWS Elemental MediaConnect may be used to receive the feeds for delivery to the ABR encoders or forwarding to other parties (e.g. syndication).

1. The ABR encoders run in separate Availability Zones (AZs), each ingesting the feed from one of the two contribution encoders. The ABR encoders create the multiple renditions for the origin service or packager. When supported, the input timecode can be used to keep the encoders synchronized, making smooth failover possible in the origin service or packager, or at the player level. AWS Elemental MediaLive and AWS Elemental MediaPackage offer this functionality natively.

1. The origin and packaging service provides a storage location for the content segments and manifests, and may also dynamically transform the content into supported formats (e.g. HLS, MPEG-DASH, MSS) for various devices and players.

1. The Content Delivery Network (CDN) acts as a caching layer for the origin, consolidating requests and moving content closer to the viewer to improve overall speed of delivery. The CDN may also include processing components to perform viewer authorization and tokenization.