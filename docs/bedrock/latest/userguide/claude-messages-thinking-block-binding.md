

# Preserved thinking
<a name="claude-messages-thinking-block-binding"></a>

## Overview
<a name="claude-messages-thinking-block-binding-overview"></a>

On Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5, each thinking block is tied to the model and the conversation that produced it. On Claude Mythos 5.1, thinking blocks are tied to the model only; the conversation prefix isn't checked. The API checks that the system prompt, the tool list, and all messages before the block are unchanged when you replay that block in a later request. This protects the integrity of Claude's reasoning: reasoning produced under one set of instructions cannot be replayed under a different set.

If your harness sends conversation history back exactly as it received it, nothing changes for you. If you edit history between requests — injecting per-turn reminders, summarizing older turns, or rebuilding the system prompt — the API rejects the request by default.

**What is checked on replay**


| **Check** | **Description** | 
| --- | --- | 
| Model | The model reading the block is allowed to read the producer's thinking. A model cannot read another model's thinking unless the two are explicitly compatible. This check applies on any thinking-capable model. A block that fails this check is always dropped as model\_binding\_mismatch, and the request still succeeds. For which models read each other's blocks, see [Model compatibility](#claude-messages-thinking-block-binding-model-compatibility). | 
| Conversation prefix | The top-level system prompt, tools, and all message content before the block are unchanged from the request that produced it. Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5 run this check. By default, a failed check returns a 400 error. Claude Mythos 5.1 doesn't run this check: a block replayed after the prefix changed reaches the model, and prefix\_mismatch\_behavior has no effect. | 
| Organization | The thinking block was produced by the same AWS account, or an account in the same customer group. A block replayed from a different account — or one minted in a Claude app (claude.ai or Claude Code) — is removed before the model runs; the request still succeeds. Applies on Claude Sonnet 5.5 and Claude Haiku 5.5. | 

**Note**  
A thinking block whose signature has been altered or cannot be decrypted always returns a 400, regardless of these checks or the beta value.

## Model compatibility
<a name="claude-messages-thinking-block-binding-model-compatibility"></a>

When you switch models partway through a conversation, the model check decides whether earlier thinking blocks reach the new model. Blocks that the new model can't read are dropped for that request; the API doesn't edit your `messages`, so the blocks are used again if you switch back to a model that can read them.


| **Thinking blocks produced by** | **Read by** | **Dropped as `model_binding_mismatch` on** | 
| --- | --- | --- | 
| Claude Fable 5.1 | Claude Fable 5.1, Claude Mythos 5.1 | Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Opus 5 | 
| Claude Mythos 5.1 | Claude Mythos 5.1, Claude Fable 5.1 | Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, Claude Opus 5 | 
| Claude Opus 5.5 | Claude Opus 5.5, Claude Fable 5.1, Claude Mythos 5.1 | Claude Sonnet 5.5, Claude Haiku 5.5, Claude Opus 5 | 
| Claude Sonnet 5.5 | Claude Sonnet 5.5, Claude Opus 5.5 | Claude Haiku 5.5, Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5 | 
| Claude Haiku 5.5 | Claude Haiku 5.5, Claude Opus 5.5, Claude Sonnet 5.5 | Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5 | 

## The block\_binding request object (beta)
<a name="claude-messages-thinking-block-binding-request-object"></a>

Add `block_binding` to the `thinking` object and include the beta value in `anthropic_beta` to control what happens when a prefix mismatch is detected:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["thinking-binding-controls-2026-08-01"],
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive",
        "block_binding": {
            "prefix_mismatch_behavior": "drop_block"
        }
    },
    "messages": [{ "role": "user", "content": "Your prompt here" }]
}
```

`block_binding` accepts one field, `prefix_mismatch_behavior`, which controls what the API does with a thinking block that fails the conversation prefix check. `mismatch_behavior` is accepted as a deprecated alias for this field. Setting both `prefix_mismatch_behavior` and `mismatch_behavior` in the same request returns a `400 invalid_request_error`: `cannot set both block_binding.prefix_mismatch_behavior and block_binding.mismatch_behavior; send only prefix_mismatch_behavior`. Sent without the beta value, `block_binding` returns `400 thinking.adaptive.block_binding: Extra inputs are not permitted`. Malformed values also return a 400 naming the field. On Claude Sonnet 5.5 and Claude Haiku 5.5, `block_binding` works only with `thinking.type: "adaptive"`.

## Controlling mismatch behavior
<a name="claude-messages-thinking-block-binding-mismatch-behavior"></a>


| **Value** | **Behavior on a failed check** | 
| --- | --- | 
| "error" (default) | Request fails with 400 invalid\_request\_error naming the failed block. Not retryable; returned before any streaming events. | 
| "drop\_block" | Request succeeds with 200. The failing block is removed before the model, along with every later thinking block in the conversation, and each removed block is listed in input\_transformations. Dropping blocks restarts the prompt cache from the first dropped block and can increase output tokens, so treat drop\_block as a temporary fix while you remove the edit that causes the mismatch. | 

Neither value changes the model check, which always drops.

## The input\_transformations response array
<a name="claude-messages-thinking-block-binding-input-transformations"></a>

When the beta value is sent, the response may include a top-level `input_transformations` array describing any blocks that were removed:

```
{
    "type": "message", "role": "assistant", "content": [ ... ],
    "stop_reason": "end_turn",
    "usage": {"input_tokens": 18234, "output_tokens": 911},
    "input_transformations": [
        {"type": "thinking_dropped", "path": "messages.3.content.0", "reason": "prefix_binding_mismatch"}
    ]
}
```

This is a top-level array (a sibling of `usage`), present only with the beta value; `[]` when no blocks were removed and absent otherwise. Each entry contains a `path` identifying the removed block and a `reason`: `model_binding_mismatch` (created by a different model), `prefix_binding_mismatch` (the conversation prefix changed), `organization_binding_mismatch` (created by another account or customer group), or `end_user_binding_mismatch` (created in a Claude app). In streaming responses, the array appears within the message object inside the `message_start` event. Removed blocks do not count toward `input_tokens`.

## Organization-locked thinking
<a name="claude-messages-thinking-block-binding-organization-locked"></a>

On Claude Sonnet 5.5 and Claude Haiku 5.5, each thinking block is also bound to the AWS account (or customer group) that produced it, in addition to the model and conversation-prefix checks. A block replayed from a different account, or one minted in a Claude app (claude.ai or Claude Code), is dropped before the model runs; the request still succeeds and the model does not see that earlier reasoning.

By default the drop is silent. With the `thinking-binding-controls-2026-08-01` beta, each dropped block is listed in the top-level `input_transformations` array:

```
{
    "input_transformations": [
        {"type": "thinking_dropped", "path": "messages.1.content.0", "reason": "organization_binding_mismatch"}
    ]
}
```

Replaying thinking blocks within the same AWS account (or customer group) is unaffected. Without the `thinking-binding-controls-2026-08-01` beta, the response does not include an `input_transformations` field. In the same-account case with the beta, the field is present as an empty array (`[]`).

This binding applies on Claude Sonnet 5.5 and Claude Haiku 5.5; earlier models are unaffected.

## Error responses
<a name="claude-messages-thinking-block-binding-error-responses"></a>

When `prefix_mismatch_behavior` is `"error"`, a prefix mismatch returns:

```
{
    "type": "error",
    "error": {
        "type": "invalid_request_error",
        "message": "messages.3.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to \"drop_block\". The `system` prompt differs from the one this block was created with."
    }
}
```

The last sentence names what changed (for example, the `system` prompt). If the request doesn't include the `thinking-binding-controls-2026-08-01` beta value, the message instead ends with a reminder that `prefix_mismatch_behavior` requires that beta value.

This error is permanent for that request — an automatic retry loop will not clear it. When you catch it, either strip all thinking blocks from history and retry, or retry with `prefix_mismatch_behavior: "drop_block"` and the beta header.

## Guidance for multi-turn and agentic applications
<a name="claude-messages-thinking-block-binding-guidance"></a>
+ Replay assistant turns exactly as they were returned, including thinking blocks with empty `thinking` text, and keep the system prompt and tools stable within a conversation. A serializer that skips empty thinking blocks silently removes the model's earlier reasoning.
+ Changes that invalidate later thinking blocks include editing earlier messages, changing `system` or `tools`, re-rendering an earlier message with different values (such as the current date), and changing earlier tool results or images. For an image or document referenced by URL, the check covers the fetched content, so a URL whose content changes between turns also invalidates later thinking.
+ Changes that are safe include appending messages and changing `output_config.effort`, `max_tokens`, `tool_choice`, `metadata`, or `cache_control`. Server-side compaction doesn't count as an edit.
+ Removing thinking blocks from the start or end of the history, or removing all of them, is valid. Removing a thinking block from the middle invalidates every later thinking block.
+ Avoid one-off content injected into earlier turns (for example, a transient system message or reminder text appended to the last user turn). These change the conversation prefix and invalidate later thinking blocks. Use mid-conversation system messages instead.
+ If your application rewrites conversation history, drop thinking blocks from the rewritten point onward, or set `prefix_mismatch_behavior` to `"drop_block"`.
+ When using the Converse API with a model that supports it, pass the beta value and `thinking.block_binding` through `additionalModelRequestFields`.
+ If you build a library, proxy, or gateway, pass the caller's `anthropic_beta` values and `thinking.block_binding` through unchanged, return `input_transformations` to the caller, and leave `role: "system"` messages where the caller put them.
+ Log `input_transformations` in production. Any `prefix_binding_mismatch` entry means something before that block changed. Ignore entries with types or reasons you don't recognize.