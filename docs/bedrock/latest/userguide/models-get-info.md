# Get information about foundation models

In the Amazon Bedrock console, you can find overarching information about Amazon Bedrock foundation model providers and the models they provide in the **Providers** and **Base models** sections.

Use the API to retrieve information about Amazon Bedrock foundation model, including its ARN, model ID, modalities and features it supports, and whether it is deprecated or not, in a [FoundationModelSummary](../APIReference/API_FoundationModelSummary.md "../APIReference/API_FoundationModelSummary.md") object.

- To return information about all the foundation models that Amazon Bedrock provides, send a [ListFoundationModels](../APIReference/API_ListFoundationModels.md "../APIReference/API_ListFoundationModels.md") request.

###### Note

The response also returns model IDs that aren't in the [base model ID](models-supported.md "models-supported.md") or base model IDs for Provisioned Throughput charts. These model IDs are deprecated or for backwards compability.

- To return information about a specific foundation model, send a [GetFoundationModel](../APIReference/API_GetFoundationModel.md "../APIReference/API_GetFoundationModel.md") request, specifying the [model ID](models-supported.md "models-supported.md").
  Choose a tab to see code examples in an interface or language.

AWS CLI
List the Amazon Bedrock foundation models.

```
aws bedrock list-foundation-models
```

Get information about Anthropic Claude v2.

```
aws bedrock get-foundation-model --model-identifier anthropic.claude-v2
```

Python
List the Amazon Bedrock foundation models.

```
import boto3
bedrock = boto3.client(service_name='bedrock')

bedrock.list_foundation_models()
```

Get information about Anthropic Claude v2.

```
import boto3
bedrock = boto3.client(service_name='bedrock')

bedrock.get_foundation_model(modelIdentifier='anthropic.claude-v2')
```
