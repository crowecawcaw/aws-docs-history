

# SMREL03-BP01 Implement multi-tier distribution with origin redundancy and content delivery network (CDN) failover
<a name="smrel03-bp01"></a>

Design your distribution architecture with redundant origin services across multiple regions and CDN failover mechanisms so that content remains continuously available during component failures or traffic spikes.

**Desired outcome:**
+ Viewers receive uninterrupted streaming content even when individual origin servers, CDN points of presence, or entire regions experience outages or performance degradation.

**Benefits of establishing this best practice:**
+ Removes single points of failure in content delivery
+ Provides automatic scaling to handle traffic spikes
+ Improves global viewer experience through optimized content delivery
+ Reduces origin server load through effective caching strategies
+ Enables rapid recovery from regional outages

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Deploy origin services across multiple Availability Zones and regions with automatic traffic routing based on health checks. Use multiple CDNs to distribute risk and optimize performance based on geographic location and real-time performance metrics. Implement origin shielding to reduce load and provide additional caching layers.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure redundant origin services with automatic failover:** Set up AWS Elemental MediaPackage channels with appropriate origin endpoints and health checks. Consider deploying MediaPackage channels in multiple AWS regions for disaster recovery. Implement origin shielding to reduce direct origin requests and provide additional caching layers.

1. **Configure CloudFront distributions with origin groups:** Set up multiple origins within origin groups for redundancy with health check-based routing. Configure appropriate caching behaviors, time to live (TTL) values, and price class settings for optimal global delivery. Implement Lambda@Edge for dynamic content optimization based on viewer conditions.

1. **Optimize caching and implement quality monitoring:** Configure cache warming for live events, appropriate TTL values for content types, and invalidation workflows. Monitor cache hit ratios and CloudFront performance metrics including error rates. Use AWS Elemental MediaPackage MQCS (Media Quality Confidence Scores) for automated quality assessment.

1. **Set up full monitoring and alerting:** Monitor origin health, CloudFront performance, and viewer experience metrics across all regions. Configure automated alerting for distribution failures, quality degradation, and performance issues. Implement real-time quality monitoring with automatic optimization based on MQCS data.

Build redundancy into your live contribution path from the source to AWS. Single points of failure in contribution will affect your entire streaming workflow and viewer experience.

Choose protocols like SRT (Secure Reliable Transport) and RIST (Reliable Internet Stream Transport) with ARQ (Automatic Repeat Request) in preference to UDP-based Real-time Transport Protocol (RTP) that lack retransmission capabilities. SRT and RIST automatically detect packet loss and request retransmission of missing data. While RTP-FEC (Forward Error Correction) can recover from moderate packet loss using redundant data, it can't recover when packet loss exceeds the FEC overhead ratio and lacks the adaptive retransmission capabilities of ARQ-based protocols.

Implement dual-path contribution using Society of Motion Picture and Television Engineers (SMPTE) 2022-7 (seamless protection switching). Send identical streams over separate network routes so packet loss on one path can be recovered using data from the alternate stream. This helps protect against network path failures without interrupting your live stream.

Deploy redundant contribution encoders in different physical locations. Each encoder should connect to AWS through diverse network paths. If one encoder fails, traffic can failover to the backup encoder without viewer impact.

Monitor contribution stream health continuously. Alert on signal loss, high packet loss rates, or encoder failures. Implement automatic failover between contribution sources when health thresholds are exceeded.

Design file transfer workflows that can recover from network interruptions and validate content integrity. Large media files require reliable transfer mechanisms that can resume after failures.

Use transfer methods with built-in retry logic and checksum validation. Implement bandwidth management to avoid file transfers affecting live streaming operations. Validate all uploaded content before it enters processing workflows. Check file format, duration, and basic quality metrics to catch issues early in the workflow.