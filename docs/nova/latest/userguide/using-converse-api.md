# Using the Converse API

###### Note

This documentation is for Amazon Nova Version 1. For information on how to use the Converse API with Amazon Nova 2, visit [Using the Converse API](../nova2-userguide/using-converse-api.md "../nova2-userguide/using-converse-api.md").

One method of invoking the Amazon Nova understanding models (Amazon Nova Micro, Lite, Pro, and Premier)
is through the Converse API. The components discussed previously are utilized while
maintaining a consistent schema across the model providers. This approach offers a convenient
way to implement more portable applications by leveraging a consistent API, enabling existing
applications using other models to be more easily ported to the Nova models. The Converse API
supports the following model features:

- **Converse:** basic multi-turn conversations with buffered
  (as opposed to streamed) responses is supported
- **ConverseStream:** multi-turn conversations with a streamed response for more incremental generation and a more interactive feel
- **System prompts:** system instructions such as personas or response guidelines
- **Document chat:** interact with and query documents or
  collections of documents
- **Vision:** image and video inputs
- **Tool use:** function calling to support various external tools
- **Streaming tool use:** combine tool use and real-time generation streaming
- **Guardrails:** prevent inappropriate or harmful
  content

###### Important

The timeout period for inference calls to Amazon Nova is 60 minutes.
By default, AWS SDK clients timeout after 1 minute. We recommend that you increase the
read timeout period of your AWS SDK client to at least 60 minutes. For example, in the
AWS Python botocore SDK, change the value of the `read_timeout`field in
[botocore.config](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html# "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#") to at least 3600.

```
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1",
    config=Config(
        connect_timeout=3600,  # 60 minutes
        read_timeout=3600,     # 60 minutes
        retries={'max_attempts': 1}
    )
)
```

You can use Amazon Nova models with Converse API as you would with any other model. Set the
modelId to one of the following to use the Amazon Nova models.

| Amazon Nova Micro      | Amazon Nova Lite      | Amazon Nova Pro      | Amazon Nova Premier      |
| ---------------------- | --------------------- | -------------------- | ------------------------ |
| amazon.nova-micro-v1:0 | amazon.nova-lite-v1:0 | amazon.nova-pro-v1:0 | amazon.nova-premier-v1:0 |

The Converse API supports the following inference parameters passed as a JSON object under the `inferenceConfig` attribute:

- `maxTokens` - The maximum number of tokens to allow in the response.
- `stopSequences` - A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.
- `temperature` - The likelihood of the model selecting higher-probability options while generating a response.
- `topP` - The percentage of most-likely candidates that the model considers for the next token.
  The additional parameter "topK" can be passed through the `additionalModelRequestFields` attribute, as shown below.

Here's an example of how to use Converse API with boto3, the AWS SDK for Python with
Amazon Nova Lite:

```
`import boto3
import json

client = boto3.client("bedrock-runtime")

system = [{ "text": "You are a helpful assistant" }]

messages = [
 {"role": "user", "content": [{"text": "Write a short story about dragons"}]},
]

inf_params = {"maxTokens": 300, "topP": 0.1, "temperature": 0.3}

additionalModelRequestFields = {
 "inferenceConfig": {
 "topK": 20
 }
}

model_response = client.converse(
 modelId="us.amazon.nova-lite-v1:0",
 messages=messages,
 system=system,
 inferenceConfig=inf_params,
 additionalModelRequestFields=additionalModelRequestFields
)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])`
```

For more details on Converse API and how to make use of it please refer to [_Carry out a conversation with the Converse API
operations_](../../../bedrock/latest/userguide/conversation-inference.md "../../../bedrock/latest/userguide/conversation-inference.md").
