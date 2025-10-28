# Real-time vector embedding blueprints

Amazon MSK (Managed Streaming for Apache Kafka) supports Amazon Managed Service for Apache Flink blueprints to generate vector-embeddings using Amazon Bedrock, streamlining the process to build real-time AI applications powered by up-to-date, contextual data. The MSF blueprint simplifies the process of incorporating the latest data from your Amazon MSK streaming pipelines into your generative AI models, eliminating the need to write custom code to integrate real-time data streams, vector databases, and large language models.

You can configure the MSF blueprint to continuously generate vector embeddings using
Bedrock's embedding models, then index those embeddings in OpenSearch Service for their Amazon MSK data
streams. This allows you to combine the context from real-time data with Bedrock's powerful
large language models to generate accurate, up-to-date AI responses without writing custom
code. You can also choose to improve the efficiency of data retrieval using built-in support
for data chunking techniques from LangChain, an open-source library, supporting high-quality
inputs for model ingestion. The blueprint manages the data integration and processing
between MSK, the chosen embedding model, and the OpenSearch vector store, allowing you to
focus on building your AI applications, rather than managing the underlying
integration.

Real-time vector embedding blueprints is available in the following AWS Regions:

- N. Virginia - us-east-1
- Ohio - us-east-2
- Oregon - us-west-2
- Mumbai - ap-south-1
- Seoul - ap-northeast-2
- Singapore - ap-southeast-1
- Sydney - ap-southeast-2
- Tokyo - ap-northeast-1
- Canada Central - ca-central-1
- Frankfurt - eu-central-1
- Ireland - eu-west-1
- London - eu-west-2
- Paris - eu-west-3
- Sao Paulo - sa-east-1

###### Topics

- [Logging and observability](ai-vector-embedding-integration-logging-observability.md "ai-vector-embedding-integration-logging-observability.md")
- [Notes before enabling real-time vector embedding blueprints](ai-vector-embedding-integration-notes.md "ai-vector-embedding-integration-notes.md")
- [Deploy streaming data vectorization blueprint](ai-vector-embedding-integration-deploy.md "ai-vector-embedding-integration-deploy.md")
