# Monitor your token usage by counting tokens before running inference

When you run model inference, the number of tokens that you send in the input contributes to the cost of the request and towards the quota of tokens that you can use per minute and per day. The [CountTokens](../APIReference/API_runtime_CountTokens.md "../APIReference/API_runtime_CountTokens.md") API helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.

###### Note

Using the [CountTokens](../APIReference/API_runtime_CountTokens.md "../APIReference/API_runtime_CountTokens.md") API doesn't incur charges.

Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model to run inference.

You can use the `CountTokens` API to do the following:

- Estimate costs before sending inference requests.
- Optimize prompts to fit within token limits.
- Plan for token usage in your applications.

###### Topics

- [Supported models and Regions for token counting](#count-tokens-supported "#count-tokens-supported")
- [Count tokens in a request](#count-tokens-use "#count-tokens-use")
- [Try an example](#count-tokens-example "#count-tokens-example")

## Supported models and Regions for token counting

Count tokens API is supported in the following Regions (for more information about Regions supported in Amazon Bedrock see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")):

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Asia Pacific (Tokyo)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Ireland)
- Europe (London)
- South America (São Paulo)

Count tokens API is supported for the following foundation models (to see which Regions support each model, refer to [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md")):

- Anthropic Claude 3.5 Haiku
- Anthropic Claude 3.5 Sonnet v2
- Anthropic Claude 3.5 Sonnet
- Anthropic Claude 3.7 Sonnet
- Anthropic Claude Opus 4
- Anthropic Claude Sonnet 4

## Count tokens in a request

To count the number of input tokens in an inference request, send a [CountTokens](../APIReference/API_runtime_CountTokens.md "../APIReference/API_runtime_CountTokens.md") request with an [Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt"), Specify the model in the header and the input to count tokens for in the `body` field. The value of the `body` field depends on whether you're counting input tokens for an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") request:

- For an `InvokeModel` request, the format of the `body` is a string representing a JSON object whose format depends on the model that you specify.
- For a `Converse` request, the format of the `body` is a JSON object specifying the `messages` and `system` prompts included in the conversation.

## Try an example

The examples in this section let you count tokens for an `InvokeModel` and `Converse` request with Anthropic Claude 3 Haiku.

###### Prerequisites

- You've downloaded AWS SDK for Python (Boto3) and your configuration is set up such that your credentials and default AWS Region are automatically recognized.
- Your IAM identity has permissions for the following actions (for more information, see [Action, resources, and condition keys for Amazon Bedrock](../../../service-authorization/latest/reference/list_amazonbedrock.md "../../../service-authorization/latest/reference/list_amazonbedrock.md")):
  - bedrock:CountTokens – Allows the usage of `CountTokens`.
  - bedrock:InvokeModel – Allows the usage of `InvokeModel` and `Converse`. Should be scoped to the `arn:${Partition}:bedrock:${Region}::foundation-model/anthropic.claude-3-haiku-20240307-v1:0`, at minimum.

To try out counting tokens for an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") request, run the following Python code:

```
import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime")

input_to_count = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
})

response = bedrock_runtime.count_tokens(
    modelId="anthropic.claude-3-5-haiku-20241022-v1:0",
    input={
        "invokeModel": {
            "body": input_to_count
        }
    }
)

print(response["inputTokens"])

```

To try out counting tokens for a [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md") request, run the following Python code:

```
import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime")

input_to_count = {
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What is the capital of France?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "The capital of France is Paris."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "text": "What is its population?"
                }
            ]
        }
    ],
    "system": [
        {
            "text": "You're an expert in geography."
        }
    ]
}

response = bedrock_runtime.count_tokens(
    modelId="anthropic.claude-3-5-haiku-20241022-v1:0",
    input={
        "converse": input_to_count
    }
)

print(response["inputTokens"])

```
