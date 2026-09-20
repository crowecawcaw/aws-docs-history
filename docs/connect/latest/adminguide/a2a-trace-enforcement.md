

# Trace data requirements for external AI agents
<a name="a2a-trace-enforcement"></a>

Connect Customer uses trace data to give you full visibility into everything happening on a contact, across all Connect AI agents and external AI agents. Every external AI agent endpoint must send the required trace data during every collaboration. This page explains what is required, how Connect Customer monitors compliance, and what happens if an external AI agent stops sending trace data.

Connect Customer will disable external AI agent endpoints that do not send the required trace data. Connect Customer will notify you when an external AI agent endpoint is disabled. This protects the observability and quality management capabilities your team depends on for every contact. If you do not provide us with traces, you are operating without visibility, and we have limited ways to support you.

## What is required
<a name="a2a-trace-enforcement-required"></a>

Every external AI agent must send the following trace data fields for every collaboration:

1. **Input and output messages.** The messages sent to and received from the external AI agent during the collaboration, recorded as span events.

1. **Tool calls and their results.** If the external AI agent invokes tools during processing, both the tool call and the tool result must be present as span events in the trace.

1. **Per-span timing.** Each span must include `startTimeUnixNano` and `endTimeUnixNano` with valid timestamps.

If an external AI agent does not send these fields, Connect Customer treats the trace as incomplete. For additional encouraged fields that improve observability but are not enforced, see [Observability for collaborating AI agents](a2a-observability.md).

## How enforcement works
<a name="a2a-trace-enforcement-how"></a>

Connect Customer monitors trace delivery from every external AI agent endpoint on every contact. If Connect Customer detects that an external AI agent endpoint is not sending the required trace data, Connect Customer will disable that endpoint for new contacts.

This monitoring is automatic and continuous. External AI agents are expected to send complete trace data from the first contact onward.

## Related topics
<a name="a2a-trace-enforcement-related"></a>
+ [Observability for collaborating AI agents](a2a-observability.md)
+ [Agent-to-agent collaboration](a2a-collaboration.md)
+ [Set up collaboration with an external AI agent](a2a-setup-external.md)