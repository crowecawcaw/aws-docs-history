

# OpenTelemetry Protocol (OTLP) Endpoint
<a name="xray-opentelemetry"></a>

OpenTelemetry is an open-source observability framework that provides IT teams with standardized protocols and tools for collecting and routing telemetry data. It delivers a unified format for instrumenting, generating, gathering, and exporting application telemetry data, such as metrics, logs, and traces to monitoring platforms for analysis and insights. By using OpenTelemetry, teams can avoid vendor lock-in, ensuring flexibility in their observability solutions.

You can use OpenTelemetry to directly send traces to an OpenTelemetry Protocol (OTLP) endpoint, and get out-of-the box application performance monitoring experiences in [CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Intro.html).

For more information, see [OpenTelemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html).

The OTLP traces endpoint (`https://xray.{{region}}.amazonaws.com/v1/traces`) supports two authentication methods:
+ **AWS Signature Version 4 (SigV4)** – Recommended. Uses short-term credentials, for example from an IAM role.
+ **Bearer token (API key)** – For workloads that can't use the AWS SDK or short-term credentials. For more information, see [Setting up bearer token authentication for traces](xray-opentelemetry-bearer-token.md).