

# Scenario 10: Implementation of SGAI (Server-Guided Ad Insertion) on AWS

 Server-Guided Ad Insertion (SGAI) is a hybrid approach combining server-side manifest intelligence with client-side ad execution. The server generates manifests with SCTE-35 markers that CDN caches as non-viewer-specific content, while the client device handles personalized ad fetching. This architecture enables CDN-cacheable manifests that scale to millions of concurrent viewers while maintaining per-viewer ad personalization and client-side measurement accuracy. 

## Characteristics
<a name="s10-characteristics"></a>
+  Publisher needs per-viewer personalized ad delivery at FAST channel scale, across millions of concurrent viewers. 
+  Fully server-side SSAI generates per-session manifests, scaling origin infrastructure linearly with viewer count, which is prohibitively expensive at scale. 
+  Low-latency live content (live sports, news) requires early ad break notification to avoid the 15–30 second SSAI latency buffer. 
+  Interactive ad formats (overlays, pause ads, shoppable ads) require client-side rendering capability that SSAI can't support. 
+  Publisher wants CDN cacheability (from hybrid SGAI) combined with per-viewer personalization (from client-side ad fetching). 
+  Measurement beacons from client side provide actual ad renders rather than server-side estimates. 

## Reference architecture
<a name="s10-reference-architecture"></a><a name="scenario-10-fig1"></a>

![SGAI and SSAI parallel deployment architecture on AWS showing the shared MediaLive/MediaPackage origin, CloudFront CDN layer, and the divergent paths for SGAI players (cacheable manifests + client-side personalization) and SSAI players (personalized manifests + server-side stitching)](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-10-sgai-implementation.jpg)

*SGAI and SSAI parallel deployment architecture on AWS showing the shared MediaLive/MediaPackage origin, CloudFront CDN layer, and the divergent paths for SGAI players (cacheable manifests \+ client-side personalization) and SSAI players (personalized manifests \+ server-side stitching)*


 The architecture consists of the following components: 

1.  **AWS Elemental MediaLive**: Encodes live streams and delivers compressed output to MediaPackage V2 for packaging. Outputs to a single MediaPackage Channel and Endpoint serving both SGAI and SSAI paths. 

1.  **AWS Elemental MediaPackage V2**: Packages the stream into both standard HLS and Low-Latency HLS (LL-HLS) formats from a single channel/endpoint. Outputs are used by both SGAI and SSAI players. 

1.  **Amazon CloudFront**: CDN layer between viewers and AWS Elemental MediaTailor. For SGAI players, CloudFront caches non-personalized media playlists (containing SCTE-35 markers) and forwards requests to MediaTailor only on cache misses. For LL-HLS, players poll frequently to pick up partial segments, multiplying the request volume that CloudFront absorbs as cache hits. 

1.  **AWS Elemental MediaTailor (SGAI mode)**: Initialized with ?aws.insertionMode=GUIDED query parameter. Generates non-viewer-specific media playlists with SCTE-35 markers. These manifests are CDN-cacheable, so a single cached copy serves all concurrent viewers. 

1.  **Ad Decision Server (ADS)**: When SGAI players encounter ad breaks, they send personalized requests to the ADS with targeting parameters (device type, geography, and viewing context). The ADS returns an ASSET-LIST with ad pod URLs and tracking information. Deployed on ECS across multiple Availability Zones with PersonalizationThresholdSeconds configured as the MediaTailor safety net. 

1.  **Ad creative CDN (Amazon CloudFront)**: Pre-transcoded ad creatives served from S3 through CloudFront. Pre-transcoded to match content stream profiles during campaign onboarding. Campaign-flight TTLs avoid per-impression origin fetches. 

1.  **AWS Elemental MediaTailor (SSAI mode)**: Parallel path for SSAI players initialized with ?aws.insertionMode=STITCHED. Generates personalized manifests per viewer, which are not CDN-cacheable. Players receive ad segments stitched directly into their personalized playlist. 

1.  **Amazon ElastiCache Serverless (VAST cache)**: Caches VAST/VMAP responses from upstream demand partners, keyed by ad break context with TTL aligned to campaign flight duration. Reduces ADS response latency and upstream SSP API call volume. 

## Configuration notes
<a name="s10-configuration-notes"></a>

### Selecting the ad insertion approach
<a name="selecting-the-ad-insertion-approach"></a>

 Choose your approach based on content type and business requirements: 
+  **SGAI (GUIDED mode)**: For live content (especially live sports), when real-time personalization on CTV is needed, or when interactive ad formats (overlays, pause ads, shoppable ads) are required. CDN-cacheable, with the best scale economics. 
+  **SSAI (STITCHED mode)**: For CTV and FAST channel VOD where uninterrupted playback and ad-blocker resistance are essential and personalization requirements are modest. Per-viewer stitching cost scales linearly with viewers. 

### SGAI ADS deployment
<a name="sgai-ads-deployment"></a>

 Deploy the ADS on ECS across at least 2 Availability Zones with ALB health checks that validate VAST request processing (not just HTTP 200). Set PersonalizationThresholdSeconds in MediaTailor to 2 seconds for live content. If the ADS doesn't respond within threshold, MediaTailor inserts fallback slate automatically. Configure Application Auto Scaling targeting p95 ADS response latency of 200 ms. 

### Pre-transcoded creatives
<a name="pre-transcoded-creatives"></a>

 Transcode all ad creatives during campaign onboarding to match the content stream profile (resolution, codec, and bit rate). Store pre-transcoded creatives on S3 with CloudFront distribution and Cache-Control: max-age TTLs set to the campaign end date. This avoids real-time transcoding latency during ad breaks and reduces per-impression origin fetches to near zero. 

### VAST response caching
<a name="vast-response-caching"></a>

 Deploy Amazon ElastiCache Serverless for VAST/VMAP response caching. Key cache entries by ad break context (content genre, viewer segment, daypart) with TTL aligned to campaign flight duration (30–300 seconds). Target 60%\+ cache hit ratio for recurring ad pod contexts. This reduces both ADS response latency and upstream demand partner API call volume. 

### Low-Latency HLS considerations
<a name="low-latency-hls-considerations"></a>

 For LL-HLS, players poll frequently to pick up partial segments. This multiplies the request volume on the CDN and origin. CloudFront's caching of non-personalized SGAI playlists is critical to absorbing this request volume. Configure CloudFront with short TTLs (seconds) for live manifests and appropriate caching headers so that players consistently receive fresh segment URLs while the playlist itself is cached. 

### Player-side resilience
<a name="player-side-resilience"></a>

 Implement player-side retry with jitter for ad stream fetch failures (maximum 2 retries, 500 ms timeout per attempt, total budget = break duration minus 1 second). Configure partial pod delivery so players serve successfully loaded ads and fill remaining break time with slate rather than abandoning the entire break. Encode SCTE-35 markers in both the HLS manifest (EXT-X-DATERANGE tags) and transport stream (spliceinfo sections) for dual-signal redundancy. 