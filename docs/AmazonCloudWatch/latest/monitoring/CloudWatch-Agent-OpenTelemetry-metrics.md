

# Receive OTLP data with the Classic configuration (legacy)

**This is a legacy configuration**  
The `otlp` source on this page is a legacy approach retained for existing Classic configurations. For new configurations, use the `opentelemetry` section of the agent configuration. It sends metrics, logs, and traces to the CloudWatch OTLP endpoints as OpenTelemetry data, which you can query with PromQL. For more information, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md).  
Use the `otlp` source on this page only if you already use the Classic configuration and need its destinations.

The `otlp` source in the Classic `metrics` and `traces` sections opens a local OTLP endpoint on the agent. Your OpenTelemetry SDK sends data to that endpoint, and the agent converts it before sending it to CloudWatch. Metrics are published as CloudWatch metrics in a namespace, and you can't query them with PromQL.

**Don't configure both on the same endpoints**  
Don't configure an `otlp` source here and in the `opentelemetry` section on the same endpoints. If you do, the agent sends each data point to both destinations, and you're charged for both.

To use the source, add an `otlp` section to the Classic `metrics` or `traces` section of the agent configuration file. The `otlp` section has the following fields:
+ `grpc_endpoint` – Optional. Specifies the address for the CloudWatch agent to use to listen for OpenTelemetry metrics or traces sent using gRPC Remote Procedure Calls. The format is `ip:port`. This address must match the address set for the gRPC exporter in the OpenTelemetry SDK. If you omit this field, the default of `127.0.0.1:4317` is used.
+ `http_endpoint` – Optional. Specifies the address for the CloudWatch agent to use to listen for OpenTelemetry metrics or traces sent over HTTP. The format is `ip:port`. This address must match the address set for the HTTP exporter in the OpenTelemetry SDK. If you omit this field, the default of `127.0.0.1:4318` is used.
+ `tls` – Optional. Specifies that the server should be configured with TLS.
  + `cert_file` – Path to the TLS certificate to use for TLS required connections.
  + `key_file` – Path to the TLS key to use for TLS required connections.

The `otlp` section can be placed in multiple sections within the CloudWatch agent configuration file depending on how and where you want to send the metrics and traces.

**Important**  
Each `otlp` section requires a unique endpoint and port. For detailed information about splitting the metrics and traces endpoints, see [OTLP Exporter Configuration](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/) in the OpenTelemetry SDK documentation.

To send metrics to CloudWatch or Amazon Managed Service for Prometheus, add the `otlp` section under `metrics_collected` within the `metrics` section. For more information about sending metrics to different destinations, see [Manually create or edit the CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md). The following example shows a configuration that sends metrics to CloudWatch:

**Note**  
 If you are running the agent in containerized environments and sending telemetry from outside the agent container's network, make sure to specify the endpoint as `0.0.0.0` instead of the default endpoint `127.0.0.1`. The OTLP receiver doesn't authenticate senders, so restrict access to these ports with security groups.

```JSON
{
  "metrics": {
    "metrics_collected": {
      "otlp": {
        "grpc_endpoint": "127.0.0.1:4317",
        "http_endpoint": "127.0.0.1:4318"
      }
    }
  }
}
```

To send traces to AWS X-Ray, add the `otlp` section under `traces_collected` within the `traces` section. The following example shows a configuration that sends traces to X-Ray. Because each `otlp` section needs its own endpoint, this example uses different ports from the metrics example so that you can use both:

```JSON
{
  "traces": {
    "traces_collected": {
      "otlp": {
        "grpc_endpoint": "127.0.0.1:4315",
        "http_endpoint": "127.0.0.1:4316"
      }
    }
  }
}
```