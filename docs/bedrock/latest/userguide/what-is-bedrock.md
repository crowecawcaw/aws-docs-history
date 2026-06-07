# Overview

Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](models.md "models.md") from leading AI companies, enabling you to build and scale generative AI applications.

## Quickstart

Read the [Quickstart](getting-started.md "getting-started.md") to write your first API call using Amazon Bedrock in under five minutes.

Messages API

```
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="anthropic.claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response)
```

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

Converse API

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='anthropic.claude-opus-4-7',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```

Invoke API

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-7',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```

## Supported models

Bedrock supports [100+ foundation models](models.md "models.md") from industry-leading providers, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, and OpenAI.

|                                                                               |                                                                                    |              |                                                                                    |                                                                        |            |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- |
| Amazon logo with curved arrow from A to Z forming a smile.<br>**Amazon Nova** | Orange rounded square icon with white radial loading spinner design.<br>**Claude** | **DeepSeek** | Spherical icon with horizontal stripes or segments across its surface.<br>**Kimi** | Red waveform icon representing audio or voice activity.<br>**MiniMax** | **OpenAI** |

## What's new?

- **OpenAI GPT-5.5 and GPT-5.4 now available in Amazon Bedrock**: OpenAI's frontier models for complex professional work, agentic coding, reasoning, and long-running tasks are now available through the Responses API on Amazon Bedrock. See the [GPT-5.5](model-card-openai-gpt-55.md "model-card-openai-gpt-55.md") and [GPT-5.4](model-card-openai-gpt-54.md "model-card-openai-gpt-54.md") model cards for details.
- **[Claude Opus 4.7 now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/04/claude-opus-4.7-amazon-bedrock/ "https://aws.amazon.com/about-aws/whats-new/2026/04/claude-opus-4.7-amazon-bedrock/")**: Anthropic's most capable Opus model to date, delivering improvements across agentic coding, professional work, and long-running tasks.
- **[Claude Mythos Preview (Gated Research Preview)](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-claude-mythos/ "https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-claude-mythos/")**: Anthropic's most advanced AI model with state-of-the-art capabilities across cybersecurity, software coding, and complex reasoning tasks. Available in gated preview in US East (N. Virginia).
- **[Cost allocation by IAM user and role](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-iam-cost-allocation/ "https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-iam-cost-allocation/")**: Amazon Bedrock now supports cost allocation by IAM principal in AWS Cost and Usage Report 2.0 and Cost Explorer, enabling customers to attribute model inference costs across users, teams, and projects.

## Start Building

|                                                                        |                                                                                                                                                                         |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud icon with bidirectional arrows indicating sync or data transfer. | Explore the [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") supported by Amazon Bedrock. |
| Wrench and screwdriver icon on purple background.                      | Build using the [Making inference requests](inference.md "inference.md") operations provided by Amazon Bedrock.                                                         |
|                                                                        | Customize your models to improve performance and quality. [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md")      |
