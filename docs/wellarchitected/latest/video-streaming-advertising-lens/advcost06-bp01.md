

# ADVCOST06-BP01 Use programmatic channel assembly to remove dedicated encoding infrastructure
<a name="advcost06-bp01"></a>

 Traditional linear channels require live encoding infrastructure that runs around the clock regardless of viewership. Programmatic channel assembly creates linear channels from existing VOD assets without ongoing encoding, which removes the most expensive infrastructure component for back-catalog FAST channels. 

 **Desired outcome:** 
+  FAST channels are assembled programmatically from VOD assets without dedicated around-the-clock encoding infrastructure. 
+  Around-the-clock encoding compute costs are avoided for VOD-based FAST channels, and the saving is quantified against the pricing model the workload actually ran on. 
+  Multiple FAST channels are assembled from the same VOD library without proportional encoding infrastructure cost increases. 
+  Source catalogs are confirmed to meet the packaging requirements for assembly before a migration is committed, so eligibility is established rather than assumed. 

 **Common anti-patterns:** 
+  Running continual live encoding infrastructure (such as AWS Elemental MediaLive) for FAST channels assembled entirely from pre-encoded VOD assets, and replicating that same architecture when launching new catalog channels, so ongoing compute costs accrue for encoding that produces no incremental value over the existing VOD transcode outputs. 
+  Creating separate encoding pipelines and VOD asset copies for each FAST channel rather than assembling multiple channels programmatically from a shared VOD library, which duplicates storage and encoding costs proportionally with channel count. 
+  Inserting SCTE-35 markers into live-encoded streams to define ad break positions when programmatic channel assembly allows ad breaks to be defined directly in the schedule, which adds encoding complexity and cost for functionality that the assembly layer provides natively. 
+  Failing to quantify the total cost difference between continual encoding and programmatic channel assembly before making architectural decisions. 
+  Building that comparison on the wrong meters: quoting on-demand encoding rates to a workload already under a reserved commitment, or estimating assembled-channel cost from output and rendition counts rather than from running channel-hours. 
+  Assuming an existing VOD catalog is eligible without checking how it was encoded, only to hit program transitions that force a full re-encode of per-title or automated ABR sources. 

 **Benefits of establishing this best practice:** 
+  Remove the need for continual live encoding compute costs 
+  No SCTE-35 marker insertion required: ad breaks defined in schedule 
+  Maximize content reuse across multiple FAST channels from a single VOD library 
+  Scale channel count without proportional encoding infrastructure costs 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 FAST channels fall into two architectural categories based on their source material. Channels built from live feeds (sports, news, and live events) require real-time encoding because the content doesn't exist in advance. Channels assembled from pre-encoded VOD assets (back-catalog movies, series reruns, themed compilations) don't. Running constant live encoding infrastructure for the second category pays ongoing compute costs for encoding that produces no value beyond what already exists in the VOD transcode outputs. 

 Programmatic channel assembly creates a linear viewing experience by stitching pre-encoded VOD segments according to a schedule, producing a manifest that players consume identically to a live stream. The assembled output defines ad break positions directly in the schedule, without SCTE-35 marker insertion during encoding. This reduces both encoding complexity and cost. [AWS Elemental MediaTailor Channel Assembly](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly.html) provides this capability as a managed service. 

 [MediaLive](https://aws.amazon.com/medialive/) bills per input, per output, and per add-on feature by the hour, so a channel's rate depends on the ABR ladder size regardless of viewership. A continual channel is exactly the case AWS documents reserved pricing for, and a 12-month commitment lowers the hourly rate substantially against on-demand. A customer running continual linear playout has usually already made that commitment, so an on-demand comparison overstates the migration saving several times over. Build the comparison from the customer's actual committed rate, taken from the current [MediaLive pricing](https://aws.amazon.com/medialive/pricing/) page. Reserved rates are charged for every hour of the commitment period whether the channel runs. 

 Channel Assembly bills on a different dimension. [MediaTailor pricing](https://aws.amazon.com/mediatailor/pricing/) charges an hourly rate for a running linear channel, rounded up to the nearest minute, and only while that channel is active. It bills the channel, not the channel's outputs, so a channel with both an HLS and a DASH output bills once, and estimating from output or rendition count inflates the line item. The rate depends on the channel tier: basic channels schedule VOD only, and standard channels schedule both VOD and live sources, so choosing the tier a workflow requires affects cost and belongs in the design phase. Because no encoding happens, adding a second or tenth channel from the same library doesn't multiply encoding cost, though each running channel adds its own channel-hour charge. 

 Channel assembly produces non-viewer-specific manifests. Every viewer watching the same channel at the same time receives the same manifest, and personalized ad insertion happens downstream. The documented path is to "pair your channel with a MediaTailor SSAI playback configuration." Because that manifest isn't personalized, it can be cached, and caching drives the cost savings. Personalized SSAI manifests can't be cached and are served with a zero-second TTL. A [CloudFront](https://aws.amazon.com/cloudfront/) distribution serving cached assembled manifests handles many concurrent viewers from edge cache without proportional origin requests. Server-guided ad insertion is an alternative downstream mode that keeps manifests cacheable at the player, but it is HLS-only for server-side tracking, requires player opt-in, and doesn't support ad prefetching or Ad-ID decoration, so weigh those limits before adopting it in place of SSAI. 

 Eligibility comes down to a set of indicators, and packaging blocks more migrations than signal processing does. According to the [workflow guidance](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-workflows.html), "Channel Assembly doesn't support per-title encoding or automated ABR encoding. These methods produce assets with different rendition counts and durations, which causes playback failures at program transitions." Per-title and automated ABR are common in existing VOD catalogs, so a back catalog can look eligible on content type and still require re-encoding to a fixed ladder with uniform rendition counts and consistent segment durations, which is unbudgeted transcode spend and schedule risk. If a channel needs live signal processing such as live-encoder captions, real-time graphics, or live audio mixing, choose the live-to-live or mixed workflow with an upstream encoder instead. This requirement does not disqualify the channel. The limitation appears at design time as a missing feature, and playback continues normally. Playback failures at transitions trace to mismatched rendition counts or ABR ladders, differing durations across package configurations, and, for live sources, missing \#EXT-X-PROGRAM-DATE-TIME tags or mismatched target durations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit the source catalog's packaging before assessing the channel:** For each candidate FAST channel, confirm the assets were produced with a fixed ABR ladder rather than per-title or automated ABR, and that all sources share a rendition count, consistent segment durations, and matching bitrates and resolutions. Treat a catalog that fails this as requiring a re-encode, and price that re-encode into the business case before committing to the migration. 

1.  **Build the cost comparison from the customer's current pricing model:** Identify whether the existing MediaLive channels run on demand or under a reserved commitment, and compare against the appropriate rate rather than the list on-demand rate. Estimate the Channel Assembly side from running channel-hours per channel and the basic or standard tier the channel requires, remembering that a channel with multiple outputs is billed once. 

1.  **Select the workflow that matches the source mix:** Choose the VOD-to-live workflow for a catalog-only channel, and the live-to-live or mixed workflow where the channel needs live segments or live signal processing such as encoder captions, real-time graphics, or live audio mixing. The tier and the ad-break mechanism follow from this choice, since scheduled ad breaks apply to VOD sources and live sources pass their existing markers through. 

1.  **Configure the program schedule and place ad breaks on segment boundaries:** Import the VOD sources, then define play order and ad breaks. Set each ad break's OffsetMillis to fall on a segment boundary across every track in the source, including audio and closed captions. The [API reference](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdBreak.html) states the value "must fall within 100ms of a segment boundary, otherwise the ad break will be skipped", while the workflow guidance describes non-aligned offsets as adjusted to the nearest boundary. Because the two AWS sources differ on the failure mode, align offsets deliberately rather than relying on either behavior, and use shorter segments where you need placement precision. Add programs to a running linear channel at least 10 minutes before air time, and at least 15 minutes ahead for live programs using absolute transitions. 

1.  **Validate transitions and ad-break signaling before cutover:** Play through several program transitions and confirm each scheduled break appears. Monitor the channel assembly alerts for duration, target-duration, rendition, and codec mismatches, which report the packaging problems that cause stalling at transitions, and for the alert that fires when no common segment boundary exists at an ad slate's start time. 

1.  **Cache the assembled manifests and attach the monetization path:** Put a CloudFront distribution in front of the assembled-manifest origin and set manifest TTLs for the channel's live or VOD pattern. Pair the channel with an SSAI playback configuration downstream to monetize it, and confirm the caching behavior you configured survives that pairing. 

1.  **Decommission redundant encoding infrastructure:** After validating channel assembly for eligible channels, decommission MediaLive channels and associated input infrastructure. Release any reservations that no longer have a matching workload, since reserved rates are charged for every hour of the commitment period whether a channel runs. Update IaC to help avoid recreation, then calculate and document realized savings against the pre-migration baseline. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST06-BP02 Optimize VOD storage costs for FAST channel source content](advcost06-bp02.md) 

 **Related documents:** 
+  [Integrate MediaTailor SSAI with channel assembly for monetized linear channels](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-ca-integration.html) 
+  [Channel assembly workflows and content requirements](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-workflows.html) 
+  [Getting started with MediaTailor channel assembly](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-getting-started.html) 
+  [AdBreak API reference](https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AdBreak.html) 
+  [Channel assembly alerts](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-alerts.html) 
+  [Optimizing CDN caching for MediaTailor workflows](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimize-caching.html) 
+  [AWS Elemental MediaTailor pricing](https://aws.amazon.com/mediatailor/pricing/) 
+  [AWS Elemental MediaLive pricing](https://aws.amazon.com/medialive/pricing/) 

 **Related services:** 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 