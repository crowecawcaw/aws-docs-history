# Spans, event records, and telemetry signals

Amazon Bedrock AgentCore Evaluations processes two telemetry signals to understand your agent’s behavior:

- **Spans** describe individual operations. A span carries metadata about an operation: its name, scope, timestamps, and attributes. A span might also carry the conversation content, or that content might live in a separate event record.
- **Event records** carry payload content in a `body` field: the inputs and outputs of models, tools, and the agent. An event record is correlated to its span by a shared `traceId` and `spanId`. Event records follow the OpenTelemetry events convention. For more information, see [References](#supported-frameworks-telemetry-references "#supported-frameworks-telemetry-references").
  To evaluate a session, the service needs both the spans and, where applicable, their correlated event records. For each span, the service does the following:

1. Identifies the span’s type from framework-specific attributes. For details, see the per-framework pages.
2. Reads the values it needs, such as the user prompt, the agent response, and tool inputs and outputs. These values come from the span’s attributes or from its correlated event record.

**Topics**

- [How ADOT splits telemetry](#supported-frameworks-telemetry-collection "#supported-frameworks-telemetry-collection")
- [Where spans and event records are stored](#supported-frameworks-telemetry-location "#supported-frameworks-telemetry-location")
- [Where the service reads content](#supported-frameworks-telemetry-extraction "#supported-frameworks-telemetry-extraction")
- [References](#supported-frameworks-telemetry-references "#supported-frameworks-telemetry-references")

## How ADOT splits telemetry

When your agent runs with the AWS Distro for OpenTelemetry (ADOT), telemetry is **split**. As spans are exported, ADOT extracts the large conversation content (model prompts and completions, tool inputs and outputs) out of the span attributes and emits it as separate **event records**. The resulting span carries only metadata and small attributes.

This split keeps span documents small, although it preserves the full conversation content in event records.

```
                          ADOT collection (split)

   Instrumented agent
          |
          |  span with attributes + content
          v
   +--------------------+
   |       ADOT         |  extracts conversation content
   +--------------------+
          |                          |
          | span                     | event record(s)
          | (metadata, attributes)   | (body: input / output messages)
          v                          v
   +--------------------+   +-----------------------+
   |  aws/spans         |   |  event-record         |
   |  log group         |   |  log group            |
   +--------------------+   +-----------------------+
          |                          |
          +-----------+--------------+
                      v
            Evaluation service
       (joins span + event record by traceId / spanId)
```

After the split, the conversation content lives in the event record `body` (for example, `body.input.messages` and `body.output.messages`), and the span carries the identifying attributes used to classify it.

## Where spans and event records are stored

When ADOT collects telemetry, it exports spans and event records to Amazon CloudWatch, but to **different** locations.

- **Spans** are stored in the `aws/spans` log group. This log group is created when **Transaction Search** is enabled, which is a prerequisite for evaluation. For details on enabling Transaction Search, see [AgentCore Observability](observability-telemetry.md "observability-telemetry.md").
- **Event records** are stored in a log group that depends on where your agent is hosted:

  - **On Amazon Bedrock AgentCore Runtime**: the Runtime emits event records to its log group, `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>`, in the `otel-rt-logs` log stream, and configures this export for you.
  - **Hosted outside AgentCore Runtime** (for example, on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), or AWS Lambda): your agent emits event records to the log group you configure through the `OTEL_EXPORTER_OTLP_LOGS_HEADERS` environment variable.

To evaluate a session, the service reads spans from `aws/spans` and joins them with their correlated event records from the appropriate log group.

## Where the service reads content

Conversation content can live in different places, depending on the framework and instrumentation library. The evaluation service reads it from whichever location holds it:

- **Event record body**: when ADOT splits the content into a separate event record (described above), the service reads it from the event record `body` correlated to the span.
- **Span attributes**: some instrumentation libraries keep the content on the span as attributes.
- **Inline span events**: some instrumentation libraries attach the content to the span as inline events.

The identifying attributes used to classify a span always remain on the span in every case. This includes the attribute that marks a span as an invoke agent span or an execute tool span. Only the location of the larger conversation content differs. The per-framework pages list both the identifying attributes and the content locations for each instrumentation library.

## References

These OpenTelemetry specifications describe the conventions that AgentCore Evaluations builds on:

- [Trace semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/trace/ "https://opentelemetry.io/docs/specs/semconv/general/trace/"): the structure and semantics of spans and traces.
- [Event semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/events/ "https://opentelemetry.io/docs/specs/semconv/general/events/"): the structure and semantics of event records.
- [Generative-AI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai "https://github.com/open-telemetry/semantic-conventions-genai"): the `gen_ai.*` attributes used to describe agent, model, and tool operations.
