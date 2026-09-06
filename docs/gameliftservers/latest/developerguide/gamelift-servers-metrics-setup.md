

# Implementation
<a name="gamelift-servers-metrics-setup"></a>

Select your implementation path based on your development environment:

## SDK implementation
<a name="sdk-implementation"></a>


| SDK Type | SDK Setup | Custom Metrics | API Reference | 
| --- | --- | --- | --- | 
| Go SDK | [Complete Setup Guide](https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk/blob/main/telemetry-metrics/METRICS.md) | [Go Metrics API](https://github.com/amazon-gamelift/amazon-gamelift-servers-go-server-sdk/blob/main/telemetry-metrics/CUSTOM_METRICS.md) | [Go Actions and Data Types](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk-go-actions.html) | 
| C\# SDK | [Complete Setup Guide](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/blob/main/telemetry-metrics/METRICS.md) | [C\# Metrics API](https://github.com/amazon-gamelift/amazon-gamelift-servers-csharp-server-sdk/blob/main/telemetry-metrics/CUSTOM_METRICS.md) | [C\# Actions and Data Types](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-csharp-actions.html) | 
| C\+\+ SDK | [Complete Setup Guide](https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk/blob/main/telemetry-metrics/METRICS.md) | [C\+\+ Metrics API](https://github.com/amazon-gamelift/amazon-gamelift-servers-cpp-server-sdk/blob/main/telemetry-metrics/CUSTOM_METRICS.md) | [C\+\+ Actions and Data Types](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-cpp-actions.html) | 

## Plugin implementation
<a name="plugin-implementation"></a>


| Plugin | Plugin Setup | Custom Metrics | API Reference | 
| --- | --- | --- | --- | 
| Unreal | [Complete Setup Guide](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal/blob/main/TelemetryMetrics/METRICS.md) | [Unreal Metrics API](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unreal/blob/main/TelemetryMetrics/CUSTOM_METRICS.md) | [Unreal Actions and Data Types](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-unreal-actions.html) | 
| Unity | [Complete Setup Guide](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity/blob/main/TelemetryMetrics/METRICS.md) | [Unity Metrics API](https://github.com/amazon-gamelift/amazon-gamelift-plugin-unity/blob/main/TelemetryMetrics/CUSTOM_METRICS.md) | [C\# Actions and Data Types](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-csharp-actions.html) | 

## Implementation workflow
<a name="implementation-workflow"></a>

Each implementation follows a two-step process:

1. **Complete Setup Guide (METRICS.md)** — Infrastructure deployment, AWS infrastructure configuration, fleet setup, and Grafana dashboard configuration.

1. **API Implementation Guide (CUSTOM\_METRICS.md)** — Language-specific SDK usage, metric types, custom metrics creation, and advanced configuration.

### Verification
<a name="verification"></a>

1. Validate metrics flow by checking your [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) workspace or Amazon CloudWatch console for incoming telemetry data.

1. Check dashboard visibility in [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) using the pre-built dashboards.

1. Test custom metrics by verifying they appear in your monitoring dashboards.

**Note**  
After completing implementation, return to this page and go to the [Available metrics](gamelift-servers-metrics-types.md) page.