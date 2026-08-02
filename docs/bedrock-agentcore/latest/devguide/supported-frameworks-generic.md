# Generic framework support

Amazon Bedrock AgentCore Evaluations has dedicated handling for specific agent frameworks. For agents built with other frameworks, the service falls back to **generic framework support**. Generic framework support reads any framework that follows one of the two conventions the service understands, using the same span classification and field extraction described for the named frameworks, without framework-specific parsing.

Generic framework support is a best-effort fallback. It works when your framework emits standard convention attributes and stores conversation content in the expected locations. It does not apply framework-specific parsing, so content that a framework wraps in a proprietary structure (for example, a nested request object or a custom message envelope) is extracted as a stringified value rather than a cleanly parsed prompt, response, or tool argument.

**Topics**

- [Supported conventions](#generic-conventions "#generic-conventions")
- [How spans are identified](#generic-span-identification "#generic-span-identification")
- [How evaluation fields are extracted](#generic-extraction "#generic-extraction")

  - [OpenTelemetry convention](#generic-extraction-otel "#generic-extraction-otel")
  - [OpenInference convention](#generic-extraction-openinference "#generic-extraction-openinference")

- [Limitations](#generic-limitations "#generic-limitations")

## Supported conventions

The service selects how to read each span from the span’s `scope.name`. When no dedicated handling is registered for a scope, the service processes the span with generic framework support, based on the scope name prefix:

| Convention    | Scope name prefix                 |
| ------------- | --------------------------------- |
| OpenTelemetry | `opentelemetry.instrumentation.*` |
| OpenInference | `openinference.instrumentation.*` |

Dedicated framework handling always takes precedence over generic framework support for the same scope. Generic framework support applies only to scopes that match one of these prefixes but have no dedicated handling.

Some scopes match the OpenTelemetry prefixes but are not GenAI agent frameworks. These are transport and infrastructure instrumentation, such as HTTP clients (`httpx`, `urllib3`, `urllib`, `aiohttp_client`), web frameworks (`starlette`, `fastapi`), the Model Context Protocol (MCP) instrumentation, and the AWS SDK (`botocore`) instrumentation, including its `bedrock-agentcore` and `bedrock-runtime` scopes. The service excludes these scopes from generic framework support so that their spans do not produce spurious agent, tool, or inference spans.

## How spans are identified

Generic framework support classifies each span into one of three types using the standard identifying attribute for its convention. The attribute is always present on the span, regardless of where the conversation content is stored.

###### Example

OpenTelemetry
The service classifies spans using `gen_ai.operation.name`, and falls back to `traceloop.span.kind` when the operation name is absent.

| Span type    | Identifying attribute                                                            |
| ------------ | -------------------------------------------------------------------------------- |
| Invoke agent | `gen_ai.operation.name` = `invoke_agent` (or `traceloop.span.kind` = `workflow`) |
| Execute tool | `gen_ai.operation.name` = `execute_tool` (or `traceloop.span.kind` = `tool`)     |
| Inference    | `gen_ai.operation.name` = `chat` (or `llm.request.type` = `chat`)                |

OpenInference
The service classifies spans using `openinference.span.kind`.

| Span type    | Identifying attribute                          |
| ------------ | ---------------------------------------------- |
| Invoke agent | `openinference.span.kind` = `AGENT` or `CHAIN` |
| Execute tool | `openinference.span.kind` = `TOOL`             |
| Inference    | `openinference.span.kind` = `LLM`              |

## How evaluation fields are extracted

For each classified span, the service reads the values it needs, such as the user prompt, agent response, and tool inputs and outputs. As with the named frameworks, the location of the conversation content depends on how telemetry was collected: when the AWS Distro for OpenTelemetry (ADOT) splits telemetry, the content lives in the correlated event record; when telemetry is not split, it stays on the span as attributes. For more information, see [Spans, event records, and telemetry signals](supported-frameworks-telemetry.md "supported-frameworks-telemetry.md").

Under generic framework support, the service tries multiple locations for each field and uses the first one that holds a value. Because a generic framework’s content format is not known in advance, each extracted value is stringified rather than parsed into a framework-specific structure.

### OpenTelemetry convention

For frameworks using the OpenTelemetry convention, the service reads each field from the following locations, in order:

- **User prompt** (invoke agent span): from the event record `body.input`; then from the `gen_ai.task.input` span attribute.
- **Agent response** (invoke agent span): from the event record `body.output`; then from the `gen_ai.task.output` span attribute. If neither is present, the service falls back to the first user message and last assistant message it collected from the trace’s inference spans.
- **Inference messages** (inference span): from the event record `body.input.messages` and `body.output.messages`; then from the `gen_ai.input.messages` and `gen_ai.output.messages` span attributes.
- **Tool name** (execute tool span): from the `gen_ai.tool.name` span attribute; then from the `traceloop.entity.name` span attribute.
- **Tool arguments** (execute tool span): from the `gen_ai.tool.call.arguments` span attribute; then from the event record `body.input`; then from the `traceloop.entity.input` span attribute.
- **Tool result** (execute tool span): from the `gen_ai.tool.call.result` span attribute; then from the event record `body.output`; then from the `traceloop.entity.output` span attribute.
- **System prompt** (inference span): from the `gen_ai.system_instructions` span attribute.

### OpenInference convention

For frameworks using the OpenInference convention, the service reads each field from the following locations, in order:

- **User prompt** (invoke agent span): from the `input.value` span attribute; then from the event record body input.
- **Agent response** (invoke agent span): from the `output.value` span attribute; then from the event record body output.
- **Inference messages** (inference span): from the span’s OpenInference message attributes (for example, `llm.input_messages.` and `llm.output_messages.`); then from `input.value` and `output.value`; then from the event record body.
- **Tool arguments** (execute tool span): from the `input.value` span attribute; then from the event record body input.
- **Tool result** (execute tool span): from the `output.value` span attribute; then from the event record body output.
- **System prompt** (inference span): from the inference span attributes; then from the event record body.
- **Available tools**: from the inference span’s tool-definition attributes (`llm.tools.*`); then parsed from the serialized request in the event record body or `input.value`.

## Limitations

Consider the following when relying on generic framework support:

- **Convention required.** The service can apply generic framework support only to scopes under the `opentelemetry.instrumentation.` or `openinference.instrumentation.` prefixes. A framework that emits a scope name outside these prefixes is not covered.
- **Standard attributes required.** Generic framework support depends on the standard identifying attributes (`gen_ai.operation.name`, `traceloop.span.kind`, or `openinference.span.kind`). Spans without a recognized identifying attribute are skipped.
- **No framework-specific parsing.** Generic framework support stringifies content rather than parsing framework-specific structures. If your framework wraps the prompt, response, or tool arguments in a proprietary envelope, the extracted value can include that surrounding structure. For the cleanest extraction, use a framework with dedicated handling.
- **Attribute fallback for unknown scopes.** For a scope with no dedicated handling and no matching convention prefix, the service falls back to reading the `agentcore.invocation.user_prompt` and `agentcore.invocation.agent_response` span attributes, which the AgentCore SDK or explicit instrumentation can emit. This recovers only the top-level agent prompt and response, not inference or tool spans.
