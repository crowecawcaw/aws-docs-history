# Using the Invoke API

Another method of invoking the Amazon Nova understanding models (Amazon Nova Micro, Lite, Pro, and Premier) is via the Invoke API. The Invoke API for Amazon Nova models is designed to be consistent
with the Converse API, allowing for the same unification to be extended to support users who
are on the Invoke API (_with the exception of the document understanding feature,
which is specific to the Converse API_). The components discussed previously are
utilized while maintaining a consistent schema across the model providers. The Invoke API
supports the following model features:

- **InvokeModel:** basic multi-turn conversations with
  buffered (as opposed to streamed) responses is supported
- **InvokeModel With Response Stream:** multi-turn conversations with a streamed response for more incremental generation and a more interactive feel
- **System prompts:** system instructions such as personas or response guidelines
- **Vision:** image and video inputs
- **Tool use:** function calling to select various external tools
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

Here's an example of how to use the Invoke Streaming API with boto3, the AWS SDK for Python with
Amazon Nova Lite:

```
`# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import boto3
import json
from datetime import datetime

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

LITE_MODEL_ID = "us.amazon.nova-lite-v1:0"

# Define your system prompt(s).
system_list = [
 {
 "text": "Act as a creative writing assistant. When the user provides you with a topic, write a short story about that topic."
 }
]

# Define one or more messages using the "user" and "assistant" roles.
message_list = [{"role": "user", "content": [{"text": "A camping trip"}]}]

# Configure the inference parameters.
inf_params = {"maxTokens": 500, "topP": 0.9, "topK": 20, "temperature": 0.7}

request_body = {
 "schemaVersion": "messages-v1",
 "messages": message_list,
 "system": system_list,
 "inferenceConfig": inf_params,
}

start_time = datetime.now()

# Invoke the model with the response stream
response = client.invoke_model_with_response_stream(
 modelId=LITE_MODEL_ID, body=json.dumps(request_body)
)

request_id = response.get("ResponseMetadata").get("RequestId")
print(f"Request ID: {request_id}")
print("Awaiting first token...")

chunk_count = 0
time_to_first_token = None

# Process the response stream
stream = response.get("body")
if stream:
 for event in stream:
 chunk = event.get("chunk")
 if chunk:
 # Print the response chunk
 chunk_json = json.loads(chunk.get("bytes").decode())
 # Pretty print JSON
 # print(json.dumps(chunk_json, indent=2, ensure_ascii=False))
 content_block_delta = chunk_json.get("contentBlockDelta")
 if content_block_delta:
 if time_to_first_token is None:
 time_to_first_token = datetime.now() - start_time
 print(f"Time to first token: {time_to_first_token}")

 chunk_count += 1
 current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
 # print(f"{current_time} - ", end="")
 print(content_block_delta.get("delta").get("text"), end="")
 print(f"Total chunks: {chunk_count}")
else:
 print("No response stream received.")`
```

For more information about the Invoke API operations, including the request and response syntax, see [InvokeModelWithResponseStream](../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md") in the Amazon Bedrock API documentation.
