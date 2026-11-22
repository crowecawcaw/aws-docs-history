

# Example: Send Jaeger or Zipkin traces to OpenTelemetry

You can send Jaeger or Zipkin spans through the CloudWatch agent to the CloudWatch X-Ray OTLP traces endpoint. The agent has `jaeger` and `zipkin` receivers available for an appended OpenTelemetry collector configuration, so you point your existing Jaeger or Zipkin clients at the agent instead of running a separate collector.

The prerequisites are the same as for the OpenTelemetry configuration, with one addition. For the required agent version and the IAM and network prerequisites, see [Create a CloudWatch agent configuration for OpenTelemetry](CloudWatch-Agent-OpenTelemetry-config.md). In addition, you must enable Transaction Search before you send traces to the X-Ray OTLP traces endpoint. You can send traces to that endpoint only after Transaction Search is enabled.

As in the preceding example, add a custom suffix to each component and pipeline name, shown in the following examples as {{suffix}}. The suffix prevents merge conflicts with the pipelines that the CloudWatch agent creates automatically.

Create the appended collector configuration file. Add a `jaeger` receiver, a `batch` processor, and an `otlphttp` exporter that sends to the CloudWatch X-Ray OTLP traces endpoint. Authenticate the exporter with a `sigv4auth` extension. Replace {{aa-example-1}} with your Region.

```yaml
extensions:
  sigv4auth/{{suffix}}:
    service: xray        # "xray" for traces, not "monitoring"
    region: {{aa-example-1}}

receivers:
  jaeger/{{suffix}}:
    protocols:
      grpc:
        endpoint: 0.0.0.0:14250
      thrift_http:
        endpoint: 0.0.0.0:14268

processors:
  batch/{{suffix}}: {}

exporters:
  otlphttp/{{suffix}}:            # the endpoint supports HTTP only, not gRPC
    traces_endpoint: https://xray.{{aa-example-1}}.amazonaws.com/v1/traces
    compression: gzip
    auth:
      authenticator: sigv4auth/{{suffix}}

service:
  extensions: [sigv4auth/{{suffix}}]
  pipelines:
    traces/{{suffix}}:
      receivers: [jaeger/{{suffix}}]
      processors: [batch/{{suffix}}]
      exporters: [otlphttp/{{suffix}}]
```

Load the Classic configuration file with the `fetch-config` option, and then append the collector configuration file with the `append-config` option.

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/tmp/agent.json -s
```

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a append-config -m ec2 -c file:/tmp/otel.yaml -s
```

Zipkin spans are sent the same way, with one difference in the receiver. Instead of the `jaeger` receiver, use a `zipkin` receiver, which listens on `0.0.0.0:9411` by default, and reference it in the pipeline's `receivers` list in place of `jaeger/{{suffix}}`. Have your Zipkin clients send to that endpoint. The `otlphttp` exporter and its `sigv4auth` extension, the `fetch-config` and `append-config` commands, and the validation step are the same as for Jaeger.

The agent forwards the spans to the CloudWatch X-Ray OTLP traces endpoint, and you view them in Transaction Search.