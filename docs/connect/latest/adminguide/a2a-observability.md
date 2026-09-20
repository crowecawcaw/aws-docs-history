

# Observability for collaborating AI agents
<a name="a2a-observability"></a>

When an AI agent collaborates with other agents during a contact, Connect Customer collects trace data from every collaboration automatically. This trace data provides visibility into what each collaborator did during the contact, including the messages exchanged, tools invoked, and time spent on each step.

You can use trace data to evaluate collaborator quality, debug unexpected behavior, and verify that collaborators are meeting your operational standards.

**Topics**
+ [What trace data is collected](#a2a-observability-what-collected)
+ [Required trace data](#a2a-observability-required)
+ [Encouraged trace data](#a2a-observability-encouraged)
+ [Voice collaboration transcripts](#a2a-observability-transcripts)
+ [Related topics](#a2a-observability-related)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)

## What trace data is collected
<a name="a2a-observability-what-collected"></a>

Each time your Connect AI agent brings in a collaborator, Connect Customer opens a trace context and records the collaborator's activity as OpenTelemetry spans. The trace captures the full lifecycle of the collaboration, from the initial request through the final response or conversation transfer.

Trace data falls into two categories: required fields that collaborators must send, and encouraged fields that improve observability but are not enforced.

## Required trace data
<a name="a2a-observability-required"></a>

Collaborators must send the following trace data for every collaboration. These fields are mandatory, and Connect Customer monitors their delivery.

1. **Input and output messages.** The messages sent to and received from the collaborator during the collaboration, recorded as span events.

1. **Tool calls and their results.** If the collaborator invokes tools during processing, both the tool call and the tool result must be present as span events in the trace.

1. **Per-span timing.** Each span must include `startTimeUnixNano` and `endTimeUnixNano` with valid timestamps.

If a collaborator does not send these fields, Connect Customer treats the trace as incomplete.

## Encouraged trace data
<a name="a2a-observability-encouraged"></a>

The following fields are strongly encouraged. They improve your ability to evaluate collaborator performance and debug issues, but they are not enforced.

1. **Model identifier.** The name or identifier of the foundation model used by the collaborator.

1. **Token counts.** Input and output token counts for each inference step.

1. **Time to first token.** The elapsed time between when the request was submitted and when the first inference token was generated, when the collaborator can measure it.

1. **Finish reason per step.** Why each processing step ended (for example, stop sequence, max tokens, or tool invocation). The contact-level finish type (COMPLETE, ESCALATE, OUT\_OF\_DOMAIN, COMPLETE\_WITH\_ERROR) is mandatory through the A2A protocol itself and is recorded by Connect Customer regardless of what the collaborator sends.

1. **Sub-agent detail.** If the collaborator delegates work internally to other agents, detail about those sub-agent invocations.

1. **Reasoning output.** Chain-of-thought or reasoning tokens produced per turn.

## Voice collaboration transcripts
<a name="a2a-observability-transcripts"></a>

For voice collaborations using bidirectional audio streaming, trace data also includes transcripts that are used to maintain conversation history across the collaboration.

## Related topics
<a name="a2a-observability-related"></a>
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Trace data requirements for external AI agents](a2a-trace-enforcement.md)