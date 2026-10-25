

# Structured outputs for Anthropic Claude models
<a name="claude-messages-structured-outputs"></a>

Claude models on Amazon Bedrock return schema-compliant JSON on both the `bedrock-runtime` and `bedrock-mantle` endpoints. Responses conform to a JSON schema that you define, which removes the need for custom parsing, retry logic, or post-processing.

For the concepts behind structured outputs, the request workflow, the full list of supported JSON Schema features, and more examples, see [Get validated JSON results from models](structured-output.md).

## Why use structured outputs with Claude
<a name="claude-messages-structured-outputs-why"></a>

Structured outputs provide the following advantages for Claude applications:
+ Every response is valid JSON, which eliminates parsing errors and exceptions.
+ Results are type-safe. Field types are enforced, and required fields are always present.
+ Schema violations do not require retry logic.
+ Responses contain only the fields that your schema defines, which can reduce output tokens and inference cost for high-volume workloads.
+ Structured outputs are production ready, so you can deploy at scale without additional schema-validation code.

## Supported Claude models and endpoints
<a name="claude-messages-structured-outputs-models"></a>

Structured outputs is available across the Claude Sonnet, Opus, Haiku, Fable, and Mythos model families. Support varies by model and endpoint. Some Claude models are available on `bedrock-runtime`, some on `bedrock-mantle`, and many on both. On `bedrock-runtime`, you can use the Converse API, the InvokeModel API, or the Anthropic Messages API. On `bedrock-mantle`, you use the Anthropic Messages API.

For the exact endpoints and AWS Regions a specific model supports, see that model's [model card](model-cards.md).

## Structured outputs mechanisms
<a name="claude-messages-structured-outputs-mechanisms"></a>

Claude models support two mechanisms for structured outputs:
+ **JSON Schema output format**. Constrains the model's response to a JSON schema. Use this mechanism for data extraction, report generation, and API responses.
+ **Strict tool use**. Add `strict: true` to a tool definition to validate tool names and inputs against the schema. Use this mechanism for agentic workflows, function calling, and multi-step automation.

You can use these mechanisms independently or together.

## Structured outputs on the bedrock-runtime endpoint
<a name="claude-messages-structured-outputs-runtime"></a>

With the InvokeModel API, you send the Anthropic-native request body, so the schema goes in `output_config.format` as a JSON object (not a JSON string). The following example extracts customer details into a schema-compliant JSON object.

```
import boto3
import json

REGION = "us-east-1"  # Choose your preferred Region

bedrock_runtime = boto3.client(service_name="bedrock-runtime", region_name=REGION)

# Define the JSON schema for structured output
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "description": "Customer name"},
        "email": {"type": "string", "description": "Customer email address"},
        "plan_interest": {"type": "string", "description": "Product plan of interest"},
        "demo_requested": {"type": "boolean", "description": "Whether a demo was requested"}
    },
    "required": ["name", "email", "plan_interest", "demo_requested"],
    "additionalProperties": False
}

response = bedrock_runtime.invoke_model(
    modelId="global.anthropic.claude-sonnet-5-5",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [
            {"role": "user", "content": (
                "Paulo Santos (paulo@example.com) is interested in our Enterprise plan "
                "and wants to schedule a demo for next Tuesday at 2pm."
            )}
        ],
        "output_config": {"format": {"type": "json_schema", "schema": schema}}
    })
)
body = json.loads(response["body"].read())

# Check the stop reason before parsing
if body["stop_reason"] == "end_turn":
    result_text = next(b["text"] for b in body["content"] if b["type"] == "text")
    print(json.dumps(json.loads(result_text), indent=2))
elif body["stop_reason"] == "max_tokens":
    print("Response truncated: increase max_tokens and retry.")
```

The response conforms to your schema, so no additional validation is required.

For a Converse API example (which uses `outputConfig.textFormat`), see [Get validated JSON results from models](structured-output.md).

## Structured outputs on the bedrock-mantle endpoint
<a name="claude-messages-structured-outputs-mantle"></a>

The `bedrock-mantle` endpoint is designed for agentic applications that use server-side tools, background inference, and stateful conversations. Strict tool use ensures that tool parameters match your input schema. The following example defines a weather tool with `strict: true`.

```
import json
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-sonnet-5",
    max_tokens=512,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather for a specified location",
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city and state, e.g., San Francisco, CA"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "Temperature unit"}
                },
                "required": ["location", "unit"],
                "additionalProperties": False
            }
        }
    ]
)

for block in message.content:
    if block.type == "tool_use":
        print(f"Tool: {block.name}")
        print(f"Input: {json.dumps(block.input, indent=2)}")
```

Setting `strict: true` constrains the tool input to match the schema exactly. The location field is always a string, unit is always celsius or fahrenheit, and the model cannot add fields outside the schema.

## Example: classification at scale with Claude Haiku 5.5
<a name="claude-messages-structured-outputs-classification"></a>

Lightweight Claude models such as Haiku 5.5 are well suited to high-volume, repetitive workloads such as classification and routing. In the following example, enums restrict the output to a fixed set of labels.

```
import boto3
import json

REGION = "us-east-1"  # Choose your preferred Region

bedrock_runtime = boto3.client(service_name="bedrock-runtime", region_name=REGION)

# Classification schema: enums restrict output to a fixed set of labels
schema = {
    "type": "object",
    "properties": {
        "category": {"type": "string", "enum": ["billing", "technical", "account", "sales", "other"], "description": "Primary ticket category"},
        "priority": {"type": "string", "enum": ["low", "medium", "high", "urgent"], "description": "Urgency based on business impact"},
        "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"], "description": "Customer sentiment"},
        "escalate": {"type": "boolean", "description": "Whether a human should review immediately"},
        "reason": {"type": "string", "description": "One-sentence justification for the classification"}
    },
    "required": ["category", "priority", "sentiment", "escalate", "reason"],
    "additionalProperties": False
}

ticket = (
    "Our production API calls have been failing with 500 errors since this morning. "
    "We're losing orders every minute. This is the second outage this month!"
)

response = bedrock_runtime.invoke_model(
    modelId="global.anthropic.claude-haiku-5-5",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "system": "You are a support ticket classifier. Classify the ticket accurately.",
        "messages": [
            {"role": "user", "content": f"Classify this support ticket:\n\n{ticket}"}
        ],
        "output_config": {"format": {"type": "json_schema", "schema": schema}}
    })
)
body = json.loads(response["body"].read())

if body["stop_reason"] == "end_turn":
    result_text = next(b["text"] for b in body["content"] if b["type"] == "text")
    result = json.loads(result_text)
    print(json.dumps(result, indent=2))
    if result["escalate"]:
        print(f"Escalating to on-call: {result['category']} / {result['priority']}")
elif body["stop_reason"] == "max_tokens":
    print("Response truncated: increase max_tokens and retry.")
```

## Common use cases
<a name="claude-messages-structured-outputs-usecases"></a>
+ **Data extraction**. Extract fields from invoices, contracts, emails, and transcripts into JSON that always matches your schema, ready to load into databases or customer relationship management (CRM) systems.
+ **Reliable agent tool calls**. Validate tool arguments against their schemas at generation time, so that multi-step agent workflows run without failures from malformed input.
+ **Classification at scale**. Classify tickets, leads, or content by category, priority, and sentiment for routing, moderation, and evaluation.

## Learn more
<a name="claude-messages-structured-outputs-learn-more"></a>

Structured outputs for Claude models is generally available on both the `bedrock-runtime` and `bedrock-mantle` endpoints. To learn more about supported JSON Schema features, the request workflow, and best practices, see [Get validated JSON results from models](structured-output.md).