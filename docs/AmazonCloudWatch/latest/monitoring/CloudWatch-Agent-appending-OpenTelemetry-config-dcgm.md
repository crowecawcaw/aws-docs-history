

# Example: Send NVIDIA GPU (DCGM) metrics to OpenTelemetry

With the Classic configuration, the CloudWatch agent collects NVIDIA GPU metrics and publishes them as CloudWatch metrics in a namespace. To publish GPU metrics as OpenTelemetry metrics instead, scrape the NVIDIA Data Center GPU Manager (DCGM) exporter with a `prometheus` receiver in an appended OpenTelemetry collector configuration. The agent has no `dcgm` receiver in the `opentelemetry` section of its configuration file, so you add a `prometheus` receiver through an appended collector configuration. The other Classic metrics in the agent configuration, such as CPU, memory, and disk, are unaffected.

**Note**  
On Amazon EKS, you don't need this manual configuration. Install the Amazon CloudWatch Observability Amazon EKS add-on and NVIDIA GPU metrics are collected for you. The recommended solution for GPU monitoring on Amazon EKS is Accelerated Compute Insights. For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md) and [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md). The following steps are for Amazon EC2 instances and self-managed clusters.

The prerequisites are the same as for the OpenTelemetry configuration, with one addition. For the required agent version and the IAM and network prerequisites, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md). In addition, you need a GPU instance with the NVIDIA driver installed, and NVIDIA DCGM with the `dcgm-exporter` running. By default, the `dcgm-exporter` exposes Prometheus-format GPU metrics at `http://localhost:9400/metrics`. To install the dcgm-exporter, see [Install DCGM Exporter](https://docs.nvidia.com/datacenter/dcgm/latest/gpu-telemetry/dcgm-exporter.html) on the NVIDIA website.

As in the preceding example, add a custom suffix to each component and pipeline name, shown in the following examples as {{suffix}}. The suffix prevents merge conflicts with the pipelines that the CloudWatch agent creates automatically.

**To send NVIDIA GPU (DCGM) metrics to the OpenTelemetry path**

1. Confirm that the `dcgm-exporter` is running and exposing Prometheus-format metrics. By default, it serves them at `http://localhost:9400/metrics`.

   ```
   curl -s http://localhost:9400/metrics | head
   ```

1. Create the appended collector configuration file. Add a `prometheus` receiver that scrapes the `dcgm-exporter`, standard processors, and an `otlphttp` exporter that sends to the CloudWatch metrics OTLP endpoint. Authenticate the exporter with a `sigv4auth` extension. Replace {{aa-example-1}} with your Region.

   ```yaml
   extensions:
     sigv4auth/{{suffix}}:
       service: monitoring        # always "monitoring" for metrics
       region: {{aa-example-1}}
   
   receivers:
     prometheus/{{suffix}}:
       config:
         scrape_configs:
           - job_name: dcgm
             scrape_interval: 60s
             metrics_path: /metrics
             static_configs:
               - targets: [localhost:9400]
   
   processors:
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
         receivers: [prometheus/{{suffix}}]
         processors: [resourcedetection/{{suffix}}, batch/{{suffix}}]
         exporters: [otlphttp/{{suffix}}]
   ```

   The `dcgm-exporter` metrics arrive from the `prometheus` receiver as gauges and sums that already carry a valid aggregation temporality and start time, which the CloudWatch metrics OTLP endpoint accepts. The pipeline therefore does not need a `transform` processor to convert them. Its processors are only `resourcedetection/{{suffix}}` and `batch/{{suffix}}`.

1. Load the Classic configuration file with the `fetch-config` option, and then append the collector configuration file with the `append-config` option.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/agent.json -s
   ```

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -c file:/tmp/otel.yaml -s
   ```

1. Confirm that the metrics appear in CloudWatch. These metrics are now OpenTelemetry metrics, which you query with PromQL in Query Studio. For more information, see [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md).

The exact set of GPU metrics depends on the `dcgm-exporter` configuration, which determines the fields that the exporter publishes. For the available fields and how to configure them, see the `dcgm-exporter` documentation on the NVIDIA website.

If you previously collected NVIDIA GPU metrics with the Classic `nvidia_gpu` configuration, remove that entry so the agent does not publish the same GPU metrics as both CloudWatch metrics and OpenTelemetry metrics. The corresponding Classic metrics in the `CWAgent` namespace then stop updating.