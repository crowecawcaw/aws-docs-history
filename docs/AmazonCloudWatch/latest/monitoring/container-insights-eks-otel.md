

# OTel Container Insights (Recommended)
<a name="container-insights-eks-otel"></a>

OTel Container Insights is the recommended approach for enabling Container Insights on Amazon EKS clusters. Built on OpenTelemetry, it provides comprehensive observability across metrics and logs with a simplified deployment model and active ongoing development.

Both OTel Container Insights and Enhanced Container Insights (Classic) use the same `amazon-cloudwatch-observability` Amazon EKS add-on. The difference is the add-on version and configuration, not a different product. OTel Container Insights is the newer, actively developed configuration of that add-on.

This approach is designed for the following use cases:
+ New Amazon EKS customers who want the best-supported path to cluster observability
+ Existing customers looking to consolidate on a single, modern telemetry pipeline
+ Teams adopting OpenTelemetry who want native integration with CloudWatch

## Key benefits
<a name="container-insights-eks-otel-benefits"></a>

OTel Container Insights provides the following benefits:
+ **Simplified setup** — Enable full observability in minutes through the console, AWS CLI, or CloudFormation
+ **Comprehensive signals** — Collect metrics and logs from a single agent deployment
+ **Enhanced observability** — Access detailed Kubernetes metrics, pod-level insights, and correlated signals
+ **Active development** — Receives new features, performance improvements, and expanded signal coverage on an ongoing basis
+ **OpenTelemetry-native** — Built on the OpenTelemetry Collector, aligning with the industry-standard observability framework

## Why this approach is recommended
<a name="container-insights-eks-otel-comparison"></a>

OTel Container Insights is recommended over other Container Insights approaches because it provides the broadest signal coverage (metrics and logs) with the simplest deployment model. Other approaches are in maintenance-only mode or require more complex manual configuration.

The following table compares OTel Container Insights with Enhanced Container Insights (Classic).


| Consideration | OTel Container Insights | Enhanced Container Insights (Classic) | 
| --- | --- | --- | 
| Signals | Metrics, Logs | Metrics, Logs | 
| Enhanced observability | Yes | Yes | 
| Maintenance status | Active development | Maintenance | 
| Deployment complexity | Low | Low | 

## Metric sources and receivers
<a name="container-insights-eks-otel-receivers"></a>

OTel Container Insights collects metrics from open-source receivers and automatically enriches them with OpenTelemetry semantic conventions. Unlike Enhanced Container Insights (Classic), which uses proprietary metric names, OTel Container Insights preserves the original metric names from each source. This makes them compatible with existing PromQL dashboards and community documentation.

OTel Container Insights collects open-source metrics from multiple receivers using the OpenTelemetry Protocol (OTLP) at 30-second granularity. Metrics use their original source names (for example, `container_cpu_usage_seconds_total` from cAdvisor) rather than CloudWatch-format names, and you can query them with PromQL.

The following table lists the available receivers and their prerequisites.


| Receiver | What it collects | Prerequisites | 
| --- | --- | --- | 
| cAdvisor | Container CPU, memory, network, disk/filesystem metrics | Built into kubelet — no additional setup | 
| Prometheus Node Exporter | Node-level CPU, memory, disk, filesystem, network, system, VMStat, netstat/socket metrics | Included in the add-on | 
| Kube State Metrics | Pod, node, Deployment, DaemonSet, StatefulSet, ReplicaSet, Job, CronJob, Service, Namespace, PV, PVC metrics | Included in the add-on | 
| Kubernetes API Server | API server and etcd metrics | Available on control plane | 
| NVIDIA DCGM | GPU utilization, memory, power/thermal, throttling, error/reliability, NVLink metrics | NVIDIA device plugin and container toolkit required | 
| AWS Neuron Monitor | NeuronCore, NeuronDevice, and Neuron system metrics | Neuron driver and device plugin required | 
| AWS Elastic Fabric Adapter | EFA networking metrics | EFA device plugin required | 
| NVMe | NVMe SMART health metrics | No additional setup | 

Each metric is enriched with up to 150 labels from the following three sources:

1. **Telemetry source native labels** — From the original receiver (for example, `pod`, `namespace`, `container` from cAdvisor)

1. **OpenTelemetry resource attributes** — Following OTel semantic conventions for Kubernetes, Host, and Cloud

1. **Kubernetes pod and node labels** — All labels from the Kubernetes API, prefixed with `k8s.pod.label.*` and `k8s.node.label.*`

## Dual publishing and migration
<a name="container-insights-eks-otel-dual-publishing"></a>

OTel Container Insights is disabled by default. To enable it, set `otelContainerInsights.enabled` to `true` in the add-on configuration.

Starting with add-on version v6.2.0, the add-on supports publishing metrics through both Enhanced Container Insights (Classic) and OTel Container Insights simultaneously. This allows you to validate the new metrics pipeline before fully migrating.

To enable OTel Container Insights alongside Enhanced Container Insights (Classic), run the following command.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerInsights":{"enabled":true},"otelContainerInsights":{"enabled":true}}'
```

To disable OTel Container Insights and keep only Enhanced Container Insights (Classic), run the following command.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":false}}'
```

To disable Enhanced Container Insights (Classic) and keep only OTel Container Insights, run the following command.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerInsights":{"enabled":false},"otelContainerInsights":{"enabled":true}}'
```

## Getting started
<a name="container-insights-eks-otel-topics"></a>

Use the following topics to set up and configure OTel Container Insights on your Amazon EKS clusters.

**Topics**
+ [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md) — Get started with OTel Container Insights using the fastest setup path.
+ [Enable OTel Container Insights from the console](container-insights-eks-otel-console.md) — Enable OTel Container Insights through the AWS Management Console.
+ [Deploy OTel Container Insights with Helm](container-insights-eks-otel-helm.md) — Deploy OTel Container Insights using the Helm chart for flexible, GitOps-friendly management.
+ [Deploy OTel Container Insights with CloudFormation](container-insights-eks-otel-cfn.md) — Deploy OTel Container Insights using a CloudFormation template.
+ [Sending logs to Amazon CloudWatch](container-insights-eks-otel-logs.md) — Configure log collection for your Amazon EKS clusters.
+ [Advanced configuration for OTel Container Insights on Amazon EKS](container-insights-eks-otel-advanced.md) — Customize and fine-tune OTel Container Insights for your environment.