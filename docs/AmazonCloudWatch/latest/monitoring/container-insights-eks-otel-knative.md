

# Collecting Knative Serving metrics with OTel Container Insights

Knative Serving is an open-source platform that runs request-driven services on Kubernetes and scales them with load, including to zero. KServe uses it in its default Serverless mode: each InferenceService becomes a Knative service. Container Insights collects two kinds of Knative metrics:
+ **Data plane** – Request metrics from the queue-proxy sidecar that Knative adds to every revision pod. Each request to the service passes through it.
+ **Control plane** – Metrics from the Knative autoscaler, activator, controller, and webhook.

Knative metrics help you answer operational questions such as:
+ How many requests does each service or model receive, and how long do they take?
+ How many pods does the autoscaler want, and how many are ready?
+ Is a revision in panic mode because of a traffic spike?

For the model server's own metrics, see [Collecting vLLM metrics with OTel Container Insights](container-insights-eks-otel-vllm.md). For the KServe controller, see [Collecting KServe metrics with OTel Container Insights](container-insights-eks-otel-kserve.md).

## Prerequisites
<a name="container-insights-eks-otel-knative-prereqs"></a>

Knative metrics collection is enabled by default when the following requirements are met.
+ Amazon EKS cluster running Kubernetes 1.28 or later
+ Knative Serving installed and running in the cluster (default namespace: `knative-serving`)
+ On Knative Serving 1.19 and later, Knative configured to serve Prometheus metrics (see [Turning on metrics in Knative Serving 1.19 and later](#container-insights-eks-otel-knative-119))
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ The `amazon-cloudwatch-observability` add-on in `ACTIVE` status

## Configuring Knative metrics collection
<a name="container-insights-eks-otel-knative-enable"></a>

Data plane and control plane collection are both enabled by default, and you can turn each off separately. If Knative is not installed, the pipelines find no targets and do nothing.
+ `otelContainerInsights.solutions.knative.dataPlane.enabled` – Turns queue-proxy request metrics on or off. To collect them from one namespace only, set `dataPlane.namespace`. Empty means all namespaces.
+ `otelContainerInsights.solutions.knative.controlPlane.enabled` – Turns component metrics on or off. If Knative Serving runs in a namespace other than `knative-serving`, set `controlPlane.namespace`.

To disable all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`. The following Helm values show the default configuration.

```yaml
otelContainerInsights:
  solutions:
    enabled: true
    knative:
      dataPlane:
        enabled: true
        namespace: ""
      controlPlane:
        enabled: true
        namespace: knative-serving
```

To disable Knative metrics using the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"solutions":{"knative":{"dataPlane":{"enabled":false},"controlPlane":{"enabled":false}}}}}' \
  --resolve-conflicts OVERWRITE
```

To disable Knative metrics using the Helm chart, run the following command.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.knative.dataPlane.enabled=false \
  --set otelContainerInsights.solutions.knative.controlPlane.enabled=false
```

After you enable Knative metrics, the CloudWatch agent scrapes the following targets every 30 seconds:
+ Data plane – On each node, the queue-proxy of every revision pod on that node (pods with the label `serving.knative.dev/revision`), on the port named `http-usermetric` (9091).
+ Control plane – From the cluster scraper, the autoscaler, activator, controller, and webhook pods, on the port named `metrics` (9090).

## Turning on metrics in Knative Serving 1.19 and later
<a name="container-insights-eks-otel-knative-119"></a>

Knative Serving 1.19 moved to the OpenTelemetry SDK and exports no metrics by default: ports 9090 and 9091 refuse connections until Knative is told to serve Prometheus metrics. The `metrics-protocol` setting covers the control plane, and `request-metrics-protocol` covers the queue-proxy. To turn both on, run the following commands.

```bash
kubectl -n knative-serving patch configmap config-observability --type merge \
  -p '{"data":{"metrics-protocol":"prometheus","request-metrics-protocol":"prometheus"}}'
kubectl -n knative-serving rollout restart deployment
```

The components read `metrics-protocol` only at startup, so the command restarts them. The queue-proxy setting applies to revision pods that start after the change.

Knative Serving 1.19 also renamed its metrics with a `kn` prefix, for example `autoscaler_desired_pods` became `kn_revision_pods_desired`. Container Insights collects both name sets, so the metric names in CloudWatch depend on the Knative version that you run.

## Knative metrics pipeline architecture
<a name="container-insights-eks-otel-knative-architecture"></a>

Each Knative pipeline uses the following data flow:

1. The Prometheus receiver discovers the Knative pods using Kubernetes service discovery: on each node for the data plane, and in the cluster scraper for the control plane.

1. The receiver scrapes each pod's metrics. The data plane pipeline keeps request metrics (`kn_serving_*`, or `revision_*` request metrics on Knative Serving 1.18 and earlier). The control plane pipeline drops Go runtime, process, and `promhttp_*` metrics.

1. The OpenTelemetry processor chain attributes each metric to its pod and Deployment, and adds cloud resource attributes. Data plane metrics from the predictor of a KServe InferenceService also carry `aws.service.type` set to `ai_inference`.

1. The exporter sends the enriched metrics to CloudWatch through OTLP.

Which metrics exist depends on the KServe deployment mode. In Serverless mode, the default, all of them are present. In RawDeployment mode, KServe does not use Knative, so there are no Knative metrics. Use the model server's metrics and the horizontal pod autoscaler metrics from kube-state-metrics instead.

**Note**  
Data plane metrics are pod-scoped. Control plane metrics are cluster-scoped.

## Istio sidecars with strict mutual TLS
<a name="container-insights-eks-otel-knative-istio"></a>

KServe and Knative do not inject Istio sidecars into revision pods by default. If you turn on sidecar injection in a namespace and enforce `STRICT` mutual TLS, the sidecar rejects the agent's plain HTTP scrape, because the agent is not part of the mesh. Allow plain text on the metrics port of those pods. The following example does this for KServe predictor pods. Replace {{model-namespace}} with the namespace of your models.

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: allow-metrics-scrape
  namespace: {{model-namespace}}
spec:
  selector:
    matchLabels:
      component: predictor
  mtls:
    mode: STRICT
  portLevelMtls:
    9091:
      mode: PERMISSIVE
```

Port-level settings take effect only with a workload selector.

## Available metrics
<a name="container-insights-eks-otel-knative-metrics"></a>

The following table lists commonly used Knative metrics, with their Knative Serving 1.19 and later names.


| Metric name | Category | Description | 
| --- | --- | --- | 
| kn\_serving\_invocation\_duration\_seconds | Data plane | Duration of requests through the queue-proxy, by response code | 
| kn\_revision\_request\_concurrency | Autoscaling | Concurrent requests that the autoscaler observes per revision | 
| kn\_revision\_concurrency\_stable | Autoscaling | Average concurrency over the stable window | 
| kn\_revision\_concurrency\_panic | Autoscaling | Average concurrency over the panic window | 
| kn\_revision\_concurrency\_target | Autoscaling | Target concurrency per pod | 
| kn\_revision\_panic\_mode | Autoscaling | 1 if the revision is in panic mode, 0 otherwise | 
| kn\_revision\_pods\_desired | Autoscaling | Pods that the autoscaler wants | 
| kn\_revision\_pods\_requested | Autoscaling | Pods requested from Kubernetes | 
| kn\_revision\_pods\_count | Autoscaling | Pods that exist for the revision | 
| kn\_revision\_pods\_not\_ready\_count | Autoscaling | Pods that are not ready | 
| kn\_revision\_pods\_pending\_count | Autoscaling | Pods that are pending | 
| kn\_revision\_capacity\_excess | Autoscaling | Spare request capacity beyond the target burst capacity | 
| kn\_activator\_stats\_conn\_reachable | Activator | Whether the activator can reach the autoscaler | 
| kn\_autoscaler\_scrape\_duration\_seconds | Autoscaler | Time the autoscaler takes to collect revision metrics | 
| kn\_workqueue\_depth | Controller | Items waiting in a controller work queue | 
| kn\_workqueue\_retries\_total | Controller | Work queue retries | 
| kn\_workqueue\_process\_duration\_seconds | Controller | Time to process an item from a work queue | 
| kn\_webhook\_handler\_duration\_seconds | Webhook | Webhook request duration | 