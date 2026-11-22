

# OTLP ingestion

The CloudWatch agent on every node of your cluster serves an OpenTelemetry Protocol (OTLP) endpoint. Your applications, OpenTelemetry SDKs, and collectors can send metrics, traces, and logs to it, and the agent sends them to CloudWatch. The endpoint is on by default, and is available in version 8.0.0 and later of the Amazon CloudWatch Observability Amazon EKS add-on and Helm chart.

The agent adds the same Kubernetes and cloud attributes to this telemetry as Container Insights adds to the pod that sent it, including pod and node labels. You can then correlate your application telemetry with your infrastructure metrics.

The endpoint replaces the `default:otel` agent configuration of earlier Helm chart versions. The chart now ignores `default:otel`, and only `otlp.enabled` decides whether the endpoint is on.

## Prerequisites
<a name="eks-observability-addon-otlp-endpoint-prereqs"></a>
+ Version 8.0.0 or later of the add-on or the Helm chart.
+ IAM permissions for the CloudWatch agent to write metrics to CloudWatch, logs to CloudWatch Logs, and traces to X-Ray. The install procedure attaches the [CloudWatchAgentServerPolicy](managed-policies-cloudwatch.md#managed-policies-cloudwatch-CloudWatchAgentServerPolicy) managed policy for this. For more information, see [Install the CloudWatch agent with the Amazon CloudWatch Observability EKS add-on or the Helm chart](install-CloudWatch-Observability-EKS-addon.md).
+ For traces, Transaction Search turned on in the account and Region. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md).

## Sending telemetry to the endpoint
<a name="eks-observability-addon-otlp-endpoint-send"></a>

The endpoint accepts OTLP over gRPC on port 4317 and over HTTP on port 4318, in plaintext. Send to the `cloudwatch-agent` Service in the `amazon-cloudwatch` namespace, which routes each request to the agent on the same node as the sender. For example, set the following environment variables on a container that uses an OpenTelemetry SDK:

```yaml
env:
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    value: http://cloudwatch-agent.amazon-cloudwatch:4318
  - name: OTEL_EXPORTER_OTLP_PROTOCOL
    value: http/protobuf
```

The SDK adds the path for each signal, such as `/v1/metrics` or `/v1/traces`. The HTTP endpoint accepts request bodies up to 20 MiB.

The agent sends each signal to its CloudWatch destination:
+ Metrics go to CloudWatch as OpenTelemetry metrics, which you query with PromQL.
+ Traces go to X-Ray and appear in Transaction Search. When span metrics are on, the agent also computes request count, error, and duration metrics from the traces it receives.
+ Logs go to the log group `/aws/cwagent/{{cluster-name}}/otlp`, in a log stream named `{{namespace}}/{{service.namespace}}/{{service.name}}` when those values are known. A sender can choose another log group and log stream with the `aws.log.group.name` and `aws.log.stream.name` resource attributes.

## Attributes that the agent adds
<a name="eks-observability-addon-otlp-endpoint-enrichment"></a>

The agent identifies the pod that sent the telemetry from the `k8s.pod.uid`, `k8s.pod.name`, and `k8s.namespace.name` attributes that the sender set, and otherwise from the connection's source IP address. It then adds the standard telemetry attributes (see [Standard telemetry attributes](eks-standard-telemetry-attributes.md)):
+ The namespace, pod, container, node, and workload attributes (`k8s.*`), including `k8s.workload.name` and `k8s.workload.type`.
+ The pod and node labels, as `k8s.pod.label.*` and `k8s.node.label.*` attributes. The `otelFilters.podLabels` and `otelFilters.nodeLabels` settings decide which labels are added. For more information, see [Telemetry filters](eks-observability-addon-telemetry-filters.md).
+ The cloud and host attributes of the node, `k8s.cluster.name`, and `cloud.resource_id`.
+ The service identity attributes, such as `service.name`, when the sender did not set them. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).

## Configuring the endpoint
<a name="eks-observability-addon-otlp-endpoint-configure"></a>

The following configuration values control the endpoint.


| Value | Default | Description | 
| --- | --- | --- | 
| otlp.enabled | true | Turns the endpoint on or off. | 
| otlp.grpc.enabled | true | Serves OTLP over gRPC. | 
| otlp.grpc.port | 4317 | The node port for OTLP over gRPC. | 
| otlp.http.enabled | true | Serves OTLP over HTTP. | 
| otlp.http.port | 4318 | The node port for OTLP over HTTP. | 
| otlp.spanMetrics.enabled | true | Computes request count, error, and duration metrics from the received traces. | 

At least one protocol must be on, and the two ports must differ. A port cannot be one that the agent already uses: 2000, 4311, 4314, 4315, 4316, 8125, 25826, or 25888.

The following add-on configuration turns the endpoint off:

```json
{
  "otlp": {
    "enabled": false
  }
}
```

The agent pods use host networking. If another collector on the node already holds port 4317 or 4318, one of the two pods stays `Pending`. The following configuration moves the endpoint to other ports:

```json
{
  "otlp": {
    "grpc": {
      "port": 14317
    },
    "http": {
      "port": 14318
    }
  }
}
```

The following configuration serves gRPC only:

```json
{
  "otlp": {
    "http": {
      "enabled": false
    }
  }
}
```

The following configuration keeps the endpoint but turns off span metrics:

```json
{
  "otlp": {
    "spanMetrics": {
      "enabled": false
    }
  }
}
```

With the Helm chart, set the same values in a values file or with `--set`, for example `--set otlp.enabled=false`.

A custom CloudWatch agent configuration can open its own OTLP receivers alongside this endpoint, but they must use other ports. If a custom receiver uses the same port, the agent can't bind it and doesn't start.