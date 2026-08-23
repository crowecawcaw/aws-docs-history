# Overview

Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](models.md "models.md") from leading AI companies, enabling you to build and scale generative AI applications.

## Quickstart

Read the [Quickstart](getting-started.md "getting-started.md") to write your first API call using Amazon Bedrock in under five minutes. For new applications, we recommend the `bedrock-runtime` endpoint.

Messages API

```
from anthropic import Anthropic
from aws_bedrock_token_generator import provide_token

token = provide_token(region="us-east-1")

client = Anthropic(
    base_url="https://bedrock-runtime.us-east-1.amazonaws.com/anthropic",
    api_key=token,
)

response = client.messages.create(
    model="global.anthropic.claude-opus-4-7",
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

Amazon Bedrock supports [100+ foundation models](models.md "models.md") from industry-leading providers, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, OpenAI, and xAI.

|                                                                               |                                                                                    |                                |                                                                                    |                                                                        |                            |                      |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------- | -------------------- |
| Amazon logo with curved arrow from A to Z forming a smile.<br>**Amazon Nova** | Orange rounded square icon with white radial loading spinner design.<br>**Claude** | DeepSeek logo.<br>**DeepSeek** | Spherical icon with horizontal stripes or segments across its surface.<br>**Kimi** | Red waveform icon representing audio or voice activity.<br>**MiniMax** | OpenAI logo.<br>**OpenAI** | xAI logo.<br>**xAI** |

## What's new?

- [Grok 4.6 from xAI now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-grok-4-6/ "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-grok-4-6/"): xAI's latest flagship model, built for long-running agents, coding, and knowledge work, with a 500K context window and configurable reasoning efforts (low, medium, high, xhigh). Available in all AWS Regions where Amazon Bedrock is offered. See the [Grok 4.6](model-card-xai-grok-4-6.md "model-card-xai-grok-4-6.md") model card for details.
- [Amazon Bedrock expands API support and adds cross-Region inference for OpenAI models](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/ "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/"): OpenAI GPT-5.6 Sol, Terra, and Luna are now available on the `bedrock-runtime` endpoint through the Responses, Converse, and Chat Completions APIs, and now support Global and Geo cross-Region inference for higher throughput and lower per-token cost (including new US Geo CRIS). See [Cross-Region inference](cross-region-inference.md "cross-region-inference.md") for details.
- [Daybreak Red and Daybreak Blue from OpenAI now available in Amazon Bedrock (limited availability)](https://aws.amazon.com/about-aws/whats-new/2026/08/openai-daybreak-red-and-blue-on-amazon-bedrock/ "https://aws.amazon.com/about-aws/whats-new/2026/08/openai-daybreak-red-and-blue-on-amazon-bedrock/"): Specialized cybersecurity models from OpenAI's Daybreak initiative, available to eligible customers. Daybreak Red (GPT-5.6 Cyber) is purpose-trained for vulnerability research, exploit reproduction, and mitigation development. Daybreak Blue (GPT-5.6 Sol) has safeguards calibrated for defensive cybersecurity work. See the [Daybreak Red: GPT-5.6 Cyber](model-card-openai-gpt-56-cyber.md "model-card-openai-gpt-56-cyber.md") and [Daybreak Blue: GPT-5.6 Sol](model-card-openai-gpt-daybreak-blue-56-sol.md "model-card-openai-gpt-daybreak-blue-56-sol.md") model cards for details.
- [Web Search now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web/ "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-web/"): A built-in server-side tool that grounds OpenAI GPT models on Amazon Bedrock in current web knowledge through a single tool-use parameter in the Responses API, with no third-party search vendor to onboard and no data egress from your AWS environment. Available in US East (N. Virginia), US East (Ohio), and US West (Oregon). See [Web Search](web-search.md "web-search.md") for details.
- [OpenAI GPT-5.6 Sol, Terra, and Luna now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/ "https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/"): A family of models from OpenAI that ranges from advanced reasoning to fast, cost-effective inference, now generally available through the Responses API on Amazon Bedrock. See the [GPT-5.6 Sol](model-card-openai-gpt-56-sol.md "model-card-openai-gpt-56-sol.md"), [GPT-5.6 Terra](model-card-openai-gpt-56-terra.md "model-card-openai-gpt-56-terra.md"), and [GPT-5.6 Luna](model-card-openai-gpt-56-luna.md "model-card-openai-gpt-56-luna.md") model cards for details.

## Start building

|                                                                                                             |                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud icon with bidirectional arrows indicating sync or data transfer.                                      | Explore the [APIs supported by Amazon Bedrock](apis.md "apis.md") and [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") supported by Amazon Bedrock. |
| Wrench and screwdriver icon on purple background.                                                           | Build using the [Making inference requests](inference.md "inference.md") operations provided by Amazon Bedrock.                                                         |
| Amazon Bedrock model customization options including fine-tuning, continued pre-training, and distillation. | Customize your models to improve performance and quality. [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md")      |
