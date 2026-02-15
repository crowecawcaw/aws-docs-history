# Quickstart

In this section, we will show you how to get started with Amazon Bedrock within a few minutes. We will use the OpenAI-compatible APIs: [Responses API](bedrock-mantle.md "bedrock-mantle.md") and [Chat Completions API](inference-chat-completions.md "inference-chat-completions.md"), and the [Invoke](inference-invoke.md "inference-invoke.md") and [Converse API](conversation-inference.md "conversation-inference.md") to show you how run an inference request. See [Build](build.md "build.md") for list of complete APIs.

**Step 1 - AWS Account:** If you have an AWS account already, skip this step and go to step 2. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup") and follow instructions.

**Step 2 - API key:** Once you have an AWS account, you can create a long-term API key to authenticate your requests to Amazon Bedrock. To do that, go to the [Amazon Bedrock service in AWS Console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long term key. For more information, see the [API keys](api-keys.md "api-keys.md") section in the [Build](build.md "build.md") chapter.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

Responses/Chat Completions API

```
pip install boto3 openai
```

Invoke/Converse API

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

Responses/Chat Completions API

```
OPENAI_API_KEY="<provide your long term key>" OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
```

Invoke/Converse API

```
AWS_BEARER_TOKEN_BEDROCK="<provide your long term key>"
```

**Step 5 - Run your first inference request:** Amazon Bedrock supports [100+ foundation models](models.md "models.md"). Choose a model, and then use the following Python code to run your first inference request. Save the file as `bedrock-first-request.py`

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

Execute the code with Python by using the command:

```
python3 bedrock-first-request.py
```

You should see the output of your inference request.

To learn more about using other APIs and endpoints, please refer to [Build](build.md "build.md").
