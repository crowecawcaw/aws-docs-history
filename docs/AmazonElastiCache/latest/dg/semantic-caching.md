

# Using Amazon ElastiCache for Valkey for semantic caching
<a name="semantic-caching"></a>

Large language models (LLMs) are the foundation for generative AI and agentic AI applications that power use cases from chatbots and search assistants to code generation tools and recommendation engines. As the use of AI applications in production grows, customers seek ways to optimize cost and performance. Most AI applications invoke the LLM for every user query, even when queries are repeated or semantically similar. Semantic caching is a method to reduce cost and latency in generative AI applications by reusing responses for identical or semantically similar requests using vector embeddings.

This topic explains how to implement a semantic cache using vector search on Amazon ElastiCache for Valkey, including the concepts, architecture, implementation, benchmarks, and best practices.

**Note**  
To build semantic caching with AI agents, visit the [Agent tools for ElastiCache](AgentTools.md) page to install the ElastiCache Skill and Valkey MCP server. They provide the knowledge as well as automatic embedding generation and similarity search for setting up semantic caching workflows.

**Topics**
+ [Overview of semantic caching](semantic-caching-overview.md)
+ [Why ElastiCache for Valkey for semantic caching](semantic-caching-why-elasticache.md)
+ [Solution architecture](semantic-caching-architecture.md)
+ [Prerequisites](semantic-caching-prerequisites.md)
+ [Implementing a semantic cache with ElastiCache for Valkey](semantic-caching-implementation.md)
+ [Impact and benchmarks](semantic-caching-benchmarks.md)
+ [Multi-turn conversation caching](semantic-caching-multi-turn.md)
+ [Best practices](semantic-caching-best-practices.md)
+ [Related resources](semantic-caching-related-resources.md)