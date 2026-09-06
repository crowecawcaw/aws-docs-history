

# Set up Vercel AI SDK telemetry for AgentCore Evaluations
<a name="supported-frameworks-vercel-ai"></a>

This page explains how to instrument a [Vercel AI SDK](https://sdk.vercel.ai/) agent, how spans are identified, and how evaluation fields are extracted. The Vercel AI SDK is a TypeScript-only framework, so all support on this page applies to TypeScript agents.

**Note**  
AgentCore Evaluations supports the Vercel AI SDK for TypeScript agents only. Python is not supported at this time.

 **Topics** 
+  [TypeScript agent support](#vercel-ai-typescript) 
  +  [Instrument your agent](#vercel-ai-instrument) 
  +  [How spans are identified](#vercel-ai-span-identification) 
  +  [How evaluation fields are extracted](#vercel-ai-extraction) 
  +  [Example spans from a TypeScript agent](#vercel-ai-examples-typescript) 

## TypeScript agent support
<a name="vercel-ai-typescript"></a>

A Vercel AI SDK agent produces spans under the scope name `@aws/aws-distro-opentelemetry-instrumentation-vercel-ai`.

### Instrument your agent
<a name="vercel-ai-instrument"></a>

Instrument a Vercel AI SDK agent with the AWS Distro for OpenTelemetry (ADOT). Add the AWS Distro Node autoinstrumentation package (`@aws/aws-distro-opentelemetry-node-autoinstrumentation`) to your dependencies. It includes the built-in Vercel AI instrumentation, which activates at startup and emits the scope name `@aws/aws-distro-opentelemetry-instrumentation-vercel-ai`.

 `package.json`:

```
{
  "dependencies": {
    "@aws/aws-distro-opentelemetry-node-autoinstrumentation": "^0.12.0"
  }
}
```

The instrumentation follows the OpenTelemetry generative-AI semantic conventions: it classifies spans with `gen_ai.operation.name` and carries the conversation in `gen_ai.*` attributes.

**Note**  
Instrumentation is one step in setting up observability. To export telemetry for evaluation, complete the full setup in [Set up observability](supported-frameworks-telemetry.md#supported-frameworks-setup).

### How spans are identified
<a name="vercel-ai-span-identification"></a>

The Vercel AI instrumentation sets the `gen_ai.operation.name` attribute on each span. The evaluation service uses this attribute to classify spans:


| Span type | Identifying attribute | 
| --- | --- | 
| Invoke agent |  `gen_ai.operation.name` = `invoke_agent`  | 
| Execute tool |  `gen_ai.operation.name` = `execute_tool`  | 
| Inference |  `gen_ai.operation.name` = `chat`  | 

### How evaluation fields are extracted
<a name="vercel-ai-extraction"></a>

The Vercel AI SDK serializes messages in two shapes, and AgentCore Evaluations reads both:
+ An **object-dict** shape on the input of the invoke agent and inference spans, in which `gen_ai.input.messages` is a JSON object with a `system` field (the system prompt) and a `messages` array (for example, `{"system": "…​", "messages": [{"role": "user", "content": "…​"}]}`).
+ A **parts-list** shape on the output, in which each message carries a `parts` array of typed content blocks (for example, `[{"role": "assistant", "parts": [{"type": "text", "content": "…​"}]}]`).

AgentCore Evaluations pulls the text out of both shapes: the user prompt from the last user message in the input, the system prompt from the `system` field, and the agent response from the text parts of the output.

The Vercel AI instrumentation uses unified telemetry, so the conversation content stays on the span as attributes:
+  **User prompt** and **agent response**: from `gen_ai.input.messages` and `gen_ai.output.messages` on the invoke agent span.
+  **System prompt**: from the `system` field of the object-dict in `gen_ai.input.messages`.
+  **Tool call**: the tool name from `gen_ai.tool.name`, and the arguments and result from `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result`, on the execute tool span.

For more information, see [Example spans from a TypeScript agent](#vercel-ai-examples-typescript).

### Example spans from a TypeScript agent
<a name="vercel-ai-examples-typescript"></a>

With unified telemetry, the conversation content stays on the span attributes and no separate event record is produced. The following examples are from a TypeScript Vercel AI SDK travel-planning agent deployed on Amazon Bedrock AgentCore Runtime, using an Amazon Bedrock model.

**Note**  
These examples are not complete spans. They show representative data from a real agent interaction, with some fields omitted and long values truncated for readability.

**Example**  
The `gen_ai.operation.name` attribute (`invoke_agent`) identifies this as an invoke agent span. The `gen_ai.input.messages` attribute holds the system prompt and conversation in the object-dict shape, and `gen_ai.output.messages` holds the agent response in the parts-list shape.  

```
{
  "traceId": "6a6bd3b14c8d91ed1e70a3906b551618",
  "spanId": "fa0dce44446e3d24",
  "name": "invoke_agent",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-vercel-ai",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "invoke_agent",
    "gen_ai.provider.name": "aws.bedrock",
    "gen_ai.request.model": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "gen_ai.input.messages": "{\"system\": \"You are a travel planning assistant ...\", \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how can you help me\"}]}",
    "gen_ai.output.messages": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"Hello! I'm your travel planning assistant ...\"}]}]",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`execute_tool`) identifies this as an execute tool span; `gen_ai.tool.name` holds the tool name. The `gen_ai.tool.call.arguments` attribute holds the tool arguments, and the `gen_ai.tool.call.result` attribute holds the tool result.  

```
{
  "traceId": "6a6bd3b14c8d91ed1e70a3906b551618",
  "spanId": "b64c37adefae74f0",
  "name": "execute_tool search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-vercel-ai",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "execute_tool",
    "gen_ai.tool.name": "search_flights",
    "gen_ai.tool.type": "function",
    "gen_ai.tool.call.id": "toolu_bdrk_01LzXXJCfpfuS7Bpf7e1qLMg",
    "gen_ai.tool.call.arguments": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "gen_ai.tool.call.result": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`chat`) identifies this as an inference span. It carries the model metadata and, in `gen_ai.tool.definitions`, the list of tools available to the agent. The conversation messages for the model call are in `gen_ai.input.messages` (object-dict shape) and `gen_ai.output.messages` (parts-list shape).  

```
{
  "traceId": "6a6bd3b14c8d91ed1e70a3906b551618",
  "spanId": "1865614ca1b88dfb",
  "name": "chat us.anthropic.claude-sonnet-4-5-20250929-v1:0",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-vercel-ai",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "chat",
    "gen_ai.provider.name": "aws.bedrock",
    "gen_ai.request.model": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "gen_ai.response.model": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "gen_ai.usage.input_tokens": 1258,
    "gen_ai.usage.output_tokens": 241,
    "gen_ai.input.messages": "{\"system\": \"You are a travel planning assistant ...\", \"messages\": [{\"role\": \"user\", \"content\": \"Hey, how can you help me\"}]}",
    "gen_ai.output.messages": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"Hello! I'm your travel planning assistant ...\"}]}]",
    "gen_ai.tool.definitions": "[{\"type\": \"function\", \"name\": \"search_flights\", \"description\": \"Search for available flights between cities.\", ...}]",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```