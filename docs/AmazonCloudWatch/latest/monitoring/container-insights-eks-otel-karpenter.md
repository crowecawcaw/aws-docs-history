

# Collecting Karpenter metrics with OTel Container Insights
<a name="container-insights-eks-otel-karpenter"></a>

Karpenter is the recommended node autoscaler for Amazon EKS. Container Insights collects Karpenter metrics through Prometheus scraping. With Container Insights, you gain built-in visibility into node provisioning, scaling speed, and resource use. You do not need to set up Prometheus or Grafana manually.

Karpenter metrics help you answer operational questions such as:
+ Why is my pod pending?
+ How fast is Karpenter provisioning nodes?
+ Is consolidation working effectively?

## Prerequisites
<a name="container-insights-eks-otel-karpenter-prereqs"></a>

Karpenter metrics collection is enabled by default when the following requirements are met.
+ Amazon EKS cluster running Kubernetes 1.28 or later
+ Karpenter installed and running in the cluster (default namespace: `kube-system`)
+ OTel Container Insights enabled on the cluster (see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md))
+ The `amazon-cloudwatch-observability` add-on in `ACTIVE` status

## Configuring Karpenter metrics collection
<a name="container-insights-eks-otel-karpenter-enable"></a>

Karpenter metrics collection is enabled by default. If you already have OTel Container Insights enabled (`otelContainerInsights.enabled: true`) and Karpenter is running in your cluster, metrics start flowing automatically with no additional configuration.

If the Karpenter scrape target is not present in the cluster, the pipeline finds no pods and does nothing.

To disable Karpenter metrics collection, set `otelContainerInsights.solutions.karpenter.enabled` to `false`. To disable all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`. The global toggle overrides individual solution settings. If `solutions.enabled` is `false`, no solutions collect metrics, even if their individual `enabled` flag is `true`.

The following Helm values show the default configuration.

```
otelContainerInsights:
  solutions:
    enabled: true
    karpenter:
      enabled: true
```

To disable Karpenter metrics using the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"solutions":{"karpenter":{"enabled":false}}}}' \
  --resolve-conflicts OVERWRITE
```

To disable Karpenter metrics using the Helm chart, run the following command.

```
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.karpenter.enabled=false
```

After you enable Karpenter metrics, the CloudWatch agent finds Karpenter pods by the label `app.kubernetes.io/name=karpenter`. It scrapes the `/metrics` endpoint on the port named `http-metrics` (default 8080) every 30 seconds.

## Karpenter metrics pipeline architecture
<a name="container-insights-eks-otel-karpenter-architecture"></a>

The Karpenter metrics pipeline uses the following data flow:

1. The Prometheus receiver discovers Karpenter pods using Kubernetes service discovery.

1. The receiver scrapes the `/metrics` endpoint on each Karpenter pod.

1. The OpenTelemetry processor chain adds Kubernetes and cloud resource labels to each metric.

1. The exporter sends the enriched metrics to CloudWatch through OTLP.

The Karpenter pipeline runs independently from other metric pipelines (API server, Kube State Metrics, cAdvisor). This means a failure in one pipeline does not affect the others. If the Karpenter scrape target goes down, other pipelines keep working.

**Note**  
Karpenter metrics are cluster-scoped.

## Viewing the Karpenter dashboard
<a name="container-insights-eks-otel-karpenter-dashboard"></a>

After you turn on Karpenter metrics, you can view the dashboard in the CloudWatch console.

**To view the Karpenter dashboard**

1. Open the CloudWatch console at [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Container Insights**, then choose **Performance monitoring**.

1. For **Service**, choose **EKS OTEL**.

1. In the navigation pane, expand **Solutions** and choose **Karpenter**.

The dashboard displays 30 metrics organized into 8 categories: Pod Scheduling, Node Resources, Cluster State, NodePool, Cloud Provider, Disruption, Interruption, and Controller Health.

## Available metrics
<a name="container-insights-eks-otel-karpenter-metrics"></a>

The following table lists the 30 Karpenter metrics that Container Insights collects.


| Metric name | Category | Description | 
| --- | --- | --- | 
| karpenter\_pods\_state | Pod Scheduling | Number of pods by state (phase label) | 
| karpenter\_pods\_bound\_duration\_seconds | Pod Scheduling | Time for pods to reach bound state | 
| karpenter\_nodes\_allocatable | Node Resources | Allocatable resources per node by resource type | 
| karpenter\_nodes\_total\_daemon\_requests | Node Resources | Total resource requests from DaemonSet pods | 
| karpenter\_nodes\_total\_daemon\_limits | Node Resources | Total resource limits from DaemonSet pods | 
| karpenter\_nodes\_total\_pod\_requests | Node Resources | Total resource requests from all pods | 
| karpenter\_nodes\_total\_pod\_limits | Node Resources | Total resource limits from all pods | 
| karpenter\_nodes\_system\_overhead | Node Resources | Resources reserved for system daemons | 
| karpenter\_nodes\_current\_lifetime\_seconds | Node Resources | Current age of each node in seconds | 
| karpenter\_cluster\_state\_node\_count | Cluster State | Number of nodes tracked in Karpenter cluster state | 
| karpenter\_cluster\_state\_synced | Cluster State | Whether cluster state is synced (1=synced, 0=unsynced) | 
| karpenter\_cluster\_state\_unsynced\_time\_seconds | Cluster State | Duration cluster state has been unsynced | 
| karpenter\_cluster\_utilization\_percent | Cluster State | Percentage of allocatable resources used by pod requests | 
| karpenter\_nodepools\_limit | NodePool | Configured resource limits per NodePool | 
| karpenter\_nodepools\_usage | NodePool | Current resource usage per NodePool | 
| karpenter\_cloudprovider\_duration\_seconds | Cloud Provider | Cloud provider API call latency by method | 
| karpenter\_cloudprovider\_instance\_type\_cpu\_cores | Cloud Provider | Available vCPU cores per instance type | 
| karpenter\_cloudprovider\_instance\_type\_memory\_bytes | Cloud Provider | Available memory per instance type | 
| karpenter\_cloudprovider\_instance\_type\_offering\_available | Cloud Provider | Whether an instance type offering is available | 
| karpenter\_cloudprovider\_instance\_type\_offering\_price\_estimate | Cloud Provider | Estimated hourly price per instance type offering | 
| karpenter\_voluntary\_disruption\_eligible\_nodes | Disruption | Nodes eligible for voluntary disruption by reason | 
| karpenter\_voluntary\_disruption\_consolidation\_timeouts\_total | Disruption | Number of consolidation evaluation timeouts | 
| karpenter\_voluntary\_disruption\_decision\_evaluation\_duration\_seconds | Disruption | Time to evaluate disruption decisions | 
| karpenter\_nodes\_created\_total | Node Resources | Total nodes created by Karpenter | 
| karpenter\_nodes\_terminated\_total | Node Resources | Total nodes terminated by Karpenter (by reason) | 
| karpenter\_interruption\_received\_messages\_total | Interruption | SQS interruption messages received (spot, rebalance, etc.) | 
| karpenter\_interruption\_deleted\_messages\_total | Interruption | SQS interruption messages deleted/processed | 
| controller\_runtime\_reconcile\_errors\_total | Controller Health | Total reconciliation errors across controllers | 
| workqueue\_depth | Controller Health | Current depth of the controller work queue | 
| leader\_election\_master\_status | Controller Health | Whether this instance is the elected leader (1=leader, 0=standby) | 