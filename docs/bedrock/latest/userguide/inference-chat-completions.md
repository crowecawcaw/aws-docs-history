# Invoke a model with the OpenAI Chat Completions API

You can run model inference using the [OpenAI Create chat completion API](https://platform.openai.com/docs/api-reference/chat/create "https://platform.openai.com/docs/api-reference/chat/create") with Amazon Bedrock models.

You can call the Create chat completion API in the following ways:

- Make an HTTP request with an Amazon Bedrock Runtime endpoint.
- Use an OpenAI SDK request with an Amazon Bedrock Runtime endpoint.
  Select a topic to learn more:

###### Topics

- [Supported models and Regions for the OpenAI Chat Completions API](#inference-chat-completions-supported "#inference-chat-completions-supported")
- [Prerequisites to use the Chat Completions API](#inference-chat-completions-prereq "#inference-chat-completions-prereq")
- [Create a chat completion](#inference-chat-completions-create "#inference-chat-completions-create")
- [Include a guardrail in a chat completion](#inference-chat-completions-guardrails "#inference-chat-completions-guardrails")

## Supported models and Regions for the OpenAI Chat Completions API

You can use the Create chat completion API with all OpenAI models supported in Amazon Bedrock and in the AWS Regions that support these models. For more information about supported models and regions, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

## Prerequisites to use the Chat Completions API

To see prerequisites for using the Chat Completions API, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK

- **Authentication** – The OpenAI SDK only supports authentication with an Amazon Bedrock API key. Generate an Amazon Bedrock API key to authenticate your request. To learn about Amazon Bedrock API keys and how to generate them, see [Generate Amazon Bedrock API keys to easily authenticate to the Amazon Bedrock API](api-keys.md "api-keys.md").
- **Endpoint** – Find the endpoint that corresponds to the AWS Region to use in [Amazon Bedrock Runtime endpoints and quotas](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt"). If you use an AWS SDK, you might only need to specify the region code and not the whole endpoint when you set up the client.
- **Install an OpenAI SDK** – For more information, see [Libraries](https://platform.openai.com/docs/libraries "https://platform.openai.com/docs/libraries") in the OpenAI documentation.

HTTP request

- **Authentication** – You can authenticate with either your AWS credentials or with an Amazon Bedrock API key.

Set up your AWS credentials or generate an Amazon Bedrock API key to authenticate your request.

    + To learn about setting up your AWS credentials, see [Programmatic access with AWS security credentials](../../../IAM/latest/UserGuide/security-creds-programmatic-access.md "../../../IAM/latest/UserGuide/security-creds-programmatic-access.md").
    + To learn about Amazon Bedrock API keys and how to generate them, see [Generate Amazon Bedrock API keys to easily authenticate to the Amazon Bedrock API](api-keys.md "api-keys.md").

- **Endpoint** – Find the endpoint that corresponds to the AWS Region to use in [Amazon Bedrock Runtime endpoints and quotas](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt"). If you use an AWS SDK, you might only need to specify the region code and not the whole endpoint when you set up the client.

## Create a chat completion

Refer to the following resources in the OpenAI documentation for details about the Create chat completion API:

- [Request body parameters](https://platform.openai.com/docs/api-reference/chat/create "https://platform.openai.com/docs/api-reference/chat/create")
- [Response body parameters](https://platform.openai.com/docs/api-reference/chat/object "https://platform.openai.com/docs/api-reference/chat/object")

###### Note

Amazon Bedrock currently doesn't support the other OpenAI Chat completion API operations.

To learn how to use the OpenAI Create chat completion API, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)
To create a chat completion with the OpenAI SDK, do the following:

1. Import the OpenAI SDK and set up the client with the following fields:
   - `base_url` – Prefix the Amazon Bedrock Runtime endpoint to `/openai/v1`, as in the following format:

   ```
   https://`${bedrock-runtime-endpoint}`/openai/v1
   ```

   - `api_key` – Specify an Amazon Bedrock API key.
   - `default_headers` – If you need to include any headers, you can include them as key-value pairs in this object. You can alternatively specify headers in the `extra_headers` when making a specific API call.

2. Use the `chat.completions.create()` method with the client and minimally specify the `model` and `messages` in the request body.

The following example calls the Create chat completion API in `us-west-2`. Replace `$AWS_BEARER_TOKEN_BEDROCK` with your actual API key.

```
from openai import OpenAI

client = OpenAI(
    base_url="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
    api_key="$AWS_BEARER_TOKEN_BEDROCK" # Replace with actual API key
)

completion = client.chat.completions.create(
    model="openai.gpt-oss-20b-1:0",
    messages=[
        {
            "role": "developer",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
)

print(completion.choices[0].message)
```

HTTP request
To create a chat completion with a direct HTTTP request, do the following:

1. Specify the URL by prefixing the Amazon Bedrock Runtime endpoint to `/openai/v1/chat/completions`, as in the following format:

```
`https://${bedrock-runtime-endpoint}`/openai/v1/chat/completions
```

2. Specify your AWS credentials or an Amazon Bedrock API key in the `Authorization` header.
3. In the request body, specify at least the `model` and `messages` in the request body.

The following example uses curl to call the Create chat completion API in `us-west-2`. Replace `$AWS_BEARER_TOKEN_BEDROCK` with your actual API key:

```
curl -X POST https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1/chat/completions \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer $AWS_BEARER_TOKEN_BEDROCK" \
   -d '{
    "model": "openai.gpt-oss-20b-1:0",
    "messages": [
        {
            "role": "developer",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}'
```

## Include a guardrail in a chat completion

To include safeguards in model input and responses, apply a [guardrail](guardrails.md "guardrails.md") when running model invocation by including the following [extra parameters](https://github.com/openai/openai-python#undocumented-request-params "https://github.com/openai/openai-python#undocumented-request-params") as fields in the request body:

- `extra_headers` – Maps to an object containing the following fields, which specify extra headers in the request:
  - `X-Amzn-Bedrock-GuardrailIdentifier` (required) – The ID of the guardrail.
  - `X-Amzn-Bedrock-GuardrailVersion` (required) – The version of the guardrail.
  - `X-Amzn-Bedrock-Trace` (optional) – Whether or not to enable the guardrail trace.

- `extra_body` – Maps to an object. In that object, you can include the `amazon-bedrock-guardrailConfig` field, which maps to an object containing the following fields:
  - `tagSuffix` (optional) – Include this field for [input tagging](guardrails-tagging.md "guardrails-tagging.md").

For more information about these parameters in Amazon Bedrock Guardrails, see [Test your guardrail](guardrails-test.md "guardrails-test.md").

To see examples of using guardrails with OpenAI chat completions, choose the tab for your preferred method, and then follow the steps:

OpenAI SDK (Python)

```
import openai
from openai import OpenAIError

# Endpoint for Amazon Bedrock Runtime
bedrock_endpoint = "https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1"

# Model ID
model_id = "openai.gpt-oss-20b-1:0"

# Replace with actual values
bedrock_api_key = "$AWS_BEARER_TOKEN_BEDROCK"
guardrail_id = "GR12345"
guardrail_version = "DRAFT"

client = openai.OpenAI(
    api_key=bedrock_api_key,
    base_url=bedrock_endpoint,
)

try:
    response = client.chat.completions.create(
        model=model_id,
        # Specify guardrail information in the header
        extra_headers={
            "X-Amzn-Bedrock-GuardrailIdentifier": guardrail_id,
            "X-Amzn-Bedrock-GuardrailVersion": guardrail_version,
            "X-Amzn-Bedrock-Trace": "ENABLED",
        },
        # Additional guardrail information can be specified in the body
        extra_body={
            "amazon-bedrock-guardrailConfig": {
                "tagSuffix": "xyz"  # Used for input tagging
            }
        },
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "assistant",
                "content": "Hello! How can I help you today?"
            },
            {
                "role": "user",
                "content": "What is the weather like today?"
            }
        ]
    )

    request_id = response._request_id
    print(f"Request ID: {request_id}")
    print(response)

except OpenAIError as e:
    print(f"An error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        request_id = e.response.headers.get("x-request-id")
        print(f"Request ID: {request_id}")
```

OpenAI SDK (Java)

```
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponseFor;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

// Endpoint for Amazon Bedrock Runtime
String bedrockEndpoint = "http://bedrock-runtime.us-west-2.amazonaws.com/openai/v1"

// Model ID
String modelId = "openai.gpt-oss-20b-1:0"

// Replace with actual values
String bedrockApiKey = "$AWS_BEARER_TOKEN_BEDROCK"
String guardrailId = "GR12345"
String guardrailVersion = "DRAFT"

OpenAIClient client = OpenAIOkHttpClient.builder()
        .apiKey(bedrockApiKey)
        .baseUrl(bedrockEndpoint)
        .build()

ChatCompletionCreateParams request = ChatCompletionCreateParams.builder()
        .addUserMessage("What is the temperature in Seattle?")
        .model(modelId)
        // Specify additional headers for the guardrail
        .putAdditionalHeader("X-Amzn-Bedrock-GuardrailIdentifier", guardrailId)
        .putAdditionalHeader("X-Amzn-Bedrock-GuardrailVersion", guardrailVersion)
        // Specify additional body parameters for the guardrail
        .putAdditionalBodyProperty(
                "amazon-bedrock-guardrailConfig",
                JsonValue.from(Map.of("tagSuffix", JsonValue.of("xyz"))) // Allows input tagging
        )
        .build();

HttpResponseFor<ChatCompletion> rawChatCompletionResponse =
        client.chat().completions().withRawResponse().create(request);

final ChatCompletion chatCompletion = rawChatCompletionResponse.parse();

System.out.println(chatCompletion);
```
