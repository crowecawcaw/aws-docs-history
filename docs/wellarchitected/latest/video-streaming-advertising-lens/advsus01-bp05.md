

# ADVSUS01-BP05 Serve cacheable ad manifests to reduce origin requests and server-side compute at scale

 Server-guided ad insertion (SGAI) generates non-personalized media manifests with standard ad markers that a content delivery network can cache and reuse across many viewers. Server-side ad insertion (SSAI), by contrast, stitches a viewer-specific manifest for each session, which defeats shared caching and makes origin load grow with the audience. At live FAST-channel scale, choosing cacheable manifests reduces origin requests and the server-side compute behind them. 

 **Desired outcome:** 
+  SGAI manifests are non-viewer-specific and CDN-cacheable, substantially reducing origin requests and the server-side compute they drive compared with per-viewer SSAI. 
+  Ad creatives are pre-transcoded during campaign onboarding, so playback never triggers real-time transcoding at the moment of an ad break. 
+  The ad decision service is colocated with the manifest and caching tiers to minimize per-decision network traversal. 

 **Common anti-patterns:** 
+  Generating a personalized, viewer-specific manifest for every session in workflows where the ad payload doesn't actually differ per viewer, which defeats CDN caching and scales origin load with the audience. 
+  Transcoding ad creatives in real time during the ad break instead of preparing them ahead of campaign flight puts compute on the critical path at its most latency-sensitive moment. 
+  Serving ad creatives directly from the origin on every request rather than caching them at the edge, which repeats identical fetches for the same creative. 
+  Scaling ad-decision capacity reactively after prime-time demand has already arrived leaves requests queued and compute spent on retries and backpressure. 
+  Placing the ad decision service far from the manifest and caching tiers, so every ad decision pays avoidable cross-network latency. 

 **Benefits of establishing this best practice:** 
+  Fewer origin requests and lower server-side compute at scale, which is the practical proxy for reduced energy and carbon across live ad-supported streaming. 
+  Lower and more predictable ad-break latency because manifests are served from cache and creatives are pre-transcoded. 
+  Reduced cost from edge caching, creative reuse, and capacity provisioned ahead of demand rather than during it. 
+  Less risk of viewer-facing rebuffering and ad-break stalls during peak audience events. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Ad-insertion sustainability depends on whether the manifest a viewer receives is shared across viewers or unique to each session. When the ad payload varies per viewer, server-side stitching is unavoidable, but many live and FAST-channel workflows insert the same ads for large audience segments. In those cases every session becomes a cache miss, so origin requests and server-side compute grow linearly with concurrent viewers instead of staying flat. Identify which workflows need per-viewer personalization and which only inherited it from an SSAI default. 

 Transcoding a creative to match the content profile is unavoidable work. Real-time transcoding during playback puts that compute on the critical path at the most latency-sensitive moment. Transcoding once during campaign onboarding amortizes it across every impression. Network placement has the same effect. When the ad decision service, manifest service, and cache sit far apart, each ad decision adds cross-network latency that caching cannot eliminate. Move predictable work earlier, and move frequently accessed objects closer to the viewer. 

 A high manifest cache-hit ratio is a direct signal that you have removed per-viewer origin work. The origin-request reduction at FAST scale depends on your audience concurrency and content mix, so measure it in your workload. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure MediaTailor in SGAI mode for CDN-cacheable manifests:** Set aws.insertionMode=GUIDED in AWS Elemental MediaTailor playback session parameters so manifests are non-personalized. Configure Amazon CloudFront to cache the SGAI playlists. Track the manifest cache-hit ratio and treat a high ratio as the signal that per-viewer origin processing has been avoided, setting your target from observed audience concurrency rather than a fixed headline figure. 

1.  **Pre-transcode ad creatives during campaign onboarding:** For each ad creative, transcode to match the content stream profile (resolution, codec, and bit rate) during trafficking. Store pre-transcoded creatives in Amazon S3 with CloudFront distribution. Set cache TTLs aligned to campaign flight dates. This removes the need for real-time transcoding compute during ad breaks. 

1.  **Cache VAST and VMAP responses in Amazon ElastiCache colocated with the ad decision service:** Configure VAST and VMAP response caching in Amazon ElastiCache Serverless with a TTL matching campaign flight duration (on the order of tens to a few hundred seconds), and place the cache in the same Availability Zone as the ad decision service. Measure the cache hit ratio for recurring ad pods and tune the TTL against ad-freshness needs. Each cache hit avoids an upstream SSP API call, reducing network traversal and compute. 

1.  **Implement predictive ADS scaling:** Configure scheduled scaling to pre-scale ADS capacity ahead of anticipated prime-time peaks, setting the lead time from how long your own capacity takes to become ready and from the observed shape of the demand ramp. Pre-scaling avoids the reactive scaling cycle where demand exceeds capacity, which queues requests and wastes compute. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP02 Choose HTTP/2 or HTTP/3 to lower bytes transferred and connection overhead](advsus01-bp02.md) 

 **Related documents:** 
+  [Server-guided ad insertion in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/server-guided.html) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon ElastiCache Serverless](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 