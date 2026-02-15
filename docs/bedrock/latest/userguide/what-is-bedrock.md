# Overview

Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](models.md "models.md") from leading AI companies, enabling you to build and scale generative AI applications.

## Quickstart

Responses API

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Can you explain the features of Amazon Bedrock?"
    )
print(response)
```

Chat Completions API

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-6-v1',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```

Converse API

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='anthropic.claude-opus-4-6-v1',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```

Read the [Quickstart](getting-started.md "getting-started.md") to write your first API call using Amazon Bedrock in under five minutes.

## Models supported

Bedrock supports [100+ foundation models](models.md "models.md") from industry-leading providers, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, and OpenAI.

|                |                     |                  |               |                  |                 |
| -------------- | ------------------- | ---------------- | ------------- | ---------------- | --------------- |
| **Nova 2 Pro** | **Claude Opus 4.6** | **Deepseek 3.2** | **Kimi K2.5** | **MiniMax M2.1** | **GPT-OSS-20B** |

## What's new?

- **[Six new open weight models](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-adds-support-six-open-weights-models/ "https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-adds-support-six-open-weights-models/")**: Amazon Bedrock now supports six new models spanning frontier reasoning and agentic coding: DeepSeek V3.2, MiniMax M2.1, GLM 4.7, GLM 4.7 Flash, Kimi K2.5, and Qwen3 Coder Next.
- **Claude 4.6 [now available](https://aws.amazon.com/about-aws/whats-new/2026/2/claude-opus-4.6-available-amazon-bedrock/ "https://aws.amazon.com/about-aws/whats-new/2026/2/claude-opus-4.6-available-amazon-bedrock/")**: According to Anthropic, Opus 4.6 is their most intelligent model and the world's best model for coding, enterprise agents, and professional work. Read more here.
- **Server-side tools**: Amazon Bedrock [now supports](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-server-side-custom-tools-responses-api/ "https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-server-side-custom-tools-responses-api/") server-side tools in the Responses API using OpenAI API-compatible service endpoints.
- **1-hour prompt caching duration**: Amazon Bedrock [now supports](https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-one-hour-duration-prompt-caching/ "https://aws.amazon.com/about-aws/whats-new/2026/01/amazon-bedrock-one-hour-duration-prompt-caching/") a 1-hour time-to-live (TTL) option for prompt caching for select Anthropic Claude models.
- **NVIDIA Nemotron 3 Nano [now available](https://aws.amazon.com/about-aws/whats-new/2025/12/nvidia-nemotron-3-nano-amazon-bedrock/ "https://aws.amazon.com/about-aws/whats-new/2025/12/nvidia-nemotron-3-nano-amazon-bedrock/")**: NVIDIA Nemotron 3 Nano 30B A3B delivers high reasoning performance, native tool calling support, and extended context processing with 256k token context window.

## Start Building

|     |                                                                                                                                                                         |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     | Explore the [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") supported by Amazon Bedrock. |
|     | Build using the [Submit prompts and generate responses with model inference](inference.md "inference.md") operations provided by Amazon Bedrock.                        |
|     | Customize your models to improve performance and quality. [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md")      |
