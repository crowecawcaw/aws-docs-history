# Supported Regions and models for model sharing

The following list provides links to general information about Regional and model support in Amazon Bedrock:

- For a list of Region codes and endpoints supported in Amazon Bedrock, see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md#bedrock_region "../../../general/latest/gr/bedrock.md#bedrock_region").
- For a list of Amazon Bedrock model IDs to use when calling Amazon Bedrock API operations, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").
  The following table shows the models that you can share and the Regions from which you can share:

| Provider  | Model                          | Regions supporting foundation model                                              |
| --------- | ------------------------------ | -------------------------------------------------------------------------------- |
| Amazon    | Titan Multimodal Embeddings G1 | us-east-1<br>us-west-2<br>ap-south-1<br>ap-southeast-2<br>eu-west-1<br>eu-west-3 |
| Amazon    | Titan Image Generator G1       | us-east-1<br>us-west-2<br>ap-south-1<br>eu-west-1                                |
| Amazon    | Titan Text G1<br>• Express     | us-east-1<br>us-west-2<br>ap-south-1<br>ap-southeast-2<br>eu-west-1<br>eu-west-3 |
| Amazon    | Titan Text G1<br>• Lite        | us-east-1<br>us-west-2<br>ap-south-1<br>ap-southeast-2<br>eu-west-1<br>eu-west-3 |
| Anthropic | Claude 3 Haiku                 | us-east-1<br>us-west-2<br>ap-south-1<br>ap-southeast-2<br>eu-west-1<br>eu-west-2 |

###### Note

Custom Amazon Titan Text Premier models aren't shareable because they can't be [copied to a Region](copy-model.md "copy-model.md").
