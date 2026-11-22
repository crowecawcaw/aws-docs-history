

# What is Amazon OpenSearch Memory?

Amazon OpenSearch Memory is a fully managed memory service for AI agents. Your agent or application sends the conversations and data it works with to OpenSearch Memory as *events*. OpenSearch Memory extracts the facts, summaries, and other details worth keeping from those events and stores them as *memories*. Your agent then searches those memories to recall what it learned, across sessions and over time.

With OpenSearch Memory, you don't build or operate a memory system yourself. You don't run a vector database, write extraction prompts for common cases, or manage the pipeline that turns raw conversation into durable knowledge. You create a *space*, choose the kinds of memory you want, send events, and search.

**Topics**
+ [Benefits](#memory-benefits)
+ [Related resources](#memory-related-resources)
+ [How Amazon OpenSearch Memory works](memory-how-it-works.md)
+ [Getting started with Amazon OpenSearch Memory](memory-getting-started.md)
+ [Working with spaces in Amazon OpenSearch Memory](memory-spaces.md)
+ [Security in Amazon OpenSearch Memory](memory-security.md)
+ [Monitoring Amazon OpenSearch Memory](memory-monitoring.md)
+ [Best practices for Amazon OpenSearch Memory](memory-best-practices.md)
+ [Endpoints and quotas for Amazon OpenSearch Memory](memory-quotas.md)
+ [Error handling in Amazon OpenSearch Memory](memory-errors.md)
+ [Troubleshooting Amazon OpenSearch Memory](memory-troubleshooting.md)

## Benefits
<a name="memory-benefits"></a>

OpenSearch Memory has the following benefits:
+ **Fully managed** – OpenSearch Memory handles storage, indexing, extraction, and the model calls that extraction needs. There are no servers to provision, no software to patch, and no maintenance windows. You don't request access to any foundation model or grant any model permissions.
+ **Fast writes** – [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) returns as soon as the event is stored. OpenSearch Memory extracts memories afterward, in the background, so your agent's response time doesn't depend on how long extraction takes.
+ **Memories that stay current** – By default, OpenSearch Memory consolidates new memories with what it already knows. When a user who said "I live in Seattle" later says "I moved to Austin," the stored fact is updated rather than duplicated or contradicted. For more information, see [Consolidation](memory-strategies.md#memory-strategies-consolidation).
+ **Familiar search** – You search memories with a subset of the OpenSearch Query DSL, including `match`, `neural`, `hybrid`, and `bool` queries. Results come back ranked by relevance. For more information, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).
+ **Isolated by user** – Searches are scoped to one actor, so one user's memories never surface for another. You can also enforce this in IAM with the `osm:actorId` condition key. For more information, see [Identity and Access Management for Amazon OpenSearch Memory](security-iam-memory.md).
+ **Retention you control** – You choose how long a space keeps events (1 to 365 days) and memories (from 1 day to 10 years, or indefinitely). Expired events and memories are removed for you. For more information, see [Configuring retention](memory-spaces.md#memory-spaces-retention).

For more information, see [How Amazon OpenSearch Memory works](memory-how-it-works.md). To get started, see [Getting started with Amazon OpenSearch Memory](memory-getting-started.md).

## Related resources
<a name="memory-related-resources"></a>

For more information, see the following related resources:
+ [Amazon OpenSearch Memory API Reference](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/Welcome.html)
+ [AWS CLI commands for Amazon OpenSearch Memory](https://docs.aws.amazon.com/cli/latest/reference/opensearchmemory/)
+ [SDKs & Tools](https://aws.amazon.com/tools/)