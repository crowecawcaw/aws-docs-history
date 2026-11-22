

# ADVPERF06-BP07 Pre-classify publisher content for contextual targeting at ingest time

 Move contextual classification out of the auction path by classifying content at ingest time, before any viewer arrives. When you trigger classification asynchronously as new content is published, you keep synchronous foundation model inference off the bid evaluation path, where it would add 50–200 ms and push response times beyond the auction deadline. 

 **Desired outcome:** 
+  Bid requests are enriched with IAB taxonomy contextual signals without adding latency to the auction path. Classification completes before the first ad request arrives. 
+  Content classification results are cached in ElastiCache with a 24-hour TTL, enabling sub-millisecond contextual signal retrieval during bid evaluation. 
+  Cache hit ratio targets 95% for established content, with alerts on miss rate spikes that indicate new content not classified. 

 **Common anti-patterns:** 
+  Invoking foundation model inference synchronously on every ad request, so the auction path takes on 50–200 ms of latency for content that could have been classified at publish time. 
+  Classifying content at request time for pages or video segments that have already been published. 
+  Re-classifying unchanged content on every page load instead of caching results for the content's lifetime. 

 **Benefits of establishing this best practice:** 
+  Async pre-classification at publish time removes classification latency from the auction path entirely. Contextual signal retrieval during bid evaluation is a sub-millisecond cache lookup rather than a 50–200 ms model inference call. 
+  Pre-classified contextual signals improve bid quality as DSPs bid higher on verified brand-safe, contextually relevant inventory with accurate IAB taxonomy labels. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Contextual advertising uses content signals (page topic, video content genre, and brand safety classifications) to match ads to relevant inventory without relying on user-level tracking. Contextual classification using foundation models ([Amazon Bedrock Data Automation](https://aws.amazon.com/bedrock/bda/), [Amazon Comprehend](https://aws.amazon.com/comprehend/)) adds 50–200 ms of latency per inference call, which is incompatible with real-time bidding auction deadlines. 

 Separate the classification timing from the auction timing. Content exists before any viewer requests it. A video is uploaded, processed, and published before the first viewer watches it, and a webpage is published before the first reader visits it. When you classify at publish time, results are ready before any ad request arrives. 

 A contextual classification stays stable. Audience attributes change as behavior changes, so they need refreshing. A video's topic and brand-safety profile are properties of the content itself, so one inference applies to every impression of that content. Cost then scales with the size of the catalog rather than with traffic volume, which reduces an unaffordable per-request expense to a modest per-title one. Key the precomputed value to the content so it stays retrievable however the content is addressed at auction time, because the bidder cannot retrieve a value under a key it cannot reconstruct from the bid request. 

 Pre-classification opens a timing window. Content published moments before its first request may be requested before classification finishes, and live content compresses that window toward zero. During the window, proceed with a generic classification: the impression sells at less than an accurate label would earn, but that beats forfeiting the impression by waiting for the real answer. Record this choice explicitly. 

 Stability holds only under certain conditions. Content can be edited after publication, a brand-safety judgment can change when external events change what a topic means, and a classifier improves over time while cached values remain frozen. A TTL alone handles slow drift but none of these cases, because it re-classifies on a clock rather than on the event that made the old answer wrong. Decide what triggers re-classification, and accept that some staleness will remain. 

 The fallback path returns a default classification without an error signal, so cache effectiveness tells you whether the practice is working. A rising miss rate means impressions are being sold on generic signals, and nothing in the auction reports an error, so treat the miss rate as a revenue metric rather than an infrastructure one. Classification failures behave the same way. An item that never completes leaves a permanently unclassified record that looks like content not yet requested. Route failures to a visible queue for review. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Trigger content classification asynchronously through Amazon EventBridge at publish time:** Configure EventBridge rules that match S3 object creation events for new video or document content. The EventBridge rule invokes a Lambda function that calls Amazon Bedrock Data Automation (BDA) to extract IAB taxonomy categories, brand safety classifications, and scene segment metadata. This pipeline runs asynchronously after content publish and completes classification before viewers arrive. 

1.  **Store classification results in Amazon ElastiCache with a 24-hour TTL:** After BDA returns classification results, store them in ElastiCache keyed by content URL or video segment ID with a 24-hour TTL. Content classification rarely changes after publish. A 24-hour TTL balances freshness with cache efficiency. For content that is updated (for example, a live article with expanding coverage), trigger re-classification through EventBridge on the content update event. 

1.  **Enrich bid requests with cached contextual signals at auction time:** During bid evaluation, add a sub-millisecond ElastiCache lookup for the content URL or segment ID in the bid request. If a cache hit is found, add the IAB taxonomy categories and brand safety signals to the outbound bid request extension fields. If the cache misses (new content not classified), add a default IAB category (for example, IAB24: Uncategorized) rather than invoking Bedrock synchronously. 

1.  **Monitor cache hit ratio and alert on miss rate spikes:** Publish ElastiCache cache hit and miss counts as CloudWatch custom metrics dimensioned by content type (video, article, and audio). Set a target cache hit ratio of 95% for established content (content published more than 2 hours ago). Configure CloudWatch alarms that alert when the miss rate exceeds 10% over a 5-minute window. This indicates either a cache configuration issue or a surge of newly published content that has not been classified. 

1.  **Handle BDA classification failures gracefully:** Configure the Lambda classification function with retry logic (3 retries with exponential backoff) and a dead-letter queue (SQS) for events that exhaust retries. Items in the DLQ should be re-processed during off-peak hours. Store a classification\_status field alongside results in ElastiCache so bid evaluation code can distinguish between "not classified" and "classification failed" cache entries, applying appropriate fallback behavior for each case. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF01-BP04 Evaluate AI/ML-based architecture for optimization](advperf01-bp04.md) 

 **Related documents:** 
+  [Automate video insights for contextual advertising using Amazon Bedrock Data Automation](https://aws.amazon.com/blogs/machine-learning/automate-video-insights-for-contextual-advertising-using-amazon-bedrock-data-automation/) 
+  [Amazon Bedrock Data Automation overview](https://docs.aws.amazon.com/bedrock/latest/userguide/data-automation.html) 
+  [IAB Tech Lab Content Taxonomy](https://iabtechlab.com/standards/content-taxonomy/) 

 **Related services:** 
+  [Amazon Bedrock Data Automation](https://aws.amazon.com/bedrock/bda/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 