# Set up Claude Code with a bearer token

On this path, Claude Code sends OpenTelemetry (OTel) metrics directly to the Amazon CloudWatch
native OTLP metrics endpoint and authenticates with a bearer token (a CloudWatch metrics API key).
No OpenTelemetry collector is required. This is the fastest way for an individual developer
or a small team to get Claude Code metrics into the Coding Agent Insights
dashboards.

###### Important

Bearer tokens are long-term credentials. We recommend them only where short-term
AWS credentials are not feasible, such as developer laptops outside AWS. For the
security trade-offs and key rotation guidance, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md"). Organizations that
federate identity through corporate SSO should use the enterprise rollout with Claude
apps gateway instead. See [Set up Claude Code with the Claude apps gateway](coding-agents-claude-code-gateway.md "coding-agents-claude-code-gateway.md").

## Prerequisites

- Claude Code installed on the developer's machine.
- A working way for Claude Code to call a model for inference. This telemetry
  setup is independent of inference, so you can use either an Anthropic account
  (the default Claude Code provider) or Amazon Bedrock. To use Amazon Bedrock for inference, see
  [Claude Code on
  Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock "https://code.claude.com/docs/en/amazon-bedrock") in the Claude Code documentation.
- A CloudWatch metrics API key (bearer token), created from an IAM user that has
  CloudWatch metrics permissions. For the procedure that creates the IAM user and
  generates the key, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md").

## Configure the metrics exporter

Claude Code configures OpenTelemetry through environment variables. Set the following
variables in the shell that launches Claude Code (or in your shell profile) to enable
metrics, select the OTLP/HTTP protocol, and point the metrics exporter at the CloudWatch
metrics endpoint with your bearer token in the `Authorization` header.
Include the full `/v1/metrics` path.

```
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="https://monitoring.`region`.amazonaws.com/v1/metrics"
export OTEL_EXPORTER_OTLP_METRICS_HEADERS="Authorization=Bearer `YOUR_API_KEY`"
```

###### Note

Treat the bearer token as a secret. Avoid committing it to source control or shell
profiles that are shared or backed up insecurely. Rotate the key periodically as
described in [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md").

## Add identity and organizational attributes

The Coding Agent Insights dashboards group usage by developer, team, department, and
other organizational dimensions. Provide these as OTel _resource_
attributes through the `OTEL_RESOURCE_ATTRIBUTES` environment variable. Set
the values from your developer's identity and your organization's structure.

```
export OTEL_RESOURCE_ATTRIBUTES="\
user.id=`alias`,\
user.email=`developer@example.com`,\
user.name=`Jane Doe`,\
department=`engineering`,\
team.id=`platform`,\
cost_center=`cc-1234`,\
organization=`example-corp`,\
location=`us-seattle`,\
role=`software-engineer`,\
manager=`manager@example.com`"
```

###### Note

Setting these as resource attributes (rather than per-datapoint attributes)
matches the shape the dashboards expect, so you can group by
`@resource.team.id`, `@resource.department`, and similar
labels. Claude Code stamps metric-level dimensions such as `model` and
`type` on the metrics automatically.

## Verify and view

Run Claude Code to generate metrics, and then confirm the data reached CloudWatch.

###### To verify metrics

1. Run a Claude Code session that performs some work.
2. In the CloudWatch console, choose **GenAI Observability**,
   **Coding Agent Insights**, and then the Claude Code tab.
   Metrics typically appear within a few minutes.
3. Optionally, query the metrics directly with PromQL. For more information, see
   [PromQL querying](CloudWatch-PromQL-Querying.md "CloudWatch-PromQL-Querying.md").

For the complete, continually updated guidance, see the [Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock "https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock") on GitHub.
