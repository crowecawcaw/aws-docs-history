

# ADVPERF06-BP05 Minimize SGAI ad break latency with CDN-cached manifests, pre-transcoded creatives, and scaled ADS
<a name="advperf06-bp05"></a>

 Ad breaks in SGAI (Server-Guided Ad Insertion) workflows must start with no viewer-perceptible buffering. Non-personalized manifests stay cacheable on a CDN, so origin requests don't grow with viewer count, and a pre-transcoded creative library removes transcoding from the critical path between the ad decision and playback. 

 **Desired outcome:** 
+  Ad breaks start with no viewer-perceptible buffering, and the ad decision completes inside the configured ad decision server (ADS) request timeout. 
+  The ADS sustains peak concurrent request rates across FAST channels without latency degradation at prime-time onset. 
+  Non-personalized SGAI manifests are served from CDN cache, so origin load doesn't scale linearly with viewer count. 
+  Pre-transcoded creatives are stitched without transcoding, removing conditioning latency from the ad break. 

 **Common anti-patterns:** 
+  Generating viewer-specific manifests server-side (SSAI mode) rather than non-personalized SGAI manifests, which defeats CDN caching and increases origin load linearly with viewer count. 
+  Supplying only progressive-delivery creatives to the ad decision server, so ad conditioning stays in the critical path of every break. 
+  Deploying the ADS in a different Region from the MediaTailor playback configuration, which adds tens of milliseconds to every ad decision request. 
+  Treating the personalization threshold as a latency control, which changes underfill behavior instead and can abandon partially filled breaks. 
+  Fetching ad decisions from upstream demand partners on every request without caching, so the same upstream calls repeat at prime-time peaks. 

 **Benefits of establishing this best practice:** 
+  Cacheable SGAI manifests serve one cached copy to many concurrent viewers, scaling FAST channel ad serving without per-viewer origin processing. 
+  Preconditioned creatives are stitched directly from the ADS response, so no transcoding step sits between the ad decision and the break. 
+  Caching the ad decision reduces per-request decision latency and absorbs upstream demand-partner response variability. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 SGAI separates manifest generation from ad personalization. MediaTailor emits cacheable, non-personalized media playlists carrying [HLS interstitial](https://docs.aws.amazon.com/mediatailor/latest/ug/server-guided.html) markers: an EXT-X-DATERANGE tag with CLASS="com.apple.hls.interstitial" and an X-ASSET-LIST URI, derived from the SCTE-35 signals in the upstream manifest. Those playlists contain no viewer-specific data, so one cached copy serves many concurrent viewers, unlike SSAI, which generates a unique manifest per viewer session and scales origin infrastructure linearly with viewer count. 

 The request path determines where the latency budget is spent. The player never contacts the ADS directly. When the play head nears the interstitial marker, the player requests the X-ASSET-LIST URI from [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/), and MediaTailor then calls the ADS, receives the VAST or VMAP response, and returns a personalized asset list to the player. Every ad decision traverses MediaTailor, and the timeouts that bound it belong to MediaTailor, not the player. [AdsRequestTimeoutMilliseconds](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdsPersonalizationTimeouts.html) caps how long MediaTailor waits for a single ADS response, defaulting to 3000. LiveMaximumAdsPersonalizationTimeMilliseconds caps total ADS activity for a live manifest including VAST wrapper redirects, defaulting to 10000. Tighten both to the budget the break can absorb. 

 [PersonalizationThresholdSeconds](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PlaybackConfiguration.html) sets the maximum duration of *underfilled* ad time tolerated in a break, and it applies to ad replacement rather than ad insertion because it depends on an underlying content stream. Exceed it and MediaTailor abandons personalization for that break and shows the underlying content. Set it too low against a partially filled avail and you discard breaks you could have monetized, so derive the value from expected fill rate and avail duration. AWS's live SGAI example configuration uses 1, and the valid minimum is 1. 

 Tighter co-locataion when placing Regions does not always work when services are in contact with each other. MediaTailor is a regional managed service with no Availability Zone to colocate against, and intra-Region cross-AZ latency is negligible against any ad-decision budget. Deploy the ADS in the same Region as the playback configuration and spread its tasks across at least two Availability Zones. 

 Preconditioning is also on the critical path. Transcoding ads to match the content stream is MediaTailor's default behavior and happens after the VAST response arrives, so pre-transcoding creatives to [Amazon S3](https://aws.amazon.com/s3/) doesn't remove it on its own. MediaTailor skips conditioning only when the playback configuration's [streaming media file conditioning](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) is set to NONE and the ADS returns direct links to the pre-transcoded streaming manifests. Treat CloudFront as a cache in front of S3 rather than the storage tier. The first request per edge location is a miss. 

 What you cache in front of the ADS determines whether caching is safe. Reusing a verbatim VAST body across requests re-serves the tracking and impression URIs it contains, which misreports delivery. Cache the decision instead, meaning which creatives play in what order for a given context key, and regenerate the tracking URIs per request. Confirm with each upstream demand partner that response reuse is permitted under the integration terms before you enable it. A decision cache TTL bounds pacing and budget staleness, not campaign flight length. Anchor it to the interval you can tolerate being wrong about pacing, because a longer TTL raises overdelivery risk. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable guided ad insertion on the playback configuration:** Set InsertionMode to PLAYER\_SELECT on the MediaTailor [playback configuration](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutPlaybackConfiguration.html). The default, STITCHED\_ONLY, forces every session to stitched server-side insertion, so a session that requests guided mode without this prerequisite silently receives SSAI instead. Apply this to the ad-insertion playback configuration rather than to a channel assembly channel. 

1.  **Request guided sessions from the player:** Append aws.insertionMode=GUIDED to the HLS multivariant playlist request, or send {"insertionMode":"GUIDED"} in the POST body to the session-initialization endpoint for players that create sessions explicitly. Confirm the returned manifest carries EXT-X-DATERANGE interstitial tags rather than stitched ad segments. 

1.  **Verify CDN caching of the non-personalized manifests:** Serve the SGAI manifests through [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and monitor cache hit ratio to confirm that manifests are served from cache rather than the MediaTailor origin. If you later enable guided prefetch, prefetch requires per-session manifest requests and variant manifests are no longer CDN-cacheable, which is a direct trade against this step. 

1.  **Precondition the creative library:** Transcode each creative to the bit rate variants of the content stream using [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/), store the output in Amazon S3, and serve it through CloudFront. Provide the pre-transcoded manifest URLs to the ADS for use in VAST responses, with delivery="streaming" media files and relative child manifest paths in the same directory as the parent. Set streaming media file conditioning to NONE on the playback configuration so MediaTailor stitches these without transcoding. 

1.  **Bound the ad decision with MediaTailor's ADS timeouts:** Set AdsRequestTimeoutMilliseconds and LiveMaximumAdsPersonalizationTimeMilliseconds to the budget the break can absorb, rather than leaving the 3000 and 10000 defaults. Set PersonalizationThresholdSeconds from your expected fill rate and avail duration, and configure [SlateAdUrl](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html) separately if you want slate to fill unused avail time. 

1.  **Deploy the ADS in-Region across multiple Availability Zones:** Run the ADS on [Amazon ECS](https://aws.amazon.com/ecs/) in the same Region as the playback configuration, with tasks spread across at least two Availability Zones. Where a cache fronts the ADS, select [Amazon ElastiCache Serverless](https://aws.amazon.com/elasticache/features/) subnets in the Availability Zones the tasks run in and enable the client's Read from Replica feature so reads are served from a replica in the caller's Availability Zone, accepting eventual consistency. 

1.  **Scale the ADS on a capacity-proportional metric:** Target-track [Application Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-autoscaling.html) on a metric that moves inversely with capacity, such as CPU utilization or requests per task, because latency percentiles stay flat until saturation and then spike. Drive a step scaling policy from a p95 latency alarm as the saturation backstop. For known cyclical prime-time patterns, add a [predictive scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-auto-scaling.html) policy in forecast-only mode first, then switch to forecast and scale with SchedulingBufferTime set so tasks are ready before forecasted demand. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF06-BP04 Optimize Prebid Server adapter concurrency and timeout budgets](advperf06-bp04.md) 

 **Related documents:** 
+  [MediaTailor server-guided ad insertion overview and implementation](https://docs.aws.amazon.com/mediatailor/latest/ug/server-guided.html) 
+  [Using preconditioned ads with AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) 
+  [Use historical patterns to scale Amazon ECS services with predictive scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-auto-scaling.html) 
+  [Unlock increased monetization and lower TCO with Server-Guided Ad Insertion](https://aws.amazon.com/blogs/media/unlock-increased-monetization-and-lower-tco-with-server-guided-ad-insertion-for-vod/) 
+  [Part 1: How to optimize ad delivery with AWS Elemental MediaTailor](https://aws.amazon.com/blogs/media/part-1-how-to-optimize-ad-delivery-with-aws-elemental-mediatailor/) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon ElastiCache Serverless](https://aws.amazon.com/elasticache/features/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 