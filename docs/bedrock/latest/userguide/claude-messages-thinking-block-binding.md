# Preserved thinking

## Overview

On Claude Fable 5.1, each thinking block is tied to the conversation that produced it. The API checks that the system prompt, the tool list, and all messages before the block are unchanged when you replay that block in a later request. This protects the integrity of Claude's reasoning: reasoning produced under one set of instructions cannot be replayed under a different set.

If your harness sends conversation history back exactly as it received it, nothing changes for you. If you edit history between requests — injecting per-turn reminders, summarizing older turns, or rebuilding the system prompt — the API rejects the request by default.

**What is checked on replay**

| **Check**           | **Description**                                                                                                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model               | The model reading the block is allowed to read the producer's thinking. A model cannot read another model's thinking unless the two are explicitly compatible. This check applies on any thinking-capable model.                 |
| Conversation prefix | The top-level system prompt, tools, and all message content before the block are unchanged from the request that produced it. Claude Fable 5.1 runs this check. Claude Mythos 5.1 records the same signature but doesn't run it. |

###### Note

A thinking block whose signature has been altered or cannot be decrypted always returns a 400, regardless of these checks or the beta value.

## The block\_binding request object (beta)

Add `block_binding` to the `thinking` object and include the beta value in `anthropic_beta` to control what happens when a prefix mismatch is detected:

```
{
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["thinking-binding-controls-2026-08-01"],
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive",
        "block_binding": {
            "mismatch_behavior": "drop_block"
        }
    },
    "messages": [{ "role": "user", "content": "Your prompt here" }]
}
```

`block_binding` accepts one field, `mismatch_behavior`, which controls what the API does with a thinking block that fails the conversation prefix check. Sent without the beta value, `block_binding` returns a 400. Malformed values also return a 400 naming the field.

## Controlling mismatch behavior

| **Value**           | **Behavior on a failed check**                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"error"` (default) | Request fails with `400 invalid_request_error` naming the failed block. Not retryable; returned before any streaming events.                                                                      |
| `"drop_block"`      | Request succeeds with 200. The failing block is removed before the model, along with every later thinking block in the conversation, and each removed block is listed in `input_transformations`. |

Neither value changes the model check, which always drops.

## The input\_transformations response array

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

This is a top-level array (a sibling of `usage`), present only with the beta value; `[]` when no blocks were removed and absent otherwise. Each entry contains a `path` identifying the removed block and a `reason` — one of `model_binding_mismatch` or `prefix_binding_mismatch`. In streaming responses, the array appears within the message object inside the `message_start` event. Removed blocks do not count toward `input_tokens`.

## Error responses

When `mismatch_behavior` is `"error"`, a prefix mismatch returns:

```
{
    "type": "error",
    "error": {
        "type": "invalid_request_error",
        "message": "messages.3.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.mismatch_behavior` to \"drop_block\"."
    }
}
```

This error is permanent for that request — an automatic retry loop will not clear it. When you catch it, either strip all thinking blocks from history and retry, or retry with `mismatch_behavior: "drop_block"` and the beta header.

## Guidance for multi-turn and agentic applications

- Replay assistant turns exactly as they were returned, and keep the system prompt and tools stable within a conversation.
- Avoid one-off content injected into earlier turns (for example, a transient system message or reminder text appended to the last user turn). These change the conversation prefix and invalidate later thinking blocks. Use mid-conversation system messages instead.
- If your application rewrites conversation history, drop thinking blocks from the rewritten point onward, or set `mismatch_behavior` to `"drop_block"`.
- When using the Converse API with a model that supports it, pass the beta value and `thinking.block_binding` through `additionalModelRequestFields`.
