

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