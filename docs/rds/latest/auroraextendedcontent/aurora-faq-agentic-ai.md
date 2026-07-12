# Agentic AI

###### Topics

- [What is pgvector and how does it work with Amazon Aurora?](#aurora-faq-what-is-pgvector-and-how-does-it-work-with-amazon-aurora "#aurora-faq-what-is-pgvector-and-how-does-it-work-with-amazon-aurora")
- [Can I use Aurora machine learning to keep vector embeddings up to date?](#aurora-faq-can-i-use-aurora-machine-learning-to-keep-vector-embeddings- "#aurora-faq-can-i-use-aurora-machine-learning-to-keep-vector-embeddings-")
- [How does Amazon Aurora integrate with Amazon Bedrock?](#aurora-faq-how-does-amazon-aurora-integrate-with-amazon-bedrock "#aurora-faq-how-does-amazon-aurora-integrate-with-amazon-bedrock")
- [How does Amazon Aurora integrate with Amazon Bedrock AgentCore?](#aurora-faq-how-does-amazon-aurora-integrate-with-amazon-bedrock-agentco "#aurora-faq-how-does-amazon-aurora-integrate-with-amazon-bedrock-agentco")
- [How does optimized reads for Aurora PostgreSQL improve vector search performance?](#aurora-faq-how-does-optimized-reads-for-aurora-postgresql-improve-vecto "#aurora-faq-how-does-optimized-reads-for-aurora-postgresql-improve-vecto")

## What is pgvector and how does it work with Amazon Aurora?

[pgvector](https://github.com/pgvector/pgvector "https://github.com/pgvector/pgvector") is an open-source extension for PostgreSQL supported by Aurora PostgreSQL. You can use pgvector to store, search, index, and query hundreds of billions of vector embeddings generated from AI and ML models — such as those from [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") or [Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/").

Vector embeddings are numerical representations of semantic meaning for content like text, images, and video. With pgvector, you can perform efficient semantic similarity searches combined with traditional tabular data in Aurora, enabling applications like:

- Personalized recommendations
- Chatbots and customer service agents
- Candidate matching
- Next-best-action recommendations

For Aurora PostgreSQL, using optimized reads with pgvector increases queries per second for vector search by up to 9x for workloads exceeding available instance memory. Read our [blog on vector database capabilities](https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/ "https://aws.amazon.com/blogs/database/leverage-pgvector-and-amazon-aurora-postgresql-for-natural-language-processing-chatbots-and-sentiment-analysis/").

## Can I use Aurora machine learning to keep vector embeddings up to date?

Yes. [Aurora machine learning](https://aws.amazon.com/rds/aurora/machine-learning/ "https://aws.amazon.com/rds/aurora/machine-learning/") (ML) exposes ML models as SQL functions, allowing you to call models, pass data, and return predictions using standard SQL. While pgvector requires embeddings to be stored in the database, Aurora ML can make this a real-time process by making periodic calls to [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/") or [Amazon SageMaker](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to return the most recent embeddings from your model.

## How does Amazon Aurora integrate with Amazon Bedrock?

There are two methods to integrate Aurora with Amazon Bedrock for agentic AI applications:

- Aurora ML: Access foundation models in Amazon Bedrock directly through SQL for both [Aurora MySQL](../../../AmazonRDS/latest/AuroraUserGuide/mysql-ml.md "../../../AmazonRDS/latest/AuroraUserGuide/mysql-ml.md") and [Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/postgresql-ml.md "../../../AmazonRDS/latest/AuroraUserGuide/postgresql-ml.md").
- [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/"): Configure Aurora PostgreSQL as your vector store in Amazon Bedrock Knowledge Bases in one click for [Retrieval-Augmented Generation (RAG)](../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md "../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md") use cases.

Read our [blog](https://aws.amazon.com/blogs/database/accelerate-your-generative-ai-application-development-with-amazon-bedrock-knowledge-bases-quick-create-and-amazon-aurora-serverless/ "https://aws.amazon.com/blogs/database/accelerate-your-generative-ai-application-development-with-amazon-bedrock-knowledge-bases-quick-create-and-amazon-aurora-serverless/") and documentation on [Using Aurora PostgreSQL as a knowledge base for Amazon Bedrock](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.md").

## How does Amazon Aurora integrate with Amazon Bedrock AgentCore?

Aurora integrates with [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/") to help you bring AI agents to production faster. You can persist agent memories within Aurora — a trusted, fully managed database — enabling agentic AI architectures where agents maintain context across sessions. Aurora also works with agentic frameworks such as Letta and LangGraph, as well as AI-coding assistants such as v0 by Vercel.

## How does optimized reads for Aurora PostgreSQL improve vector search performance?

Optimized reads with pgvector increases queries per second for vector search by up to 9x in workloads that exceed available instance memory. This is possible due to the tiered caching capability that automatically caches data evicted from the in-memory database buffer cache onto local storage. Read our [blog](https://aws.amazon.com/blogs/database/accelerate-generative-ai-workloads-on-amazon-aurora-with-optimized-reads-and-pgvector/ "https://aws.amazon.com/blogs/database/accelerate-generative-ai-workloads-on-amazon-aurora-with-optimized-reads-and-pgvector/") and documentation on how to [improve query performance for Aurora PostgreSQL with Aurora Optimized Reads](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.md").
