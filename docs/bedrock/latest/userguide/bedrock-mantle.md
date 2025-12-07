# Generate responses using OpenAI APIs

Amazon Bedrock provides OpenAI compatible API endpoints for model inference, powered by Mantle, a
distributed inference engine for large-scale machine learning model serving. These endpoints
allow you to use familiar OpenAI SDKs and tools with Amazon Bedrock models, enabling you to migrate
existing applications with minimal code changes—simply update your base URL and API key.

Key benefits include:

- **Asynchronous inference** – Support for
  long-running inference workloads through the Responses API
- **Stateful conversation management** –
  Automatically rebuild context without manually passing conversation history with
  each request
- **Simplified tool use** – Streamlined
  integration for agentic workflows
- **Flexible response modes** – Support for both
  streaming and non-streaming responses
- **Easy migration** – Compatible with existing
  OpenAI SDK codebases

## Supported Regions and Endpoints

Amazon Bedrock is available in the following AWS Regions:

| Region Name               | Region         | Endpoint                              |
| ------------------------- | -------------- | ------------------------------------- |
| US East (Ohio)            | us-east-2      | bedrock-mantle.us-east-2.api.aws      |
| US East (N. Virginia)     | us-east-1      | bedrock-mantle.us-east-1.api.aws      |
| US West (Oregon)          | us-west-2      | bedrock-mantle.us-west-2.api.aws      |
| Asia Pacific (Jakarta)    | ap-southeast-3 | bedrock-mantle.ap-southeast-3.api.aws |
| Asia Pacific (Mumbai)     | ap-south-1     | bedrock-mantle.ap-south-1.api.aws     |
| Asia Pacific (Tokyo)      | ap-northeast-1 | bedrock-mantle.ap-northeast-1.api.aws |
| Europe (Frankfurt)        | eu-central-1   | bedrock-mantle.eu-central-1.api.aws   |
| Europe (Ireland)          | eu-west-1      | bedrock-mantle.eu-west-1.api.aws      |
| Europe (London)           | eu-west-2      | bedrock-mantle.eu-west-2.api.aws      |
| Europe (Milan)            | eu-south-1     | bedrock-mantle.eu-south-1.api.aws     |
| Europe (Stockholm)        | eu-north-1     | bedrock-mantle.eu-north-1.api.aws     |
| South America (São Paulo) | sa-east-1      | bedrock-mantle.sa-east-1.api.aws      |

## Prerequisites

Before using OpenAI APIs, ensure you have the following:

- **Authentication** – You can authenticate
  using:
  - Amazon Bedrock API key (required for OpenAI SDK)
  - AWS credentials (supported for HTTP requests)

- **OpenAI SDK** (optional) – Install the
  OpenAI Python SDK if using SDK-based requests.
- **Environment variables** – Set the
  following environment variables:
  - `OPENAI_API_KEY` – Set to your Amazon Bedrock API key
  - `OPENAI_BASE_URL` – Set to the Amazon Bedrock endpoint for your
    region (for example, `https://bedrock-mantle.us-east-1.api.aws/v1`)

## Models API

The Models API allows you to discover available models in Amazon Bedrock powered by Mantle. Use this API to
retrieve a list of models you can use with the Responses API and Chat Completions API.
For complete API details, see the [OpenAI Models
documentation](https://platform.openai.com/docs/api-reference/models "https://platform.openai.com/docs/api-reference/models").

### List available models

To list available models, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)

```
# List all available models using the OpenAI SDK
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

from openai import OpenAI

client = OpenAI()

models = client.models.list()

for model in models.data:
    print(model.id)

```

HTTP request
Make a GET request to `/v1/models`:

```
# List all available models
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

curl -X GET $OPENAI_BASE_URL/models \
   -H "Authorization: Bearer $OPENAI_API_KEY"

```

## Responses API

The Responses API provides stateful conversation management with support for
streaming, background processing, and multi-turn interactions. For complete API details,
see the [OpenAI
Responses documentation](https://platform.openai.com/docs/api-reference/responses "https://platform.openai.com/docs/api-reference/responses").

### Basic request

To create a response, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)

```
# Create a basic response using the OpenAI SDK
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input=[
        {"role": "user", "content": "Hello! How can you help me today?"}
    ]
)

print(response)

```

HTTP request
Make a POST request to `/v1/responses`:

```
# Create a basic response
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

curl -X POST $OPENAI_BASE_URL/responses \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $OPENAI_API_KEY" \
   -d '{
    "model": "openai.gpt-oss-120b",
    "input": [
        {"role": "user", "content": "Hello! How can you help me today?"}
    ]
}'

```

### Stream responses

To receive response events incrementally, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)

```
# Stream response events incrementally using the OpenAI SDK
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="openai.gpt-oss-120b",
    input=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for event in stream:
    print(event)

```

HTTP request
Make a POST request to `/v1/responses` with `stream`
set to `true`:

```
# Stream response events incrementally
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

curl -X POST $OPENAI_BASE_URL/responses \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $OPENAI_API_KEY" \
   -d '{
    "model": "openai.gpt-oss-120b",
    "input": [
        {"role": "user", "content": "Tell me a story"}
    ],
    "stream": true
}'

```

## Chat Completions API

The Chat Completions API generates conversational responses. For complete API details,
see the [OpenAI
Chat Completions documentation](https://platform.openai.com/docs/api-reference/chat/create "https://platform.openai.com/docs/api-reference/chat/create").

### Create a chat completion

To create a chat completion, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)
Configure the OpenAI client using environment variables:

```
# Create a chat completion using the OpenAI SDK
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message)

```

HTTP request
Make a POST request to `/v1/chat/completions`:

```
# Create a chat completion
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

curl -X POST $OPENAI_BASE_URL/chat/completions \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $OPENAI_API_KEY" \
   -d '{
    "model": "openai.gpt-oss-120b",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
}'

```

### Enable streaming

To receive responses incrementally, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)

```
# Stream chat completion responses incrementally using the OpenAI SDK
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

```

HTTP request
Make a POST request to `/v1/chat/completions` with `stream` set to `true`:

```
# Stream chat completion responses incrementally
# Requires OPENAI_API_KEY and OPENAI_BASE_URL environment variables

curl -X POST $OPENAI_BASE_URL/chat/completions \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $OPENAI_API_KEY" \
   -d '{
    "model": "openai.gpt-oss-120b",
    "messages": [
        {"role": "user", "content": "Tell me a story"}
    ],
    "stream": true
}'

```
