

# Amazon CloudWatch agent
<a name="CloudWatch-OTLPCloudWatchAgent"></a>

The CloudWatch agent is built on the OpenTelemetry Collector, so you can use it to receive OpenTelemetry data and send it to the CloudWatch OTLP endpoints. In most cases, this is the recommended way to send OpenTelemetry data to CloudWatch, because a single agent can also power curated experiences such as CloudWatch Application Signals and CloudWatch Enhanced Container Insights.

You can configure the agent to send OpenTelemetry data to the CloudWatch OTLP endpoints in two ways:
+ **Using the agent configuration file (recommended)** – Add an `opentelemetry` section to your CloudWatch agent configuration file and enable the `otlp` source. The agent receives OTLP metrics, logs, and traces and forwards each signal to the correct CloudWatch OTLP endpoint. The agent sets the endpoints, the Region, and request signing for you, so you do not specify endpoint URLs or a `sigv4auth` extension. For the fields you can set, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md).
+ **Appending an OpenTelemetry collector configuration in YAML (advanced)** – Supply an OpenTelemetry collector configuration in YAML and append it to the agent's own configuration. Use this approach when you need components or pipeline topologies that the agent configuration file does not expose.

**Note**  
Make sure Transaction Search is enabled before you send traces to the OTLP traces endpoint.

## Send OpenTelemetry data using the agent configuration file
<a name="CloudWatch-OTLPCloudWatchAgent-ConfigFile"></a>

Add an `opentelemetry` section to your CloudWatch agent configuration file and include the `otlp` source under `collect`. When the agent starts with this configuration, it listens for OTLP data and forwards the received metrics, logs, and traces to the CloudWatch OTLP endpoints. For the fields you can set and their defaults, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md).

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

For pipelines that the agent configuration file does not expose, you can append an OpenTelemetry collector configuration in YAML. Start the agent with your CloudWatch agent configuration file, then append the OpenTelemetry YAML file:

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -c file:/tmp/agent.json -s
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -c file:{{/tmp/otel.yaml}} -s
```

The agent merges the two configurations on startup and logs the resolved configuration. To avoid merge conflicts with pipelines that the agent creates automatically, add a custom suffix to each component and pipeline name in your OpenTelemetry YAML (for example, `otlphttp/cwagent`).

### Supported OpenTelemetry components
<a name="CloudWatch-OTLPCloudWatchAgent-Components"></a>

The following OpenTelemetry components are available for you to configure in your appended YAML configuration. Use the component type name shown here as the key in your YAML.


| Component type | Available components | 
| --- | --- | 
| Receivers | `otlp`, `prometheus`, `statsd`, `collectd`, `jmx`, `hostmetrics`, `filelog`, `tcplog`, `udplog`, `jaeger`, `zipkin`, `kafka`, `kubeletstats` | 
| Processors | `batch`, `memory_limiter`, `filter`, `attributes`, `resource`, `resourcedetection`, `metricstransform`, `transform`, `cumulativetodelta`, `deltatocumulative`, `deltatorate`, `groupbyattrs`, `groupbytrace`, `k8sattributes`, `metricsgeneration`, `metricstarttime`, `probabilistic_sampler`, `span`, `tail_sampling` | 
| Exporters | `otlphttp`, `awsemf`, `awscloudwatchlogs`, `awsxray`, `prometheusremotewrite`, `debug` | 
| Extensions | `sigv4auth`, `headers_setter`, `file_storage`, `health_check`, `pprof`, `zpages` | 

The CloudWatch agent only supports writing telemetry to AWS destinations.

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

## Example: send application metrics through the agent without a separate collector
<a name="CloudWatch-OTLPCloudWatchAgent-Example"></a>

This example shows how to send application metrics to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints through the CloudWatch agent, from an application that is instrumented with an OpenTelemetry SDK. Your application exports OTLP to the agent that runs alongside it, and the agent forwards the metrics to CloudWatch. You do not run a separate collector to do this.

**Important**  
Starting with agent version 1.300070.0, the CloudWatch agent receives OTLP from any OpenTelemetry SDK and forwards metrics, traces, and logs to the CloudWatch OTLP endpoints. The agent handles AWS SigV4 signing, the Region, and endpoint selection for you. Because of this, you no longer need to run a separate AWS Distro for OpenTelemetry (ADOT) or OpenTelemetry collector alongside the agent. This applies whether the agent runs on Amazon EC2, Amazon ECS (as a sidecar or a daemon), or Amazon EKS. Keep the ADOT SDK and auto-instrumentation that generates telemetry in your application. You remove only the standalone ADOT or OpenTelemetry collector that ran alongside the agent. If you configured OpenTelemetry metrics collection before this capability shipped, you likely have a redundant collector that you can now remove.

### Prerequisites
<a name="CloudWatch-OTLPCloudWatchAgent-Example-Prerequisites"></a>

Before you begin, make sure that you have the following:
+ CloudWatch agent version 1.300070.0 or later. Earlier versions do not support the agent's OTLP receiver.
**Note**  
The agent version in a Linux distribution's package repository might be older than the required version. For example, on Amazon Linux 2023, `dnf install amazon-cloudwatch-agent` installs version 1.300069.1, which is below the 1.300070.0 minimum and does not support the OTLP receiver. To get a qualifying version, install the RPM that matches your instance architecture:  
For x86\_64 instances, use `https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm`.
For arm64 instances, such as AWS Graviton, use `https://amazoncloudwatch-agent.s3.amazonaws.com/amazon_linux/arm64/latest/amazon-cloudwatch-agent.rpm`.
To verify the installed version, read `/opt/aws/amazon-cloudwatch-agent/bin/CWAGENT_VERSION`. If the repository version is older than 1.300070.0, install the agent from the CloudWatch agent download instead.
+ The permissions that the agent needs to send telemetry to the CloudWatch OTLP endpoints. The agent signs requests with its own credentials, and the `CloudWatchAgentServerPolicy` managed policy grants the permissions to send metrics, logs, and traces to these endpoints.
+ An application that is instrumented with an OpenTelemetry SDK or ADOT and exports OTLP to the agent over gRPC (port 4317) or HTTP (port 4318).

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

On Amazon ECS, run the CloudWatch agent as a sidecar container in the same task as your application, or as a daemon service on each container instance. When the agent runs as a sidecar, your application exports OTLP to `localhost` within the task (port 4317 for gRPC or port 4318 for HTTP). When the agent runs as a daemon service, your application exports OTLP to the agent on the host. In both cases, the agent forwards the metrics to the CloudWatch OTLP endpoints.

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