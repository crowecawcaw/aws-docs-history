

# Adaptive thinking
<a name="claude-messages-adaptive-thinking"></a>

Adaptive thinking lets Claude dynamically decide when and how much to think based on the complexity of each request, instead of requiring a fixed thinking token budget. Adaptive thinking reliably drives better performance than extended thinking with a fixed `budget_tokens`. No beta header is required.

The following models support adaptive thinking. Each model's card describes its thinking defaults, whether thinking can be turned off, and its supported effort levels under **Reasoning**. For a side-by-side comparison, see [Thinking configuration by model](#claude-messages-adaptive-thinking-config-by-model).


| Model | Model ID | 
| --- | --- | 
| [Claude Haiku 5.5](model-card-anthropic-claude-haiku-5-5.md) | `anthropic.claude-haiku-5-5` | 
| [Claude Sonnet 5.5](model-card-anthropic-claude-sonnet-5-5.md) | `anthropic.claude-sonnet-5-5` | 
| [Claude Opus 5.5](model-card-anthropic-claude-opus-5-5.md) | `anthropic.claude-opus-5-5` | 
| [Claude Fable 5.1](model-card-anthropic-claude-fable-5-1.md) | `anthropic.claude-fable-5-1` | 
| [Claude Mythos 5.1](model-card-anthropic-claude-mythos-5-1.md) | `anthropic.claude-mythos-5-1` | 
| [Claude Opus 5](model-card-anthropic-claude-opus-5.md) | `anthropic.claude-opus-5` | 
| [Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md) | `anthropic.claude-sonnet-5` | 
| [Claude Mythos 5](model-card-anthropic-claude-mythos-5.md) | `anthropic.claude-mythos-5` | 
| [Claude Fable 5](model-card-anthropic-claude-fable-5.md) | `anthropic.claude-fable-5` | 
| [Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md) | `anthropic.claude-opus-4-8` | 
| [Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md) | `anthropic.claude-opus-4-7` | 
| [Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md) | `anthropic.claude-opus-4-6-v1` | 
| [Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md) | `anthropic.claude-sonnet-4-6` | 

**Important**  
**Adaptive thinking is on by default on Claude 5 and later models.** A request that omits the `thinking` field runs with adaptive thinking. On Claude Opus 4.8 and earlier models, the same request runs without thinking, so an application migrated from an earlier model without changes will produce thinking output — and be billed for those thinking tokens as output tokens — even though the request body did not change.  
Omitting the `thinking` field doesn't turn thinking off, and neither does a zero or reduced `budget_tokens` (`"enabled"` returns a 400 error on these models). To turn thinking off where the model allows it, send `"thinking": {"type": "disabled"}`, or `"between_tools"` on Claude Sonnet 5.5. Some models can't turn thinking off; see [Thinking configuration by model](#claude-messages-adaptive-thinking-config-by-model).  
Because `max_tokens` is a hard limit on total output — thinking plus response text — revisit `max_tokens` for workloads that previously ran without thinking. If you were using disabled thinking on Claude Sonnet 4.6, consider adaptive thinking with a lower `output_config.effort` level on Claude Sonnet 5 instead of disabling it.

## Thinking configuration by model
<a name="claude-messages-adaptive-thinking-config-by-model"></a>

The following table shows how each model handles each `thinking.type` value. A 400 error means the request is rejected with a `ValidationException`.


| Model | No `thinking` field | `"adaptive"` | `"enabled"` with `budget_tokens` | `"between_tools"` | `"disabled"` | 
| --- | --- | --- | --- | --- | --- | 
| Claude Opus 5.5 | Adaptive | Adaptive | 400 error | 400 error | 400 error | 
| Claude Sonnet 5.5 | Adaptive | Adaptive | 400 error | Up-front thinking off at high effort or below | 400 error | 
| Claude Haiku 5.5 | Adaptive | Adaptive | 400 error | 400 error | Thinking off at high effort or below | 
| Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5 | Adaptive | Adaptive | 400 error | 400 error | 400 error | 
| Claude Opus 5 | Adaptive | Adaptive | 400 error | 400 error | Thinking off at high effort or below | 
| Claude Sonnet 5 | Adaptive | Adaptive | 400 error | 400 error | Thinking off | 
| Claude Opus 4.8, Claude Opus 4.7 | Thinking off | Adaptive | 400 error | 400 error | Thinking off | 
| Claude Opus 4.6, Claude Sonnet 4.6 | Thinking off | Adaptive | Extended thinking (deprecated) | 400 error | Thinking off | 

"At `high` effort or below" means that combining that thinking type with `xhigh` or `max` effort returns a 400 error: `output_config.effort 'xhigh' is not supported when thinking is disabled on this model`. On those models, use adaptive thinking with a lower effort level instead of turning thinking off.

`thinking.type: "enabled"` and `budget_tokens` are deprecated on Claude Opus 4.6 and Claude Sonnet 4.6 and will be removed in a future model release. Older models (Claude Sonnet 4.5, Claude Opus 4.5, and earlier) don't support adaptive thinking and require `thinking.type: "enabled"` with `budget_tokens`.

## How adaptive thinking works
<a name="claude-messages-adaptive-thinking-how-it-works"></a>

In adaptive mode, Claude evaluates the complexity of each request and decides whether and how much to think. A simple question might get a direct answer with no thinking block, while a multi-step problem triggers deeper reasoning. The same conversation can contain turns with and without thinking, so don't build application logic that assumes every assistant turn starts with a thinking block. Higher effort levels make thinking more likely and deeper, but no effort level guarantees a thinking block on every request. In a tool-use loop, follow-up requests that only process tool results can skip thinking at any effort level.

Adaptive thinking also automatically enables [Interleaved thinking (beta)](claude-messages-extended-thinking.md#claude-messages-extended-thinking-tool-use-interleaved). This means Claude can think between tool calls, making it especially effective for agentic workflows.

Set `thinking.type` to `"adaptive"` in your API request:

------
#### [ CLI ]

```
aws bedrock-runtime invoke-model \
--model-id "global.anthropic.claude-opus-5-5" \
--body '{
"anthropic_version": "bedrock-2023-05-31",
"max_tokens": 16000,
"thinking": {
"type": "adaptive",
"display": "summarized"
},
"messages": [
{
"role": "user",
"content": "Three players A, B, C play a game. Each has a jar with 100 balls numbered 1-100. Simultaneously, each draws one ball. A beats B if As number > Bs number (mod 100, treating 100 as 0 for comparison). Similarly for B vs C and C vs A. The overall winner is determined by majority of pairwise wins (ties broken randomly). Is there a mixed strategy Nash equilibrium where each player draws uniformly? If not, characterize the equilibrium."
}
]
}' \
--cli-binary-format raw-in-base64-out \
output.json && cat output.json | jq '.content[] | {type, thinking: .thinking[0:200], text}'
```

------
#### [ Python ]

```
import boto3
import json

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

response = bedrock_runtime.invoke_model(
    modelId="global.anthropic.claude-opus-5-5",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 16000,
        "thinking": {
            "type": "adaptive",
            "display": "summarized"
        },
        "messages": [{
            "role": "user",
            "content": "Explain why the sum of two even numbers is always even."
        }]
    })
)

response_body = json.loads(response["body"].read())

for block in response_body["content"]:
    if block["type"] == "thinking":
        print(f"\nThinking: {block['thinking']}")
    elif block["type"] == "text":
        print(f"\nResponse: {block['text']}")
```

------
#### [ TypeScript ]

```
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

async function main() {
    const client = new BedrockRuntimeClient({});

    const command = new InvokeModelCommand({
        modelId: "global.anthropic.claude-opus-5-5",
        body: JSON.stringify({
            anthropic_version: "bedrock-2023-05-31",
            max_tokens: 16000,
            thinking: {
                type: "adaptive",
                display: "summarized"
            },
            messages: [{
                role: "user",
                content: "Explain why the sum of two even numbers is always even."
            }]
        })
    });

    const response = await client.send(command);
    const responseBody = JSON.parse(new TextDecoder().decode(response.body));

    for (const block of responseBody.content) {
        if (block.type === "thinking") {
            console.log(`\nThinking: ${block.thinking}`);
        } else if (block.type === "text") {
            console.log(`\nResponse: ${block.text}`);
        }
    }
}

main().catch(console.error);
```

------

On Claude 5 and later models, `display` defaults to `omitted`, so these examples set `"display": "summarized"` to return readable thinking text. For more information, see [Controlling thinking visibility with the display parameter](#claude-messages-adaptive-thinking-display).

## Adaptive thinking with the effort parameter
<a name="claude-messages-adaptive-thinking-effort"></a>

You can combine adaptive thinking with the effort parameter to guide how much thinking Claude does. The effort level acts as soft guidance for Claude's thinking allocation:


| Effort level | Thinking behavior | 
| --- | --- | 
| max | Claude thinks the most readily and at the greatest depth, with no constraint on thinking length. Supported on Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. Requests using max on unsupported models return an error. | 
| xhigh | Claude thinks more readily and at greater depth than at high, suited to long-running agentic work. Supported on Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, Claude Opus 4.8, and Claude Opus 4.7. | 
| high (default on most models) | Claude thinks on most requests that benefit from it. Provides deep reasoning on complex tasks. | 
| medium (default on Claude Opus 5.5 and Claude Haiku 5.5) | Claude uses moderate thinking. May skip thinking for simple queries. | 
| low | Claude minimizes thinking. Skips thinking for simple tasks where speed matters most. | 

Setting `effort` to the model's default produces the same behavior as omitting it. Because Claude Opus 5.5 defaults to `medium`, a request that omits `effort` runs one level lower on Claude Opus 5.5 than on Claude Opus 5.

**Important**  
The `effort` parameter must be placed inside a separate `output_config` object in your request body — not inside the `thinking` object. Placing `effort` inside `thinking` returns a 400 error: `thinking.adaptive.effort: Extra inputs are not permitted`.

The following example shows how to set the effort level when using the InvokeModel API:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive"
    },
    "output_config": {
        "effort": "high"
    },
    "messages": [{
        "role": "user",
        "content": "Your prompt here"
    }]
}
```

## Turning off up-front thinking on Claude Sonnet 5.5
<a name="claude-messages-adaptive-thinking-between-tools"></a>

Claude Sonnet 5.5 rejects `"thinking": {"type": "disabled"}` with a 400 error. To turn off the thinking that Claude Sonnet 5.5 does before it responds, set `thinking.type` to `"between_tools"`. This is the lowest thinking setting on Claude Sonnet 5.5. The model doesn't think before responding, but it still returns short progress updates between tool calls.

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "thinking": {"type": "between_tools"},
    "output_config": {"effort": "medium"},
    "messages": [{"role": "user", "content": "Your prompt here"}]
}
```
+ `between_tools` works at `low`, `medium`, and `high` effort. At `xhigh` or `max`, the request returns a 400 error.
+ `between_tools` accepts no other fields. Setting `display` alongside it returns a 400 error.
+ Other models return `"thinking.type.between_tools" is not supported for this model`.

## Controlling thinking visibility with the display parameter
<a name="claude-messages-adaptive-thinking-display"></a>

When you use adaptive thinking, the `display` field controls whether Claude returns the text of its reasoning. Set it inside the `thinking` object, alongside `"type": "adaptive"`:


| Display value | Behavior | 
| --- | --- | 
| omitted (default on Claude 5 and later models) | The response still contains a thinking block, but its thinking text is empty. The block carries a signature, so you can pass it back unchanged in multi-turn conversations. | 
| summarized | The thinking block contains a summary of Claude's reasoning as text. This is the default on Claude Opus 4.6, Claude Sonnet 4.6, and earlier models. | 
| updates (beta) | Thinking blocks are returned with empty thinking text, as with omitted, and the short progress updates that some models write between tool calls are returned as readable text. Requires the thinking-display-updates-2026-08-18 value in anthropic\_beta. | 

`summarized` and `omitted` are generally available and don't require a beta header. Without the beta value, `updates` or any other value returns a `400` error: `thinking.adaptive.display: Input should be 'summarized', 'omitted'`. `display` isn't valid with `thinking.type: "disabled"` or `"between_tools"`. You're billed for the full thinking tokens regardless of the `display` value.

**Note**  
Setting `summarized` doesn't guarantee that reasoning text is returned. Some models accept the parameter but return no thinking text, and some don't return a thinking block at all. Read the `thinking` field of the response rather than assuming that a request accepted with `summarized` produced reasoning text.

The following example requests summarized reasoning when using the InvokeModel API:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive",
        "display": "summarized"
    },
    "messages": [{
        "role": "user",
        "content": "Your prompt here"
    }]
}
```

## Thinking token usage
<a name="claude-messages-adaptive-thinking-usage"></a>

Thinking tokens are billed as output tokens. To see how many output tokens were spent on thinking, read `usage.output_tokens_details.thinking_tokens` in the response. This value counts the full reasoning that the model generated, not the summarized text returned in the response, and is always less than or equal to `output_tokens`. It is `0` when the model skipped thinking. When streaming, the breakdown appears only in the final `message_delta` event.

```
"usage": {
    "input_tokens": 52,
    "output_tokens": 498,
    "output_tokens_details": {
        "thinking_tokens": 312
    }
}
```

`output_tokens` remains the total used for billing. Because thinking counts toward `max_tokens`, set `max_tokens` high enough for both the reasoning and the answer. If responses stop with `stop_reason: "max_tokens"`, raise `max_tokens` or lower the effort level.

## Using adaptive thinking with the Converse API
<a name="claude-messages-adaptive-thinking-converse"></a>

When using the [Converse API](conversation-inference.md), pass the `thinking` and `effort` parameters inside `additionalModelRequestFields`. The following example shows adaptive thinking with the default effort level:

```
import boto3, json

bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

response = bedrock_runtime.converse(
    modelId="global.anthropic.claude-opus-5-5",
    messages=[{
        "role": "user",
        "content": [{"text": "Explain why the sum of two even numbers is always even."}]
    }],
    additionalModelRequestFields={
        "thinking": {
            "type": "adaptive"
        }
    }
)

print(json.dumps(response["output"], indent=2, default=str))
```

To specify an effort level, add the `effort` field inside a separate `output_config` object in `additionalModelRequestFields`:

```
response = bedrock_runtime.converse(
    modelId="global.anthropic.claude-opus-5-5",
    messages=[{
        "role": "user",
        "content": [{"text": "What is 2 + 2?"}]
    }],
    additionalModelRequestFields={
        "thinking": {
            "type": "adaptive"
        },
        "output_config": {
            "effort": "low"
        }
    }
)
```

## Setting effort per turn (beta)
<a name="claude-messages-adaptive-thinking-per-turn-effort"></a>

This feature is a Beta Service as defined in the AWS Service Terms. On Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5, Claude Fable 5.1, and Claude Mythos 5.1, you can change the effort level partway through a conversation instead of setting it once for the whole request. Insert a system message that carries an `output_config.effort` value at any point in the `messages` array. The new effort level applies to the turns that follow it. The request returns 200 with no change to the response shape.

To use per-turn effort, include one of the following `anthropic_beta` values: `mid-conversation-output-config-2026-07-01`, `mid-conversation-effort-2026-08-01`, `per-turn-control-2026-07-01`, or `per-message-effort-2026-07-01`.

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["mid-conversation-effort-2026-08-01"],
    "max_tokens": 16000,
    "output_config": {"effort": "high"},
    "messages": [
        {"role": "user", "content": "First question"},
        {"role": "assistant", "content": "First answer"},
        {"role": "system", "content": [], "output_config": {"effort": "low"}},
        {"role": "user", "content": "A simpler follow-up question"}
    ]
}
```

**Note**  
Without one of the listed beta values — or on a model that does not support per-turn effort — a request that includes `output_config` on a system message returns `400 messages.N.output_config: Extra inputs are not permitted`. A per-turn `task_budget` is not supported and also returns a 400.  
Claude Opus 5, Claude Sonnet 5, and Claude Opus 4.8 don't support per-turn effort and return the same error even with a beta value. On Claude Sonnet 5.5 with `thinking.type: "between_tools"` and on Claude Haiku 5.5 with `thinking.type: "disabled"`, effort can't change mid-conversation; use adaptive thinking to vary effort per turn.

## Prompt caching
<a name="claude-messages-adaptive-thinking-prompt-caching"></a>

Consecutive requests that keep the same thinking configuration preserve prompt cache breakpoints. Switching between thinking modes (for example, from `adaptive` to `disabled`) invalidates the cache, including breakpoints on the system prompt and tool definitions, so the next request writes the cache again. Pick a thinking mode for each conversation and keep it.

To change effort for later turns of a conversation, use [Setting effort per turn (beta)](#claude-messages-adaptive-thinking-per-turn-effort) on models that support it.

## Tuning thinking behavior
<a name="claude-messages-adaptive-thinking-tuning"></a>

If Claude is thinking more or less often than you'd like, lower or raise the effort level first. You can also add guidance to your system prompt:

```
Extended thinking adds latency and should only be used when it
will meaningfully improve answer quality — typically for problems
that require multi-step reasoning. When in doubt, respond directly.
```

**Note**  
On Claude Sonnet 5.5 and Claude Haiku 5.5, prompt guidance to think less doesn't reliably reduce thinking. Lower the effort level instead.

**Warning**  
Steering Claude to think less often may reduce quality on tasks that benefit from reasoning. Measure the impact on your specific workloads before deploying prompt-based tuning to production. Consider testing with lower effort levels first.

## Connector text summarization (beta)
<a name="claude-messages-adaptive-thinking-connector-summarization"></a>

On Claude Fable 5, text that the model emits between tool calls (sometimes called "connector text" — for example, "Let me check that file next...") is summarized server-side and returned as a thinking block rather than a plain text content block. The thinking block uses the same shape as any other thinking block (empty text with a signature under the default `omitted` display, described in [Controlling thinking visibility with the display parameter](#claude-messages-adaptive-thinking-display)).

**Customer impact:**
+ **Response shape:** Tool-use responses from Claude Fable 5 may contain additional thinking blocks where previous models emitted plain text between `tool_use` blocks. There is no new content block type. Final assistant answers (after all tool use is complete) are unaffected and remain plain text.
+ **Multi-turn handling:** Pass these thinking blocks back unchanged in multi-turn conversations — the same handling as protected thinking (signature validated on passback; silently stripped if sent to a different model).
+ **Scope:** Connector summarization applies only after a `tool_result` exists in the conversation. Narration before the first tool call in a fresh conversation remains plain text. Short text segments may pass through as plain text without summarization.

This feature is enabled server-side for Claude Fable 5. There is no customer opt-in or opt-out.