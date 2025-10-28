# GENPERF04-BP01 Test vector store features for latency and

relevant performance

Optimizing a data retrieval system for generative AI typically has
more to do with data architecture and meta data than the foundation
model selected. This best practice encourages high data quality and
data architecture to accelerate data-driven generative AI workloads.

**Desired outcome:** When
implemented, this best practice facilitates expedient data storage
and access, with accurate and relevant data retrieval.

**Benefits of establishing this best
practice:**
[Consider
mechanical sympathy](../framework/perf-dp.md "../framework/perf-dp.md") - Optimizing a data storage system for a
generative AI workload can be as simple as changing vector indexes
or modifying the chunking strategy. Familiarize yourself with how
the system performs data storage and retrieval to best optimize the
database.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Optimizing vector store features for generative AI requires a
holistic approach to search architecture. Begin with effective
chunking and embedding strategies, as these have greater effects
on performance and can only be addressed before data enters the
search engine. There are several popular chunking strategies to
select from, including fixed-size, hierarchical, or semantic. Some
vector base solutions like Amazon Bedrock allow for custom
chunking strategies. There are several factors to consider when
selecting a chunking strategy. Evaluate the available options when
configuring a vector store.

When selecting an approximate nearest neighbor (ANN) algorithm,
consider the trade-offs between accuracy, speed, memory usage, and
scalability. Common options include locality-sensitive hashing
(LSH) for fast indexing, hierarchical navigable small world (HNSW)
for high accuracy, inverted file index (IVF) for balance, and
product quantization (PQ) for compact storage. Benchmark multiple
algorithms with your specific dataset to find the optimal balance.

Organize indices hierarchically, with top-level indices for
general information and lower-level indices for detailed data.
This approach generally outperforms single, all-encompassing
indices.

For search optimization in AI-driven queries, focus on
machine-to-machine interactions. Implement query expansion using
AI-generated context, and shift fuzzy matching towards semantic
similarity. Leverage hybrid search approaches that combine
semantic understanding with traditional retrieval techniques to
enhance result relevance.

Continually monitor performance across all system components,
including embedding generation, index construction, query
processing, and result retrieval. Track latency, throughput, and
resource utilization. Prepare for scenarios where performance
bottlenecks may shift between layers as your system scales and
usage patterns change.

Maintain data quality through regular assessments of freshness,
accuracy, and representativeness. Monitor for data drift and
implement processes for continuous data ingestion and periodic
re-embedding. Use automated checks, human review, and AI output
analysis to maintain data quality. Establish clear governance
policies, and maintain version control of your vector store.

Remember that optimizations in one area can affect the entire
system. Stay adaptable to new techniques and algorithms to
maintain a high-performing, efficient knowledge retrieval system
that delivers accurate, contextually relevant information for your
generative AI application.

### Implementation steps

1. Identify the most important performance KPI for this
   workload (for example, accuracy, speed, memory usage, or
   scalability). Consider implementing a custom search
   algorithm that supports this KPI.
2. Organize indices based on a hierarchy, where more detail is
   introduced towards the bottom of the hierarchy.
3. Establish query latency monitoring on the data retrieval
   system to verify the database latency is consistently
   monitored and alerted upon.
4. Perform regular data quality checks, verifying that data is
   assessed for quality before being placed into a database.

## Resources

**Related practices:**

- [PERF05-BP02](../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md "../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md")
- [PERF05-BP03](../performance-efficiency-pillar/perf_process_culture_workload_performance.md "../performance-efficiency-pillar/perf_process_culture_workload_performance.md")

**Related guides, videos, and documentation:**

- [Working
  with vector search collections](../../../opensearch-service/latest/developerguide/serverless-vector-search.md "../../../opensearch-service/latest/developerguide/serverless-vector-search.md")
- [Vector
  search features and limits](../../../memorydb/latest/devguide/vector-search-limits.md "../../../memorydb/latest/devguide/vector-search-limits.md")

**Related examples:**

- [Amazon OpenSearch Service's vector database capabilities
  explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/ "https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/")
- [Building
  scalable, secure, and reliable RAG applications using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/ "https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/")
- [Dive
  deep into vector data stores using Amazon Bedrock Knowledge
  Bases](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/ "https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/")
