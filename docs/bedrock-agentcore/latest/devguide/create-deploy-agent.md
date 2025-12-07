# Create and deploy your agent

If you have an agent already up and running in AgentCore Runtime, you can skip the
following steps

###### Topics

- [Pick a supported framework](#supported-frameworks "#supported-frameworks")
- [Create and deploy your agent](#create-deploy-agent-steps "#create-deploy-agent-steps")

## Pick a supported framework

AgentCore Evaluations currently supports the following agentic frameworks and
instrumentation libraries

- Strands Agent
- LangGraph configured with one of the following instrumentation
  libraries
  - `opentelemetry-instrumentation-langchain`
  - `openinference-instrumentation-langchain`

## Create and deploy your agent

Create and deploy your agent by following the [Get Started guide for AgentCore
Runtime](../../../runtime-getting-started.md "../../../runtime-getting-started.md"). Setup observability using [Get started with AgentCore
Observability](../../../observability-get-started.md "../../../observability-get-started.md"). You can find additional examples in the [AgentCore Evaluations Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations "https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations").
