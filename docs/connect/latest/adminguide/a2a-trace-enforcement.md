

# Trace data requirements for external AI agents
<a name="a2a-trace-enforcement"></a>

Connect Customer uses trace data to give you full visibility into everything that happens on a contact, across all Connect AI agents and external AI agents. Every external AI agent endpoint must send the required trace data during every collaboration. This page explains what is required, how Connect Customer monitors compliance, and what happens if an external AI agent stops sending trace data.

This page applies to external AI agents only. When the collaborator is another Connect AI agent, Connect Customer publishes its traces automatically.

Connect Customer disables external AI agent endpoints that do not send the required trace data. This protects the observability and quality management capabilities that your team depends on for every contact. If you do not provide traces, you operate without visibility, and we have limited ways to support you.

## What is required
<a name="a2a-trace-enforcement-required"></a>

Every external AI agent must publish `TRACING_SPAN` events from its server for every turn of every collaboration. Each turn's traces must include the following:

1. **Input and output messages.** The input message that the external AI agent received and the output message that it sent, recorded as span events.

1. **Tool inputs and results.** If the external AI agent invokes tools during processing, each tool span must include both the tool input and the tool result.

1. **Valid timing.** Each span must include `startTimeUnixNano` and `endTimeUnixNano` with valid timestamps.

If an external AI agent does not send these fields, Connect Customer treats the trace as incomplete. Other fields, such as token usage, model, and agent name, are encouraged but not enforced. For more information about encouraged fields, see [Observability for collaborating AI agents](a2a-observability.md).

For information about how to build and send trace spans, see [Tracing](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html#a2a-dg-tracing) in the A2A protocol contract and the [TRACING\_SPAN sample](https://docs.aws.amazon.com/connect/latest/devguide/a2a-sample-events.html#a2a-dg-sample-tracing-span) in A2A sample events. For a summary of server requirements, see [Build an external AI agent server](a2a-external-server.md).

## How enforcement works
<a name="a2a-trace-enforcement-how"></a>

Connect Customer monitors trace delivery from every external AI agent endpoint on every contact. If Connect Customer detects that an external AI agent endpoint is not sending the required trace data, Connect Customer disables that endpoint for new contacts.

This monitoring is automatic and continuous. External AI agents must send complete trace data from the first contact onward.

## Related topics
<a name="a2a-trace-enforcement-related"></a>
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Set up an external AI agent integration](a2a-setup-external.md)
+ [Build an external AI agent server](a2a-external-server.md)
+ [A2A protocol contract for external AI agents](https://docs.aws.amazon.com/connect/latest/devguide/a2a-developer-guide.html)