

# Scenario 11: Implementation of FAST Channel for VOD workflows on AWS

 Free Ad-Supported Streaming TV (FAST) channels transform dormant back-catalog VOD content into around-the-clock ad-supported linear streaming channels. Publishers create new revenue streams from existing content libraries without broadcast infrastructure investment. Distributors expand their channel lineups with free ad-supported tiers that attract cost-conscious viewers. 

## Characteristics
<a name="s11-characteristics"></a>
+  Publisher has a large VOD library and wants to monetize it as continuous linear channels without around-the-clock live encoding costs. 
+  Multiple FAST channels can be assembled from the same VOD library without proportional infrastructure cost increases. 
+  Channels must operate continuously, because any playout interruption immediately affects all concurrent viewers. 
+  Ad monetization through SGAI or SSAI requires reliable SCTE-35 marker generation and ADS availability. 
+  EPG (Electronic Program Guide) generation must be automated and accurate for distribution to downstream systems. 
+  Content licensing workflows require tracking which assets are scheduled, when they play, and for how long. 

## Reference architecture
<a name="s11-reference-architecture"></a><a name="scenario-11-fig1"></a>

![FAST Channel VOD workflow architecture on AWS showing the content pipeline from mezzanine asset ingest through transcoding, packaging, linear channel assembly with dynamic ad insertion, and CDN delivery to viewers](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-11-fast-channel-vod.jpg)

*FAST Channel VOD workflow architecture on AWS showing the content pipeline from mezzanine asset ingest through transcoding, packaging, linear channel assembly with dynamic ad insertion, and CDN delivery to viewers*


 The architecture consists of the following components: 

1.  **Mezzanine assets (Amazon S3)**: Source content files uploaded by content operations. Trigger AWS Elemental MediaConvert transcoding jobs through S3 event notifications or EventBridge rules. S3 Cross-Region Replication provides origin redundancy for playback resilience. 

1.  **AWS Elemental MediaConvert**: Transcodes mezzanine files to multi-bit rate HLS (adaptive bit rate ladder: 1080p, 720p, 480p, and 360p). Outputs to Amazon S3 as packaged ABR assets. Also pre-transcodes all ad creatives to match the content stream profile during campaign onboarding. 

1.  **AWS Elemental MediaPackage VOD**: Ingests the multi-bit rate HLS output from MediaConvert and outputs one or more packaged formats (HLS, CMAF, and DASH) into separate S3 destinations. Each packaged format is a Source that Channel Assembly can reference. 

1.  **AWS Elemental MediaTailor Channel Assembly**: Imports one or more packaged formats from MediaPackage VOD as Sources. Creates a continuous Channel consisting of a looping sequence of Programs. Each Program references a specific Source and an optional ad break slate Source. Outputs the channel manifest with ad break positions signaled by SCTE-35 markers. 

1.  **AWS Elemental MediaTailor (SGAI/SSAI)**: Replaces slate content in the channel assembly output with dynamically served ads. For SGAI: generates CDN-cacheable manifests with ad opportunities signaled. For SSAI: stitches personalized ads into per-viewer manifests. Connects to the Ad Decision Server (ADS) for VAST responses. 

1.  **Amazon CloudFront**: Delivers channel segments and optionally playlists to viewers globally. For SGAI deployments, CloudFront caches non-viewer-specific playlists, dramatically reducing origin request volume at scale. Origin failover groups use primary and secondary S3 buckets in different regions. 

1.  **Pre-flight validation (AWS Lambda \+ EventBridge)**: Lambda function triggered every 15 minutes by EventBridge validates scheduled assets for the next 30 minutes: asset IDs exist in S3, durations match scheduled slots, no scheduling gaps, all renditions present. Failures route to SNS for content operations notification with 30 minutes of remediation time. 

1.  **Slate content pool (Amazon S3)**: 4–8 hours of genre-appropriate filler content, pre-transcoded to all output renditions, stored in a dedicated S3 bucket with cross-region replication. MediaTailor Channel Assembly uses slate to fill scheduling gaps automatically. 

## Configuration notes
<a name="s11-configuration-notes"></a>

### Channel assembly for cost efficiency
<a name="channel-assembly-for-cost-efficiency"></a>

 Use MediaTailor Channel Assembly for all FAST channels assembled entirely from pre-encoded VOD content. This avoids around-the-clock MediaLive encoding costs, the largest infrastructure expense for traditional linear channels. For channels requiring live signal processing (live sports, breaking news inserts), a hybrid approach combining a live MediaLive pipeline with Channel Assembly for the remainder of the schedule is appropriate. 

### Content origin resilience
<a name="content-origin-resilience"></a>

 Enable S3 Cross-Region Replication on the packaged content bucket (primary → secondary region). Configure CloudFront origin failover groups with the primary and secondary buckets. Test failover by simulating primary bucket unavailability and measuring the CloudFront transition time. Enable S3 Object Lock (governance mode) on this week's scheduled content to guard against accidental deletion during active playout. 

### EPG automation
<a name="epg-automation"></a>

 Automate EPG generation from the Channel Assembly schedule output. When Channel Assembly schedules are updated, trigger a Lambda function that formats the EPG in the required format for each distribution system (XMLTV, proprietary API formats). Distribute EPG data to downstream systems 24–48 hours in advance. EPG inaccuracies cause viewer dissatisfaction and app store issues, and automation reduces manual entry errors. 

### Ad monetization configuration
<a name="ad-monetization-configuration"></a>

 For FAST channel ad monetization, configure MediaTailor with SGAI mode to generate CDN-cacheable manifests. Maintain a slate content pool for ad break gap filling when ADS is unavailable. Configure PersonalizationThresholdSeconds appropriately. ADS unavailability should result in house ads or slate, not blank breaks. Pre-transcode all ad creatives to match channel output renditions during campaign setup (not at playback time). 

### Pre-flight validation
<a name="pre-flight-validation"></a>

 Run EPG completeness validation 60 minutes before scheduled playout. Validate: all referenced asset IDs exist in S3, durations are within 5-second tolerance of scheduled slot durations, no scheduling gaps exist, and all required renditions are available. Alert content operations through SNS for any validation failures. This provides enough lead time for remediation before viewers are affected. 

### Operational monitoring
<a name="operational-monitoring"></a>

 Configure CloudWatch alarms on MediaLive metrics (OutputVideoFrameRate = 0 indicates channel failure). Deploy a synthetic viewer probe (Lambda running every 5 minutes) that fetches the channel manifest and validates HTTP 200 response, current segment timestamps, and segment URL accessibility. Alert if 3 consecutive probe checks fail. This catches viewer-facing issues that infrastructure metrics may not reveal immediately. 