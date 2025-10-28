# Troubleshoot Amazon Q in Connect self-service issues

Use this topic to help diagnose and resolve common issues with Amazon Q in Connect self-service
functionality.

###### Contents

- [Enable logging for
  Amazon Q in Connect self-service interactions](#viewing-logs-for-q-in-connect-self-service "#viewing-logs-for-q-in-connect-self-service")
- [Customers are
  unexpectedly receiving "Escalating to agent..."](#customers-unexpectedly-receiving-escalating-to-agent "#customers-unexpectedly-receiving-escalating-to-agent")
- [Self-service chat or voice
  call is unexpectedly terminating](#self-service-unexpectedly-terminating "#self-service-unexpectedly-terminating")

## Enable logging for

Amazon Q in Connect self-service interactions

To troubleshoot self-service issues effectively, you need to view the logs for
Amazon Q in Connect self-service interactions. Use the following instructions to enable CloudWatch
Logging, Amazon Lex logging, and Amazon Connect logging.

- **CloudWatch Logs**: Enable CloudWatch Logging for your
  Amazon Q in Connect instance by following the steps in [Monitor
  Amazon Q in Connect](monitor-q-assistants-cloudwatch.md "monitor-q-assistants-cloudwatch.md").

Self-service interactions generate log entries with the event type
`TRANSCRIPT_SELF_SERVICE_MESSAGE` in the following
format:

```
{
    "assistant_id": "{UUID}",
    "event_timestamp": 1751414298692,
    "event_type": "TRANSCRIPT_SELF_SERVICE_MESSAGE",
    "session_id": "{UUID}",
    "utterance": "[CUSTOMER]...",
    "prompt": "{prompt used}",
    "prompt_type": "SELF_SERVICE_PRE_PROCESS|SELF_SERVICE_ANSWER_GENERATION",
    "completion": "{Response from model}",
    "model_id": "{model id e.g.: us.amazon.nova-pro-v1:0}",
    "session_message_id": "{UUID}",
    "parsed_response": "{model response}"
}
```

- **Amazon Lex logging**: Enable Amazon Lex logging by
  following the steps in [Logging errors with
  error logs in Amazon Lex V2](../../../exv2/latest/dg/monitoring-cloudwatch.md "../../../exv2/latest/dg/monitoring-cloudwatch.md").
- **Amazon Connect logging**: Enable Amazon Connect logging by
  adding a [Set logging behavior](set-logging-behavior.md "set-logging-behavior.md") flow block in your Amazon Connect
  flow.

## Customers are

unexpectedly receiving "Escalating to agent..."

Unexpected agent escalation occurs when there's an error during the self-service
bot interaction or when the model doesn't produce a valid `tool_use`
response for `SELF_SERVICE_PRE_PROCESS`.

### Troubleshooting steps

1. **Check the Amazon Q in Connect logs**: Examine the
   `completion` attribute in the associated log
   entry.
2. **Validate the stop reason**: Confirm
   that the `stop_reason` is `tool_use`.
3. **Verify parsed response**: Check if the
   `parsed_response` field is populated, as this represents
   the response you'll receive from the model.

### Known issue with Claude 3

Haiku

If you're using Claude 3 Haiku for self-service pre-processing, there's a
known issue where it generates the `tool_use` JSON as text, resulting
in a `stop_reason` of `end_turn` instead of
`tool_use`.

**Solution**: Update your custom prompt to wrap
the `tool_use` JSON string inside `<tool>` tags by
adding this instruction:

```
You MUST enclose the tool_use JSON in the <tool> tag
```

## Self-service chat or voice

call is unexpectedly terminating

This issue can occur due to timeouts or errors from Amazon Lex or incorrect Amazon Nova
Pro configuration. These issues are described below.

### Timeouts from Amazon Lex

- **Symptoms**: Amazon Connect logs show "Internal
  Server Error" for the [Get customer input](get-customer-input.md "get-customer-input.md") block
- **Cause**: Your self-service bot timed
  out while providing results within the 10-second limit. Timeout errors
  won't appear in Amazon Q in Connect logs.
- **Solution**: Simplify your prompt by
  removing complex reasoning to reduce processing time.

### Errors from Amazon Lex

- **Missing Amazon Q in Connect flow block**: Ensure
  you've added the [Amazon Q in Connect](q-block.md "q-block.md")
  block to your Amazon Connect flow. A common oversight is missing this block,
  which results in the following error:

```
com.amazonaws.services.lexruntimev2.model.ValidationException: Amazon Lex needs active session for Amazon Q in Connect.
                            Please provide valid session attribute x-amz-lex:q-in-connect:session-arn
```

- **General Amazon Lex errors**: Check Amazon Lex
  logs for any errors and address them accordingly.

### Amazon Nova Pro

configuration

If you're using Amazon Nova Pro for your custom AI prompts, ensure that the
tool_use examples follow [Python-compatible
format](create-ai-prompts.md#nova-pro-aiprompt "create-ai-prompts.md#nova-pro-aiprompt").
