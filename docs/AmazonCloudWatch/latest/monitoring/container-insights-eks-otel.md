

# OTel Container Insights (Recommended)

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

OTel Container Insights collects metrics from open-source receivers and automatically enriches them with OpenTelemetry semantic conventions. Unlike Enhanced Container Insights (Classic), which uses proprietary metric names, OTel Container Insights preserves the original metric names from each source. This makes them compatible with most existing PromQL dashboards and community documentation.

OTel Container Insights collects open-source metrics from multiple receivers using the OpenTelemetry Protocol (OTLP) at 30-second granularity. Metrics use their original source names (for example, `container_cpu_usage_seconds_total` from cAdvisor) rather than CloudWatch-format names, and you can query them with PromQL.

The following table lists the available receivers and their prerequisites.


| Receiver | What it collects | Prerequisites | 
| --- | --- | --- | 
| cAdvisor | Container CPU, memory, network, disk, and file system metrics. Each container\_\* series measures one application container. The container\_network\_\* series measure the pod. | Built into kubelet — no additional setup | 
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

1. **Kubernetes pod and node labels** — Labels from the Kubernetes API, prefixed with `k8s.pod.label.*` and `k8s.node.label.*`. Container Insights does not send some generated labels.

## Dual publishing and migration
<a name="container-insights-eks-otel-dual-publishing"></a>

OTel Container Insights is disabled by default. To enable it, set `otelContainerInsights.enabled` to `true` in the add-on configuration.

Starting with add-on version v6.2.0, the add-on supports publishing metrics through both Enhanced Container Insights (Classic) and OTel Container Insights simultaneously. This allows you to validate the new metrics pipeline before fully migrating.

To enable OTel Container Insights alongside Enhanced Container Insights (Classic), run the following command.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerInsights":{"enabled":true},"otelContainerInsights":{"enabled":true}}'
```

To disable OTel Container Insights and keep only Enhanced Container Insights (Classic), run the following command.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":false}}'
```

To disable Enhanced Container Insights (Classic) and keep only OTel Container Insights, run the following command.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"containerInsights":{"enabled":false},"otelContainerInsights":{"enabled":true}}'
```

## Upgrading OTel Container Insights to version 7.0.0
<a name="container-insights-eks-otel-upgrade-v7"></a>

Version 7.0.0 of the add-on and Helm chart removes duplicate and generated data from OTel Container Insights metrics. This lowers the number of series and the size of each data point, which lowers your ingested volume and cost. Before you upgrade from a 6.x version, update the queries, dashboards, and alarms that use the following items.
+ **Pod-level cAdvisor series** — The pod and pause container series of the `container_*` metrics are no longer sent, except for `container_network_*`. A query that sums a `container_*` metric by pod without a container filter now returns about half of its earlier value. The new value is correct, because the earlier value counted each container twice. To get the new value on 6.x, add `container!=""`, for example `sum by (pod) (rate(container_cpu_usage_seconds_total{container!=""}[5m]))`.
+ **Node exporter scrape metrics** — `node_scrape_collector_duration_seconds` and `node_scrape_collector_success` are no longer sent.
+ **Removed deprecated attributes** — `net.host.name`, `net.host.port`, and `http.scheme` are no longer sent. Use `server.address`, `server.port`, and `url.scheme`, which have the same values.
+ **Resource-level copies of raw labels** — In PromQL, selectors such as `"@resource.pod"` no longer match. Use the data point label, such as `pod`.
+ **Generated node and pod labels** — Labels that repeat the instance type, Region, or zone, and a few Karpenter status labels, are no longer sent. Use `host.type`, `cloud.region`, and `cloud.availability_zone` instead.
+ **Availability Zone** — Kube State Metrics series that name neither a node nor a pod, such as Deployment, namespace, and Service series, no longer have `cloud.availability_zone`. Remove zone filters from queries and alarms on these series.

**Important**  
Check your alarms before you upgrade. A threshold alarm on a pod-level `container_*` sum can stop going into `ALARM`, because the value drops by about half. An alarm on a removed label or attribute gets no data. Its state then depends on how the alarm treats missing data.

**To upgrade to version 7.0.0**

1. Find your current version. For the add-on, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```bash
   aws eks describe-addon \
     --cluster-name {{cluster-name}} \
     --addon-name amazon-cloudwatch-observability \
     --query addon.addonVersion --output text
   ```

   For the Helm chart, run the following command.

   ```bash
   helm list -n amazon-cloudwatch
   ```

1. Update the queries, dashboards, and alarms that use the items in the previous list.

1. Upgrade the add-on or the Helm chart. Amazon EKS does not update the add-on to a new version on its own. To stay on 6.x with the add-on, do not update it, or pass a 6.x version to `--addon-version` when you update it. With Helm, `helm upgrade` without `--version` installs the latest chart. To stay on 6.x, pass `--version 6.7.0`.

1. After the upgrade, make sure that your dashboards show data and that your alarms are in the state that you expect.

## Getting started
<a name="container-insights-eks-otel-topics"></a>

Use the following topics to set up and configure OTel Container Insights on your Amazon EKS clusters.

**Topics**
+ [Quick start](container-insights-eks-otel-quickstart.md) — Get started with OTel Container Insights using the fastest setup path.
+ [Enable from the console](container-insights-eks-otel-console.md) — Enable OTel Container Insights through the AWS Management Console.
+ [Deploy with Helm](container-insights-eks-otel-helm.md) — Deploy OTel Container Insights using the Helm chart for flexible, GitOps-friendly management.
+ [Deploy with CloudFormation](container-insights-eks-otel-cfn.md) — Deploy OTel Container Insights using a CloudFormation template.
+ [Sending logs to Amazon CloudWatch](container-insights-eks-otel-logs.md) — Configure log collection for your Amazon EKS clusters.
+ [Advanced configuration](container-insights-eks-otel-advanced.md) — Customize and fine-tune OTel Container Insights for your environment.
+ [Correlating DRA-allocated devices to pods with OTel Container Insights](container-insights-eks-otel-dra.md) — Attribute the metrics of EFA and Neuron devices that DRA allocates to the pods that use them.
+ [Custom telemetry](eks-observability-addon-custom-telemetry.md) — Send your own application telemetry to CloudWatch over OTLP, and scrape ServiceMonitor and PodMonitor targets.
+ [OpenTelemetry service identity](eks-observability-addon-service-identity.md) — Give each of your services one consistent name across its telemetry.
+ [Standard telemetry attributes](eks-standard-telemetry-attributes.md) — See the resource attributes that the CloudWatch agent adds to your OpenTelemetry telemetry.
+ [Optimizing costs](eks-observability-addon-cost-controls.md) — Limit which namespaces, metrics, and Kubernetes labels the add-on sends.