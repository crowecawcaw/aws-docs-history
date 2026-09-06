

# Rate limits and quotas
<a name="rate-limits"></a>

Claude Platform on AWS assigns Tier 1 rate limits when you subscribe. Anthropic manages rate limits directly, not through AWS quota systems.

## Default limits
<a name="_default_limits"></a>

Claude Platform on AWS uses Anthropic’s standard tier schedule, identical to the first-party Claude API. Tier 1 limits apply per workspace. Limits are pooled by model family. For example, all Opus models share one combined limit, all Sonnet models share another, and all Haiku models share a third.

For current Tier 1 values (RPM, ITPM, OTPM) and higher-tier thresholds, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits) on the Anthropic documentation website. The Anthropic page is the source of truth and is updated when limits change.

## Rate limit headers
<a name="_rate_limit_headers"></a>

Every response includes headers that report your current rate limit status. Key headers:
+  `anthropic-ratelimit-requests-limit` — Maximum requests per minute
+  `anthropic-ratelimit-requests-remaining` — Requests remaining in the current window
+  `anthropic-ratelimit-requests-reset` — Time when the request limit resets (RFC 3339)
+  `anthropic-ratelimit-tokens-limit` — Maximum combined tokens (input \+ output) per minute
+  `anthropic-ratelimit-tokens-remaining` — Combined tokens remaining in the current window
+  `anthropic-ratelimit-tokens-reset` — Time when the combined token limit resets (RFC 3339)
+  `anthropic-ratelimit-input-tokens-limit` / `-remaining` / `-reset` — Input-token-specific headers
+  `anthropic-ratelimit-output-tokens-limit` / `-remaining` / `-reset` — Output-token-specific headers
+  `retry-after` — On a 429 response, the number of seconds to wait before retrying

See [Response headers](https://platform.claude.com/docs/en/api/rate-limits#response-headers) on the Anthropic documentation website for the complete set.

## Requesting higher limits
<a name="_requesting_higher_limits"></a>

Unlike the first-party Claude API, automatic tier advancement does not apply on Claude Platform on AWS. To request higher limits, contact your Anthropic account representative with your workspace ID and desired throughput. For tier thresholds and other details, see [Rate limits](https://platform.claude.com/docs/en/api/rate-limits) on the Anthropic documentation website.

## Rate limit errors
<a name="_rate_limit_errors"></a>

When you exceed a rate limit, the API returns HTTP 429 with a `rate_limit_error` type. Implement exponential backoff with jitter in your retry logic. The `retry-after` header indicates how many seconds to wait before retrying.