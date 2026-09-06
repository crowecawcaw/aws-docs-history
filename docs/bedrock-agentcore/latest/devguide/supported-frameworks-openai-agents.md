

# OpenAI Agents
<a name="supported-frameworks-openai-agents"></a>

This page explains how to instrument an [OpenAI Agents](https://openai.github.io/openai-agents-python/) agent, how spans are identified, and how evaluation fields are extracted. AgentCore Evaluations supports OpenAI Agents built in Python and TypeScript; this page covers each language separately, in [Python agent support](#openai-agents-python) and [TypeScript agent support](#openai-agents-typescript).

 **Topics** 
+  [Python agent support](#openai-agents-python) 
  +  [Instrument your agent](#openai-agents-instrument) 
  +  [How spans are identified](#openai-agents-span-identification) 
  +  [How evaluation fields are extracted](#openai-agents-extraction) 
    +  [From event records](#openai-agents-extraction-event-records) 
    +  [From span attributes](#openai-agents-extraction-attributes) 
  +  [Example spans in split telemetry](#openai-agents-examples-split) 
  +  [Example spans in unified telemetry](#openai-agents-examples-unified) 
+  [TypeScript agent support](#openai-agents-typescript) 
  +  [Instrument your agent](#openai-agents-typescript-instrument) 
  +  [How spans are identified](#openai-agents-typescript-span-identification) 
  +  [How evaluation fields are extracted](#openai-agents-typescript-extraction) 
  +  [Example spans from a TypeScript agent](#openai-agents-examples-typescript) 

## Python agent support
<a name="openai-agents-python"></a>

A Python OpenAI Agents agent emits spans under the scope name `opentelemetry.instrumentation.openai_agents` (OpenTelemetry) or `openinference.instrumentation.openai_agents` (OpenInference).

### Instrument your agent
<a name="openai-agents-instrument"></a>

You can instrument an OpenAI Agents agent with either of two instrumentation libraries: **OpenTelemetry** (`opentelemetry-instrumentation-openai-agents`) or **OpenInference** (`openinference-instrumentation-openai-agents`). Amazon Bedrock AgentCore Evaluations supports both libraries. The libraries emit different scope names and use different span attributes. The evaluation service extracts the same values from each.

When your agent runs with the AWS Distro for OpenTelemetry (ADOT), such as on Amazon Bedrock AgentCore Runtime, you do not need to add explicit instrumentation code. Adding the instrumentation library to your project’s dependencies is enough. ADOT discovers it at startup and activates it automatically.

Add the instrumentation library for the path you want to your dependencies. Use the latest available version unless you have a reason to pin.

**Example**  
NOTE: Use version `0.61.0` or later. This is the earliest version tested with the evaluation service.  
Add `opentelemetry-instrumentation-openai-agents` to your dependencies. The scope name emitted is `opentelemetry.instrumentation.openai_agents`.  
 `requirements.txt`:  

```
opentelemetry-instrumentation-openai-agents>=0.61.0
```
 `pyproject.toml`:  

```
[project]
dependencies = [
    "opentelemetry-instrumentation-openai-agents>=0.61.0",
]
```
NOTE: Use version `1.5.0` or later. This is the earliest version tested with the evaluation service.  
Add `openinference-instrumentation-openai-agents` to your dependencies. The scope name emitted is `openinference.instrumentation.openai_agents`.  
 `requirements.txt`:  

```
openinference-instrumentation-openai-agents>=1.5.0
```
 `pyproject.toml`:  

```
[project]
dependencies = [
    "openinference-instrumentation-openai-agents>=1.5.0",
]
```

**Note**  
Instrumentation is one step in setting up observability. To export telemetry for evaluation, complete the full setup in [Set up observability](supported-frameworks-telemetry.md#supported-frameworks-setup).

### How spans are identified
<a name="openai-agents-span-identification"></a>

The attribute used to classify spans differs between the two instrumentation libraries.

**Example**  
The OpenTelemetry instrumentation library classifies spans using the `gen_ai.operation.name` attribute.  


| Span type | Identifying attribute | 
| --- | --- | 
| Invoke agent |  `gen_ai.operation.name` = `invoke_agent`  | 
| Execute tool |  `gen_ai.operation.name` = `execute_tool`  | 
| Inference |  `gen_ai.operation.name` = `chat`  | 
OpenAI Agents also emits internal turn-boundary spans with `gen_ai.operation.name` = `unknown`. The evaluation service skips these.
The OpenInference instrumentation library classifies spans using the `openinference.span.kind` attribute.  


| Span type | Identifying attribute | 
| --- | --- | 
| Invoke agent |  `openinference.span.kind` = `AGENT` or `CHAIN`  | 
| Execute tool |  `openinference.span.kind` = `TOOL`  | 
| Inference |  `openinference.span.kind` = `LLM`  | 
With the OpenInference library, the `AGENT` and `CHAIN` spans are empty structural containers: they carry no conversation content. The user prompt and agent response are reconstructed from the inference (`LLM`) spans in the same trace.

### How evaluation fields are extracted
<a name="openai-agents-extraction"></a>

OpenAI Agents serializes messages in a parts-based format, in which each message carries a `parts` array of typed content blocks (for example, `[{"role": "user", "parts": [{"type": "text", "content": "…​"}]}]`). With the OpenTelemetry library, AgentCore Evaluations parses the text out of these parts. With the OpenInference library, the model output is the full OpenAI Response object, and AgentCore Evaluations reads the response text from `output[].content[].text`.

The location of this content depends on how telemetry was collected. The identifying attribute (`gen_ai.operation.name` or `openinference.span.kind`) is on the span in both cases. For more information, see [Telemetry setup and delivery](supported-frameworks-telemetry.md).

#### From event records
<a name="openai-agents-extraction-event-records"></a>

With split telemetry, AgentCore Evaluations reads conversation content from the event record correlated to each span. The location of tool inputs and outputs differs between the two libraries:
+  **OpenTelemetry**:
  +  **User prompt** and **agent response**: from the invoke agent span’s event record, in `body.input` and `body.output`.
  +  **Tool call**: the tool name from `gen_ai.tool.name`, and the arguments and result from `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result` on the execute tool span. With the OpenTelemetry library, tool arguments and results remain on the span attributes even with split telemetry.
+  **OpenInference**:
  +  **User prompt** and **agent response**: reconstructed from the inference span’s event record. AgentCore Evaluations reads the messages from `body.input` and `body.output`, then backfills the empty invoke agent span with the user prompt and agent response.
  +  **Tool call**: the tool name from `tool.name` on the execute tool span. The tool arguments and result come from that span’s event record, in `body.input` and `body.output`.

For more information, see [Example spans in split telemetry](#openai-agents-examples-split).

#### From span attributes
<a name="openai-agents-extraction-attributes"></a>

With unified telemetry, the same content stays on the span as attributes. The attributes depend on the instrumentation library:
+  **OpenTelemetry**:
  +  **User prompt** and **agent response**: from `gen_ai.input.messages` and `gen_ai.output.messages` on the invoke agent span.
  +  **Tool call**: the tool name from `gen_ai.tool.name`, and the arguments and result from `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result`, on the execute tool span.
+  **OpenInference**:
  +  **User prompt** and **agent response**: from the indexed message attributes on the inference span (`llm.input_messages.*` and `llm.output_messages.*`), then backfilled onto the empty invoke agent span.
  +  **Tool call**: the tool name from `tool.name`, and the arguments and result from `input.value` and `output.value`, on the execute tool span.

For more information, see [Example spans in unified telemetry](#openai-agents-examples-unified).

### Example spans in split telemetry
<a name="openai-agents-examples-split"></a>

With split telemetry, the span carries the identifying attributes and the content lives in a correlated event record. The following examples are from a Python OpenAI Agents travel-planning agent deployed on Amazon Bedrock AgentCore Runtime. The same agent is shown under each instrumentation library.

**Note**  
These examples are not complete spans. They show representative data from a real agent interaction, with some fields omitted and long values truncated for readability.

#### OpenTelemetry
<a name="openai-agents-examples-split-otel"></a>

**Example**  
The `gen_ai.operation.name` attribute (`invoke_agent`) identifies this as an invoke agent span.  

```
{
  "traceId": "6a01eef11066751d68f90def0da1f80a",
  "spanId": "3a300b0b3fe650e4",
  "name": "invoke_agent openaiOtelTravel",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "invoke_agent",
    "gen_ai.agent.name": "openaiOtelTravel",
    "gen_ai.system": "openai",
    "gen_ai.provider.name": "openai",
    "gen_ai.request.model": "gpt-4o-mini-2024-07-18",
    "session.id": "sea-nyc-trip-2-turns-openai-otel"
  },
  "status": {
    "code": "OK"
  }
}
```
The correlated event record carries the conversation. Each message’s `content` is the OpenAI parts-format array; the user prompt is the text of the user message and the agent response is the text of the assistant message.  

```
{
  "spanId": "3a300b0b3fe650e4",
  "traceId": "6a01eef11066751d68f90def0da1f80a",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents"
  },
  "body": {
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "[{\"role\": \"user\", \"parts\": [{\"type\": \"text\", \"content\": \"Hey, how can you help me\"}]}]"
        }
      ]
    },
    "output": {
      "messages": [
        {
          "role": "assistant",
          "content": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"I can assist you with planning your trips ...\"}]}]"
        }
      ]
    }
  }
}
```
The `gen_ai.operation.name` attribute (`execute_tool`) identifies this as an execute tool span; `gen_ai.tool.name` holds the tool name. With the OpenTelemetry library, the tool arguments and result stay on the span attributes even with split telemetry.  

```
{
  "traceId": "6a01eefa5c52f3d86a35038f35f5ba30",
  "spanId": "3cbc4ea5f73fef81",
  "name": "execute_tool search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "execute_tool",
    "gen_ai.tool.name": "search_flights",
    "gen_ai.tool.type": "function",
    "gen_ai.tool.call.arguments": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "gen_ai.tool.call.result": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns-openai-otel"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`chat`) identifies this as an inference span. This span carries the model metadata and, in `gen_ai.tool.definitions`, the list of tools available to the agent. The conversation messages for the model call live in the correlated event record, in `body.input` and `body.output`.  

```
{
  "traceId": "6a01eef11066751d68f90def0da1f80a",
  "spanId": "7c1f9a2b4d6e8a03",
  "name": "openai.response",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "chat",
    "gen_ai.provider.name": "openai",
    "gen_ai.request.model": "gpt-4o-mini-2024-07-18",
    "gen_ai.response.model": "gpt-4o-mini-2024-07-18",
    "gen_ai.usage.input_tokens": 269,
    "gen_ai.usage.output_tokens": 78,
    "gen_ai.tool.definitions": "[{\"type\": \"function\", \"function\": {\"name\": \"search_flights\", \"description\": \"Search for available flights between cities.\", \"parameters\": { ... }}}]",
    "session.id": "sea-nyc-trip-2-turns-openai-otel"
  },
  "status": {
    "code": "OK"
  }
}
```

```
{
  "spanId": "7c1f9a2b4d6e8a03",
  "traceId": "6a01eef11066751d68f90def0da1f80a",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents"
  },
  "body": {
    "input": {
      "messages": [
        {
          "role": "user",
          "content": "[{\"role\": \"user\", \"parts\": [{\"type\": \"text\", \"content\": \"Hey, how can you help me\"}]}]"
        }
      ]
    },
    "output": {
      "messages": [
        {
          "role": "assistant",
          "content": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"I can assist you with planning your trips ...\"}]}]"
        }
      ]
    }
  }
}
```

#### OpenInference
<a name="openai-agents-examples-split-openinference"></a>

With the OpenInference library, the invoke agent (`AGENT`) span is an empty container. AgentCore Evaluations reconstructs the user prompt and agent response from the inference (`LLM`) span, whose content lives in a correlated event record.

**Example**  
The `openinference.span.kind` attribute (`AGENT`) identifies this as an invoke agent span. The span carries no conversation content.  

```
{
  "traceId": "6a387ee61078243c1cc455ed45c6c313",
  "spanId": "9a1c7dce81b692cd",
  "name": "openaiOInfTravel",
  "kind": "INTERNAL",
  "scope": {
    "name": "openinference.instrumentation.openai_agents",
    "version": "1.5.0"
  },
  "attributes": {
    "openinference.span.kind": "AGENT",
    "graph.node.id": "openaiOInfTravel",
    "llm.system": "openai",
    "session.id": "sea-nyc-trip-2-turns-openai-oi"
  },
  "status": {
    "code": "OK"
  }
}
```
The `openinference.span.kind` attribute (`TOOL`) identifies this as an execute tool span; `tool.name` holds the tool name. The tool arguments and result live in the correlated event record.  

```
{
  "traceId": "6a387ef07b8f4f3732fab45d3c0b51ff",
  "spanId": "b4e78cb0a06a6fe2",
  "name": "search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "openinference.instrumentation.openai_agents",
    "version": "1.5.0"
  },
  "attributes": {
    "openinference.span.kind": "TOOL",
    "tool.name": "search_flights",
    "input.mime_type": "application/json",
    "output.mime_type": "application/json",
    "session.id": "sea-nyc-trip-2-turns-openai-oi"
  },
  "status": {
    "code": "OK"
  }
}
```

```
{
  "spanId": "b4e78cb0a06a6fe2",
  "traceId": "6a387ef07b8f4f3732fab45d3c0b51ff",
  "scope": {
    "name": "openinference.instrumentation.openai_agents"
  },
  "body": {
    "input": {
      "messages": [
        { "role": "user", "content": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}" }
      ]
    },
    "output": {
      "messages": [
        { "role": "assistant", "content": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}" }
      ]
    }
  }
}
```
The `openinference.span.kind` attribute (`LLM`) identifies this as an inference span. Message roles and tool definitions are on the span attributes; the message content lives in the correlated event record. ADOT flattens the input roles to `user`, so AgentCore Evaluations uses the last plain-text input message as the user prompt. The output message is the OpenAI Response object, from which AgentCore Evaluations reads the response text.  

```
{
  "traceId": "6a387ee61078243c1cc455ed45c6c313",
  "spanId": "1221a062c7f90a8e",
  "name": "response",
  "kind": "INTERNAL",
  "scope": {
    "name": "openinference.instrumentation.openai_agents",
    "version": "1.5.0"
  },
  "attributes": {
    "openinference.span.kind": "LLM",
    "llm.model_name": "gpt-4o-mini-2024-07-18",
    "llm.input_messages.0.message.role": "system",
    "llm.input_messages.1.message.role": "user",
    "llm.output_messages.0.message.role": "assistant",
    "llm.tools.0.tool.json_schema": "{\"type\": \"function\", \"function\": {\"name\": \"search_flights\", ...}}",
    "session.id": "sea-nyc-trip-2-turns-openai-oi"
  },
  "status": {
    "code": "OK"
  }
}
```

```
{
  "spanId": "1221a062c7f90a8e",
  "traceId": "6a387ee61078243c1cc455ed45c6c313",
  "scope": {
    "name": "openinference.instrumentation.openai_agents"
  },
  "body": {
    "input": {
      "messages": [
        { "role": "user", "content": "[{\"content\": \"Hey, how can you help me\", \"role\": \"user\"}]" },
        { "role": "user", "content": "You are a travel planning assistant. Help users plan trips ..." },
        { "role": "user", "content": "Hey, how can you help me" }
      ]
    },
    "output": {
      "messages": [
        {
          "role": "assistant",
          "content": "{\"id\": \"resp_abc123...\", \"output\": [{\"type\": \"message\", \"content\": [{\"type\": \"output_text\", \"text\": \"I can assist you with planning your trips ...\"}]}]}"
        }
      ]
    }
  }
}
```

### Example spans in unified telemetry
<a name="openai-agents-examples-unified"></a>

With unified telemetry, the same content stays on the span attributes and no separate event record is produced. The following examples are from a Python OpenAI Agents travel-planning agent. The same agent is shown under each instrumentation library.

**Note**  
These examples are not complete spans. They show representative data from a real agent interaction, with some fields omitted and long values truncated for readability.

#### OpenTelemetry
<a name="openai-agents-examples-unified-otel"></a>

**Example**  
The `gen_ai.input.messages` attribute holds the user prompt, and the `gen_ai.output.messages` attribute holds the agent response. Both are OpenAI parts-format arrays.  

```
{
  "traceId": "6a4de7b85e61747e6b568a1f4768e89d",
  "spanId": "50656fd77904d125",
  "name": "invoke_agent openaiOtelTravel",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "invoke_agent",
    "gen_ai.agent.name": "openaiOtelTravel",
    "gen_ai.system": "openai",
    "gen_ai.input.messages": "[{\"role\": \"user\", \"parts\": [{\"type\": \"text\", \"content\": \"Hey, how can you help me\"}]}]",
    "gen_ai.output.messages": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"I can assist you with planning your trips ...\"}]}]",
    "session.id": "sea-nyc-trip-2-turns-unified"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.tool.call.arguments` attribute holds the tool arguments, and the `gen_ai.tool.call.result` attribute holds the tool result.  

```
{
  "traceId": "6a4de7c376913db82e6f0f336a16731d",
  "spanId": "8840e8e23724ebd7",
  "name": "execute_tool search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "execute_tool",
    "gen_ai.tool.name": "search_flights",
    "gen_ai.tool.call.arguments": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "gen_ai.tool.call.result": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns-unified"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`chat`) identifies this as an inference span. The model metadata and the `gen_ai.tool.definitions` attribute (the list of tools available to the agent) stay inline on the span.  

```
{
  "traceId": "6a4de7b85e61747e6b568a1f4768e89d",
  "spanId": "9b2c1e5f7a3d0846",
  "name": "openai.response",
  "kind": "INTERNAL",
  "scope": {
    "name": "opentelemetry.instrumentation.openai_agents",
    "version": "0.62.1"
  },
  "attributes": {
    "gen_ai.operation.name": "chat",
    "gen_ai.provider.name": "openai",
    "gen_ai.request.model": "gpt-4o-mini-2024-07-18",
    "gen_ai.response.model": "gpt-4o-mini-2024-07-18",
    "gen_ai.usage.input_tokens": 269,
    "gen_ai.usage.output_tokens": 78,
    "gen_ai.tool.definitions": "[{\"type\": \"function\", \"function\": {\"name\": \"search_flights\", \"description\": \"Search for available flights between cities.\", \"parameters\": { ... }}}]",
    "session.id": "sea-nyc-trip-2-turns-unified"
  },
  "status": {
    "code": "OK"
  }
}
```

#### OpenInference
<a name="openai-agents-examples-unified-openinference"></a>

**Example**  
The `input.value` attribute holds the tool arguments, and the `output.value` attribute holds the tool result.  

```
{
  "traceId": "6a387ef07b8f4f3732fab45d3c0b51ff",
  "spanId": "d5a1c9e70b46f312",
  "name": "search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "openinference.instrumentation.openai_agents",
    "version": "1.5.1"
  },
  "attributes": {
    "openinference.span.kind": "TOOL",
    "tool.name": "search_flights",
    "input.value": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "output.value": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns-oi"
  },
  "status": {
    "code": "OK"
  }
}
```
The message content is inline on the indexed attributes. The `llm.input_messages.*` attributes hold the system prompt and user prompt, and the `llm.output_messages.*` attributes hold the agent response. AgentCore Evaluations reconstructs the user prompt and agent response from this span and backfills the empty invoke agent (`AGENT`) span.  

```
{
  "traceId": "6a387ee61078243c1cc455ed45c6c313",
  "spanId": "c9f0a2b41d773e88",
  "name": "response",
  "kind": "INTERNAL",
  "scope": {
    "name": "openinference.instrumentation.openai_agents",
    "version": "1.5.1"
  },
  "attributes": {
    "openinference.span.kind": "LLM",
    "llm.model_name": "gpt-4o-mini-2024-07-18",
    "llm.input_messages.0.message.role": "system",
    "llm.input_messages.0.message.content": "You are a travel planning assistant ...",
    "llm.input_messages.1.message.role": "user",
    "llm.input_messages.1.message.content": "Hey, how can you help me",
    "llm.output_messages.0.message.role": "assistant",
    "llm.output_messages.0.message.contents.0.message_content.text": "I can assist you with planning your trips ...",
    "session.id": "sea-nyc-trip-2-turns-oi"
  },
  "status": {
    "code": "OK"
  }
}
```

## TypeScript agent support
<a name="openai-agents-typescript"></a>

A TypeScript OpenAI Agents agent emits the same span types, identifying attributes, and content layout as a Python agent, so the evaluation service reads it the same way. There are two TypeScript instrumentation libraries, each with its own scope name.

### Instrument your agent
<a name="openai-agents-typescript-instrument"></a>

Add the instrumentation library for the convention you want to your TypeScript dependencies. Use the latest available version unless you have a reason to pin.

**Example**  
For TypeScript agents on ADOT, add the AWS Distro Node autoinstrumentation package (`@aws/aws-distro-opentelemetry-node-autoinstrumentation`) to your dependencies. It includes the built-in OpenAI Agents instrumentation, which activates at startup and emits the scope name `@aws/aws-distro-opentelemetry-instrumentation-openai-agents`.  
 `package.json`:  

```
{
  "dependencies": {
    "@aws/aws-distro-opentelemetry-node-autoinstrumentation": "^0.12.0"
  }
}
```
Add `@arizeai/openinference-instrumentation-openai-agents` to your dependencies. The scope name emitted is `@arizeai/openinference-instrumentation-openai-agents`.  
 `package.json`:  

```
{
  "dependencies": {
    "@arizeai/openinference-instrumentation-openai-agents": "^0.2.2"
  }
}
```

**Note**  
Instrumentation is one step in setting up observability. To export telemetry for evaluation, complete the full setup in [Set up observability](supported-frameworks-telemetry.md#supported-frameworks-setup).

### How spans are identified
<a name="openai-agents-typescript-span-identification"></a>

Span identification is the same as for a Python agent. The ADOT-native OpenTelemetry library (from the AWS Distro Node autoinstrumentation package `@aws/aws-distro-opentelemetry-node-autoinstrumentation`, emitting the scope name `@aws/aws-distro-opentelemetry-instrumentation-openai-agents`) sets `gen_ai.operation.name`, and the OpenInference JS library (`@arizeai/openinference-instrumentation-openai-agents`) sets `openinference.span.kind`. For the values, see [How spans are identified](#openai-agents-span-identification) under [Python agent support](#openai-agents-python).

### How evaluation fields are extracted
<a name="openai-agents-typescript-extraction"></a>

Field extraction reads the same attributes as for a Python agent. Note that with the ADOT-native TypeScript library, the invoke agent span is a structural container: the user prompt and agent response are reconstructed from the inference (`chat`) span rather than the invoke agent span, unlike the Python OpenTelemetry library, which keeps them on the invoke agent span. For where each field is read from, see [How evaluation fields are extracted](#openai-agents-extraction) under [Python agent support](#openai-agents-python).

### Example spans from a TypeScript agent
<a name="openai-agents-examples-typescript"></a>

The following examples are from a TypeScript OpenAI Agents travel-planning agent deployed on Amazon Bedrock AgentCore Runtime with unified telemetry. The same agent is shown under each instrumentation library.

**Note**  
These examples are not complete spans. They show representative data from a real agent interaction, with some fields omitted and long values truncated for readability.

#### OpenTelemetry
<a name="openai-agents-examples-typescript-otel"></a>

With the ADOT-native library (from the AWS Distro Node autoinstrumentation package `@aws/aws-distro-opentelemetry-node-autoinstrumentation`, emitting the scope name `@aws/aws-distro-opentelemetry-instrumentation-openai-agents`), the invoke agent span is a structural container and the conversation content lives on the inference (`chat`) span, in the parts-format `gen_ai.input.messages` and `gen_ai.output.messages` attributes. AgentCore Evaluations reconstructs the user prompt and agent response from the inference span.

**Example**  
The `gen_ai.operation.name` attribute (`invoke_agent`) identifies this as an invoke agent span. The span carries the agent name and tool list but no conversation content.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "9a1c7dce81b692cd",
  "name": "invoke_agent openaiAdotTS",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-openai-agents",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "invoke_agent",
    "gen_ai.agent.name": "openaiAdotTS",
    "gen_ai.provider.name": "openai",
    "open_ai.agent.tools": "[\"search_flights\", \"book_flight\", \"search_hotels\", \"book_hotel\", \"search_activities\", \"book_activity\"]",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`execute_tool`) identifies this as an execute tool span; `gen_ai.tool.name` holds the tool name. The `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result` attributes hold the tool arguments and result.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "3cbc4ea5f73fef81",
  "name": "execute_tool search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-openai-agents",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "execute_tool",
    "gen_ai.tool.name": "search_flights",
    "gen_ai.tool.type": "function",
    "gen_ai.tool.call.arguments": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "gen_ai.tool.call.result": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `gen_ai.operation.name` attribute (`chat`) identifies this as an inference span. The `gen_ai.input.messages` and `gen_ai.output.messages` attributes hold the conversation in the parts-format, `gen_ai.system_instructions` holds the system prompt, and `gen_ai.tool.definitions` lists the tools available to the agent.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "7c1f9a2b4d6e8a03",
  "name": "chat gpt-4o-mini-2024-07-18",
  "kind": "INTERNAL",
  "scope": {
    "name": "@aws/aws-distro-opentelemetry-instrumentation-openai-agents",
    "version": "0.12.0"
  },
  "attributes": {
    "gen_ai.operation.name": "chat",
    "gen_ai.provider.name": "openai",
    "gen_ai.response.model": "gpt-4o-mini-2024-07-18",
    "gen_ai.input.messages": "[{\"role\": \"user\", \"parts\": [{\"type\": \"text\", \"content\": \"Hey, how can you help me\"}]}]",
    "gen_ai.output.messages": "[{\"role\": \"assistant\", \"parts\": [{\"type\": \"text\", \"content\": \"I can assist you with planning your trips ...\"}]}]",
    "gen_ai.system_instructions": "[{\"type\": \"text\", \"content\": \"You are a travel planning assistant ...\"}]",
    "gen_ai.tool.definitions": "[{\"type\": \"function\", \"name\": \"search_flights\", \"description\": \"Search for available flights between cities.\", ...}]",
    "gen_ai.usage.input_tokens": 422,
    "gen_ai.usage.output_tokens": 82,
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```

#### OpenInference
<a name="openai-agents-examples-typescript-openinference"></a>

With the OpenInference JS library, the invoke agent (`AGENT`) and turn (`CHAIN`) spans are empty containers. AgentCore Evaluations reconstructs the user prompt and agent response from the inference (`LLM`) span, whose messages are on the indexed `llm.input_messages.*` and `llm.output_messages.*` attributes.

**Example**  
The `openinference.span.kind` attribute (`AGENT`) identifies this as an invoke agent span. The span carries no conversation content.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "9a1c7dce81b692cd",
  "name": "openaiAgentsOInf",
  "kind": "INTERNAL",
  "scope": {
    "name": "@arizeai/openinference-instrumentation-openai-agents",
    "version": "0.2.2"
  },
  "attributes": {
    "openinference.span.kind": "AGENT",
    "graph.node.id": "openaiAgentsOInf",
    "llm.system": "openai",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `openinference.span.kind` attribute (`TOOL`) identifies this as an execute tool span; `tool.name` holds the tool name. The `input.value` and `output.value` attributes hold the tool arguments and result.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "b4e78cb0a06a6fe2",
  "name": "search_flights",
  "kind": "INTERNAL",
  "scope": {
    "name": "@arizeai/openinference-instrumentation-openai-agents",
    "version": "0.2.2"
  },
  "attributes": {
    "openinference.span.kind": "TOOL",
    "tool.name": "search_flights",
    "input.value": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"date\": \"2025-03-15\"}",
    "output.value": "{\"origin\": \"SEA\", \"destination\": \"NYC\", \"flights\": [ ... ]}",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```
The `openinference.span.kind` attribute (`LLM`) identifies this as an inference span. The `llm.input_messages.*` attributes hold the system prompt and user prompt, the `llm.output_messages.*` attributes hold the agent response, and the `llm.tools.*.tool.json_schema` attributes hold the tool definitions. AgentCore Evaluations reconstructs the user prompt and agent response from this span and backfills the empty invoke agent (`AGENT`) span.  

```
{
  "traceId": "6a6bc695459e41aa14a172bb41d3246d",
  "spanId": "1221a062c7f90a8e",
  "name": "response",
  "kind": "INTERNAL",
  "scope": {
    "name": "@arizeai/openinference-instrumentation-openai-agents",
    "version": "0.2.2"
  },
  "attributes": {
    "openinference.span.kind": "LLM",
    "llm.model_name": "gpt-4o-mini-2024-07-18",
    "llm.input_messages.0.message.role": "system",
    "llm.input_messages.0.message.content": "You are a travel planning assistant ...",
    "llm.input_messages.1.message.role": "user",
    "llm.input_messages.1.message.content": "Hey, how can you help me",
    "llm.output_messages.0.message.role": "assistant",
    "llm.output_messages.0.message.contents.0.message_content.text": "I can assist you with travel planning by ...",
    "llm.tools.0.tool.json_schema": "{\"type\": \"function\", \"function\": {\"name\": \"search_flights\", ...}}",
    "session.id": "sea-nyc-trip-2-turns"
  },
  "status": {
    "code": "OK"
  }
}
```