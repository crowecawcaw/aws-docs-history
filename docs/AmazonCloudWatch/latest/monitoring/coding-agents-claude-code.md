# Set up OpenTelemetry for Claude Code

Claude Code emits OpenTelemetry (OTel) metrics about token usage, sessions, code edits,
tool calls, and cost. When you send these metrics to Amazon CloudWatch, they populate the Claude Code
tab of the Coding Agent Insights dashboards. For more information about the dashboards, see
[Coding Agent Insights](coding-agents-insights.md "coding-agents-insights.md").

Claude Code configures its OTel exporter through environment variables. Two setup paths
are available, depending on how your developers run Claude Code.

## Choose a setup path

- **Bearer token** — Claude Code sends OTLP
  metrics directly to the CloudWatch native OTLP endpoint, authenticating with an
  `Authorization: Bearer` header. Identity and organizational
  attributes are supplied through the `OTEL_RESOURCE_ATTRIBUTES`
  environment variable. This path needs no collector and is the fastest way for an
  individual developer or a small team to get started. See [Set up Claude Code with a bearer token](coding-agents-claude-code-bearer-token.md "coding-agents-claude-code-bearer-token.md").
- **Enterprise rollout with Claude apps gateway**
  — For organizations that need centralized control over developer access,
  identity federation, and telemetry collection. Deploy a self-hosted gateway that
  sits between your developers' Claude Code clients and your model provider.
  Developers sign in with your corporate IdP instead of holding API keys or cloud
  credentials. The gateway holds the upstream credential, enforces model access
  and managed settings by IdP group, and relays usage telemetry to your
  observability stack. Supports Amazon Bedrock, Claude Platform on AWS, Google Cloud,
  and Microsoft Foundry as upstreams. See [Set up Claude Code with the Claude apps gateway](coding-agents-claude-code-gateway.md "coding-agents-claude-code-gateway.md").

###### Note

The bearer token path configures only how Claude Code sends
_telemetry_ to CloudWatch; it is independent of how Claude Code calls a
model for _inference_, so you can use it with any model provider.
The enterprise rollout with Claude apps gateway combines telemetry configuration
with centralized inference access and supports multiple backends including
Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry.

For the complete, continually updated guidance, including deployment templates and
setup scripts, see the [Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock "https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock") on GitHub.

###### Topics

- [Set up Claude Code with a bearer token](coding-agents-claude-code-bearer-token.md "coding-agents-claude-code-bearer-token.md")
- [Set up Claude Code with the Claude apps gateway](coding-agents-claude-code-gateway.md "coding-agents-claude-code-gateway.md")
