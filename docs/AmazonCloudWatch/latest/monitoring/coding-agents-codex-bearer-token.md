# Set up OpenAI Codex with a bearer token

On this path, OpenAI Codex sends OpenTelemetry (OTel) metrics directly to the Amazon CloudWatch
native OTLP metrics endpoint and authenticates with a bearer token (a CloudWatch metrics API key).
No OpenTelemetry collector is required. This is the fastest way for an individual developer
or a small team to get Codex metrics into the Coding Agent Insights dashboards.

###### Important

Bearer tokens are long-term credentials. We recommend them only where short-term
AWS credentials are not feasible, such as developer laptops outside AWS. For the
security trade-offs and key rotation guidance, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md"). Organizations that
federate identity through corporate SSO should use the enterprise rollout instead. See
[Set up OpenAI Codex for an enterprise rollout](coding-agents-codex-enterprise.md "coding-agents-codex-enterprise.md").

## Prerequisites

- OpenAI Codex installed on the developer's machine.
- A working way for Codex to call a model for inference. This telemetry setup is
  independent of inference, so you can use either an OpenAI account (the default
  Codex provider) or Amazon Bedrock. To use Amazon Bedrock for inference, see [Amazon
  Bedrock](https://developers.openai.com/codex/amazon-bedrock "https://developers.openai.com/codex/amazon-bedrock") in the OpenAI Codex documentation.
- A CloudWatch metrics API key (bearer token), created from an IAM user that has
  CloudWatch metrics permissions. For the procedure that creates the IAM user and
  generates the key, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md "CloudWatch-OTLP-MetricsBearerTokenAuth.md").

## Configure the metrics exporter

Codex reads its configuration from `~/.codex/config.toml`. Add an
`[otel.metrics_exporter]` section that points at the CloudWatch metrics OTLP
endpoint and sends your bearer token in the `Authorization` header. Include
the full `/v1/metrics` path; Codex does not append it for you.

```
[otel]
environment = "production"

[otel.metrics_exporter]
otlp-http = { endpoint = "https://monitoring.`region`.amazonaws.com/v1/metrics", protocol = "binary", headers = { "Authorization" = "Bearer `YOUR_API_KEY`" } }
```

###### Note

Some Codex versions do not expand environment variables inside header values, so
the API key is shown inline. Treat `config.toml` as a secret: restrict
its file permissions (for example, `chmod 600 ~/.codex/config.toml`) and
do not commit it to source control.

## Add identity and organizational attributes

The Coding Agent Insights dashboards group usage by developer, team, department, and
other organizational dimensions. Provide these as OTel _resource_
attributes through the `OTEL_RESOURCE_ATTRIBUTES` environment variable in the
shell that launches Codex. Set the values from your developer's identity and your
organization's structure.

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
labels. Codex stamps metric-level dimensions such as `model` and
`token_type` on the metrics automatically.

## Verify and view

Run Codex for a few turns to generate metrics, and then confirm the data reached
CloudWatch.

###### To verify metrics

1. Run a Codex session that performs some work (for example, ask it to run a
   command and edit a file).
2. In the CloudWatch console, choose **GenAI Observability**,
   **Coding Agent Insights**, and then the Codex tab. Metrics
   typically appear within a few minutes.
3. Optionally, query the metrics directly with PromQL. For more information, see
   [PromQL querying](CloudWatch-PromQL-Querying.md "CloudWatch-PromQL-Querying.md").

For the complete, continually updated guidance, see the [guidance for Codex on Amazon Bedrock](https://github.com/openai-on-aws/guidance-codex "https://github.com/openai-on-aws/guidance-codex") on GitHub.
