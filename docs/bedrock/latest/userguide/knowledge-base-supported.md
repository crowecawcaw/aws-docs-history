# Supported models and Regions for Amazon Bedrock knowledge bases

Amazon Bedrock Knowledge Bases is supported in the following Regions (for more information about Regions supported in Amazon Bedrock see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")):

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- AWS GovCloud (US-East)
- AWS GovCloud (US-West)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Mumbai)
- Asia Pacific (Hyderabad)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Spain)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- South America (São Paulo)
  You can use the following foundation models (to see which Regions support each model, refer to [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md")) for knowledge base query:

- AI21 Labs Jamba 1.5 Large
- AI21 Labs Jamba 1.5 Mini
- Amazon Nova Lite
- Amazon Nova Micro
- Amazon Nova Pro
- Anthropic Claude 3 Haiku
- Anthropic Claude 3 Sonnet
- Anthropic Claude 3.5 Haiku
- Anthropic Claude 3.5 Sonnet v2
- Anthropic Claude 3.5 Sonnet
- Anthropic Claude 3.7 Sonnet
- Anthropic Claude Opus 4
- Anthropic Claude Sonnet 4.5
- Anthropic Claude Sonnet 4
- Cohere Command R+
- Cohere Command R
- DeepSeek DeepSeek-R1
- Meta Llama 3 70B Instruct
- Meta Llama 3 8B Instruct
- Meta Llama 3.1 405B Instruct
- Meta Llama 3.1 70B Instruct
- Meta Llama 3.1 8B Instruct
- Meta Llama 3.2 11B Instruct
- Meta Llama 3.2 90B Instruct
- Meta Llama 3.3 70B Instruct
- Mistral AI Mistral Large (24.02)
- Mistral AI Mistral Large (24.07)
- Mistral AI Mistral Small (24.02)
  Amazon Bedrock Knowledge Bases also supports the use of inference profiles for parsing data or when generating responses. With inference profiles, you can track costs and metrics, and also do cross-Region inference to distribute model inference requests across a set of Regions to allow higher throughput. You can specify an inference profile in a [RetrieveAndGenerate](../APIReference/API_agent-runtime_RetrieveAndGenerate.md "../APIReference/API_agent-runtime_RetrieveAndGenerate.md") or [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") request. For more information, see [Set up a model invocation resource using inference profiles](inference-profiles.md "inference-profiles.md").

###### Important

If you use cross-Region inference, your data can be shared across Regions.

You can also use SageMaker AI models or [custom models](custom-models.md "custom-models.md") that you train on your own data.

###### Note

If you use an SageMaker AI or custom model, you must specify the orchestration and generation prompts (for more information, see **Knowledge base prompt templates** in [Configure and customize queries and response
generation](kb-test-config.md "kb-test-config.md")). Your prompts must include information variables to access the user's input and context.

Region and model support differ for some features in Amazon Bedrock Knowledge Bases. Select a topic to view support for a feature:

###### Topics

- [Supported models for vector embeddings](#knowledge-base-supported-embeddings "#knowledge-base-supported-embeddings")
- [Supported models and Regions for parsing](#knowledge-base-supported-parsing "#knowledge-base-supported-parsing")
- [Supported models and Regions for reranking results during query](#knowledge-base-supported-rerank "#knowledge-base-supported-rerank")
- [Supported Regions for Knowledge Bases with structured data stores](#knowledge-base-supported-structured "#knowledge-base-supported-structured")

## Supported models for vector embeddings

Amazon Bedrock Knowledge Bases uses an embedding model to convert your data into vector embeddings and store the
embeddings in a vector database. For more information, see [Turning data into a knowledge base](kb-how-data.md "kb-how-data.md").

Embedding models support the following vector types.

| Model name                           | Supported vector type  | Supported number of dimensions |
| ------------------------------------ | ---------------------- | ------------------------------ |
| Amazon Titan Embeddings G1<br>• Text | Floating-point         | 1536                           |
| Amazon Titan Text Embeddings V2      | Floating-point, binary | 256, 512, 1024                 |
| Cohere Embed (English)               | Floating-point, binary | 1024                           |
| Cohere Embed (Multilingual)          | Floating-point, binary | 1024                           |

## Supported models and Regions for parsing

When converting data into vector embeddings, you have different options for parsing your data in Amazon Bedrock Knowledge Bases. For more information, see [Parsing options for your data source](kb-advanced-parsing.md "kb-advanced-parsing.md").

The following lists support for parsing options:

- The Amazon Bedrock Data Automation parser is supported in US West (Oregon) and is in preview and subject to change.
- The following foundation model families can be used as a parser:

      + Claude vision models
      + Nova vision models
      + LLama 4 vision models

  Foundation model parsing is available in AWS Regions where these models are directly available (not through cross-region inference). For current model availability by Region, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

## Supported models and Regions for reranking results during query

When retrieving knowledge base query results, you can use a reranking model to rerank results from knowledge base query. For more information, see [Query a knowledge base and retrieve data](kb-test-retrieve.md "kb-test-retrieve.md") and [Query a knowledge base and generate responses based off the retrieved data](kb-test-retrieve-generate.md "kb-test-retrieve-generate.md").

For a list of models and Regions that support reranking, see [Supported Regions and models for reranking in Amazon Bedrock](rerank-supported.md "rerank-supported.md").

## Supported Regions for Knowledge Bases with structured data stores

Knowledge Bases with structured data stores allow you to connect knowledge bases to structured data stores and convert natural language queries into SQL queries. For more information, see [Build a knowledge base by connecting to a structured data store](knowledge-base-build-structured.md "knowledge-base-build-structured.md").

Knowledge Bases with structured data stores are available in the following AWS Regions:

- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- South America (São Paulo)
- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- AWS GovCloud (US-West)
