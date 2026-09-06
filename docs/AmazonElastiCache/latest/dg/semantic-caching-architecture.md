

# Solution architecture
<a name="semantic-caching-architecture"></a>

The following architecture implements a read-through semantic cache for an agent on Amazon Bedrock AgentCore. A request follows one of two paths:
+ **Cache hit** – If ElastiCache finds a prior query above the configured similarity threshold, AgentCore returns the cached answer immediately. This path invokes only the embedding model and does not require LLM inference. This path has millisecond-level end-to-end latency and does not incur LLM inference cost.
+ **Cache miss** – If no similar prior query is found, AgentCore invokes the LLM to generate a new answer and returns it to the user. The application then caches the prompt's embedding and answer in ElastiCache so that future similar prompts can be served from the cache.