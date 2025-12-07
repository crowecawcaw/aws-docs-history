# Using the Invoke API

The Invoke API provides direct access to Amazon Nova models with more ability to control the request and response format. Unlike the Converse API which abstracts model-specific details, the Invoke API allows you to work directly with the model's native request and response structures.

###### Note

The Invoke API supports the same features as the Converse API except for document
input modality, which is specific to the Converse API.

## Request structure

An Invoke API request requires the model ID and a JSON request body:

```
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

request_body = {
    'messages': [
        {
            'role': 'user',
            'content': [{'text': 'What is machine learning?'}]
        }
    ],
    'inferenceConfig': {
        'maxTokens': 512,
        'temperature': 0.7
    }
}

response = bedrock.invoke_model(
    modelId='us.amazon.nova-2-lite-v1:0',
    body=json.dumps(request_body)
)

response_body = json.loads(response['body'].read())
content_list = response_body["output"]["message"]["content"]
# Extract the first text block
text_block = next((item for item in content_list if "text" in item), None)
if text_block is not None:
    print(text_block["text"])
```

## Request parameters

The Invoke API supports the following key parameters:

- `messages`: Array of conversation messages with role and
  content
- `system`: Optional system prompt for context and
  instructions
- `inferenceConfig`: Parameters controlling model output
  (temperature, maxTokens, topP, topK, stopSequences, reasoningConfig)
- `toolConfig`: Tool specifications and tool choice for function
  calling
