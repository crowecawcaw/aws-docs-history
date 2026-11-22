

# Receive OTLP data

The `otlp` source receives metrics, traces, and logs sent to the agent over the OpenTelemetry Protocol (OTLP), and forwards them to the CloudWatch OTLP endpoints. The agent sends logs that it receives to the `/aws/cwagent/otlp` log group, in a log stream named after the host identifier and the `service.name` resource attribute, unless the logs set the `aws.log.group.name` and `aws.log.stream.name` resource attributes. This source can include the following fields:
+ `grpc_endpoint` – Optional. Specifies the address the agent uses to listen for OTLP data sent using gRPC. The format is `ip:port`. This address must match the address set for the gRPC exporter in the OpenTelemetry SDK. If you omit this field, the agent uses the default `127.0.0.1:4317`. In a containerized deployment, set this to `0.0.0.0:4317` so the agent accepts traffic from other pods. The receiver doesn't authenticate senders, so restrict access to the port with security groups or network policies.
+ `http_endpoint` – Optional. Specifies the address the agent uses to listen for OTLP data sent over HTTP. The format is `ip:port`. This address must match the address set for the HTTP exporter in the OpenTelemetry SDK. If you omit this field, the agent uses the default `127.0.0.1:4318`. In a containerized deployment, set this to `0.0.0.0:4318` so the agent accepts traffic from other pods. The receiver doesn't authenticate senders, so restrict access to the port with security groups or network policies.
+ `span_metrics_enabled` – Optional. If `true`, the agent derives request, error, and duration metrics from received traces. The default value is `false`. The default OpenTelemetry configuration (`default:otel`) sets it to `true`.

Applications instrumented with an OpenTelemetry SDK can send metrics, logs, and traces to the agent, which forwards them to the CloudWatch OTLP endpoints. The agent signs the requests, so the application doesn't need AWS credentials.

1. Add an `otlp` source to the `opentelemetry` section. To also generate request, error, and duration metrics from the traces that the agent receives, set `span_metrics_enabled` to `true`.

   ```json
   {
     "opentelemetry": {
       "collect": {
         "host_metrics": {},
         "otlp": {
           "span_metrics_enabled": true
         }
       }
     }
   }
   ```

1. Configure the application's OpenTelemetry SDK to export to the agent. The following standard environment variables work with the SDKs for most languages:

   ```
   export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4318
   export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
   export OTEL_SERVICE_NAME={{my-service}}
   export OTEL_RESOURCE_ATTRIBUTES=deployment.environment.name={{production}}
   ```

   To send over gRPC instead, set the endpoint to `http://127.0.0.1:4317` and the protocol to `grpc`.

1. Start the agent, and then query the application's metrics in Query Studio by service name:

   ```
   {"{{my_metric}}", "@resource.service.name"="{{my-service}}"}
   ```

   To view traces, use Transaction Search. Traces require Transaction Search to be enabled.

   Application logs go to the `/aws/cwagent/otlp` log group, in a log stream named `{{host-id}}/{{my-service}}`. To use a different log group or stream, set the `aws.log.group.name` and `aws.log.stream.name` resource attributes, for example in `OTEL_RESOURCE_ATTRIBUTES`.

If the application runs in a container or on another host, set the agent's `grpc_endpoint` to `0.0.0.0:4317` and `http_endpoint` to `0.0.0.0:4318`, and restrict access to the ports with security groups or network policies, as described for the `otlp` fields earlier in this topic. For SDK setup by language, see [Example: send application metrics through the CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md#CloudWatch-OTLPCloudWatchAgent-Example).