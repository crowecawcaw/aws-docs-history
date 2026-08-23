# Quickstart

Get started with Amazon Bedrock in minutes. For new applications, we recommend the `bedrock-runtime` endpoint. The following steps walk you through running your first
inference request using the Anthropic-native [Messages API](inference-messages-api.md "inference-messages-api.md"), the OpenAI-compatible [Responses API](bedrock-mantle.md "bedrock-mantle.md") and [Chat Completions API](inference-chat-completions.md "inference-chat-completions.md"), and the [Converse](conversation-inference.md "conversation-inference.md") and [Invoke](inference-invoke.md "inference-invoke.md") APIs. For a complete list of APIs, see [Build](build.md "build.md"). After
you complete these steps, you can send inference requests to any supported foundation
model.

###### To run your first inference request

1. Sign up for an [AWS
   account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

If you already have an AWS account, skip this step. 2. Generate a short-term API key to authenticate your requests to Amazon Bedrock by opening the [**Amazon Bedrock** service in the AWS Management
Console](https://console.aws.amazon.com/bedrock/home#/api-keys/short-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/short-term/create").

For the complete procedure, see the [API keys](api-keys.md "api-keys.md") section.

For production applications, use [IAM roles or temporary credentials](../../../IAM/latest/UserGuide/security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys "../../../IAM/latest/UserGuide/security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys"). 3. Install the relevant SDK for the APIs you plan to use. Python must already be installed.

Messages API

```
pip install anthropic aws-bedrock-token-generator
```

Responses/Chat Completions API

```
pip install boto3 openai
```

Invoke/Converse API

```
pip install boto3
```

4. Set the following environment variables to use the API key for authentication.

Messages API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
ANTHROPIC_BASE_URL="https://bedrock-runtime.<your-region>.amazonaws.com/anthropic"
```

Responses/Chat Completions API

```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-runtime.<your-region>.amazonaws.com/openai/v1"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

5. Choose a model and run your first inference request.

   1. Choose a model. Amazon Bedrock supports [100+ foundation
      models](models.md "models.md").
   2. Use the following Python code to run your first inference request.

   Messages API

   ```
   from anthropic import Anthropic
   from aws_bedrock_token_generator import provide_token

   token = provide_token(region="us-east-1")

   client = Anthropic(api_key=token)

   response = client.messages.create(
       model="global.anthropic.claude-opus-5",
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
       model="openai.gpt-5.6-sol",
       input="Can you explain the features of Amazon Bedrock?"
       )
   print(response)
   ```

   Chat Completions API

   ```
   from openai import OpenAI

   client = OpenAI()

   response = client.chat.completions.create(
       model="openai.gpt-5.6-sol",
       messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
       )
   print(response)
   ```

   Converse API

   ```
   import boto3

   client = boto3.client('bedrock-runtime', region_name='us-east-1')
   response = client.converse(
       modelId='global.anthropic.claude-opus-5',
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
       modelId='global.anthropic.claude-opus-5',
       body=json.dumps({
               'anthropic_version': 'bedrock-2023-05-31',
               'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
               'max_tokens': 1024
       })
    )
    print(json.loads(response['body'].read()))
   ```
   3. Save the file as `bedrock-first-request.py`.
   4. Run the code with the following command:

   ```
   python3 bedrock-first-request.py
   ```

   You should see the output of your inference request.
   To learn more about using other APIs and endpoints, see [Build](build.md "build.md").

## Next steps

Now that you have run your first request, explore the following resources to build more with Amazon Bedrock:

- [Automate tasks in your application using AI agents](agents.md "agents.md") – Create agents that can orchestrate multi-step tasks.
- [Retrieve data and generate AI responses with Amazon Bedrock Knowledge Bases](knowledge-base.md "knowledge-base.md") – Connect foundation models to your data sources.
- [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md") – Fine-tune models for your use case.
- [Evaluate the performance of Amazon Bedrock resources](evaluation.md "evaluation.md") – Evaluate model performance for your workloads.
