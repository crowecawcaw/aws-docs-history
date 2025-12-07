# Streaming responses

Streaming allows you to receive model responses incrementally as they are generated,
providing a more interactive user experience. Both the Converse API and Invoke API
support streaming.

## Streaming with ConverseStream

Use `ConverseStream` to receive responses as a stream of events:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse_stream(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Write a short story about AI.'}]
        }
    ]
)

for event in response['stream']:
    if 'contentBlockDelta' in event:
        delta = event['contentBlockDelta']['delta']
        if 'text' in delta:
            print(delta['text'], end='', flush=True)
```

## Streaming with

InvokeModelWithResponseStream

Use `InvokeModelWithResponseStream` for streaming with the Invoke
API:

```
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

request_body = {
    'messages': [
        {
            'role': 'user',
            'content': [{'text': 'Explain quantum computing.'}]
        }
    ]
}

response = bedrock.invoke_model_with_response_stream(
    modelId='us.amazon.nova-2-lite-v1:0',
    body=json.dumps(request_body)
)

for event in response['body']:
    chunk = json.loads(event['chunk']['bytes'])
    if 'contentBlockDelta' in chunk:
        delta = chunk['contentBlockDelta']['delta']
        if 'text' in delta:
            print(delta['text'], end='', flush=True)
```

## Stream event types

Streaming responses include several event types:

- `messageStart`: Indicates the start of a message
- `contentBlockStart`: Indicates the start of a content
  block
- `contentBlockDelta`: Contains incremental text or data
- `contentBlockStop`: Indicates the end of a content block
- `messageStop`: Indicates the end of the message with stop
  reason
- `metadata`: Contains usage information (token counts)
