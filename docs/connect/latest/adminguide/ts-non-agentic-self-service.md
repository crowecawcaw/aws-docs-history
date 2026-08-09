# (Legacy) Self-service issues

The following issues are specific to [legacy
self-service](generative-ai-powered-self-service.md "generative-ai-powered-self-service.md").

## Customers are unexpectedly receiving "Escalating to agent..."

Unexpected agent escalation occurs when there's an error during the
self-service bot interaction or when the model doesn't produce a valid
`tool_use` response for
`SELF_SERVICE_PRE_PROCESS`.

### Troubleshooting steps

1. **Check the AI agent
   logs**: Examine the `completion` attribute
   in the associated log entry.
2. **Validate the stop reason**: Confirm
   that the `stop_reason` is
   `tool_use`.
3. **Verify parsed response**: Check if
   the `parsed_response` field is populated, as this
   represents the response you'll receive from the model.

### Known issue with Claude 3 Haiku

If you're using Claude 3 Haiku for self-service pre-processing, there's a
known issue where it generates the `tool_use` JSON as text,
resulting in a `stop_reason` of `end_turn` instead of
`tool_use`.

**Solution**: Update your custom prompt to
wrap the `tool_use` JSON string inside
`<tool>` tags by adding this instruction:

```
You MUST enclose the tool_use JSON in the <tool> tag
```

## Self-service chat or voice call is unexpectedly terminating

This issue can occur due to timeouts from Amazon Lex or incorrect Amazon Nova Pro
configuration. These issues are described below.

### Timeouts from Amazon Lex

- **Symptoms**: Connect Customer logs show
  "Internal Server Error" for the [Get customer input](get-customer-input.md "get-customer-input.md") block
- **Cause**: Your self-service bot
  timed out while providing results within the 10-second limit.
  Timeout errors won't appear in AI agent logs.
- **Solution**: Simplify your prompt by
  removing complex reasoning to reduce processing time.

### Amazon Nova Pro configuration

If you're using Amazon Nova Pro for your custom AI prompts, ensure that
the tool\_use examples follow [Python-compatible format](create-ai-prompts.md#nova-pro-aiprompt "create-ai-prompts.md#nova-pro-aiprompt").
