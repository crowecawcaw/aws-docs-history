

# Fallback credit for refused requests (beta)
<a name="claude-messages-fallback-credit"></a>

Prompt caches are per model. When a Claude model refuses a request and you retry the same conversation on a different model, the conversation prefix that was already cached for the first model is written into the new model's cache in full, at cache-write rates. Fallback credit removes this extra cost. The refusal carries a one-time credit token. When you include the token on the retry, the retry is billed as though the conversation had been on the fallback model from the start: the overlapping prefix is billed as cache-read tokens instead of cache-write tokens.

To use fallback credit, include the beta flag `fallback-credit-2026-07-01` on both the original request and the retry. The earlier flag `fallback-credit-2026-06-01` is still accepted and returns the same refusal fields. On Amazon Bedrock, a retry redeemed under `fallback-credit-2026-06-01` doesn't report `usage.fallback_credit`. Use `fallback-credit-2026-07-01` for new code. The `server-side-fallback-2026-07-01` flag is not supported on Amazon Bedrock and returns a `400` error.

## Supported models
<a name="claude-messages-fallback-credit-supported-models"></a>

The following models issue a fallback credit token when they refuse a request. The retry must use one of the listed fallback models for that source model. You can use the base model ID or a cross-Region inference profile ID (for example, `global.anthropic.claude-opus-5-5`) for either request.


| **Source model (issues the token)** | **Model ID** | **Valid fallback models (redeem the token)** | 
| --- | --- | --- | 
| Claude Fable 5 | anthropic.claude-fable-5 | Claude Opus 5 (anthropic.claude-opus-5), Claude Opus 4.8 (anthropic.claude-opus-4-8) | 
| Claude Fable 5.1 | anthropic.claude-fable-5-1 | Claude Opus 5 (anthropic.claude-opus-5), Claude Opus 4.8 (anthropic.claude-opus-4-8) | 
| Claude Opus 5.5 | anthropic.claude-opus-5-5 | Claude Opus 5 (anthropic.claude-opus-5), Claude Opus 4.8 (anthropic.claude-opus-4-8) | 
| Claude Opus 5 | anthropic.claude-opus-5 | Claude Opus 4.8 (anthropic.claude-opus-4-8) | 
| Claude Sonnet 5.5 | anthropic.claude-sonnet-5-5 | Claude Sonnet 5 (anthropic.claude-sonnet-5) | 

Refusals from other models, including Claude Haiku 5.5, don't carry a fallback credit token. A retry after one of those refusals pays the full cost of writing the fallback model's prompt cache.

A refusal from a source model doesn't always carry a token. When no credit is available for the refusal, `fallback_credit_token` and `fallback_has_prefill_claim` are both `null`. Check for a token before you build a redeeming retry.

## Supported endpoints
<a name="claude-messages-fallback-credit-endpoints"></a>

Fallback credit works on both of the following endpoints. Where you pass the beta flag depends on the endpoint.


| **Endpoint** | **How to pass the beta flag** | 
| --- | --- | 
| bedrock-runtime (InvokeModel, InvokeModelWithResponseStream) | In the anthropic\_beta array of the request body. | 
| bedrock-runtime (/anthropic/v1/messages) | In the anthropic-beta HTTP header, or the betas parameter of the Anthropic SDK. | 
| bedrock-mantle (/anthropic/v1/messages) | In the anthropic-beta HTTP header, or the betas parameter of the Anthropic SDK. | 
| bedrock-runtime (Converse) | In the anthropic\_beta array of additionalModelRequestFields. | 

Fallback credit is available on each endpoint that the source model supports.

With `Converse`, a refusal returns `stopReason: "content_filtered"`. To get the token, add `"/stop_details"` to `additionalModelResponseFieldPaths`, and pass `fallback_credit_token` on the retry in `additionalModelRequestFields`. `Converse` doesn't report `usage.fallback_credit`. To confirm that the credit applied, check that `cacheReadInputTokens` covers the conversation prefix and `cacheWriteInputTokens` doesn't.

Redeem the token on the same endpoint that issued it. A token minted on `bedrock-mantle` can only be redeemed on `bedrock-mantle`, and a token minted on `bedrock-runtime` can only be redeemed on `bedrock-runtime`. A token sent to the other endpoint is rejected with a `request body ... does not match` error.

## How it works
<a name="claude-messages-fallback-credit-how-it-works"></a>

**Step 1: Receive a fallback credit token on refusal**

When a request to a supported source model returns `stop_reason: "refusal"` and the beta flag is present, the `stop_details` object includes two fields:
+ `fallback_credit_token` – An opaque string that represents the credit.
+ `fallback_has_prefill_claim` – A boolean that tells you which retry body shape to use. For more information, see [Redemption rules](#claude-messages-fallback-credit-redemption-rules).

```
{
  "id": "msg_bdrk_...",
  "type": "message",
  "role": "assistant",
  "model": "anthropic.claude-opus-5-5",
  "content": [],
  "stop_reason": "refusal",
  "stop_details": {
    "type": "refusal",
    "category": "cyber",
    "explanation": "This request triggered restrictions on violative cyber content and was blocked under Anthropic's Usage Policy.",
    "fallback_credit_token": "<opaque token>",
    "fallback_has_prefill_claim": false
  },
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 42029,
    "output_tokens": 1
  }
}
```

Both fields are `null` when no credit is available for the refusal, for example when no cache was read on the refused request, the model isn't a supported source model, or the beta flag is absent. Server-side minting failures produce `null`, never an error. In streaming mode, the fields are delivered in the `stop_details` of the final `message_delta` event.

Because a token requires a cache read, a refusal on the first request of a conversation, which only writes the cache, doesn't carry a token. A later refused request that reads the cached prefix does.

**Note**  
On Amazon Bedrock, `fallback_has_prefill_claim` can be absent even when a token is present. If it's absent, treat the retry shape as unknown rather than as `false`: try the continuation shape first, and fall back to the unchanged body if the retry is rejected. For more information, see [Error handling](#claude-messages-fallback-credit-error-handling).

**Step 2: Redeem the token on a retry request**

Start from the refused request body. Change `model` (or the model ID in the request path) to a valid fallback model, keep the same beta flag, and add the token as the top-level `fallback_credit_token` parameter. Send the retry within 5 minutes of the refusal.

The following example shows a retry body for `InvokeModel` with the model ID `global.anthropic.claude-opus-5`:

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "anthropic_beta": ["fallback-credit-2026-07-01"],
  "max_tokens": 4096,
  "system": "...",
  "messages": [...],
  "tools": [...],
  "fallback_credit_token": "<token from the refusal's stop_details>"
}
```

The following example shows the same retry on `bedrock-mantle`:

```
curl -X POST "https://bedrock-mantle.$BEDROCK_REGION.api.aws/anthropic/v1/messages" \
  -H "x-api-key: $BEDROCK_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: fallback-credit-2026-07-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "anthropic.claude-opus-5",
    "max_tokens": 4096,
    "system": "...",
    "messages": [...],
    "tools": [...],
    "fallback_credit_token": "<token from the refusal's stop_details>"
  }'
```

## Redemption rules
<a name="claude-messages-fallback-credit-redemption-rules"></a>


| **Rule** | **Requirement** | 
| --- | --- | 
| Time window | The token expires 5 minutes after the refusal. After that, send the retry without it. | 
| Caller binding | The token can only be redeemed by the same caller identity that received the refusal, on the same endpoint. Tokens are stateless; there is no API to inspect or revoke them. | 
| Target model | The retry must use a valid fallback model for the refused model. See [Supported models](#claude-messages-fallback-credit-supported-models). | 
| Fields that must match | system, messages, tools, tool\_choice, thinking, and cache\_control, plus output\_config, mcp\_servers, context\_management, and container if you use them. Send them as-is. Don't strip thinking or redacted\_thinking blocks from earlier turns. | 
| Fields that can change | model, max\_tokens, stop\_sequences, stream, metadata, and service\_tier. | 
| Beta flags | Send the same beta flags on the retry as on the refused request. A flag that is present on only one of the two requests causes a request body ... does not match error, even if the bodies are identical. Don't add or drop flags based on the target model. On models that include the 1M token context window by default, such as Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8, the context-1m-2025-08-07 flag has no effect. Omit it on both requests. | 
| Retry shape | Choose the retry body based on `fallback_has_prefill_claim`:+ `true` – The refused request body, unchanged, plus one appended `assistant` message whose `content` echoes the refused response's `content`. The fallback model continues the response from where the refused model stopped. Strip trailing whitespace from a final `text` block, and omit any client `tool_use` block that has no matching `tool_result`.<br />+ `false` – The refused request body, unchanged. The fallback model regenerates the response. | 

## Error handling
<a name="claude-messages-fallback-credit-error-handling"></a>

With the beta flag present, a redemption validation failure returns a `400` error. Failure conditions include:
+ Malformed or unrecognizable token
+ Token older than 5 minutes
+ Request body or beta flags don't match the refused request
+ Target model isn't a valid fallback model for the refused model
+ Token has already been redeemed

When a retry is rejected, step down through progressively simpler retries:

1. If the continuation retry (with the appended `assistant` message) is rejected, resend the refused request body unchanged, still with the token.

1. If the unchanged body is also rejected with an error that names `fallback_credit_token`, retry without the token. The credit is forfeited, but the retry goes through.

If the error message says `redemption temporarily unavailable`, the rejection is transient. Retry the same request with the same token within the 5-minute window instead of stepping down.

**Important**  
If the refused request ran server tools, a retry without the token runs those tools again and bills them again. In that case, surface the error to your caller instead of silently retrying without the token.

Without the beta flag, `fallback_credit_token` is rejected as an unknown field (`400`). The parameter is also rejected on `CountTokens` requests.

## Billing impact
<a name="claude-messages-fallback-credit-billing-impact"></a>

When a token is redeemed, the credit is applied by repricing the retry's token usage. There is no separate credit or refund line item. Compared with the same retry without a token, the retry's `usage` reports fewer `cache_creation_input_tokens` and more `cache_read_input_tokens` by the same amount. Your bill, cost and usage reports, and the `CacheWriteInputTokenCount` and `CacheReadInputTokenCount` metrics in CloudWatch reflect the repriced counts.

The following example shows the retry's usage for a conversation with a 42,000-token cached prefix that was refused by Claude Opus 5.5 and retried on Claude Opus 5:


| **Retry** | **`usage.fallback_credit`** | **`cache_creation_input_tokens`** | **`cache_read_input_tokens`** | 
| --- | --- | --- | --- | 
| Without fallback\_credit\_token | – | 42,029 | 0 | 
| With fallback\_credit\_token | {"status": {"type": "redeemed"}} | 0 | 42,033 | 

A successfully redeemed retry also reports the redemption in `usage.fallback_credit`:

```
"usage": {
  "input_tokens": 45,
  "cache_creation_input_tokens": 0,
  "cache_read_input_tokens": 42033,
  "fallback_credit": {
    "status": {"type": "redeemed"}
  },
  "output_tokens": 512
}
```

If a redeemed retry shows no shift, the token was honored but there was nothing to reprice, for example because the fallback model's cache was already warm.

Fallback credit reduces only the cost of the retry. The refused request itself is billed by its `stop_details.category`: before any output, `bio`, `frontier_llm`, and `reasoning_extraction` refusals are billed, and `cyber`, `general_harms`, and `null` refusals aren't. Amazon Bedrock always bills a mid-stream refusal. For details, see [Billing notes](model-cards-anthropic.md#model-cards-anthropic-billing-notes).

A `reasoning_extraction` refusal has no recommended fallback model. Change the prompt instead of retrying on another model.

## Limitations
<a name="claude-messages-fallback-credit-limitations"></a>
+ Refusals in batch inference jobs don't issue tokens. A token passed in a batch inference record is accepted but ignored.
+ Amazon Bedrock doesn't expose the `allowed_fallback_models` list. Use the table in [Supported models](#claude-messages-fallback-credit-supported-models).
+ Server-side fallback (the `fallbacks` parameter and the `server-side-fallback-2026-07-01` flag) isn't supported on Amazon Bedrock. You build the retry yourself. Because of this, `stop_details.recommended_model` doesn't appear in Amazon Bedrock responses.
+ If the request used `output_config.format` or a `tool_choice` that forces tool use, and the refusal arrived after server tools had run, the token can't be redeemed by either retry shape. Retry without the token.

## Example workflow
<a name="claude-messages-fallback-credit-example-workflow"></a>

1. Send a request to Claude Opus 5.5 with `"anthropic_beta": ["fallback-credit-2026-07-01"]` and a cached prompt prefix.

1. Receive a refusal with a `fallback_credit_token` in `stop_details`.

1. Within 5 minutes, retry on Claude Opus 5 with the same body and beta flags, plus the `fallback_credit_token`.

1. Check the retry's `usage`: the overlapping prefix is billed as cache-read tokens instead of cache-write tokens.

The following Python example implements this workflow with `InvokeModel`, including the retry steps described in [Error handling](#claude-messages-fallback-credit-error-handling).

```
import json
import time

import boto3
from botocore.exceptions import ClientError

client = boto3.client("bedrock-runtime", region_name="us-east-1")

SOURCE_MODEL = "global.anthropic.claude-opus-5-5"
FALLBACK_MODEL = "global.anthropic.claude-opus-5"

request = {
    "anthropic_version": "bedrock-2023-05-31",
    "anthropic_beta": ["fallback-credit-2026-07-01"],
    "max_tokens": 1024,
    "system": [
        {
            "type": "text",
            "text": "<long system prompt>",
            "cache_control": {"type": "ephemeral"},
        }
    ],
    "messages": [{"role": "user", "content": "Hello, Claude"}],
}


def invoke(model_id, body):
    response = client.invoke_model(modelId=model_id, body=json.dumps(body))
    return json.loads(response["body"].read())


def invoke_with_transient_retry(model_id, body, tries=3):
    # "redemption temporarily unavailable" is transient: resend the same body,
    # with the same token, within the 5-minute window.
    for attempt in range(tries):
        try:
            return invoke(model_id, body)
        except ClientError as error:
            transient = "redemption temporarily unavailable" in error.response["Error"]["Message"]
            if not transient or attempt == tries - 1:
                raise
            time.sleep(2 ** attempt)


def can_step_down(error, forfeit_next):
    message = error.response["Error"]["Message"]
    if error.response["Error"]["Code"] != "ValidationException":
        return False
    if "redemption temporarily unavailable" in message:
        return False  # Still transient after retries: surface it, keep the token
    # Drop the token only when the error names it.
    return not forfeit_next or "fallback_credit_token" in message


result = invoke(SOURCE_MODEL, request)
details = result.get("stop_details") or {}
token = details.get("fallback_credit_token")

if result["stop_reason"] == "refusal" and token:
    exact_body = {**request, "fallback_credit_token": token}
    attempts = []

    # Prefer the continuation shape unless the claim is explicitly false.
    if details.get("fallback_has_prefill_claim") is not False and result["content"]:
        # Omit client tool_use blocks: they have no matching tool_result.
        echoed = [block for block in result["content"] if block["type"] != "tool_use"]
        if echoed and echoed[-1]["type"] == "text":
            echoed[-1]["text"] = echoed[-1]["text"].rstrip()
        attempts.append(
            {**exact_body, "messages": [*request["messages"], {"role": "assistant", "content": echoed}]}
        )

    attempts.append(exact_body)  # Unchanged body, still with the token
    attempts.append(request)     # Last resort: forfeit the credit

    for body in attempts:
        try:
            result = invoke_with_transient_retry(FALLBACK_MODEL, body)
            break
        except ClientError as error:
            forfeit_next = attempts.index(body) == len(attempts) - 2
            if body is request or not can_step_down(error, forfeit_next):
                raise

print(json.dumps({"stop_reason": result["stop_reason"], "usage": result["usage"]}, indent=2))
```

If the token is `null`, expired, or rejected, retry without it. The credit is a cost optimization; the retry doesn't need it to succeed.