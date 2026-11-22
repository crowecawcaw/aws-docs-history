

# ADVSUS01-BP07 Classify content once at ingest to remove repeat inference from the auction path

 Content classification results don't change between one bid request and the next. A classifier invoked during bid evaluation recomputes them anyway, so inference load grows with ad traffic. Classifying each item once at publish time decouples inference from ad traffic. 

 **Desired outcome:** 
+  Bid requests are enriched with IAB taxonomy contextual signals without adding model-inference latency to the auction path. 
+  Content classification results are cached with a 24-hour TTL, so contextual signal retrieval at auction time is a sub-millisecond cache lookup rather than a synchronous model inference call. 
+  The contextual-lookup cache hit ratio meets a target derived from your own publish-to-request pattern, and miss-rate spikes that signal newly unclassified content are alarmed on. 

 **Common anti-patterns:** 
+  Foundation model inference runs synchronously on every ad request, which adds classification latency to an auction path that operates under a strict deadline. 
+  Reclassifying the same content URL on every bid request repeats model inference that delivers no new information. 
+  Contextual signals are skipped entirely to protect auction latency, which forces buyers to bid without brand-safety or category context. 
+  Classification work is coupled to ad-serving compute, so a surge in ad requests drives a proportional surge in inference load on the bidding fleet. 

 **Benefits of establishing this best practice:** 
+  Bid requests carry IAB taxonomy and brand-safety signals with no inference work in the auction path, protecting the auction latency budget. 
+  Classifying each content item once at publish time removes redundant repeat inference, lowering the compute consumed for contextual targeting. 
+  Decoupling classification from ad serving keeps inference load proportional to content publish rate rather than ad request volume. 
+  A high cache hit ratio keeps auction-time enrichment cost flat as traffic grows. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A foundation model inference call in the bid evaluation path consumes part of a response budget measured in milliseconds, which can push a bidder past the auction deadline and cost the impression. The same content URL produces identical classification results on every evaluation, yet synchronous classification re-invokes the model on every bid request for that content. Latency is a performance constraint. The resource proxy for the sustainability gain is model-inference invocation count and the compute behind it. Aim to drive inference invocations down toward one per content item. 

 A video is uploaded and published before the first viewer watches it. Classifying at publish time means results are ready before any ad request arrives, which converts an auction-time inference call into an auction-time cache lookup. The trade-off is cache freshness. Content that changes after classification needs re-triggering, and a cache miss on newly published content must not block the auction. Amazon Bedrock Data Automation extracts IAB taxonomy categories, scene segments, and brand-safety signals from video, audio, and text content without requiring custom model development. The latency dimension of the same move, including the auction-deadline arithmetic and the event-driven pipeline that implements it, is covered in [ADVPERF06-BP07 Pre-classify publisher content for contextual targeting at ingest time](advperf06-bp07.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Move classification to the content publish event:** Trigger classification when content is published rather than when a bid request arrives, so each item is classified once and the result is cached for reuse at auction time. Confirm the trigger also fires on content updates, because otherwise a stale classification persists for the cache lifetime. 

1.  **Measure inference invocations per content item:** Instrument the classification pipeline to emit an invocation count per content item alongside the bid request count it serves. The ratio between them is the efficiency signal. It approaches one invocation per content item when pre-classification is working and climbs toward one per bid request when classification drifts back onto the auction path. 

1.  **Treat the cache hit ratio as the primary efficiency indicator:** Publish contextual-lookup hit and miss counts as CloudWatch custom metrics. Set the hit-ratio target from your own catalog. Once a title has been published long enough for its first classification to be cached, nearly every subsequent lookup should hit, so measure how long that takes for your publish pipeline and target accordingly. Savings from pre-classification are proportional to the hit rate, so track the ratio as an efficiency measure rather than as a cache-health detail. 

1.  **Alert on miss-rate spikes that represent lost savings:** Configure a CloudWatch alarm on a sustained rise in the miss rate above your measured baseline, with a window long enough to ignore normal publish bursts. A sustained spike means content is reaching auction unclassified, so inference either runs on the auction path or contextual signals are dropped entirely. Route the alarm to the team that owns the classification pipeline. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF06-BP07 Pre-classify publisher content for contextual targeting at ingest time](advperf06-bp07.md) 
+  [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) 
+  [ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption](advcost05-bp03.md) 
+  [ADVSUS01-BP03 Reduce CPU time per bid in agent containers to lower fleet energy intensity](advsus01-bp03.md) 

 **Related documents:** 
+  [Videos in Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-ouput-video.html) 
+  [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/) 

 **Related services:** 
+  [Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 