

# Set up OpenTelemetry for GitHub Copilot
<a name="coding-agents-copilot"></a>

GitHub Copilot emits OpenTelemetry (OTel) metrics about token usage, requests, tool calls, and latency. When you send these metrics to Amazon CloudWatch, they populate the GitHub Copilot tab of the Coding Agent Insights dashboards. For more information about the dashboards, see [Coding Agent Insights](coding-agents-insights.md).

Copilot sends OTLP metrics directly to the CloudWatch native OTLP metrics endpoint and authenticates with a bearer token (a CloudWatch metrics API key). No OpenTelemetry collector is required. The bearer token is the supported path for Copilot today.

**Note**  
This guide covers only how to emit Copilot's OTel metrics to CloudWatch, which is independent of how Copilot calls a model for inference. Copilot uses its own models by default, but enterprises can bring their own model provider keys—including Amazon Bedrock. For more information, see [Use your own API keys](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys) in the GitHub Copilot documentation.

**Important**  
Bearer tokens are long-term credentials. We recommend them only where short-term AWS credentials are not feasible, such as developer laptops outside AWS. For the security trade-offs and key rotation guidance, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md).

## Prerequisites
<a name="coding-agents-copilot-prereqs"></a>
+ GitHub Copilot installed, on a version that supports OpenTelemetry metrics export.
+ An active GitHub Copilot subscription for model inference. Copilot uses its own models by default; to use Amazon Bedrock instead, configure a custom model key as described in [Use your own API keys](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/use-your-own-api-keys) in the GitHub Copilot documentation.
+ A CloudWatch metrics API key (bearer token), created from an IAM user that has CloudWatch metrics permissions. For the procedure that creates the IAM user and generates the key, see [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md).

## Configure the metrics exporter
<a name="coding-agents-copilot-configure"></a>

Configure Copilot's OpenTelemetry exporter to send metrics to the CloudWatch metrics endpoint with your bearer token in the `Authorization` header. Set the following environment variables in the environment that launches Copilot. Set `COPILOT_OTEL_ENABLED=true` to turn on OpenTelemetry. Copilot uses the standard OpenTelemetry variables for all signals; it does not support metrics-specific overrides. Set `OTEL_EXPORTER_OTLP_ENDPOINT` to the base endpoint *without* the `/v1/metrics` path — the exporter appends the signal path for you.

```
export COPILOT_OTEL_ENABLED=true
export OTEL_EXPORTER_OTLP_ENDPOINT="https://monitoring.{{region}}.amazonaws.com"
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer {{YOUR_API_KEY}}"
```

**Note**  
Treat the bearer token as a secret. Avoid committing it to source control or to shared shell profiles, and rotate the key periodically as described in [Setting up bearer token authentication for Metrics](CloudWatch-OTLP-MetricsBearerTokenAuth.md).

## Add identity and organizational attributes
<a name="coding-agents-copilot-attributes"></a>

The Coding Agent Insights dashboards group usage by developer, team, department, and other organizational dimensions. Provide these as OTel *resource* attributes through the `OTEL_RESOURCE_ATTRIBUTES` environment variable. Set the values from your developer's identity and your organization's structure.

```
export OTEL_RESOURCE_ATTRIBUTES="\
user.id={{alias}},\
user.email={{developer@example.com}},\
user.name={{Jane Doe}},\
department={{engineering}},\
team.id={{platform}},\
cost_center={{cc-1234}},\
organization={{example-corp}},\
location={{us-seattle}},\
role={{software-engineer}},\
manager={{manager@example.com}}"
```

## Verify and view
<a name="coding-agents-copilot-verify"></a>

Use Copilot to generate metrics, and then confirm the data reached CloudWatch.

**To verify metrics**

1. Use Copilot to perform some work that generates telemetry.

1. In the CloudWatch console, choose **GenAI Observability**, **Coding Agent Insights**, and then the GitHub Copilot tab. Metrics typically appear within a few minutes.

1. Optionally, query the metrics directly with PromQL. For more information, see [PromQL querying](CloudWatch-PromQL-Querying.md).