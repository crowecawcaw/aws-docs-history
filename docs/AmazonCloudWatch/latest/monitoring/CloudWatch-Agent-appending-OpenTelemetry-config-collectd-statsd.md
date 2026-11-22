

# Example: Send collectd or StatsD metrics to OpenTelemetry

With the Classic configuration, the CloudWatch agent collects collectd metrics (see [Retrieve custom metrics with collectd](CloudWatch-Agent-custom-metrics-collectd.md)) and StatsD metrics (see [Retrieve custom metrics with StatsD](CloudWatch-Agent-custom-metrics-statsd.md)) and publishes them as CloudWatch metrics in a namespace. To publish these metrics as OpenTelemetry metrics instead, point the sender at a `collectd` or `statsd` receiver in an appended OpenTelemetry collector configuration, rather than at the Classic agent. The agent has no collectd or statsd source in the `opentelemetry` section of its configuration file, so you add these receivers through an appended collector configuration. The other Classic metrics in the agent configuration, such as CPU, memory, and disk, are unaffected.

The prerequisites are the same as for the OpenTelemetry configuration. For the required agent version and the IAM and network prerequisites, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md).

As in the preceding example, add a custom suffix to each component and pipeline name, shown in the following examples as {{suffix}}. The suffix prevents merge conflicts with the pipelines that the CloudWatch agent creates automatically.

**To send collectd metrics to the OpenTelemetry path**

1. In the Classic agent configuration file, remove the `collectd` entry from the `metrics_collected` section, and leave the rest of the file unchanged.

   ```json
   "metrics_collected": {
     "cpu": { ... },
     "mem": { ... },
     "collectd": {}        // remove this entry
   }
   ```

1. Point collectd at the collector receiver instead of the agent. In the collectd configuration file, remove or comment out the `network` plugin that sends to the agent, and add a `write_http` plugin that posts JSON to the collectd receiver's HTTP endpoint. Set `StoreRates` to `true`.

   ```
   LoadPlugin write_http
   <Plugin write_http>
     <Node "cloudwatch">
       URL "http://127.0.0.1:8081"
       Format "JSON"
       StoreRates true
     </Node>
   </Plugin>
   ```
**Note**  
The collectd `write_http` plugin might be packaged separately from collectd itself. For example, on Amazon Linux 2023, install it with `collectd-write_http`. If the plugin is configured but not installed, collectd fails to start.  

   ```
   sudo dnf install -y collectd-write_http
   ```

1. Create the appended collector configuration file. Add a `collectd` receiver on the same endpoint, standard processors, and an `otlphttp` exporter that sends to the CloudWatch metrics OTLP endpoint. Authenticate the exporter with a `sigv4auth` extension. Replace {{aa-example-1}} with your Region.

   ```yaml
   extensions:
     sigv4auth/{{suffix}}:
       service: monitoring        # always "monitoring" for metrics
       region: {{aa-example-1}}
   
   receivers:
     collectd/{{suffix}}:
       endpoint: 127.0.0.1:8081
   
   processors:
     transform/{{suffix}}:
       error_mode: ignore
       metric_statements:
         - context: metric
           statements:
             - convert_sum_to_gauge()
     resourcedetection/{{suffix}}: {}
     batch/{{suffix}}: {}
   
   exporters:
     otlphttp/{{suffix}}:            # the endpoint supports HTTP only, not gRPC
       metrics_endpoint: https://monitoring.{{aa-example-1}}.amazonaws.com/v1/metrics
       compression: gzip
       auth:
         authenticator: sigv4auth/{{suffix}}
   
   service:
     extensions: [sigv4auth/{{suffix}}]
     pipelines:
       metrics/{{suffix}}:
         receivers: [collectd/{{suffix}}]
         processors: [transform/{{suffix}}, resourcedetection/{{suffix}}, batch/{{suffix}}]
         exporters: [otlphttp/{{suffix}}]
   ```

   The collectd COUNTER and DERIVE values arrive from the `collectd` receiver as OpenTelemetry sums. These sums do not carry the aggregation temporality and start time that the CloudWatch metrics OTLP endpoint requires. Without conversion, the endpoint rejects them. Because the collectd `write_http` plugin sets `StoreRates true`, these values are already per-second rates. As a result, the `transform` processor's `convert_sum_to_gauge()` represents them correctly as gauges, which the endpoint accepts. Gauge metrics, such as memory and load, pass through unchanged.

1. Load the Classic configuration file with the `fetch-config` option, and then append the collector configuration file with the `append-config` option.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/agent.json -s
   ```

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -c file:/tmp/otel.yaml -s
   ```

   Restart collectd so that it sends to the new endpoint.

   ```
   sudo systemctl restart collectd
   ```

1. Confirm that the metrics appear in CloudWatch. These metrics are now OpenTelemetry metrics, which you query with PromQL in Query Studio. The corresponding Classic metrics in the `CWAgent` namespace stop updating. For more information, see [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md).

StatsD metrics migrate the same way, with one difference in the receiver. Instead of the `collectd` receiver and the collectd `write_http` plugin, use a `statsd` receiver. By default, this receiver is a UDP listener on `127.0.0.1:8125`. Have your StatsD clients send to that UDP endpoint.

The `statsd` receiver already emits metrics with a valid aggregation temporality and start time, which the CloudWatch metrics OTLP endpoint accepts. The StatsD pipeline therefore does not need the `transform` processor's `convert_sum_to_gauge()` that the collectd pipeline uses. Its processors are only `resourcedetection/{{suffix}}` and `batch/{{suffix}}`. The `otlphttp` exporter and its `sigv4auth` extension, the `fetch-config` and `append-config` commands, and the validation step are the same as for collectd.