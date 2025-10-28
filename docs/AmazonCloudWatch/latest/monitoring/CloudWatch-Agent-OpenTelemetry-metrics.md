# Collect metrics and traces with

OpenTelemetry

You can collect metrics and traces from your applications or services using the CloudWatch
agent with the OpenTelemetry Protocol (OTLP), which is a popular open source solution. You
can use any OpenTelemetry SDK to send metrics and traces to the CloudWatch agent. For more
information about the available OpenTelemetry SDKs, see [OpenTelemetry Supported Language APIs
& SDKs.](https://opentelemetry.io/docs/languages/ "https://opentelemetry.io/docs/languages/").

To collect OpenTelemetry metrics and traces, add an `otlp` section to the
CloudWatch agent configuration file. The section has the following fields:

- `grpc_endpoint` – Optional. Specifies the address for the CloudWatch
  agent to use to listen for OpenTelemetry metrics or traces sent using gRPC Remote
  Procedure Calls. The format is `ip:port`. This address must match the
  address set for the gRPC exporter in the OpenTelemetry SDK. If you omit this field,
  the default of `127.0.0.1:4317` is used.
- `http_endpoint` – Optional. Specifies the address for the
  CloudWatch agent to use to listen for OpenTelemetry metrics or traces sent over HTTP.
  The format is `ip:port`. This address must match the address set for the
  HTTP exporter in the OpenTelemetry SDK. If you omit this field, the default of
  `127.0.0.1:4318` is used.
- `tls` – Optional. Specifies that the server should be configured
  with TLS.

      + `cert_file` – Path to the TLS certificate to use for TLS
       required connections.
      + `key_file` – Path to the TLS key to use for TLS required
       connections.

  The `otlp` section can be placed in multiple sections within the CloudWatch agent
  configuration file depending on how and where you want to send the metrics and
  traces.

###### Important

Each `otlp` section requires a unique endpoint and port. For detailed
information about splitting the metrics and traces endpoints, see [OTLP
Exporter Configuration](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/ "https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/") in the OpenTelemetry SDK documentation.

To send metrics to CloudWatch or Amazon Managed Service for Prometheus, add the `otlp` section under
`metrics_collected` within the `metrics` section. For more
information about sending metrics to different destinations, see [Manually create or edit the
CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md"). The following example
shows a configuration that sends metrics to CloudWatch:

###### Note

If you are running the agent in containerized environments and sending telemetry
from outside the agent container’s network, make sure to specify the endpoint as
`0.0.0.0` instead of the default endpoint `127.0.0.1`.

```
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

To send metrics to Amazon CloudWatch Logs using the Embedded metric format (EMF), add the
`otlp` section under `metrics_collected` within the
`logs` section. This sends the EMF logs by default to the
`/aws/cwagent` log group and a generated log stream. The metrics are
extracted into the `CWAgent` namespace by default. The following example shows
a configuration that sends metrics as EMF logs to CloudWatch Logs:

```
{
  "logs": {
    "metrics_collected": {
      "otlp": {
        "grpc_endpoint": "127.0.0.1:4317",
        "http_endpoint": "127.0.0.1:4318"
      }
    }
  }
}

```

To send traces to AWS X-Ray, add the `otlp` section under
`traces_collected` within the `traces` section. The following
example shows a configuration that sends traces to X-Ray:

```
{
  "traces": {
    "traces_collected": {
      "otlp": {
        "grpc_endpoint": "127.0.0.1:4317",
        "http_endpoint": "127.0.0.1:4318"
      }
    }
  }
}

```
