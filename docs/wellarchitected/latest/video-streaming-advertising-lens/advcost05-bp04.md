

# ADVCOST05-BP04 Optimize knowledge base indexing frequency and retrieval strategies to minimize costs

 Advertising agents rely on knowledge bases to hold campaign intelligence, performance analytics, viewer monetization data, and brand safety guidelines. Frequent re-indexing and over-retrieval drive up costs. Configure knowledge bases to sync only when data changes, and keep chunk sizes and retrieval counts at the minimum that maintains quality. 

 **Desired outcome:** 
+  Knowledge bases sync only when underlying data changes, not on aggressive fixed schedules. 
+  Retrieval count (k) is set to the minimum that maintains agent output quality. 
+  Source data stored at optimal cost using S3 Intelligent-Tiering with lifecycle policies. 

 **Common anti-patterns:** 
+  Re-indexing all knowledge base data sources on the same aggressive schedule regardless of change frequency, so repeated embedding costs accrue on static content like brand guidelines that change rarely. 
+  Retrieving a high number of chunks (k=10 or more) by default without validating whether fewer chunks produce equivalent agent output quality, which inflates input token costs on every retrieval. 
+  Storing all knowledge base source data in S3 Standard regardless of access patterns, so premium storage rates apply to creative archives and historical campaign data accessed infrequently. 
+  Including fast-moving data (real-time performance metrics) in knowledge bases that can't sync frequently enough to stay current, which produces stale retrieval and wasted indexing costs. 
+  Never experimenting with chunk size configurations, so defaults may pass excessive or insufficient context to the model per retrieval. 

 **Benefits of establishing this best practice:** 
+  Reduced embedding and indexing costs by syncing knowledge bases only when source data actually changes. 
+  Lower per-invocation token costs by retrieving only the minimum chunks needed for quality output. 
+  Optimized storage costs through intelligent tiering of advertising data based on access frequency. 
+  Improved agent accuracy by excluding fast-moving data from knowledge bases and querying it directly through action groups where freshness matters. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) incur costs at two major points. Indexing generates embeddings when data is ingested, and retrieval returns chunks to the model as context tokens. Indexing cost depends on sync frequency and data volume. Retrieval cost depends on how many chunks (k) you fetch per query and how large each chunk is. 

 Data sources feeding advertising knowledge bases have different change rates. Brand guidelines and campaign taxonomies change quarterly at most. Campaign metadata (like flight dates, budget allocations, or targeting parameters) changes daily or weekly. Real-time performance metrics change continually. Applying the same sync schedule to all three categories means either over-indexing static content (paying repeated embedding costs for unchanged data) or under-indexing dynamic content (serving stale results that degrade agent accuracy). Separate the knowledge bases by change frequency, and give each one its own sync trigger. 

 If performance metrics change every few minutes but the knowledge base syncs hourly, agents retrieve outdated numbers and base recommendations on stale data. You pay for indexing that can't keep pace, and you still get inaccurate outputs. When data changes faster than the shortest practical sync interval, query it directly through [Amazon Bedrock action groups](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html), which provides fresher results and lower indexing costs. 

 Chunk size and retrieval count (k) create a trade-off between retrieval quality and token cost. Larger chunks provide more context per retrieval but pass more tokens to the model. Higher k values retrieve more chunks but increase input token costs linearly. The default settings in most implementations are conservative (large chunks, high k) to avoid quality degradation during initial deployment. After the system is stable, reduce both parameters step by step until quality measurably drops. 

 Source data storage costs accumulate separately from Bedrock charges. Advertising data fed into knowledge bases often includes creative archives, historical campaign records, and seasonal analytics that agents query infrequently. [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) moves objects between access tiers based on usage, which lowers storage costs for infrequently accessed data. The objects stay available when the knowledge base re-syncs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify data sources by change frequency:** For each knowledge base data source, document how frequently the underlying data changes. Remove fast-moving data (real-time metrics) from knowledge bases. Query these directly through action groups instead, which keeps the data fresh and avoids ongoing re-indexing costs. 

1.  **Configure separate knowledge bases with independent sync schedules:** Create separate knowledge bases for each data category. Configure EventBridge-triggered sync for each: weekly for static content, daily for slow-moving data, event-triggered (S3 object creation) for irregular updates. 

1.  **Tune chunk sizes and retrieval count:** Test chunk sizes from 512 to 2,048 tokens using representative advertising queries. Select the smallest chunk size that maintains retrieval accuracy. Smaller chunks mean fewer tokens passed to the model per retrieval. Start with numberOfResults=3 and increase only if agent output quality measurably degrades. 

1.  **Apply S3 Intelligent-Tiering to knowledge base source data:** Enable S3 Intelligent-Tiering on all buckets storing advertising data that feeds knowledge bases. For creative asset archives and historical campaign data accessed less than once per quarter, configure S3 Lifecycle policies to transition to Glacier Instant Retrieval. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST05-BP03 Implement prompt caching and optimize prompt design to minimize token consumption](advcost05-bp03.md) 

 **Related documents:** 
+  [How content chunking works for knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) 

 **Related services:** 
+  [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 