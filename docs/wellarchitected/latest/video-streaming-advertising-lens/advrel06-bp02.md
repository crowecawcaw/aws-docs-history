

# ADVREL06-BP02 Implement fallback ad pod strategies for unfilled ad breaks
<a name="advrel06-bp02"></a>

 When an ad decision server times out or returns no ads, the break still has to play something. If you plan only for the success path, you lose the monetization tier you could have served and control over what the viewer sees. With a deliberate fallback order, an ad-serving failure degrades to a known revenue floor. 

 **Desired outcome:** 
+  Every ad break has a defined fallback order, and you know which tier served each break. 
+  Your fallback assets are reachable and playable within the ad decision server timeout budget, so a fallback never introduces the stall it exists to avoid. 
+  Steady-state ad fill rate meets the target AWS guidance sets for Avail.FillRate and AdDecisionServer.FillRate, and you track slate or house-ad coverage separately as the degraded-mode measure. 
+  Your configuration is verified against the ad-replacement settings that suppress fallback content, so a configured slate actually plays when the ad decision server fails. 

 **Common anti-patterns:** 
+  Treating an ad decision server failure as a viewer-visible outage rather than an unfilled break, and designing against the wrong failure mode. 
+  Assuming a fallback tier exists in the ad-insertion service when it has to be built and operated by the publisher. 
+  Configuring a slate, then setting an ad-replacement personalization threshold shorter than the break duration, which suppresses that slate on exactly the failures it was configured for. 
+  Committing to a fill-rate floor that holds during an ad decision server outage, when the metric measures ads the decision server supplied. 
+  Re-serving one viewer's ad response to other viewers on a publisher-chosen expiry, without confirming that the ad server's terms, per-impression tracking, and frequency pacing permit it. 
+  Building a rendition ladder for fallback assets that the ad-insertion service produces on its own. 

 **Benefits of establishing this best practice:** 
+  Ad breaks degrade in a known order instead of falling to the lowest tier on the first error. 
+  Fallback behavior is verified rather than assumed, so the configuration matches what plays in production. 
+  Fill-tier distribution quantifies the revenue cost of an ad-serving incident. 
+  Operators can separate an ad decision server problem from a fallback-asset problem during an incident. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS Elemental MediaTailor documents exactly two outcomes for an empty VAST or VMAP response, an ad decision server timeout, an HTTP 500 from the ad decision server, or an ad that has not finished transcoding. It plays a configured slate, or, according to [slate ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html): 

 If you don't configure a slate, MediaTailor defaults to the underlying content stream when one of the above conditions is met. 

 Content bleed-through is the un-configured behavior. No AWS documentation describes a blank or black screen as an outcome, so a design premised on avoiding one is aimed at the wrong risk. 

 This constrains how many tiers are worth building. An intermediate tier between the ad decision server and slate can preserve revenue a slate cannot: a recently valid ad response may still be usable. MediaTailor accepts a single ad decision server URL for each playback configuration, with no secondary server and no response cache. Any intermediate tier is infrastructure you build, operate, and keep inside the ad decision server timeout budget. The [PRE\_ADS\_REQUEST](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks-pre-ads.html) monetization-function hook can rewrite the ad request URL through adsRequest.url, but its documented output namespace provides no field for returning an ad response. The hook fails open: 

 MediaTailor discards the function's output and proceeds as if no function were attached. 

 Reusing a stored response across viewers also raises questions outside the architecture itself, such as ad-server terms, per-impression tracking, and advertiser frequency pacing. If you want that tier, resolve those questions with your demand partners before building it, and treat it as optional, not the default. 

 Slate applies only to live and live-to-VOD workflows. A pure video-on-demand workflow needs a different floor, such as a house-ad asset returned in the response. PersonalizationThresholdSeconds governs how much unfilled time MediaTailor tolerates before it abandons personalizing the break. When the ad decision server supplies nothing, the entire break is unfilled, so a threshold shorter than the break duration puts every failure case past it. The behavior matrix on the slate page reads No slates inserted for empty VAST or VMAP, for ad decision server timeout, and for the ad-not-available case under that setting. You can hold this setting deliberately, preferring content over slate, but you can't hold it accidentally alongside a guaranteed-slate commitment. 

 AWS's [CDN monitoring](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-monitoring.html) documents Avail.FillRate and AdDecisionServer.FillRate with "Target values: Above 90% for both metrics". The metrics reference states that: 

 The maximum Avail.FillRate that MediaTailor can attain is bounded by the AdDecisionServer.FillRate. 

 A fill target is a steady-state goal that depends on the ad decision server, not a floor the fallback tiers can hold during an outage. Slate has its own metric, Avail.ObservedSlateDuration, which reports planned slate duration from asset-list responses for HLS Interstitials sessions. Track degraded-mode success in those terms. Settle internally whether a reported fill rate means the MediaTailor metric or a commercial monetized-fill measure, because the two diverge during an event. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm the workflow your fallback floor is available in:** Establish whether the channel is live, live-to-VOD, or pure video-on-demand. Slate is available for live and live-to-VOD. For a video-on-demand workflow, choose a different last-resort asset and record that decision, because a slate configuration will not take effect. 

1.  **Configure the slate as a single asset:** Supply one high-quality MP4 containing both audio and video at a URL MediaTailor can reach, and let MediaTailor transcode it. Per [slate ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html), "MediaTailor downloads the slate from the URL that you specify, and transcodes it to the same renditions as your content." If you serve the slate over HTTPS, use a certificate from a well-known certificate authority, because a self-signed certificate blocks retrieval. 

1.  **Audit **PersonalizationThresholdSeconds\*\* against your longest break:\*\* Compare the configured value to your break durations. If the threshold is shorter than a break, confirm in writing whether you intend content bleed-through or slate on ad decision server failure, and reconcile that intent with any fill commitment you have made. 

1.  **Decide explicitly whether to operate an intermediate tier:** If you want a response tier between the ad decision server and slate, scope it as a publisher-operated proxy that fronts the ad decision server and is the URL configured for ad decisioning, and confirm reuse terms with your demand partners first. If you don't, document that the order is ad decision server, then slate or content, so no one assumes a tier that isn't there. 

1.  **Host house-ad and slate assets for redundant retrieval:** Place the assets behind a distribution with a failover origin so a single origin failure doesn't remove the floor. Verify retrieval latency leaves room inside the ad decision server timeout budget. 

1.  **Alarm on **Avail.FillRate\*\* and compare it against **AdDecisionServer.FillRate**:\*\* Configure the alarm in the AWS/MediaTailor namespace against your steady-state minimum. When fill drops, the comparison separates an ad decision server supply problem from a MediaTailor-side one. Use Avail.FillRate rather than Avail.ObservedFillRate for alarming, because the observed metric is emitted only for HLS manifests at the first CUE-IN tag. 

1.  **Test each tier by inducing its trigger:** Exercise an ad decision server timeout, an empty response, and an error response against a test configuration, and confirm which tier serves each. Record the observed tier per case so the documented order matches production behavior. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL06-BP01 Deploy Ad Decision Server infrastructure across multiple Availability Zones with automated failover](advrel06-bp01.md) 
+  [ADVREL06-BP03 Design player-side resilience for SGAI manifest and ad stream retrieval](advrel06-bp03.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 

 **Related documents:** 
+  [MediaTailor slate ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html) 
+  [Monitoring MediaTailor with Amazon CloudWatch metrics](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html) 
+  [PRE\_ADS\_REQUEST monetization function hook](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks-pre-ads.html) 
+  [Monitoring CDN and MediaTailor performance](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-monitoring.html) 
+  [Unlock increased monetization and lower TCO with Server-Guided Ad Insertion](https://aws.amazon.com/blogs/media/unlock-increased-monetization-and-lower-tco-with-server-guided-ad-insertion-for-vod/) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 