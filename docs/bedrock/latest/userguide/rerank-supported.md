# Supported Regions and models for reranking in Amazon Bedrock

The following list provides links to general information about Regional and model support in Amazon Bedrock:

- For a list of Region codes and endpoints supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md#bedrock_region "../../../general/latest/gr/bedrock.md#bedrock_region").
- For a list of Amazon Bedrock model IDs to use when calling Amazon Bedrock API operations, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").
  The following table shows the reranker models you can use and the Regions in which they are supported:

###### Note

The Amazon Rerank 1.0 model is not supported in the US East (N. Virginia)
AWS Region. You can only use the Cohere Rerank 3.5 model in this Region.

| Provider | Model      | Regions supporting foundation model                          |
| -------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Amazon   | Rerank 1.0 | us-west-2 ap-northeast-1 ca-central-1 eu-central-1           |
| Cohere   | Rerank 3.5 | us-east-1 us-west-2 ap-northeast-1 ca-central-1 eu-central-1 | For more information about reranking with Cohere models and their inference parameters, see [Rerank](https://docs.cohere.com/reference/rerank "https://docs.cohere.com/reference/rerank") on the Cohere documentation website. |
