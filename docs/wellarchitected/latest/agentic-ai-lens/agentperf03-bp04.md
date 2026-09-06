

# AGENTPERF03-BP04 Establish efficient agent caching and data access patterns
<a name="agentperf03-bp04"></a>

 Agents that repeatedly fetch the same data benefit from caching, breaking the cycle of redundant retrievals speeds up every reasoning iteration. Agentic workloads often access the same tool outputs, retrieved documents, computed embeddings, and configuration data across multiple reasoning iterations, sessions, or agents in a multi-agent workflow. Without caching, each access pays the full latency and cost of the original operation. 

 **Desired outcome:** 
+  You have multi-layer caching that removes redundant computations and data fetches across reasoning iterations, sessions, and agents. 
+  You have cache hit rates monitored and optimized. 
+  You have cache invalidation policies tuned to balance freshness requirements with performance benefits. 

 **Common anti-patterns:** 
+  Implementing no caching at all, forcing agents to re-fetch the same documents, re-compute the same embeddings, and re-invoke the same tools on every reasoning iteration. 
+  Using a single cache TTL for all data types without considering freshness requirements, producing either stale data (TTL too long) or poor hit rates (TTL too short). 
+  Designing cache keys based only on exact string matching, missing cache hits for semantically equivalent queries that use different phrasing. 

 **Benefits of establishing this best practice:** 
+  Cache hits substantially reduce latency for repeated data access. 
+  Removing redundant LLM inference calls and external API invocations lowers cost. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Caching is applied at multiple layers of the agent stack, and each layer has its own invalidation discipline. 

 At the LLM inference layer, [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) caches and reuses common prompt prefixes (like system instructions and tool definitions) across invocations, reducing both latency and cost for repeated portions of prompts, prompt caching savings compound further when combined with Amazon Bedrock's Flex pricing tier for development and testing workloads. 

 At the retrieval layer, caching RAG query results under semantic cache keys (embedding-based similarity) rather than exact string matching lets semantically similar queries share cached results. 

 At the tool invocation layer, caching tool outputs based on input parameters with TTLs matched to the data's freshness requirements, a cached stock price has a very different TTL than a cached company description. 

 Cache warming is valuable where access patterns are predictable. If agents frequently access the same knowledge base sections during business hours, pre-warming the cache before peak periods avoids the first-miss penalty for early users. Data access patterns benefit from batching: retrieving multiple items in a single round trip rather than making sequential individual requests reduces both latency and connection overhead. 

 Monitoring cache hit rates, latency savings, and cost savings per cache layer in Amazon CloudWatch makes caching a tunable parameter. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify cacheable data across the agent stack:** Enumerate LLM prompt prefixes, RAG results, tool outputs, session state, and configuration data, each has its own access pattern, freshness requirement, and cache layer. 

1.  **Enable Amazon Bedrock prompt caching for common prompt prefixes shared across invocations:** Turn on [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) and structure prompts so system instructions and tool definitions appear before variable content, letting the cached prefix be reused across requests. 

1.  **Implement retrieval result caching with semantic cache keys and data-type-specific TTLs:** Cache RAG results under embedding-based similarity keys so semantically equivalent queries share results, and tune TTLs to the freshness needs of each data type rather than applying a single global TTL. 

1.  **Implement tool output caching with TTLs calibrated to data freshness requirements:** Cache tool outputs under input-parameter keys with TTLs that match how fast each tool's data changes, short TTLs for real-time data, long TTLs for static reference data. 

1.  **Monitor cache hit rates and latency savings per cache layer using CloudWatch:** Publish hit rate, miss rate, and latency savings per cache layer as CloudWatch metrics so TTLs and warming strategies can be tuned from data rather than assumption. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTPERF03-BP01 Implement tiered memory management systems](agentperf03-bp01.html) 
+  [AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision](agentperf03-bp03.html) 
+  [AGENTPERF02-BP03 Optimize agent execution paths for reduced latency](agentperf02-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) 
+  [Blog: Effectively use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/) 
+  [Blog: Optimize LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/) 
+  [Foundations of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html) 

 **Related services:** 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 