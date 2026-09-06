

# Agentic AI
<a name="aurora-features-agentic-ai"></a>

**Topics**
+ [Agent memory](#aurora-features-agent-memory)
+ [Vector database](#aurora-features-vector-database)
+ [Machine learning](#aurora-features-machine-learning)

## Agent memory
<a name="aurora-features-agent-memory"></a>

AI agents are stateless without memory. Aurora provides long-term memory for your AI agents, giving them the ability to remember past interactions and enable more intelligent, context aware, and personalized conversations.

## Vector database
<a name="aurora-features-vector-database"></a>

With Aurora PostgreSQL, you can store, search, index, and query vector embeddings alongside your transactional data – and vector search scales to hundreds of billions of vectors. You can also use Aurora PostgreSQL as your vector database in [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/). With one click, you can configure Aurora as a Knowledge Base for Bedrock and connect your organization's private data sources from Aurora to LLMs available in Bedrock to enable automated [Retrieval-Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) workflows. This makes your LLMs more knowledgeable about your specific domain and organization. Additional information is available in [Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock in one click](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.quickcreatekb.html) documentation.

## Machine learning
<a name="aurora-features-machine-learning"></a>

[Aurora machine learning (Aurora ML)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-ml.html) simplifies adding generative AI model predictions to your Aurora database. Aurora ML exposes ML models as SQL functions, allowing you to use standard SQL to call ML models, pass data to them, and return predictions, text summaries, or sentiment as query results. With Aurora ML, you can make the process of adding new embeddings to your [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-ml.html) database with the pgvector extension real-time via periodic calls to a SageMaker or Amazon Bedrock model, which returns the latest, up-to-date embeddings.