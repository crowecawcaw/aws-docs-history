# Getting started with Search

Amazon ElastiCache for Valkey supports real-time full-text, exact-match (tag), numeric range, vector, and hybrid searches. It offers a high-performance search engine optimized for AI-driven / Search / Analytics / Recommendation System related workloads, delivering latency as low as microseconds. ElastiCache for Valkey provides the lowest latency vector search with the highest throughput and best price-performance at 95%+ recall rate among popular vector databases on AWS. ElastiCache for Valkey provides capabilities to index, search, and update billions of high-dimensional vector embeddings from popular providers like Amazon Bedrock, Amazon SageMaker, Anthropic or OpenAI for fast search and retrieval with up to 99% recall. Vector search for Amazon ElastiCache is ideal for use cases where peak performance, consistency and scalability are the most important selection criteria. This includes semantic caching, AI agent memory, retrieval-augmented generation, real-time recommendations, personalization, and anomaly detection.

To learn more about the Search feature availability in ElastiCache Valkey engine versions, see [Search features and limits](search-features-limits.md "search-features-limits.md").

For a detailed description of the supported commands, examples and configuration options, see the [Command Reference](SupportedCommands.md#SupportedCommandsSearch "SupportedCommands.md#SupportedCommandsSearch").

You can learn more about the Search feature and related concepts at [Valkey Search documentation](https://valkey.io/topics/search/ "https://valkey.io/topics/search/").

###### Note

To build search workflows with AI agents, visit the [Agent tools for ElastiCache](AgentTools.md "AgentTools.md") page to install the ElastiCache Skill and Valkey MCP server. They provide the knowledge as well as tools to manage indexes, generate vector embeddings, and a unified search tool for setting up search workflows.

###### Topics

- [Search features and limits](search-features-limits.md "search-features-limits.md")
- [Choosing the appropriate configuration](choosing-configuration.md "choosing-configuration.md")
- [Search write throttling](Durability.SearchThrottling.md "Durability.SearchThrottling.md")
