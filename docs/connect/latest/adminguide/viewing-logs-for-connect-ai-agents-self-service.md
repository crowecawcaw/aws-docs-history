# Logging and tracing for AI agents

To troubleshoot AI agent issues effectively, use the following logging
and tracing options.

- **ListSpans API (recommended for orchestrator AI
  agents)**: Use the [ListSpans](../APIReference/API_amazon-q-connect_ListSpans.md "../APIReference/API_amazon-q-connect_ListSpans.md") API to retrieve AI agent execution traces for a
  session. This is the recommended starting point for debugging orchestrator AI
  agent interactions, as it provides granular visibility into agent
  orchestration flows, LLM interactions, and tool invocations, allowing you to
  trace how the AI agent reasoned through a request and which tools it
  selected and executed.
- **CloudWatch Logs**: Enable CloudWatch Logging for your
  AI agents by following the steps in [Monitor AI agents using
  CloudWatch](monitor-ai-agents.md "monitor-ai-agents.md").

Legacy self-service interactions generate log entries with the
event type `TRANSCRIPT_SELF_SERVICE_MESSAGE` in the following
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

Agentic self-service interactions generate log entries with the event type
`TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION`. These entries
include the full orchestration context such as the prompt with tool
configurations, conversation history with tool calls and results, the model
completion, and the AI agent configuration. The following example shows the
key fields:

```
{
    "assistant_id": "{UUID}",
    "event_timestamp": 1772748470993,
    "event_type": "TRANSCRIPT_LARGE_LANGUAGE_MODEL_INVOCATION",
    "session_id": "{UUID}",
    "prompt": "{full prompt including system instructions, tool configs, and conversation history}",
    "prompt_type": "ORCHESTRATION",
    "completion": "{model response with message and tool use}",
    "model_id": "{model id e.g.: us.anthropic.claude-haiku-4-5-20251001-v1:0}",
    "parsed_response": "{parsed customer-facing message}",
    "generation_id": "{UUID}",
    "ai_agent_id": "{UUID}"
}
```

- **Amazon Lex logging (self-service only)**: Enable
  Amazon Lex logging by following the steps in [Logging errors with
  error logs in Amazon Lex V2](../../../lexv2/latest/dg/error-logs.md "../../../lexv2/latest/dg/error-logs.md").
- **Connect Customer logging**: Enable Connect Customer logging by
  adding a [Set logging behavior](set-logging-behavior.md "set-logging-behavior.md") flow block in your Connect Customer
  flow.
