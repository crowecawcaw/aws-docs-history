# Getting started

Amazon Bedrock AgentCore provides built-in metrics, logs, and traces to monitor the performance of your AgentCore modular services. You can view this data
in Amazon CloudWatch. To access the full range of observability data from all AgentCore module services, instrument your code using the
AWS Distro for OpenTelemetry (ADOT) SDK.

## Add observability to your agentic resources

Before you begin, enable CloudWatch Transaction Search. For more information, see [Enable Transaction Search](Enable-TransactionSearch.md "Enable-TransactionSearch.md").

### Enable observability for AgentCore Runtime hosted agents

You can host your agents on AgentCore Runtime, a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools.
AgentCore Runtime supports any open-source framework including LangGraph, CrewAI, Strands Agents, any protocol, and any model.

To enable observability for AgentCore Runtime hosted agents, see [Configure custom observability](../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-custom "../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-custom").

For a step-by-step tutorial, see [Enabling observability for AgentCore Runtime hosted agents](https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-agentcore-runtime-hosted-agents "https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-agentcore-runtime-hosted-agents").

### Enable observability for non-AgentCore hosted agents

You can host your agents outside of AgentCore and bring your observability data into CloudWatch for end-to-end monitoring in one location.

To enable observability for non-AgentCore Runtime hosted agents, see [Configure third-party observability](../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-3p "../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-3p").

For a step-by-step tutorial, see [Enabling observability for non-AgentCore hosted agents](https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-non-agentcore-hosted-agents "https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-non-agentcore-hosted-agents").

### Enable observability for AgentCore memory, gateway, and built-in tool resources

You can gain visibility into the metrics and traces of AgentCore modular services. For more information, see [Configure CloudWatch observability](../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-cloudwatch "../../../bedrock-agentcore/latest/devguide/observability-configure.md#observability-configure-cloudwatch").

### Enable AgentCore Evaluations

You can gain visibility into AgentCore Evaluations. AgentCore Evaluations provide capabilities to monitor
and assess the performance, quality, and reliability of your AI agents. To enable observability for AgentCore
Evaluations, see [AgentCore evaluations](../../../bedrock-agentcore/latest/devguide/evaluations.md "../../../bedrock-agentcore/latest/devguide/evaluations.md").
