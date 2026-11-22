

# Telemetry filters

The `otelFilters` settings are cluster-level include and exclude lists for the OpenTelemetry telemetry that the Amazon CloudWatch Observability add-on and Helm chart collect. They are the main way to control the cost of label enrichment. Each change to a filter restarts the agent pods that it affects, because the agent reads its configuration only at startup.

The telemetry filters are available in version 8.0.0 and later of the add-on and the Helm chart.

## How filters match
<a name="eks-observability-addon-telemetry-filters-rules"></a>
+ An entry is an exact name, a prefix followed by `*` (for example `prod-*`), or `*` alone.
+ An empty `include` list, or one that contains `*`, includes everything.
+ Exclude wins over include.
+ Matching is case-sensitive.

## What each filter applies to
<a name="eks-observability-addon-telemetry-filters-scope"></a>

Each filter applies to the following telemetry.

`otelFilters.namespaces`  
Applies to the metrics and logs of OTel Container Insights, and to the metrics, traces, and logs that the OTLP endpoint receives. It doesn't apply to ServiceMonitor and PodMonitor scraping.

`otelFilters.metricNames`  
Applies to the metrics of OTel Container Insights, and to the metrics that the OTLP endpoint receives, including span metrics. It doesn't apply to ServiceMonitor and PodMonitor scraping.

`otelFilters.podLabels`, `otelFilters.nodeLabels`  
Apply to the metrics and logs of OTel Container Insights, to the metrics, traces, and logs that the OTLP endpoint receives, and to ServiceMonitor and PodMonitor scraping.

## Namespace filter
<a name="eks-observability-addon-telemetry-filters-namespaces"></a>

`otelFilters.namespaces` drops the pod and container telemetry of the namespaces that it filters out. It doesn't apply to node-level metrics, to host logs, or to the metrics of control-plane components such as Karpenter and KEDA. Records without a Kubernetes namespace always pass.

The filter never drops GPU, AWS Neuron, or EFA device metrics, because a device belongs to a pod only for a while. When the pod that uses a device is in a filtered namespace, the agent keeps the device metrics and removes their pod, namespace, and container attributes.

The following add-on configuration drops the telemetry of the `kube-system` namespace and of every namespace whose name starts with `test-`:

```json
{
  "otelFilters": {
    "namespaces": {
      "exclude": [
        "kube-system",
        "test-*"
      ]
    }
  }
}
```

## Metric name filter
<a name="eks-observability-addon-telemetry-filters-metric-names"></a>

`otelFilters.metricNames` matches the names of the metrics as they are sent to CloudWatch. For example, the entry `dcgm_fi_dev_gpu_util` doesn't match the metric `DCGM_FI_DEV_GPU_UTIL`. It doesn't apply to logs.

The following add-on configuration drops the `container_network_*` metrics:

```json
{
  "otelFilters": {
    "metricNames": {
      "exclude": [
        "container_network_*"
      ]
    }
  }
}
```

**Important**  
A non-empty `include` list keeps only the metrics on it. It drops every other OTel Container Insights metric and every other OTLP metric, including span metrics.

## Pod and node label filters
<a name="eks-observability-addon-telemetry-filters-labels"></a>

`otelFilters.podLabels` and `otelFilters.nodeLabels` decide which pod and node labels the agent adds as `k8s.pod.label.*` and `k8s.node.label.*` attributes. Each has the following settings.

`include`  
The labels that the agent collects. An empty list, or one that contains `*`, collects every label.

`exclude`  
The labels that the agent removes after it collects them. `exclude: ["*"]` removes every label of that kind.

`recommendedExclusions`  
Also removes a built-in list of high-cardinality labels, such as the topology, hostname, and instance type labels, the Karpenter and Amazon EKS Auto Mode instance labels, and controller revision markers like `pod-template-hash`. The default is `true`.

For each label, exclude wins over a named include entry, and a named include entry wins over the built-in list. A named entry is a label key, or a prefix followed by `*`, but not `*` alone. So to keep one label from the built-in list, name it in `include`, and add `*` to keep every other label too.

The following add-on configuration collects only the named pod and node labels:

```json
{
  "otelFilters": {
    "podLabels": {
      "include": [
        "app",
        "team"
      ]
    },
    "nodeLabels": {
      "include": [
        "node.kubernetes.io/instance-type",
        "topology.kubernetes.io/zone"
      ]
    }
  }
}
```

The following configuration collects no pod or node labels:

```json
{
  "otelFilters": {
    "podLabels": {
      "exclude": [
        "*"
      ]
    },
    "nodeLabels": {
      "exclude": [
        "*"
      ]
    }
  }
}
```

The following configuration keeps every pod label, including `pod-template-hash` from the built-in list:

```json
{
  "otelFilters": {
    "podLabels": {
      "include": [
        "*",
        "pod-template-hash"
      ]
    }
  }
}
```

The agent always reads the pod labels `topology.kubernetes.io/region`, `topology.kubernetes.io/zone`, `serving.kserve.io/inferenceservice`, and `component`, and the node label `topology.kubernetes.io/zone`, for its own processing. If your filters leave one of them out, the agent removes it after use.