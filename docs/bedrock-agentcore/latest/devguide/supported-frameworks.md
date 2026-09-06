# Supported agent frameworks

Amazon Bedrock AgentCore Evaluations evaluates agents built with several agent frameworks. What an agent emits as telemetry, and how that telemetry is structured, depends on the **agent framework** you build with and the **instrumentation library** you use to record it.

For each supported framework, this section describes:

- The instrumentation libraries you can use.
- How to instrument your agent.
- What the resulting spans and event records look like.
- How the evaluation service locates the values it needs, such as the user prompt, the agent response, and tool calls.
  AgentCore Evaluations supports the following frameworks and instrumentation libraries. Several frameworks are supported in both Python and TypeScript. The Python and TypeScript versions of a library emit different scope names, so each language has its own row. For a given framework and instrumentation library, the evaluation service extracts the same values from either language.

| Agent framework  | Instrumentation library                                                | Language   | Scope name                                                    | Recommended version                 |
| ---------------- | ---------------------------------------------------------------------- | ---------- | ------------------------------------------------------------- | ----------------------------------- |
| Strands Agents   | Built-in (Strands Agents SDK)                                          | Python     | `strands.telemetry.tracer`                                    | Latest                              |
| Strands Agents   | Built-in (Strands Agents SDK)                                          | TypeScript | `strands-agents`                                              | `@strands-agents/sdk`<br>`>= 1.5.0` |
| LangGraph        | OpenTelemetry (`opentelemetry-instrumentation-langchain`)              | Python     | `opentelemetry.instrumentation.langchain`                     | `>= 0.55.0`                         |
| LangGraph        | OpenInference (`openinference-instrumentation-langchain`)              | Python     | `openinference.instrumentation.langchain`                     | `>= 0.1.62`                         |
| LangGraph        | OpenTelemetry, ADOT-native                                             | TypeScript | `@aws/aws-distro-opentelemetry-instrumentation-langchain`     | `>= 0.12.0`                         |
| LangGraph        | OpenTelemetry (`@traceloop/instrumentation-langchain`)                 | TypeScript | `@traceloop/instrumentation-langchain`                        | `>= 0.27.0`                         |
| LangGraph        | OpenInference (`@arizeai/openinference-instrumentation-langchain`)     | TypeScript | `@arizeai/openinference-instrumentation-langchain`            | `>= 4.0.14`                         |
| OpenAI Agents    | OpenTelemetry (`opentelemetry-instrumentation-openai-agents`)          | Python     | `opentelemetry.instrumentation.openai_agents`                 | `>= 0.61.0`                         |
| OpenAI Agents    | OpenInference (`openinference-instrumentation-openai-agents`)          | Python     | `openinference.instrumentation.openai_agents`                 | `>= 1.5.0`                          |
| OpenAI Agents    | OpenTelemetry, ADOT-native                                             | TypeScript | `@aws/aws-distro-opentelemetry-instrumentation-openai-agents` | `>= 0.12.0`                         |
| OpenAI Agents    | OpenInference (`@arizeai/openinference-instrumentation-openai-agents`) | TypeScript | `@arizeai/openinference-instrumentation-openai-agents`        | `>= 0.2.2`                          |
| Vercel AI SDK    | OpenTelemetry, ADOT-native                                             | TypeScript | `@aws/aws-distro-opentelemetry-instrumentation-vercel-ai`     | `>= 0.12.0`                         |
| LlamaIndex       | OpenTelemetry (`opentelemetry-instrumentation-llamaindex`)             | Python     | `opentelemetry.instrumentation.llamaindex`                    | `>= 0.61.0`                         |
| LlamaIndex       | OpenInference (`openinference-instrumentation-llama-index`)            | Python     | `openinference.instrumentation.llama_index`                   | `>= 4.4.1`                          |
| Google ADK       | OpenInference (`openinference-instrumentation-google-adk`)             | Python     | `openinference.instrumentation.google_adk`                    | `>= 0.1.13`                         |
| Claude Agent SDK | OpenInference (`openinference-instrumentation-claude-agent-sdk`)       | Python     | `openinference.instrumentation.claude_agent_sdk`              | `>= 0.1.3`                          |

Each span your agent emits carries a **scope name**, which identifies the instrumentation library that produced it. The evaluation service reads this name to tell which library it is dealing with, and therefore whether it can process the span and which attributes to look for. The scope name is the value of the `scope.name` field on each span and event record.

The attribute names and the location of the conversation content differ by framework and instrumentation library. For the attributes and example spans of a single framework, see that framework’s page.

###### Note

Instrumenting your agent is only one part of producing telemetry that the evaluation service can read. Your agent must also have observability enabled, so that it exports its telemetry to Amazon CloudWatch.

For how AgentCore delivers that telemetry, where the service finds the values it needs, and the setup steps for your hosting option, see [Telemetry setup and delivery](supported-frameworks-telemetry.md "supported-frameworks-telemetry.md").

###### Topics

- [Set up Strands Agents telemetry for AgentCore Evaluations](supported-frameworks-strands.md "supported-frameworks-strands.md")
- [Set up LangGraph telemetry for AgentCore Evaluations](supported-frameworks-langgraph.md "supported-frameworks-langgraph.md")
- [OpenAI Agents](supported-frameworks-openai-agents.md "supported-frameworks-openai-agents.md")
- [Set up Vercel AI SDK telemetry for AgentCore Evaluations](supported-frameworks-vercel-ai.md "supported-frameworks-vercel-ai.md")
- [LlamaIndex](supported-frameworks-llamaindex.md "supported-frameworks-llamaindex.md")
- [Google ADK](supported-frameworks-google-adk.md "supported-frameworks-google-adk.md")
- [Claude Agent SDK](supported-frameworks-claude-agent-sdk.md "supported-frameworks-claude-agent-sdk.md")
- [Generic framework support](supported-frameworks-generic.md "supported-frameworks-generic.md")
