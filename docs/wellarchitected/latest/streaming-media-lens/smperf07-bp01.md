

# SMPERF07-BP01 Implement Server-Side Ad Insertion (SSAI) for smooth viewer experience
<a name="smperf07-bp01"></a>

Use AWS Elemental MediaTailor to implement SSAI that provides smooth ad integration without client-side complexity while maintaining streaming performance and quality.

**Desired outcome:**
+ You have content and ads delivered through a single stream with matching resolution, bit rate, codec, frame rate, and audio levels so transitions are smooth.
+ Your ad pipeline uses SSAI rather than client-side ad insertion (CSAI), reducing client-side complexity and improving resilience to client-side ad blocking.
+ Your ad decision server (ADS) integration handles timeouts and outages with documented fallbacks so ad delivery failures don't break content playback.

**Common anti-patterns:**
+ Inserting ads with different bit rate, resolution, codec, or frame rate than the main content, causing visible transitions and player re-buffers.
+ Leaving audio levels unnormalized between content and ads, producing jarring volume changes during ad breaks.
+ Running without an ADS timeout and fallback, so ADS outages cause playback failures instead of graceful content continuation.

**Benefits of establishing this best practice:**
+ No visible transition or rebuffer between content and ads because both are in the same stream
+ Consistent resolution, bit rate, and audio level across content and ad segments
+ Less client-side player logic compared to CSAI implementations
+ Resilience to client-side ad blockers since ads are part of the manifest
+ Single analytics pipeline covering both content and ad impressions
+ Works across all playback devices without device-specific ad SDKs

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

SSAI works by stitching ad segments into the content manifest itself. The player sees one uninterrupted stream with no knowledge of which segments are advertising. That single-stream model is what gives SSAI its resilience to client-side ad blockers and its device-agnostic reach. It is also why format alignment between ads and content is non-negotiable. Any deviation in resolution, bit rate, codec, frame rate, or audio level becomes a visible seam in the viewer's session. The cost of SSAI is cache economics. Once ads are personalized per session, each viewer receives a unique manifest, which collapses the cache-hit-ratio for manifests and raises origin and ADS load in proportion to concurrent viewers. Plan manifest-level caching around this reality rather than fighting it, and coordinate with the content delivery network (CDN) strategy covered under cache-hit-ratio monitoring.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure the SSAI service:** Set up the SSAI service configuration with your content origin, integrate with the ADS for ad selection, and define playback configurations for live and video on demand (VOD) content types.

1. **Align content and ad format compatibility:**
+ Match video encoding parameters between content and ads
+ Align audio levels and video quality across content and advertising segments
+ Configure appropriate segment durations for smooth ad transitions
+ Implement content conditioning to match ad specifications

1. **Apply device-agnostic optimizations:**
+ Configure player integration across web, mobile, and connected TV devices
+ Set up manifest manipulation for adaptive streaming protocols
+ Optimize for diverse player capabilities and device constraints
+ Maintain a consistent viewer experience across platforms

1. **Set up ad tracking and analytics:**
+ Configure server-side ad tracking beacons and impression counting
+ Implement viewability measurement and completion tracking
+ Build a unified analytics pipeline across content and advertising
+ Enable real-time monitoring of ad performance metrics

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)
+ [SMPERF05-BP02 Select appropriate encoding settings for your content type and quality targets](smperf05-bp02.html)
+ [SMPERF07-BP02 Implement ad prefetching to optimize ad decision server performance and improve fill rates](smperf07-bp02.html)

**Related documents**
+ [AWS Elemental MediaTailor User Guide](https://docs.aws.amazon.com/mediatailor/)
+ [MediaTailor Ad Insertion Best Practices](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-insertion-best-practices.html)
+ [Server-Side Ad Insertion with AWS Media Services](https://aws.amazon.com/blogs/media/server-side-ad-insertion-with-aws-media-services/)

**Related services**
+ [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)