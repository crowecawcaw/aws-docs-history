

# Getting started
<a name="AgentCore-GettingStarted"></a>

Amazon Bedrock AgentCore provides built-in metrics, logs, and traces to monitor the performance of your AgentCore modular services. You can view this data in Amazon CloudWatch. To access the full range of observability data from all AgentCore module services, instrument your code using the AWS Distro for OpenTelemetry (ADOT) SDK.

## Add observability to your agentic resources
<a name="add-observability-agentic-resources"></a>

Before you begin, enable CloudWatch Transaction Search. For more information, see [Enable Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html).

### Enable observability for AgentCore Runtime hosted agents
<a name="enable-observability-agentcore-runtime"></a>

You can host your agents on AgentCore Runtime, a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools. AgentCore Runtime supports any open-source framework including LangGraph, CrewAI, Strands Agents, any protocol, and any model.

To enable observability for AgentCore Runtime hosted agents, see [Configure custom observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-custom).

For a step-by-step tutorial, see [Enabling observability for AgentCore Runtime hosted agents](https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-agentcore-runtime-hosted-agents).

### Enable observability for non-AgentCore hosted agents
<a name="enable-observability-non-agentcore"></a>

You can host your agents outside of AgentCore and bring your observability data into CloudWatch for end-to-end monitoring in one location.

To enable observability for non-AgentCore Runtime hosted agents, see [Configure third-party observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-3p).

For a step-by-step tutorial, see [Enabling observability for non-AgentCore hosted agents](https://aws.github.io/bedrock-agentcore-starter-toolkit/user-guide/observability/quickstart.html#enabling-observability-for-non-agentcore-hosted-agents).

### Enable observability for AgentCore memory, gateway, and built-in tool resources
<a name="enable-observability-agentcore-resources"></a>

You can gain visibility into the metrics and traces of AgentCore modular services. For more information, see [Configure CloudWatch observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-cloudwatch).

### Enable AgentCore Evaluations
<a name="enable-observability-agentcore-evaluations"></a>

You can gain visibility into AgentCore Evaluations. AgentCore Evaluations provide capabilities to monitor and assess the performance, quality, and reliability of your AI agents. To enable observability for AgentCore Evaluations, see [ AgentCore evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html).