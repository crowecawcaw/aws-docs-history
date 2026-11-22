

# Collecting KServe metrics with OTel Container Insights

KServe is an open-source model serving platform for Kubernetes. You describe a model in an InferenceService resource, and the KServe controller creates and maintains the pods that serve it. Container Insights collects the controller's own metrics, so you can see whether KServe is reconciling your InferenceServices.

KServe metrics help you answer operational questions such as:
+ Is the KServe controller reconciling InferenceServices, and how many reconciles fail?
+ How long do reconciles take?
+ Is the controller's admission webhook handling requests?

The KServe controller is not in the request path. Metrics about the requests that a model serves come from the model server and, in KServe Serverless mode, from the Knative queue-proxy. See [Collecting vLLM metrics with OTel Container Insights](container-insights-eks-otel-vllm.md) and [Collecting Knative Serving metrics with OTel Container Insights](container-insights-eks-otel-knative.md).

## Prerequisites
<a name="container-insights-eks-otel-kserve-prereqs"></a>

KServe metrics collection is enabled by default when the following requirements are met.
+ Amazon EKS cluster running Kubernetes 1.28 or later
+ KServe installed and running in the cluster (default namespace: `kserve`)
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ The `amazon-cloudwatch-observability` add-on in `ACTIVE` status

## Configuring KServe metrics collection
<a name="container-insights-eks-otel-kserve-enable"></a>

KServe metrics collection is enabled by default. If you already have OTel Container Insights enabled (`otelContainerInsights.enabled: true`) and KServe is running in your cluster, metrics start flowing automatically with no additional configuration. If KServe is not installed, the pipeline finds no target and does nothing.

If KServe runs in a namespace other than `kserve`, set `otelContainerInsights.solutions.kserve.controlPlane.namespace` to that namespace. To disable KServe metrics collection, set `otelContainerInsights.solutions.kserve.controlPlane.enabled` to `false`. To disable all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`.

The following Helm values show the default configuration.

```yaml
otelContainerInsights:
  solutions:
    enabled: true
    kserve:
      controlPlane:
        enabled: true
        namespace: kserve
```

To disable KServe metrics using the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"solutions":{"kserve":{"controlPlane":{"enabled":false}}}}}' \
  --resolve-conflicts OVERWRITE
```

To disable KServe metrics using the Helm chart, run the following command.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.kserve.controlPlane.enabled=false
```

After you enable KServe metrics, the CloudWatch agent cluster scraper finds the `kserve-controller-manager` pod by the label `control-plane: kserve-controller-manager`. The controller serves its metrics only on `127.0.0.1:8080`, so the agent scrapes them every 30 seconds through the controller's kube-rbac-proxy on port 8443, using its service account token.

## KServe metrics pipeline architecture
<a name="container-insights-eks-otel-kserve-architecture"></a>

The KServe metrics pipeline uses the following data flow:

1. The Prometheus receiver in the cluster scraper discovers the KServe controller pod using Kubernetes service discovery.

1. The receiver scrapes the controller's metrics. The pipeline keeps the controller's `controller_runtime_*` and `leader_election_*` metrics. It drops the `workqueue_*` and `rest_client_*` metrics, which the API server pipeline already collects.

1. The OpenTelemetry processor chain attributes each metric to the controller pod and its Deployment, and adds cloud resource attributes.

1. The exporter sends the enriched metrics to CloudWatch through OTLP.

The KServe pipeline runs independently from other metric pipelines. A failure in one pipeline does not affect the others.

**Note**  
KServe metrics are cluster-scoped.

## Available metrics
<a name="container-insights-eks-otel-kserve-metrics"></a>

The following table lists the KServe metrics that Container Insights collects.


| Metric name | Category | Description | 
| --- | --- | --- | 
| controller\_runtime\_reconcile\_total | Reconcile | Reconciles, by controller and result | 
| controller\_runtime\_reconcile\_errors\_total | Reconcile | Reconciles that returned an error, by controller | 
| controller\_runtime\_terminal\_reconcile\_errors\_total | Reconcile | Reconcile errors that are not retried, by controller | 
| controller\_runtime\_reconcile\_panics\_total | Reconcile | Reconciles that panicked, by controller | 
| controller\_runtime\_reconcile\_time\_seconds | Reconcile | Reconcile duration, by controller | 
| controller\_runtime\_active\_workers | Workers | Workers currently reconciling, by controller | 
| controller\_runtime\_max\_concurrent\_reconciles | Workers | Maximum concurrent reconciles, by controller | 
| controller\_runtime\_webhook\_requests\_total | Webhook | Admission webhook requests, by webhook and status code | 
| controller\_runtime\_webhook\_requests\_in\_flight | Webhook | Admission webhook requests in progress | 
| controller\_runtime\_webhook\_latency\_seconds | Webhook | Admission webhook latency | 
| controller\_runtime\_webhook\_panics\_total | Webhook | Admission webhook requests that panicked | 
| controller\_runtime\_conversion\_webhook\_panics\_total | Webhook | Conversion webhook requests that panicked | 
| leader\_election\_master\_status | Controller Health | 1 if this controller replica is the leader, 0 otherwise | 