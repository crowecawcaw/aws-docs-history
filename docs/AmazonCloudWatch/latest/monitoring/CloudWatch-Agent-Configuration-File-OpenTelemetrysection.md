

# CloudWatch agent configuration file: OpenTelemetry section

The `opentelemetry` section requires CloudWatch agent version 1.300070.0 or later. For how to check the installed version, see [Prerequisites](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-prereqs).

**Note**  
On Amazon Linux 2023, the `yum install amazon-cloudwatch-agent` and `dnf install amazon-cloudwatch-agent` commands install a version that meets this minimum. If your package repository offers a version earlier than 1.300070.0, install the agent from the CloudWatch agent download instead. For more information, see [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md).

The `opentelemetry` section can include the following fields:
+ `cluster_name` – Optional. Specifies the name of the Kubernetes cluster. The agent applies this value to all telemetry collected under the `opentelemetry` section.
+ `resource_attributes` – Optional. Specifies additional resource attributes to add to every metric, log, and trace collected under the `opentelemetry` section. This field is an object of string key-value pairs. You can specify up to 30 attributes. The maximum length of each value is 1024 characters. For attributes that the agent detects automatically, such as `cloud.region`, `host.id`, and `cloud.provider`, the detected value takes precedence. Use this field for attributes that the agent does not detect on its own.
+ `collect` – Required. Specifies which telemetry sources the agent collects. You must include at least one of the following sources. For the fields of each source and a focused example, see the per-source topic.
  + `host_metrics` – Host-level system metrics. See [Collect host metrics](CloudWatch-Agent-OpenTelemetry-config-collect-host-metrics.md).
  + `prometheus` – Metrics scraped from Prometheus targets. See [Scrape Prometheus metrics](CloudWatch-Agent-OpenTelemetry-config-prometheus.md).
  + `otlp` – Metrics, logs, and traces received from applications over OTLP. See [Receive OTLP data](CloudWatch-Agent-OpenTelemetry-config-applications.md).
  + `database_insights` – Metrics and logs from self-managed databases for CloudWatch Database Insights. See [Collect CloudWatch Database Insights metrics](CloudWatch-Agent-OpenTelemetry-config-collect-database-insights.md).
  + `files` – Log files from the host. See [Collect log files](CloudWatch-Agent-OpenTelemetry-config-collect-files.md).
  + `windows_events` – Events from the Windows Event Log. See [Collect Windows event logs](CloudWatch-Agent-OpenTelemetry-config-windows.md).

**Note**  
Make sure Transaction Search is enabled before you send traces to the OTLP traces endpoint.

The following is an example of an `opentelemetry` section that collects OTLP telemetry and a log file.

```json
"opentelemetry": {
  "collect": {
    "otlp": {
      "grpc_endpoint": "0.0.0.0:4317",
      "http_endpoint": "0.0.0.0:4318",
      "span_metrics_enabled": true
    },
    "files": {
      "collect_list": [
        {
          "file_path": "/var/log/app/*.log",
          "log_group_name": "/app/{instance_id}",
          "log_stream_name": "{hostname}",
          "timestamp_format": "%Y-%m-%d %H:%M:%S",
          "timezone": "UTC"
        }
      ]
    }
  }
}
```