

# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration
<a name="advperf05-bp02"></a>

 Cache static advertising content from edge locations near viewers and to route dynamic requests over a backbone network. This reduces latency for ad creative delivery and provides more consistent performance for dynamic advertising requests globally. 

 **Desired outcome:** 
+  Static advertising content (ad creative images, video assets, JavaScript ad tags) is served from the AWS edge location nearest to viewers, minimizing round-trip latency. 
+  Dynamic advertising requests benefit from the AWS backbone network for the portion of the journey between the edge and your origin, reducing variability introduced by public internet routing. 
+  HTTP/3 (QUIC) is enabled for ad creative delivery to avoid TCP head-of-line blocking and reduce connection establishment overhead for returning viewers. 

 **Common anti-patterns:** 
+  Serving ad creative assets directly from origin infrastructure in a single Region for a globally distributed audience, so every request pays the full geographic distance. 
+  Treating CloudFront as optional for advertising workloads, which overlooks the direct impact slow creative asset delivery has on ad viewability and viewer experience. 

 **Benefits of establishing this best practice:** 
+  Serving content from edge locations reduces the geographic distance between content and users, directly lowering time-to-first-byte for ad creatives. 
+  CloudFront's HTTP/3 support removes TCP head-of-line blocking during parallel VAST asset delivery, which especially helps when a video player fetches multiple ad creative components simultaneously. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Slow creative load times increase the likelihood that a viewer skips or abandons before the ad plays, reducing viewability scores and ultimately CPMs. Amazon CloudFront edge caching addresses this by serving assets from locations near viewers, avoiding the round-trip to origin. 

 For dynamic advertising requests (personalized ad decisions, tracking calls) that can't be cached, CloudFront still routes requests over the AWS backbone network from the edge location to your origin. The request travels over the public internet only from the viewer to the nearest AWS edge location. From the edge to origin, the request traverses the more stable and lower-latency AWS private backbone. 

 HTTP/3 with QUIC addresses two performance limitations: 

1.  **Head-of-line blocking:** In HTTP/2 over TCP, a single lost packet stalls all multiplexed streams until retransmission completes. When a video player fetches a VAST XML response, companion banners, and video segments in parallel over HTTP/2, one packet loss delays the entire ad pod assembly. QUIC streams are independent. A lost packet on one stream pauses only that stream while others continue. 
+  **Connection setup overhead:** HTTP/2 requires a full TCP and TLS handshake (2–3 round trips) for new connections. With QUIC's 0-RTT resumption, returning viewers reuse a previous connection state, so the first byte of ad creative content arrives without a full handshake. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure CloudFront to cache static advertising assets from edge locations:** Create a CloudFront distribution with your origin (S3 bucket or ALB) and configure cache behaviors for static content: ad creative images, video segments, JavaScript ad tags, and CSS assets. Set TTLs using Cache-Control headers from origin (for example, max-age=86400 for stable creative assets, shorter for assets that update with campaign changes). Enable Origin Shield to further reduce origin requests when the same creative is requested from multiple edge locations. 

1.  **Enable HTTP/3 on CloudFront distributions serving ad creatives:** In your CloudFront distribution settings under "Supported HTTP versions," select HTTP/3. CloudFront supports HTTP/3 natively. No origin changes are required. Viewers with HTTP/3-capable clients negotiate QUIC connections automatically. Older clients fall back to HTTP/2 or HTTP/1.1 transparently. 

1.  **Route dynamic advertising requests through CloudFront for backbone optimization:** Configure CloudFront behaviors for dynamic advertising requests (VAST responses, ad decision API calls, tracking pixels) with caching disabled (TTL=0). Even with caching disabled, dynamic requests benefit from routing to the nearest edge location and traversing the AWS backbone to origin, reducing the public internet portion of each request. 

1.  **Monitor CloudFront cache performance:** Configure CloudFront real-time logs to capture cache hit and miss ratios, viewer request latency, and origin response times by request type. Build CloudWatch dashboards showing cache hit rate per cache behavior (creative assets, VAST responses, dynamic endpoints). Set alarms when cache hit rate drops below your target (typically 85%\+ for stable creative assets) to detect TTL configuration issues or cache invalidation patterns that reduce efficiency. 

1.  **Use Lambda@Edge for personalization at the edge:** For advertising workloads where viewer-specific content must be injected into otherwise cacheable responses (for example, inserting a viewer ID into an ad decision redirect), use Lambda@Edge functions to modify requests and responses at CloudFront edge locations, enabling personalization without routing all requests to origin. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [New HTTP/3 Support for Amazon CloudFront](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/) 
+  [CloudFront configuration best practices](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/best-practices.html) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 