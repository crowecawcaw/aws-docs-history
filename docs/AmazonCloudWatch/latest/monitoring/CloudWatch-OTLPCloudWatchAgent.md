# Amazon CloudWatch agent

The CloudWatch agent is built on the OpenTelemetry Collector, so you can use it to receive
OpenTelemetry data and send it to the CloudWatch OTLP endpoints. For most customers, this is the
recommended way to send OpenTelemetry telemetry to CloudWatch, because a single agent can also power
curated experiences such as CloudWatch Application Signals and CloudWatch Enhanced Container Insights.

To send OpenTelemetry data through the agent today, you supply an OpenTelemetry collector
configuration in YAML and append it to the agent's own configuration. Start the agent with your
CloudWatch agent configuration file, then append the OpenTelemetry YAML file:

```
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -c file:/tmp/agent.json -s
/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -c file:`/tmp/otel.yaml` -s
```

The agent merges the two configurations on startup and logs the resolved configuration. To
avoid merge conflicts with pipelines that the agent creates automatically, add a custom suffix to
each component and pipeline name in your OpenTelemetry YAML (for example,
`otlphttp/cwagent`).

## Supported OpenTelemetry components

The following OpenTelemetry components are available for you to configure in your appended
YAML configuration. Use the component type name shown here as the key in your YAML.

| Component type | Available components                                                                                                                                                                                                                                                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Receivers      | `otlp`, `prometheus`, `statsd`,<br>`collectd`, `jmx`, `hostmetrics`,<br>`filelog`, `tcplog`, `udplog`,<br>`jaeger`, `zipkin`, `kafka`,<br>`kubeletstats`                                                                                                                                                                                     |
| Processors     | `batch`, `memory_limiter`, `filter`,<br>`attributes`, `resource`, `resourcedetection`,<br>`metricstransform`, `transform`,<br>`cumulativetodelta`, `deltatocumulative`,<br>`deltatorate`, `groupbyattrs`, `groupbytrace`,<br>`k8sattributes`, `metricsgeneration`,<br>`metricstarttime`, `probabilistic_sampler`,<br>`span`, `tail_sampling` |
| Exporters      | `otlphttp`, `awsemf`,<br>`awscloudwatchlogs`, `awsxray`,<br>`prometheusremotewrite`, `debug`                                                                                                                                                                                                                                                 |
| Extensions     | `sigv4auth`, `headers_setter`,<br>`file_storage`, `health_check`, `pprof`,<br>`zpages`                                                                                                                                                                                                                                                       |

The CloudWatch agent only supports writing telemetry to AWS destinations.

## Configuration examples

The following examples send each signal to the corresponding CloudWatch OTLP endpoint using the
`otlphttp` exporter and the `sigv4auth` extension. Each component and
pipeline name uses a `/cwagent` suffix to avoid conflicts with pipelines that the
agent creates automatically. Replace `region` with your AWS Region.

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
    metrics_endpoint: https://monitoring.`region`.amazonaws.com/v1/metrics
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "`region`"
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
    logs_endpoint: https://logs.`region`.amazonaws.com/v1/logs
    headers:
      x-aws-log-group: `my-log-group`
      x-aws-log-stream: default
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "`region`"
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
    traces_endpoint: https://xray.`region`.amazonaws.com/v1/traces
    auth:
      authenticator: sigv4auth/cwagent
extensions:
  sigv4auth/cwagent:
    region: "`region`"
    service: "xray"
service:
  extensions: [sigv4auth/cwagent]
  pipelines:
    traces/cwagent:
      receivers: [otlp/cwagent]
      exporters: [otlphttp/cwagent]
```

###### Note

Make sure Transaction Search is enabled before you send traces to the OTLP traces endpoint.
