# Container Insights with OpenTelemetry metrics for Amazon EKS

###### Preview

Container Insights with OpenTelemetry metrics provides visibility into the operational
health of your Amazon EKS cluster infrastructure. It is available in public preview at no
additional charge in US East (N. Virginia), US West (Oregon), Europe (Ireland), Asia Pacific
(Singapore), and Asia Pacific (Sydney).

The Amazon CloudWatch Observability EKS add-on collects open source metrics from your Amazon EKS
clusters and sends them to CloudWatch using the OpenTelemetry Protocol (OTLP) at 30 second
granularity. These metrics use metric names from their original sources, including cAdvisor,
Prometheus Node Exporter, NVIDIA DCGM, Kube State Metrics, and AWS Neuron Monitor. You can
query these metrics using PromQL in CloudWatch Query Studio or through the Prometheus compatible
query API.

Each metric is automatically enriched with up to 150 labels, including OpenTelemetry
semantic convention attributes and Kubernetes pod and node labels. PromQL handles aggregation
at query time, so each metric is published once per resource rather than at multiple
aggregation levels. The add-on also correlates accelerator metrics from AWS Neuron and AWS
Elastic Fabric Adapter with the specific pods and containers using them, providing visibility
that is not available from the metric sources alone.

To enable OTel Container Insights on an Amazon EKS cluster, install the Amazon CloudWatch Observability
EKS add-on version `v6.0.1-eksbuild.1` or later through the Amazon EKS console or
through infrastructure as code.

For more information about setting up OTel Container Insights, see [Setting up Container Insights](deploy-container-insights.md "deploy-container-insights.md").

For more information about querying these metrics with PromQL, see [PromQL querying](CloudWatch-PromQL-Querying.md "CloudWatch-PromQL-Querying.md").

## How OTel Container Insights compares to the Container Insights (enhanced)

The following table summarizes the differences between Container Insights (enhanced) and
OTel Container Insights.

| Feature           | Container Insights (enhanced)                                         | OTel Container Insights                                                  |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Metric names      | CloudWatch-format metrics (for example, `pod_cpu_utilization`)        | Open-source native (for example,<br>`container_cpu_usage_seconds_total`) |
| Labels per metric | 3–6 predefined dimensions per metric                                  | Up to 150 labels, including all Kubernetes pod and node labels           |
| Aggregation       | Pre-aggregated at multiple levels (cluster, namespace, workload, pod) | Raw per-resource metrics; aggregate at query time with PromQL            |
| Query language    | CloudWatch Metrics API                                                | PromQL (Prometheus-compatible)                                           |
| Metric ingestion  | CloudWatch Logs in EMF format                                         | OTLP endpoint                                                            |

## How metrics are labeled

Each metric collected by OTel Container Insights carries labels from three
sources.

Telemetry source native labels

Labels from the original metric source (for example, cAdvisor provides labels such
as `pod`, `namespace`, and `container`). These are
preserved as datapoint attributes.

OpenTelemetry resource attributes

The add-on appends resource attributes following OpenTelemetry semantic conventions
for [Kubernetes](https://opentelemetry.io/docs/specs/semconv/resource/k8s/ "https://opentelemetry.io/docs/specs/semconv/resource/k8s/"), [Host](https://opentelemetry.io/docs/specs/semconv/resource/host/ "https://opentelemetry.io/docs/specs/semconv/resource/host/"), and
[Cloud](https://opentelemetry.io/docs/specs/semconv/resource/cloud/ "https://opentelemetry.io/docs/specs/semconv/resource/cloud/"), such as `k8s.pod.name`,
`k8s.namespace.name`, `k8s.node.name`,
`host.name`, and `cloud.region`. These attributes are
consistent across all metric sources.

Kubernetes pod and node labels

All pod labels and node labels discovered from the Kubernetes API are appended as
resource attributes with the prefixes `k8s.pod.label` and
`k8s.node.label`.

For more information about how to query these attributes using PromQL, see [PromQL querying](CloudWatch-PromQL-Querying.md "CloudWatch-PromQL-Querying.md").

## Supported metrics

The following table lists the metric sources and categories collected by OTel Container
Insights.

| Metric source              | Metric category                                                                                                                                 | Prerequisites                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cAdvisor                   | CPU metrics                                                                                                                                     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| cAdvisor                   | Memory metrics                                                                                                                                  | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| cAdvisor                   | Network metrics                                                                                                                                 | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| cAdvisor                   | Disk and filesystem metrics                                                                                                                     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | CPU metrics                                                                                                                                     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | Memory metrics                                                                                                                                  | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | Disk metrics                                                                                                                                    | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | Filesystem metrics                                                                                                                              | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | Network metrics                                                                                                                                 | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | System metrics                                                                                                                                  | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | VMStat metrics                                                                                                                                  | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Prometheus Node Exporter   | Netstat and socket metrics                                                                                                                      | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NVIDIA DCGM                | GPU utilization and performance metrics                                                                                                         | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU memory metrics                                                                                                                              | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU power and thermal metrics                                                                                                                   | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU throttling metrics                                                                                                                          | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU error and reliability metrics                                                                                                               | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU NVLink metrics                                                                                                                              | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| NVIDIA DCGM                | GPU informational metrics                                                                                                                       | [NVIDIA device<br>plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") and [NVIDIA container<br>toolkit](https://github.com/NVIDIA/nvidia-container-toolkit "https://github.com/NVIDIA/nvidia-container-toolkit") must be installed.                                                                                                                                                                                                                                                                    |
| AWS Neuron Monitor         | NeuronCore metrics                                                                                                                              | [Neuron driver](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html") and [Neuron device plugin](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html") must be installed. |
| AWS Neuron Monitor         | NeuronDevice metrics                                                                                                                            | [Neuron driver](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html") and [Neuron device plugin](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html") must be installed. |
| AWS Neuron Monitor         | Neuron system metrics                                                                                                                           | [Neuron driver](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html") and [Neuron device plugin](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html") must be installed. |
| AWS Elastic Fabric Adapter | EFA metrics                                                                                                                                     | [EFA device plugin](https://github.com/aws/eks-charts/tree/master/stable/aws-efa-k8s-device-plugin "https://github.com/aws/eks-charts/tree/master/stable/aws-efa-k8s-device-plugin") must be installed.                                                                                                                                                                                                                                                                                                                                               |
| NVMe                       | NVMe SMART metrics                                                                                                                              | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Kube State Metrics         | Pod, node, Deployment, DaemonSet, StatefulSet, ReplicaSet, Job, CronJob,<br>Service, Namespace, PersistentVolume, PersistentVolumeClaim metrics | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Kubernetes API server      | API server and etcd metrics                                                                                                                     | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Disabling dual publishing

Starting with Amazon CloudWatch Observability EKS add-on version v6.0.1-eksbuild.1 or later,
the add-on publishes metrics through both Container Insights (legacy) and OTel Container
Insights by default. If you want to use only one of these, you can disable the other.

### Disable OTel Container Insights

To stop publishing OTel Container Insights metrics and use only legacy Container
Insights, set the `otelContainerInsights` configuration to disabled.

Use the following configuration value:

```
{"otelContainerInsights":{"enabled":false}}
```

Run the following command to apply the configuration:

```
aws eks update-addon \
  --cluster-name `CLUSTER_NAME` \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":false}}' \
  --region `REGION`
```

### Disable Container Insights

To stop publishing legacy Container Insights metrics and use only OTel Container
Insights, set the `containerInsights` configuration to disabled.

Use the following configuration value:

```
{"containerInsights":{"enabled":false}}
```

Run the following command to apply the configuration:

```
aws eks update-addon \
  --cluster-name `CLUSTER_NAME` \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerInsights":{"enabled":false}}' \
  --region `REGION`
```
