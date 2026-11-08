

# Use computer use tools to automate GUI tasks with Amazon Bedrock models
<a name="computer-use"></a>

Computer use lets Anthropic Claude models automate graphical user interface (GUI) tasks. The model returns `tool_use` actions such as taking a screenshot, clicking, typing, and scrolling. Your application executes those actions on a desktop or container and returns the resulting screenshot to Claude on the next turn.

Amazon Bedrock offers computer use through two interfaces:
+ **Client toolsets** – `computer_toolset_20260801` and `browser_toolset_20260801`. Generally available on the newer Claude models (see [Supported models and tool types](#computer-use-model-support)). No beta value is required.
+ **Anthropic-defined computer tools** – `computer_20251124` and `computer_20250124`. In beta on all models that support them, and the only computer use option on older models. Each request requires the matching beta value.

For the underlying tool protocol, the full list of actions, and prompt-engineering guidance, see [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) in the Anthropic documentation. This page covers the Amazon Bedrock-specific usage on top of that protocol.

**Note**  
The `computer_20251124` and `computer_20250124` computer tools are made available to you as a "Beta Service" as defined in the AWS Service Terms. They are subject to your Agreement with AWS, the AWS Service Terms, and the applicable model EULA.  
Computer use, through either interface, poses unique risks distinct from standard API features or chat interfaces. These risks are heightened when computer use interacts with the Internet. To minimize risks, consider taking precautions such as:  
Operate computer use functionality in a dedicated Virtual Machine or container with minimal privileges to prevent direct system attacks or accidents.
To prevent information theft, avoid giving computer use access to sensitive accounts or data.
Limit computer use's internet access to required domains to reduce exposure to malicious content.
To ensure proper oversight, keep a human in the loop for sensitive tasks (such as making decisions that could have meaningful real-world consequences) and for anything requiring affirmative consent (such as accepting cookies, executing financial transactions, or agreeing to terms of service).
Any content that you enable Claude to see or access can potentially override instructions or cause Claude to make mistakes or perform unintended actions. Taking proper precautions, such as isolating Claude from sensitive surfaces, is essential — including to avoid risks related to prompt injection. Before enabling or requesting permissions necessary to enable computer use features in your own products, please inform end users of any relevant risks, and obtain their consent as appropriate.

**Topics**
+ [Use computer use on Amazon Bedrock](#computer-use-bedrock-specifics)
+ [Supported models and tool types](#computer-use-model-support)
+ [Example requests](#computer-use-example-code)

## Use computer use on Amazon Bedrock
<a name="computer-use-bedrock-specifics"></a>

Computer use is supported on both the `bedrock-runtime` and `bedrock-mantle` endpoints. On `bedrock-runtime`, you can use it with the InvokeModel and Converse APIs. You can enable computer use in one of two ways, depending on the model:
+ **Anthropic-defined computer tool** – Include a tool entry whose `type` is a dated computer tool (for example, `computer_20251124`) and the matching `anthropic_beta` value (for example, `computer-use-2025-11-24`). The beta value is required. A request that omits it, or that pairs a tool type with the beta value for a different version, returns a `400 invalid_request_error`.
+ **Client toolset** – Include a tool entry whose `type` is `computer_toolset_20260801` (or `browser_toolset_20260801` for browser automation). No `anthropic_beta` value is required. A toolset entry contains only the `type` field; don't include a `name`. The model calls each tool in the toolset by its own name, for example `screenshot` or `navigate`.

Where you put the beta value depends on the endpoint and API:
+ `bedrock-runtime`, InvokeModel – the `anthropic_beta` field in the request body.
+ `bedrock-runtime`, Converse – the `anthropic_beta` field in `additionalModelRequestFields`, alongside the `tools` array that contains the computer tool.
+ `bedrock-mantle` – the `anthropic-beta` HTTP header, or the `anthropic_beta` field in the request body.

The bash (`bash_20250124`), text editor (`text_editor_20250728`), and memory (`memory_20250818`) tools don't require a beta value. For all Anthropic-defined tools and their fields, see [Computer use](model-parameters-anthropic-claude-messages-tool-use.md#model-parameters-anthropic-claude-messages-computer-use).

## Supported models and tool types
<a name="computer-use-model-support"></a>

The following table shows the computer use tool types that each Claude model accepts on the `bedrock-runtime` endpoint. Submitting a tool type that a model doesn't accept returns a `400 invalid_request_error`. The `computer_20241022` tool type isn't accepted by any model in this table.


| **Model** | **Computer tool type** | **Required beta value** | **Client toolsets (no beta value)** | 
| --- | --- | --- | --- | 
| Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8 | computer\_20251124 | computer-use-2025-11-24 | computer\_toolset\_20260801, browser\_toolset\_20260801 | 
| Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6 | computer\_20251124 | computer-use-2025-11-24 | Not supported | 
| Claude Opus 4.5 | computer\_20251124 or computer\_20250124 | computer-use-2025-11-24 (with computer\_20251124) or computer-use-2025-01-24 (with computer\_20250124) | Not supported | 
| Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.1 | computer\_20250124 | computer-use-2025-01-24 | Not supported | 

To find which endpoints each model is available on, see the model's [Models at a glance](model-cards.md).

## Example requests
<a name="computer-use-example-code"></a>

Each of the following examples asks the model to take a screenshot. The model responds with `stop_reason` set to `tool_use` and a `tool_use` block that describes the action. Your application runs the action and returns the result in a `tool_result` block on the next turn.

**InvokeModel with the computer tool**

The following Python example sends a request through the `bedrock-runtime` endpoint with the `computer_20251124` tool and the required beta value.

```
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.invoke_model(
    modelId="us.anthropic.claude-opus-4-7",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "anthropic_beta": ["computer-use-2025-11-24"],
        "max_tokens": 2048,
        "messages": [
            {"role": "user", "content": "Take a screenshot of the desktop."}
        ],
        "tools": [
            {
                "type": "computer_20251124",
                "name": "computer",
                "display_width_px": 1024,
                "display_height_px": 768,
            }
        ],
    }),
)

result = json.loads(response["body"].read())
print(result["stop_reason"])  # "tool_use" when the model issues a computer action
print(result["content"])      # contains the tool_use block describing the action
```

The model requests the action through the `computer` tool:

```
{
    "type": "tool_use",
    "name": "computer",
    "input": {"action": "screenshot"}
}
```

**InvokeModel with the computer toolset**

The following example uses `computer_toolset_20260801` instead. No beta value is required, and the toolset entry has no `name`.

```
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.invoke_model(
    modelId="us.anthropic.claude-opus-5-5",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2048,
        "messages": [
            {"role": "user", "content": "Take a screenshot of the desktop."}
        ],
        "tools": [{"type": "computer_toolset_20260801"}],
    }),
)

result = json.loads(response["body"].read())
print(result["content"])
```

The model calls the `screenshot` tool from the toolset directly. The `toolset_name` field identifies the toolset that the tool belongs to:

```
{
    "type": "tool_use",
    "name": "screenshot",
    "input": {},
    "toolset_name": "computer"
}
```

**Converse**

With the Converse API, pass the computer tool and the beta value in `additionalModelRequestFields`. The model's action is returned as a `toolUse` content block.

```
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="us.anthropic.claude-sonnet-4-6",
    messages=[
        {"role": "user", "content": [{"text": "Take a screenshot of the desktop."}]}
    ],
    inferenceConfig={"maxTokens": 2048},
    additionalModelRequestFields={
        "anthropic_beta": ["computer-use-2025-11-24"],
        "tools": [
            {
                "type": "computer_20251124",
                "name": "computer",
                "display_width_px": 1024,
                "display_height_px": 768,
            }
        ],
    },
)

print(response["stopReason"])  # "tool_use"
for block in response["output"]["message"]["content"]:
    if "toolUse" in block:
        print(block["toolUse"]["name"], block["toolUse"]["input"])
```

To use a client toolset with Converse, pass `"tools": [{"type": "computer_toolset_20260801"}]` in `additionalModelRequestFields` and omit `anthropic_beta`.

**bedrock-mantle**

On the `bedrock-mantle` endpoint (`https://bedrock-mantle.{{region}}.api.aws/anthropic/v1/messages`), send the beta value in the `anthropic-beta` header:

```
POST /anthropic/v1/messages
anthropic-version: 2023-06-01
anthropic-beta: computer-use-2025-11-24
content-type: application/json

{
    "model": "anthropic.claude-opus-5-5",
    "max_tokens": 2048,
    "messages": [
        {"role": "user", "content": "Take a screenshot of the desktop."}
    ],
    "tools": [
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768
        }
    ]
}
```

You can instead include `"anthropic_beta": ["computer-use-2025-11-24"]` in the request body. For authentication and the full `bedrock-mantle` Messages API request shape, see [Inference using Anthropic Messages API](inference-messages-api.md).