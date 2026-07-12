# Supported agent frameworks

Amazon Bedrock AgentCore Evaluations evaluates agents built with popular agent frameworks. What an agent emits as telemetry, and how that telemetry is structured, depends on the **agent framework** you build with and the **instrumentation library** you use to record it.

For each supported framework, this section describes:

- The instrumentation libraries you can use.
- How to instrument your agent.
- What the resulting spans and event records look like.
- How the evaluation service locates the values it needs, such as the user prompt, the agent response, and tool calls.
  AgentCore Evaluations supports the following frameworks and instrumentation libraries. It supports only the Python versions of these libraries.

| Agent framework  | Instrumentation library                                          | Scope name                                       | Recommended version |
| ---------------- | ---------------------------------------------------------------- | ------------------------------------------------ | ------------------- |
| Strands Agents   | Built-in (Strands Agents SDK)                                    | `strands.telemetry.tracer`                       | Latest              |
| LangGraph        | OpenTelemetry (`opentelemetry-instrumentation-langchain`)        | `opentelemetry.instrumentation.langchain`        | `>= 0.55.0`         |
| LangGraph        | OpenInference (`openinference-instrumentation-langchain`)        | `openinference.instrumentation.langchain`        | `>= 0.1.62`         |
| OpenAI Agents    | OpenTelemetry (`opentelemetry-instrumentation-openai-agents`)    | `opentelemetry.instrumentation.openai_agents`    | `>= 0.61.0`         |
| OpenAI Agents    | OpenInference (`openinference-instrumentation-openai-agents`)    | `openinference.instrumentation.openai_agents`    | `>= 1.5.0`          |
| LlamaIndex       | OpenTelemetry (`opentelemetry-instrumentation-llamaindex`)       | `opentelemetry.instrumentation.llamaindex`       | `>= 0.61.0`         |
| LlamaIndex       | OpenInference (`openinference-instrumentation-llama-index`)      | `openinference.instrumentation.llama_index`      | `>= 4.4.1`          |
| Google ADK       | OpenInference (`openinference-instrumentation-google-adk`)       | `openinference.instrumentation.google_adk`       | `>= 0.1.13`         |
| Claude Agent SDK | OpenInference (`openinference-instrumentation-claude-agent-sdk`) | `openinference.instrumentation.claude_agent_sdk` | `>= 0.1.3`          |

The **scope name** is the value of the `scope.name` field on each span and event record. The evaluation service uses it to determine whether it can process a span.

## How the service reads a session

Regardless of framework, the evaluation service reconstructs a session from two telemetry signals: **spans** and **event records**. It classifies each span by its type, then extracts content from it:

1. **Identify the span type** from framework-specific attributes. A span can be an **invoke agent span** (the top-level agent run), an **execute tool span** (a single tool call), or an **inference span** (a single model call).
2. **Extract the relevant values** from each span’s attributes or from its correlated event record. For example, the **user prompt** comes from the human (user-role) message in the agent input, and the **agent response** comes from the AI (assistant-role) message in the agent output.

The exact attribute names and content locations differ by framework and instrumentation library. The [Spans, event records, and telemetry signals](supported-frameworks-telemetry.md "supported-frameworks-telemetry.md") page explains the structure of spans and event records and where content lives. The per-framework pages describe the attributes and example data for each supported framework.

## Set up observability

Instrumenting your agent is one part of producing telemetry the evaluation service can read. Before evaluation works end to end, your agent must also have observability enabled and export its spans and event records to Amazon CloudWatch. Complete the following steps:

1. Enable CloudWatch Transaction Search, which is a prerequisite for evaluation. See [Enabling AgentCore observability](observability-configure.md#observability-configure-builtin "observability-configure.md#observability-configure-builtin").
2. Enable observability for your agent, based on where it is hosted:

   - For agents hosted on Amazon Bedrock AgentCore Runtime, see [Enabling observability in agent code for AgentCore-hosted agents](observability-configure.md#observability-configure-custom "observability-configure.md#observability-configure-custom").
   - For agents hosted on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), AWS Lambda, or other environments, see [Enabling observability for agents hosted outside of AgentCore](observability-configure.md#observability-configure-3p "observability-configure.md#observability-configure-3p").

## Sample agents

The following samples show Strands agents hosted outside Amazon Bedrock AgentCore Runtime, exporting telemetry to Amazon CloudWatch with ADOT. They focus on observability setup rather than the evaluation API. The samples use Strands, but the same hosting and telemetry-export pattern applies to other supported frameworks, such as LangGraph.

- **Amazon EKS:**
  [Observability for an EKS-hosted agent](https://github.com/awslabs/agentcore-samples/tree/main/06-workshops/06-AgentCore-observability/06-Agentcore-observability-for-eks-hosted-agent "https://github.com/awslabs/agentcore-samples/tree/main/06-workshops/06-AgentCore-observability/06-Agentcore-observability-for-eks-hosted-agent") and [Strands agent on Amazon EKS](https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-eks "https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-eks").
- **Amazon ECS:**
  [Strands agent on Amazon ECS](https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-ecs "https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-ecs").
- **AWS Lambda:**
  [Strands agent in AWS Lambda](https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-aws-lambda/02-agent-in-lambda "https://github.com/awslabs/agentcore-samples/tree/main/03-integrations/agents-hosted-outside-runtime/agents-on-aws-lambda/02-agent-in-lambda").

###### Topics
