

# ADVOPS04-BP04 Establish AdOps measurement for shoppable ad fulfillment and non-intrusive ads

 Shoppable ads use an embedding-based matching pipeline that matches image embeddings to content embeddings in an ecommerce vector store based on similarity scores. Non-intrusive ads (squeezebacks, overlays, and pause ads) operate outside conventional click-through attribution. Shoppable and non-intrusive ads require measurement approaches distinct from conventional ad attribution to demonstrate effectiveness to advertisers. 

 **Desired outcome:** 
+  Publishers have operational measurement frameworks that track shoppable ad fulfillment through the embedding-based matching pipeline and measure non-intrusive ad effectiveness using engagement-based attribution rather than conventional click-through attribution. 
+  Unified AdOps dashboards present non-conventional metrics alongside traditional ad performance data for advertiser reporting. 

 **Common anti-patterns:** 
+  Attempting to measure shoppable ads and non-intrusive formats using conventional click-through attribution, which misses the majority of engagement signals for these formats. 
+  Lacking full-pipeline monitoring for the shoppable ad embedding pipeline: image embedding generation accuracy, vector store similarity score distribution, and matching latency from identification through presentation are not tracked. 
+  No quarterly format effectiveness reviews, which leaves ad operations without data to inform format optimization and advertiser pricing. 

 **Benefits of establishing this best practice:** 
+  Publishers can demonstrate ad effectiveness for non-conventional formats to advertisers, maintaining demand and protecting CPMs for innovative inventory. 
+  Full-pipeline monitoring enables proactive detection of matching quality degradation before it affects advertiser outcomes. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Ad formats such as shoppable ads, squeezebacks, overlays, and pause ads operate outside the conventional click-through attribution model. Without dedicated measurement frameworks, publishers can't demonstrate the effectiveness of these formats to advertisers, which reduces demand partner confidence and lowers CPMs for innovative inventory. 

 For shoppable ads, the measurement pipeline covers the embedding-based matching workflow: image embedding generation (how accurately does the embedding model represent the product visual), vector store similarity score distribution (how strong is the semantic match between ad content and editorial content), match quality thresholds (minimum similarity scores for product presentations), shopping store presentation success rates (what fraction of matches surface shoppable items to viewers), and conversion funnel completion from ad exposure through purchase intent. 

 For non-intrusive formats (squeezebacks, overlays, and pause ads), engagement-based measurement replaces conventional attribution. 
+  **Squeezeback viewer retention:** What fraction of viewers remain watching when content is squeezed to accommodate the ad compared to equivalent periods without squeeze-back ads. 
+  **Overlay interaction rates and dwell time:** Active engagement with overlay ads (hovers, clicks, and interaction with interactive elements) as a proxy for attention quality. 
+  **Pause ad impression quality:** Viewability duration (how long the viewer is exposed to the pause ad) and context relevance (how well the ad content matches the paused content). 
+  **Viewer sentiment indicators:** Post-ad behavior (did the viewer continue watching, skip to the next content item, or exit the session) as indirect signals of viewer reception. 

 With Amazon Managed Service for Apache Flink, you can process engagement signals in real time for these non-conventional metrics. Quick visualizes trends in shoppable fulfillment metrics and embedding pipeline health. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define format-specific measurement frameworks:** For shoppable ads: embedding pipeline stage metrics (generation latency, similarity score distribution, match quality threshold pass rate), viewer interaction metrics (hover rate, click-to-product rate, conversion funnel completion). For squeezebacks: viewer retention during ad display compared to content-only periods. For overlays: interaction rate, dwell time, post-exposure viewing behavior. For pause ads: impression quality (viewability duration), context relevance score. 

1.  **Instrument the shoppable ad embedding pipeline with stage-level metrics:** Deploy custom CloudWatch metrics at each stage of the embedding pipeline: image embedding generation latency and accuracy, vector store similarity score distribution (histogram of scores across all matches), match quality threshold pass rate (fraction of matches meeting minimum similarity threshold), shopping store presentation success rate, and total pipeline latency from shoppable item identification through vector store lookup to store presentation. Set alarms on similarity score distribution shifts that indicate embedding model quality degradation. 

1.  **Build engagement signal collection for non-intrusive formats:** Deploy client-side event collection for engagement signals from each non-intrusive format type. Use Amazon Kinesis Data Streams to ingest events in real time. Configure event schema to capture: viewer ID (hashed), format type, ad content, editorial content at display time, interaction type, dwell time, and post-exposure viewing behavior within 5 minutes. Aggregate these events using Amazon Managed Service for Apache Flink for real-time engagement rate calculation. 

1.  **Create unified AdOps dashboards in Quick:** Build Quick dashboards presenting non-conventional metrics alongside traditional ad performance data (fill rate, eCPM, and viewability). Include trend visualizations showing engagement rates over campaign flights, match quality score distributions for shoppable ad campaigns, and viewer retention impact during squeezeback periods. Make these dashboards available to advertisers through Quick embedded analytics for transparent reporting. 

1.  **Establish quarterly format effectiveness reviews:** Schedule quarterly cross-functional reviews where ad operations and product teams analyze format-specific measurement data. Evaluate: shoppable ad match quality trends (is similarity score distribution improving with model improvements), non-intrusive format engagement rates compared to conventional pre-roll benchmarks, viewer sentiment indicators across format types, and format-specific CPM performance compared to conventional format baselines. Use review findings to inform format optimization priorities and advertiser pricing decisions. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [IAB measurement guidelines for non-standard ad formats](https://iabtechlab.com/standards/) 
+  [Amazon Managed Service for Apache Flink for real-time processing](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) 

 **Related services:** 
+  [Quick](https://aws.amazon.com/quicksight/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/) 