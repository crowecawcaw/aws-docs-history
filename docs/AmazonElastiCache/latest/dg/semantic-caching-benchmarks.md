

# Impact and benchmarks
<a name="semantic-caching-benchmarks"></a>

AWS evaluated the approach on 63,796 real user chatbot queries and their paraphrased variants from the public SemBenchmarkLmArena dataset. This dataset captures user interactions with the Chatbot Arena platform across general assistant use cases such as question answering, writing, and analysis.

The evaluation used the following configuration:
+ ElastiCache `cache.r7g.large` instance as the semantic cache store
+ Amazon Titan Text Embeddings V2 for embeddings
+ Claude 3 Haiku for LLM inference

The cache was started empty, and all 63,796 queries were streamed as random incoming user traffic, simulating real-world application traffic.

## Cost and accuracy at different similarity thresholds
<a name="semantic-caching-cost-accuracy"></a>

The following table summarizes the trade-off between cost reduction, latency improvement, and accuracy across different similarity thresholds:


| Similarity threshold | Cache hit ratio | Accuracy of cached responses | Total daily cost | Cost savings | Average latency (s) | Latency reduction | 
| --- | --- | --- | --- | --- | --- | --- | 
| Baseline (no cache) | – | – | $49.50 | – | 4.35 | – | 
| 0.99 (very strict) | 23.5% | 92.1% | $41.70 | 15.8% | 3.60 | 17.1% | 
| 0.95 (strict) | 56.0% | 92.6% | $23.80 | 51.9% | 1.84 | 57.7% | 
| 0.90 (moderate) | 74.5% | 92.3% | $13.60 | 72.5% | 1.21 | 72.2% | 
| 0.80 (balanced) | 87.6% | 91.8% | $7.60 | 84.6% | 0.60 | 86.1% | 
| 0.75 (relaxed) | 90.3% | 91.2% | $6.80 | 86.3% | 0.51 | 88.3% | 
| 0.50 (very relaxed) | 94.3% | 87.5% | $5.90 | 88.0% | 0.46 | 89.3% | 

At a similarity threshold of 0.75, semantic caching reduced LLM inference cost by up to 86% while maintaining 91% answer accuracy. The choice of LLM, embedding model, and backing store affects both cost and latency. Semantic caching delivers proportionally larger benefits when used with bigger, higher-cost LLMs.

## Individual query latency improvements
<a name="semantic-caching-latency-improvements"></a>

The following table shows the impact on individual query latency. A cache hit reduced latency by up to 59x, from multiple seconds to a few hundred milliseconds:


| Query intent | Cache miss latency | Cache hit latency | Reduction | 
| --- | --- | --- | --- | 
| "Are there instances where SI prefixes deviate from denoting powers of 10, excluding their application?" → paraphrased variant | 6.51 s | 0.11 s | 59x | 
| "Sally is a girl with 3 brothers, and each of her brothers has 2 sisters. How many sisters are there in Sally's family?" → paraphrased variant | 1.64 s | 0.13 s | 12x | 