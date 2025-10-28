# Generative AI observability

With Amazon CloudWatch, you can observe generative AI workloads, including [Amazon Bedrock AgentCore agents](https://aws.amazon.com/bedrock/agentcore/ "https://aws.amazon.com/bedrock/agentcore/"), and
gain insights into AI performance, health, and accuracy. CloudWatch provides pre-configured views
into latency, usage, and errors of your AI workloads, allowing you to detect issues faster
in components like models and agents. End-to-end prompt tracing helps you quickly identify
issues in components such as knowledge bases, tools, and models. CloudWatch's AI monitoring
capabilities are compatible with popular generative AI orchestration frameworks such
as [AWS Strands](https://strandsagents.com/latest/ "https://strandsagents.com/latest/"), LangChain, and
LangGraph, offering flexibility with your choice of framework.

CloudWatch generative AI observability enables you to:

- Assess AI application quality and accuracy at scale through automated monitoring, reducing manual review requirements by capturing model outputs, response quality metrics, and end-user interactions
- Monitor model invocations, Agents (managed, self-hosted, and third-party),
  knowledge bases, guardrails, and tools
- Progress from agent experimentation to production of innovative GenAI applications
  while ensuring superior quality, performance, and reliability. For more information,
  see [What is Amazon
  Bedrock AgentCore?](../../../bedrock-agentcore/latest/devguide/what-is-genesis.md "../../../bedrock-agentcore/latest/devguide/what-is-genesis.md")
- Identify source of errors quickly using end-to-end prompt tracing, curated
  metrics, and logs
- Troubleshoot issues across your entire GenAI application and underlying
  infrastructure, leveraging existing CloudWatch observability tools such as [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md"), [Alarms](AlarmThatSendsEmail.md "AlarmThatSendsEmail.md"), [Dashboards](CloudWatch_Dashboards.md "CloudWatch_Dashboards.md"), [Sensitive data protection](../logs/cloudwatch-logs-data-protection-policies.md "../logs/cloudwatch-logs-data-protection-policies.md"), and [Logs
  Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md")
- Access prompt traces while using Amazon Bedrock, and send structured traces of
  third-party models to CloudWatch using ADOT SDK. For information about adding
  observability to your Amazon Bedrock AgentCore agent or tool, see [Amazon Bedrock
  AgentCore](../../../bedrock-agentcore/latest/devguide/what-is-genesis.md "../../../bedrock-agentcore/latest/devguide/what-is-genesis.md")
  CloudWatch generative AI observability provides two pre-built capabilities:

###### Note

You can use the **Model Invocation** dashboard by using any models for inference in Amazon Bedrock.

- **Model Invocations** – Detailed metrics dashboard on model usage, token consumption, and a curated invocation logs table to view detailed input and output content of model inferences
- **Amazon Bedrock AgentCore agents** – Performance and decision metrics for primitives of Amazon Bedrock AgentCore such as Agents, Memory, Built-in Tools, Gateways, and Identity
  Key metrics available in these dashboards include:

- Total and average invocations
- Token usage (total, average per query, input, output)
- Latency (average, P90, P99)
- Error rates and throttling events
- Cost attribution by application, user role, or specific user

###### Topics

- [Model Invocations](model-invocations.md "model-invocations.md")
- [Amazon Bedrock AgentCore](AgentCore-Agents.md "AgentCore-Agents.md")
