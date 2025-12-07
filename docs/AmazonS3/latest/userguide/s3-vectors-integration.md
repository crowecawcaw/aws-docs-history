# Using S3 Vectors with other AWS services

S3 Vectors integrates with other AWS services to enhance your vector processing capabilities and provide comprehensive solutions for AI and machine learning workloads. These integrations allow you to leverage the cost-effective storage of S3 Vectors alongside the specialized capabilities of other AWS services.

## Available integrations

S3 Vectors provides native integrations with the following AWS services:

- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") - You can export a snapshot of a vector index to Amazon OpenSearch Service for high queries per second (QPS) and low latency vector search. Additionally, Amazon OpenSearch Service adds Amazon S3 Vectors as a new low-cost engine for customers who want to optimize cost while continuing to use Amazon OpenSearch Service API operations for advanced search functionality including hybrid search, aggregations, advanced filtering, faceted search, and more.
- [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") - Use S3 Vectors as your vector store for Retrieval Augmented Generation (RAG) applications, reducing storage costs while maintaining query performance for knowledge base operations. You can access this integration through the Amazon Bedrock console or [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/").

## Integration benefits

These integrations provide several key advantages:

- **Cost optimization**: Store large vector datasets cost-effectively in S3 Vectors while using specialized services for specific workloads, such as using Amazon OpenSearch for advanced search functionality.
- **Performance flexibility**: Choose the right integration for your performance requirements: S3 Vectors for lower throughput storage and sporadic querying, and other services for high-throughput, low-latency operations.
- **Workflow integration**: Seamlessly incorporate vector operations into existing AWS based AI and ML pipelines.
- **Simplified management**: Reduce operational complexity by using managed integrations rather than building custom solutions.

###### Topics

- [Using S3 Vectors with OpenSearch Service](s3-vectors-opensearch.md "s3-vectors-opensearch.md")
- [Using S3 Vectors with Amazon Bedrock Knowledge Bases](s3-vectors-bedrock-kb.md "s3-vectors-bedrock-kb.md")
