# Monitor with server telemetry metrics

Amazon GameLift Servers can be configured to collect and publish telemetry metrics for game servers running on managed Amazon EC2 and Container fleets. These metrics become available after deploying the telemetry collector with your server build. The metrics system supports all SDKs (C++, C#, Go), all plugins (Unreal, Unity), and the Amazon GameLift Servers Game Server Wrapper. Metrics data flows to [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md"), [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"), and [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md") dashboards (recommended for visualization).

![telemetry_metrics](images/telemetry_metrics.png)

Monitor performance across your game servers using pre-built dashboards in Amazon Managed Grafana or Amazon CloudWatch.

## Benefits of telemetry metrics

The telemetry metrics system offers five key benefits:

- **Game engine-specific metrics** — Game engine plugins (Unreal, Unity) provide native integration with engine-specific performance metrics such as server tick time, frame rate, and engine-level resource utilization that are critical for game performance optimization.
- **Custom metrics support** — Define and track your own game-specific metrics using server SDK function calls to monitor custom gameplay events, business logic performance, and application-specific data points that matter to your game.
- **Automated collection** — Metrics flow automatically after telemetry collector deployment with no additional instrumentation required and direct integration with [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md") and Amazon CloudWatch.
- **Multi-level monitoring** — Fleet-level metrics for capacity and scaling, instance-level metrics for resource utilization, and game session metrics for performance tracking.
- **Universal compatibility** — Works with all Amazon GameLift Servers-supported development environments, integrated with all server SDKs, and native support in game engine plugins.

###### Note

Telemetry metrics are available for Amazon GameLift Servers managed Amazon EC2 or container fleets running Amazon Linux 2023 or Windows.

## Before you begin

### Required AWS resources

- AWS account configured for Amazon GameLift Servers.
- Managed fleet running on:
  - Amazon EC2 with supported operating systems, OR
  - Containers with Amazon Linux 2023

- Appropriate IAM permissions

### IAM requirements

The following IAM permissions are required only if you plan to use the corresponding service:

- **[Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md")** (required only if publishing metrics to Prometheus)
  - `aps:RemoteWrite` permission
  - Access to your Prometheus workspace

- **Amazon CloudWatch** (required only if publishing metrics to Amazon CloudWatch)
  - `cloudwatch:PutMetricData` permission
  - Access to metrics namespaces

- **[Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md")** (required only if using Grafana dashboards)
  - `grafana:Read` permission
  - SSO configuration for dashboard access
