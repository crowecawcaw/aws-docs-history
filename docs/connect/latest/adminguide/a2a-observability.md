

# Observability for collaborating AI agents
<a name="a2a-observability"></a>

When an AI agent collaborates with other agents during a contact, Connect Customer collects trace data from every collaboration. This trace data provides visibility into what each collaborator did during the contact, including the messages exchanged, tools invoked, and time spent on each step. How the trace data reaches Connect Customer depends on the collaborator type:
+ **Connect AI agent collaborators.** For AI agents in your Connect Customer instance, Connect Customer publishes traces automatically. You see a trace for each AI agent that is active in the collaboration. For more information, see [AI agent traces](ai-agent-traces.md).
+ **External collaborators.** The external agent must publish trace data from its own server as `TRACING_SPAN` events. The required and encouraged fields on this page apply to external collaborators. For information about how to publish traces, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract and the [TRACING\_SPAN sample event](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-tracing-span).

You can use trace data to evaluate collaborator quality, debug unexpected behavior, and verify that collaborators are meeting your operational standards.

**Topics**
+ [What trace data Connect Customer collects](#a2a-observability-what-collected)
+ [Required trace data](#a2a-observability-required)
+ [Encouraged trace data](#a2a-observability-encouraged)
+ [Voice collaboration transcripts](#a2a-observability-transcripts)
+ [Related topics](#a2a-observability-related)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)

## What trace data Connect Customer collects
<a name="a2a-observability-what-collected"></a>

Each time your Connect AI agent brings in a collaborator, Connect Customer opens a trace context and records the collaborator's activity as OpenTelemetry spans. External agents send their spans in OpenTelemetry OTLP/JSON format inside `TRACING_SPAN` events. The trace captures the full lifecycle of the collaboration, from the initial request through the final response or conversation transfer.

For external collaborators, trace data falls into two categories: required fields that the external agent must send, and encouraged fields that improve observability but are not enforced.

## Required trace data
<a name="a2a-observability-required"></a>

External agents must send the following trace data for each turn. These fields are mandatory, and Connect Customer monitors their delivery.

1. **Input and output messages.** The input message that the collaborator received and the output message that it sent, recorded as `aws.connect.span.message` span events. Each event carries the `role`, `participant`, `type`, and `content` attributes.

1. **Tool input and result.** For each tool span, both the tool input and the tool result must be present in the trace.

1. **Per-span timing.** Each span must include `startTimeUnixNano` and `endTimeUnixNano` with valid timestamps.

If an external agent does not send these fields, Connect Customer treats the trace as incomplete. For how Connect Customer enforces these requirements, see [Trace data requirements for external AI agents](a2a-trace-enforcement.md).

## Encouraged trace data
<a name="a2a-observability-encouraged"></a>

We strongly recommend that external agents send the following fields. They improve your ability to evaluate collaborator performance and debug issues, but they are not enforced.

1. **Token counts.** Input and output token counts, in the `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens` attributes.

1. **Model identifier.** The foundation model that the collaborator used, in the `gen_ai.request.model` attribute.

1. **Total tokens.** The total token count, in the `aws.connect.usage.total_tokens` attribute.

1. **Agent name.** The name of the collaborating agent, in the `gen_ai.agent.name` attribute.

1. **Operation name.** The type of operation for the span, in the `gen_ai.operation.name` attribute.

1. **Error type.** The type of error when a span fails, in the `aws.connect.error.type` attribute.

For the full list of recognized attributes, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract.

## Voice collaboration transcripts
<a name="a2a-observability-transcripts"></a>

For voice collaborations that use bidirectional audio streaming, which is available only for external collaborators, trace data also includes transcripts that are used to maintain conversation history across the collaboration.

## Related topics
<a name="a2a-observability-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)
+ [Build an external AI agent server](a2a-external-server.md)
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)