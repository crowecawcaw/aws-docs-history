# Set up OpenTelemetry for OpenAI Codex

OpenAI Codex emits OpenTelemetry (OTel) metrics about token usage, per-turn latency, API
requests, tool calls, and approvals. When you send these metrics to Amazon CloudWatch, they populate
the Codex tab of the Coding Agent Insights dashboards. For more information about the
dashboards, see [Coding Agent Insights](coding-agents-insights.md "coding-agents-insights.md").

Codex configures its metrics exporter through the `[otel]` section of its
`config.toml` file. Two setup paths are available, depending on how your
developers run Codex.

## Choose a setup path

- **Bearer token** — Codex sends OTLP metrics
  directly to the CloudWatch native OTLP endpoint, authenticating with an
  `Authorization: Bearer` header. Identity and organizational
  attributes are supplied through the `OTEL_RESOURCE_ATTRIBUTES`
  environment variable. This path needs no collector and is the fastest way for an
  individual developer or a small team to get started. See [Set up OpenAI Codex with a bearer token](coding-agents-codex-bearer-token.md "coding-agents-codex-bearer-token.md").
- **Enterprise rollout** — For organizations
  that federate developer identity through corporate single sign-on (SSO) such as
  Okta, Microsoft Entra ID, Auth0, or AWS IAM Identity Center, centralize
  Amazon Bedrock access, and distribute a standard configuration to a fleet of
  developers. Identity and organizational attributes are derived from your
  identity provider (IdP). See [Set up OpenAI Codex for an enterprise rollout](coding-agents-codex-enterprise.md "coding-agents-codex-enterprise.md").

###### Note

The bearer token path configures only how Codex sends
_telemetry_ to CloudWatch; it is independent of how Codex calls a model
for _inference_, so you can use it with any model provider. The
enterprise rollout, in contrast, is built around centralized Amazon Bedrock access, so
Amazon Bedrock is the inference backend for that path. To use Amazon Bedrock for inference with
Codex, see [Amazon
Bedrock](https://developers.openai.com/codex/amazon-bedrock "https://developers.openai.com/codex/amazon-bedrock") in the OpenAI Codex documentation.

For the complete, continually updated guidance, including deployment templates and
setup scripts, see the [guidance for Codex on Amazon Bedrock](https://github.com/openai-on-aws/guidance-codex "https://github.com/openai-on-aws/guidance-codex") on GitHub.

###### Topics

- [Set up OpenAI Codex with a bearer token](coding-agents-codex-bearer-token.md "coding-agents-codex-bearer-token.md")
- [Set up OpenAI Codex for an enterprise rollout](coding-agents-codex-enterprise.md "coding-agents-codex-enterprise.md")
