

# Media playout and format resilience
<a name="advrel06"></a>

 Advertising media delivery spans three distinct surface types, each with its own failure characteristics. Server-Guided Ad Insertion (SGAI) combines server-side manifest manipulation with client-side ad fetching. FAST channels require continuous linear playout where any interruption is visible to all concurrent viewers at once. Innovative ad formats (overlays, squeeze-backs, and shoppable ads) introduce experimental rendering paths that can fail on specific device and player combinations without showing a visible error. A failure in any surface translates directly into blank ad breaks, frozen channels, or invisible format rendering errors, all of which erode publisher revenue and viewer experience. 


|  ADVREL06: How do you maintain ad delivery and media playout across SGAI, FAST channels, and ad formats during component failures?  | 
| --- | 
| [ADVREL06-BP01 Deploy Ad Decision Server infrastructure across multiple Availability Zones with automated failover](advrel06-bp01.md) | 
| [ADVREL06-BP02 Implement fallback ad pod strategies for unfilled ad breaks](advrel06-bp02.md) | 
| [ADVREL06-BP03 Design player-side resilience for SGAI manifest and ad stream retrieval](advrel06-bp03.md) | 
| [ADVREL06-BP04 Implement automated input failover and slate injection for continuous channel playout](advrel06-bp04.md) | 
| [ADVREL06-BP05 Design redundant content origin architecture with cross-region replication](advrel06-bp05.md) | 
| [ADVREL06-BP06 Implement proactive schedule validation and channel health monitoring](advrel06-bp06.md) | 
| [ADVREL06-BP07 Implement capability detection and fallback creative mapping for all innovative format campaigns](advrel06-bp07.md) | 
| [ADVREL06-BP08 Decouple innovative format rendering from core ad delivery pipeline](advrel06-bp08.md) | 
| [ADVREL06-BP09 Monitor format-specific error rates and implement automated format suspension](advrel06-bp09.md) | 

## Capability intent
<a name="advrel06-capability-intent"></a>
+  Ad Decision Server (ADS) infrastructure is deployed across multiple Availability Zones with automated failover using [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/), so a single-AZ failure doesn't interrupt ad decisioning for SGAI streams. 
+  Fallback ad pod strategies (default slates, cached creatives, passback chains) help avoid blank ad breaks when the primary ADS or demand partners are degraded. 
+  Player-side resilience handles manifest fetch failures, ad stream timeouts, and partial ad pod delivery without disrupting the viewer's content experience. 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) automatic input failover and [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) channel assembly with slate pools support ongoing FAST channel playout during origin failures. 
+  Content origins use [Amazon S3](https://aws.amazon.com/s3/) Cross-Region Replication with [Amazon CloudFront](https://aws.amazon.com/cloudfront/) origin failover groups for sub-second segment-level recovery. 
+  Proactive schedule validation detects missing or corrupt assets before playout time, reducing the risk of failures reaching viewers. 
+  Client-side capability detection serves innovative ad formats only to devices confirmed capable of rendering them, with mandatory fallback creatives for every format campaign. 
+  Innovative format rendering services are decoupled from the core ad delivery pipeline, so a format service failure doesn't affect standard VAST/VPAID delivery. 
+  Per-format, per-device error rate monitoring with automated format suspension helps protect revenue when a specific format degrades on a specific device type. 

## Common issues to watch for
<a name="advrel06-common-issues-to-watch-for"></a>
+  Single-AZ ADS deployment where an Availability Zone failure causes 100% ad decisioning loss for all SGAI streams. 
+  No fallback ad pod strategy, so demand partner degradation results in blank ad breaks visible to all viewers. 
+  Player implementations that stop content playback when an ad stream fetch fails, instead of skipping the ad and resuming content. 
+  Single-origin FAST channels with no [CloudFront](https://aws.amazon.com/cloudfront/) origin failover, where an [S3](https://aws.amazon.com/s3/) origin issue causes a complete channel blackout. 
+  No pre-flight schedule validation for FAST channels, so missing or corrupt assets are discovered only when viewers see black screens. 
+  Serving innovative ad formats without capability detection, producing blank slots on devices that can't render the format. 
+  Coupling format rendering services to the core ADS, so a format service bug or deployment failure degrades all ad delivery. 
+  Aggregating format error rates without per-device granularity, making it impossible to identify which format is failing on which device type. 