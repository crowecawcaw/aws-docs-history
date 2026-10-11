

# Amazon CloudWatch agent
<a name="CloudWatch-OTLPCloudWatchAgent"></a>

The CloudWatch agent is built on the OpenTelemetry Collector, so you can use it to receive OpenTelemetry data and send it to the CloudWatch OTLP endpoints. In most cases, this is the recommended way to send OpenTelemetry data to CloudWatch, because a single agent can also power curated experiences such as CloudWatch Application Signals and CloudWatch Enhanced Container Insights. For more information about installing the agent, see [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md).

You can configure the agent to send OpenTelemetry data to the CloudWatch OTLP endpoints in two ways:
+ **Using the agent configuration file (recommended)** – Add an `opentelemetry` section to your CloudWatch agent configuration file and enable the `otlp` source. The agent receives OTLP metrics, logs, and traces and forwards each signal to the correct CloudWatch OTLP endpoint. The agent sets the endpoints, the Region, and request signing for you, so you do not specify endpoint URLs or a `sigv4auth` extension. For the fields you can set, see [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-Details.md#CloudWatch-Agent-Configuration-File-OpenTelemetrysection).
+ **Appending an OpenTelemetry collector configuration in YAML (advanced)** – Supply an OpenTelemetry collector configuration in YAML and append it to the agent's own configuration. Use this approach when you need components or pipeline topologies that the agent configuration file does not expose.

## Send OpenTelemetry data using the agent configuration file
<a name="CloudWatch-OTLPCloudWatchAgent-ConfigFile"></a>

Add an `opentelemetry` section to your CloudWatch agent configuration file and include the `otlp` source under `collect`. When the agent starts with this configuration, it listens for OTLP data and forwards the received metrics, logs, and traces to the CloudWatch OTLP endpoints. For the fields you can set, their defaults, and the minimum agent version, see [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-Details.md#CloudWatch-Agent-Configuration-File-OpenTelemetrysection).

The following example configures the agent to receive OTLP data over gRPC and HTTP.

```
{
  "opentelemetry": {
    "collect": {
      "otlp": {
        "grpc_endpoint": "0.0.0.0:4317",
        "http_endpoint": "0.0.0.0:4318"
      }
    }
  }
}
```

Start the agent with this configuration the same way as any other agent configuration file.

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -c file:/tmp/agent.json -s
```

**Note**  
The agent signs requests to the CloudWatch OTLP endpoints with its own credentials. The `CloudWatchAgentServerPolicy` managed policy grants the permissions the agent needs to send metrics, logs, and traces to these endpoints.

## Append an OpenTelemetry collector configuration in YAML
<a name="CloudWatch-OTLPCloudWatchAgent-YAML"></a>

For pipelines that the agent configuration file does not expose, you can append an OpenTelemetry collector configuration in YAML. For the append procedure and the OpenTelemetry components that the agent supports, see [Appending OpenTelemetry collector configuration files](CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-appending-OpenTelemetry-config-files). The following examples show the YAML to append for each signal.

### Configuration examples
<a name="CloudWatch-OTLPCloudWatchAgent-Examples"></a>

The following examples send each signal to the corresponding CloudWatch OTLP endpoint using the `otlphttp` exporter and the `sigv4auth` extension. Each component and pipeline name uses a `/cwagent` suffix to avoid conflicts with pipelines that the agent creates automatically. Replace {{region}} with your AWS Region.

**Metrics**

```
receivers:
  otlp/cwagent:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch/cwagent: {}
exporters:
  otlphttp/cwagent:
    metrics_endpoint: https://monitoring.{{region}}.amazonaws.com/v1/metrics
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "{{region}}"
    service: "monitoring"
service:
  extensions: [sigv4auth/cwagent]
  pipelines:
    metrics/cwagent:
      receivers: [otlp/cwagent]
      processors: [batch/cwagent]
      exporters: [otlphttp/cwagent]
```

**Logs**

```
receivers:
  otlp/cwagent:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
exporters:
  otlphttp/cwagent:
    logs_endpoint: https://logs.{{region}}.amazonaws.com/v1/logs
    headers:
      x-aws-log-group: {{my-log-group}}
      x-aws-log-stream: default
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "{{region}}"
    service: "logs"
service:
  extensions: [sigv4auth/cwagent]
  pipelines:
    logs/cwagent:
      receivers: [otlp/cwagent]
      exporters: [otlphttp/cwagent]
```

**Traces**

```
receivers:
  otlp/cwagent:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
exporters:
  otlphttp/cwagent:
    traces_endpoint: https://xray.{{region}}.amazonaws.com/v1/traces
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "{{region}}"
    service: "xray"
service:
  extensions: [sigv4auth/cwagent]
  pipelines:
    traces/cwagent:
      receivers: [otlp/cwagent]
      exporters: [otlphttp/cwagent]
```

## Example: send application metrics through the CloudWatch agent
<a name="CloudWatch-OTLPCloudWatchAgent-Example"></a>

This example sends application metrics through the CloudWatch agent to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints. Instrument your application with an OpenTelemetry SDK and export OTLP to the agent that runs alongside it. The agent forwards the metrics to CloudWatch.

**You might no longer need a separate collector**  
If you set up OpenTelemetry metrics collection before the agent's OTLP receiver was available, you might be running a standalone ADOT or OpenTelemetry collector alongside the agent that you no longer need. After you upgrade to agent version 1.300070.0 or later, you can remove that collector. The agent handles AWS SigV4 signing, Region, and endpoint selection, so you no longer need to configure them in a collector. Keep the ADOT SDK and auto-instrumentation that generate telemetry in your application. For more information about configuring the agent's OTLP receiver, see [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-Details.md#CloudWatch-Agent-Configuration-File-OpenTelemetrysection).

### Prerequisites
<a name="CloudWatch-OTLPCloudWatchAgent-Example-Prerequisites"></a>

Before you begin, complete the following prerequisites:
+ Install CloudWatch agent version 1.300070.0 or later. Earlier versions do not support the agent's OTLP receiver. Some Linux package repositories offer an earlier version, so check the installed version before you continue. For more information, see [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-Details.md#CloudWatch-Agent-Configuration-File-OpenTelemetrysection).
+ Attach the `CloudWatchAgentServerPolicy` managed policy, which grants the agent permission to send metrics, logs, and traces to the CloudWatch OTLP endpoints. The agent signs these requests with its own credentials.
+ Instrument your application with an OpenTelemetry SDK or ADOT, and configure the application to export OTLP to the agent over gRPC (port 4317) or HTTP (port 4318).

### Common steps
<a name="CloudWatch-OTLPCloudWatchAgent-Example-Flow"></a>

The following steps are the same regardless of where the agent runs.

1. Configure the agent to receive OTLP data. Add an `opentelemetry` section to your CloudWatch agent configuration file and enable the `otlp` source, as shown in [Send OpenTelemetry data using the agent configuration file](#CloudWatch-OTLPCloudWatchAgent-ConfigFile). The agent forwards the received metrics to the CloudWatch OTLP endpoints.

1. Point your application's OTLP exporter at the local agent instead of the public CloudWatch endpoint (for example, `http://localhost:4318`). The agent forwards the metrics for you. The following Python example uses the OpenTelemetry SDK to export metrics to the agent.

   ```
   from opentelemetry import metrics
   from opentelemetry.sdk.metrics import MeterProvider
   from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
   from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
   
   # Point at the local CloudWatch agent, which forwards to CloudWatch
   exporter = OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics")
   reader = PeriodicExportingMetricReader(exporter, export_interval_millis=60000)
   provider = MeterProvider(metric_readers=[reader])
   metrics.set_meter_provider(provider)
   
   # Create and record a metric
   meter = metrics.get_meter("my-app")
   counter = meter.create_counter("http_requests_total", description="Total HTTP requests")
   counter.add(1, {"method": "GET", "path": "/api/users", "status": "200"})
   ```

1. Verify that your metrics are arriving. Open the CloudWatch console, navigate to **Query Studio**, and run a PromQL query for your metric. For more information, see [Verify metrics are arriving](metrics-otel-send.md#metrics-otel-send-verify) and [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md).

### Amazon EC2
<a name="CloudWatch-OTLPCloudWatchAgent-Example-EC2"></a>

Run the CloudWatch agent on the Amazon EC2 instance, and configure your application to export OTLP to the agent on the same instance. Set the application's OTLP exporter endpoint to `http://localhost:4317` for gRPC or `http://localhost:4318` for HTTP. The agent forwards the metrics to the CloudWatch OTLP endpoints.

### Amazon ECS
<a name="CloudWatch-OTLPCloudWatchAgent-Example-ECS"></a>

On Amazon ECS, run the CloudWatch agent as a sidecar container in the same task as your application. You can also run the agent as a daemon service on each container instance. When the agent runs as a sidecar, your application exports OTLP to `localhost` within the task (port 4317 for gRPC or port 4318 for HTTP). When the agent runs as a daemon service, your application exports OTLP to the agent on the host. In both cases, the agent forwards the metrics to the CloudWatch OTLP endpoints.

### Amazon EKS
<a name="CloudWatch-OTLPCloudWatchAgent-Example-EKS"></a>

On Amazon EKS, install or upgrade the CloudWatch Observability EKS add-on to version 6.6.0 or later. The add-on runs the CloudWatch agent in your cluster. Earlier versions do not expose the OTLP ports on the agent Service.

You must also supply the agent `opentelemetry` and `otlp` configuration to the add-on through its configuration values. The add-on does not enable the OTLP receiver by default. Supply the following configuration values to the add-on.

```
{
  "agent": {
    "config": {
      "opentelemetry": {
        "collect": {
          "otlp": {
            "grpc_endpoint": "0.0.0.0:4317",
            "http_endpoint": "0.0.0.0:4318"
          }
        }
      }
    }
  }
}
```

After the add-on rolls out, the `cloudwatch-agent` Service exposes ports 4317 and 4318. Your application pods export OTLP to the agent Service, and the agent forwards the metrics to the CloudWatch OTLP endpoints.

**Warning**  
When you supply `agent.config`, the add-on replaces its default agent configuration rather than merging with it. A configuration that contains only the `opentelemetry` section removes the Application Signals ports (4315, 4316, and 2000) and the `cwa-server` port (4311) from the Service. If you also use Application Signals or Container Insights, include those settings in the configuration that you supply so that you do not lose them.