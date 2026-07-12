# Agentic AI

###### Topics

- [Agent memory](#aurora-features-agent-memory "#aurora-features-agent-memory")
- [Vector database](#aurora-features-vector-database "#aurora-features-vector-database")
- [Machine learning](#aurora-features-machine-learning "#aurora-features-machine-learning")

## Agent memory

AI agents are stateless without memory. Aurora provides long-term memory for your AI agents, giving them
the ability to remember past interactions and enable more intelligent, context aware, and personalized
conversations.

## Vector database

With Aurora PostgreSQL, you can store, search, index, and query vector embeddings alongside your
transactional data – and vector search scales to hundreds of billions of vectors. You can also use Aurora
PostgreSQL as your vector database in [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/"). With one click, you can configure Aurora
as a Knowledge Base for Bedrock and connect your organization's private data sources from Aurora to LLMs
available in Bedrock to enable automated [Retrieval-Augmented Generation (RAG)](../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md "../../../sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.md") workflows. This makes your LLMs
more knowledgeable about your specific domain and organization. Additional information is available in [Aurora
PostgreSQL as a Knowledge Base for Amazon Bedrock in one click](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.quickcreatekb.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.quickcreatekb.md") documentation.

## Machine learning

[Aurora machine learning (Aurora ML)](../../../AmazonRDS/latest/AuroraUserGuide/aurora-ml.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-ml.md") simplifies adding generative AI model predictions to your Aurora
database. Aurora ML exposes ML models as SQL functions, allowing you to use standard SQL to call ML models,
pass data to them, and return predictions, text summaries, or sentiment as query results. With Aurora ML, you
can make the process of adding new embeddings to your [Aurora PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/postgresql-ml.md "../../../AmazonRDS/latest/AuroraUserGuide/postgresql-ml.md") database with the pgvector extension
real-time via periodic calls to a SageMaker or Amazon Bedrock model, which returns the latest, up-to-date
embeddings.
