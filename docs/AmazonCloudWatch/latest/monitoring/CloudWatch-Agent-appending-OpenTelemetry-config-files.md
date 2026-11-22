

# Appending OpenTelemetry collector configuration files

 The CloudWatch agent supports supplemental OpenTelemetry collector configuration files alongside its own configuration files. This feature allows you to use CloudWatch agent features such as CloudWatch Application Signals or Container Insights through the CloudWatch agent configuration and bring in your existing OpenTelemetry collector configuration with a single agent. 

For most configurations, use the `opentelemetry` section of the agent configuration file instead. Use an appended collector configuration only for OpenTelemetry Collector components that the `opentelemetry` section doesn't provide. For more information, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md).

To prevent merge conflicts with pipelines automatically created by CloudWatch agent, add a custom suffix to each of the components and pipelines in your OpenTelemetry collector configuration.

```yaml
receivers:
  otlp/custom-suffix:
    protocols:
      http:

exporters:
  awscloudwatchlogs/custom-suffix:
    log_group_name: "test-group"
    log_stream_name: "test-stream"
  
service:
  pipelines:
    logs/custom-suffix:
      receivers: [otlp/custom-suffix]
      exporters: [awscloudwatchlogs/custom-suffix]
```

To configure the CloudWatch agent, start the CloudWatch agent using the `fetch-config` option and specify the CloudWatch agent's configuration file. CloudWatch agent requires at least one CloudWatch agent configuration file.

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/agent.json -s
```

Next, use the `append-config` option while specifying the OpenTelemetry collector configuration file.

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -c file:/tmp/otel.yaml -s
```

The agent merges the two configuration files on start up and logs the resolved configuration.

The following OpenTelemetry components are available for you to configure in your appended YAML configuration. Use the component type name shown here as the key in your YAML.


| Component type | Available components | 
| --- | --- | 
| Receivers | `otlp`, `prometheus`, `statsd`, `collectd`, `jmx`, `hostmetrics`, `filelog`, `journald`, `tcplog`, `udplog`, `windowseventlog`, `jaeger`, `zipkin`, `kafka`, `kubeletstats`, `postgresql`, `awsefa`, `awsnvmereceiver`, `awsxray` | 
| Processors | `batch`, `memory_limiter`, `filter`, `attributes`, `resource`, `resourcedetection`, `metricstransform`, `transform`, `cumulativetodelta`, `deltatocumulative`, `deltatorate`, `groupbyattrs`, `groupbytrace`, `k8sattributes`, `metricsgeneration`, `metricstarttime`, `probabilistic_sampler`, `span`, `tail_sampling` | 
| Exporters | `otlphttp`, `awscloudwatchlogs`, `awsxray`, `prometheusremotewrite`, `debug` | 
| Connectors | `count`, `forward`, `routing`, `signaltometrics`, `spanmetrics` | 
| Extensions | `sigv4auth`, `headers_setter`, `file_storage`, `health_check`, `pprof`, `zpages` | 

The CloudWatch agent only supports writing telemetry to AWS destinations.

For YAML examples that send each signal to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints, see [Configuration examples](CloudWatch-OTLPCloudWatchAgent.md#CloudWatch-OTLPCloudWatchAgent-Examples).