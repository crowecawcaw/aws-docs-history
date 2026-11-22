

# Collecting vLLM metrics with OTel Container Insights

vLLM is an open-source inference engine that serves large language models through an OpenAI-compatible API. You can run it as your own Kubernetes Deployment, or as the model server of a KServe InferenceService. Container Insights collects the metrics that each vLLM server exports on its `/metrics` endpoint. You do not need to set up Prometheus or Grafana manually, and you do not need to label or annotate your pods.

vLLM metrics help you answer operational questions such as:
+ How many requests is each model server running, and how many are waiting?
+ How long do users wait for the first token, and how fast are the following tokens generated?
+ Is the KV cache close to full, and are requests being preempted?
+ How many prompt and generation tokens does each model process?

For the other parts of a KServe deployment, see [Collecting KServe metrics with OTel Container Insights](container-insights-eks-otel-kserve.md) and [Collecting Knative Serving metrics with OTel Container Insights](container-insights-eks-otel-knative.md).

## Prerequisites
<a name="container-insights-eks-otel-vllm-prereqs"></a>

vLLM metrics collection is enabled by default when the following requirements are met.
+ Amazon EKS cluster running Kubernetes 1.28 or later
+ One or more vLLM servers running in the cluster
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ The `amazon-cloudwatch-observability` add-on in `ACTIVE` status

## Configuring vLLM metrics collection
<a name="container-insights-eks-otel-vllm-enable"></a>

vLLM metrics collection is enabled by default. If you already have OTel Container Insights enabled (`otelContainerInsights.enabled: true`) and vLLM servers are running in your cluster, metrics start flowing automatically with no additional configuration. If the cluster runs no vLLM server, the pipeline finds no targets and does nothing.

To disable vLLM metrics collection, set `otelContainerInsights.solutions.vllm.enabled` to `false`. To disable all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`. The global toggle overrides individual solution settings.

The following Helm values show the default configuration.

```yaml
otelContainerInsights:
  solutions:
    enabled: true
    vllm:
      enabled: true
```

To disable vLLM metrics using the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"solutions":{"vllm":{"enabled":false}}}}' \
  --resolve-conflicts OVERWRITE
```

To disable vLLM metrics using the Helm chart, run the following command.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.vllm.enabled=false
```

## Which vLLM servers are scraped
<a name="container-insights-eks-otel-vllm-discovery"></a>

The CloudWatch agent on each node scrapes the vLLM servers on that node, every 30 seconds. It finds a container if either of the following applies:
+ **KServe** – The container named `kserve-container` in an InferenceService's predictor pods, which carry the labels `serving.kserve.io/inferenceservice` and `component: predictor`, whatever its image. Transformer and explainer pods are not scraped, and neither is the Knative queue-proxy sidecar, which serves the model server's metrics a second time.
+ **Other vLLM servers** – Any container whose image name contains `vllm`, such as `vllm/vllm-openai` or a mirror of it.

The agent resolves the port in the following order, highest precedence first:

1. On KServe pods, the serving runtime's `prometheus.kserve.io/port` annotation, and its `prometheus.kserve.io/path` annotation for the path

1. The port that the container declares

1. The server's default: 8080 on KServe pods, otherwise 8000, the default of `vllm serve`

The agent does not read `prometheus.io/scrape` or other scrape annotations from your pods. A vLLM server outside KServe that runs from an image without `vllm` in its name is not found automatically. To collect its metrics, describe it with a PodMonitor (see [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md)).

Pods that KubeRay labels `ray.io/is-ray-node=yes` are left to the Ray solution, which collects the engine metrics of Ray Serve LLM as `ray_vllm_*` (see [Collecting Ray metrics with OTel Container Insights](container-insights-eks-otel-ray.md)).

## vLLM metrics pipeline architecture
<a name="container-insights-eks-otel-vllm-architecture"></a>

The vLLM metrics pipeline uses the following data flow:

1. The Prometheus receiver on each node discovers that node's vLLM containers using Kubernetes service discovery.

1. The receiver scrapes each container's metrics endpoint. The pipeline keeps the engine's `vllm:*` metrics and the API server's `http_*` metrics, and drops the Python runtime's `python_*` and `process_*` metrics.

1. The OpenTelemetry processor chain adds Kubernetes and cloud resource attributes to each metric.

1. The exporter sends the enriched metrics to CloudWatch through OTLP.

Each metric carries the following resource attributes, in addition to the Kubernetes pod, namespace, workload, and node attributes:
+ `service.name` – The InferenceService name for KServe pods. Otherwise the workload name (Deployment, StatefulSet, DaemonSet, or Job), or the pod name if the pod has no workload.
+ `aws.service.type` – Always `ai_inference`. Use it to find model-serving telemetry without knowing the metric names.

The vLLM pipeline runs independently from other metric pipelines. A failure in one pipeline does not affect the others.

**Note**  
vLLM metrics are pod-scoped: each vLLM pod produces its own series.

## Querying vLLM metrics
<a name="container-insights-eks-otel-vllm-query"></a>

vLLM metric names contain a colon (`:`), so put the name in quotes inside the selector when you query it with PromQL. The following query returns the number of running requests for each model server in a cluster. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
sum by ("@resource.service.name") ({"vllm:num_requests_running", "@resource.k8s.cluster.name"="{{cluster-name}}"})
```

## Available metrics
<a name="container-insights-eks-otel-vllm-metrics"></a>

Container Insights collects every `vllm:*` and `http_*` metric that the server exports. The following table lists commonly used metrics. The names are those of the vLLM V1 engine (vLLM 0.10.2 and later); earlier versions export some metrics under other names, which are collected as well.


| Metric name | Category | Description | 
| --- | --- | --- | 
| vllm:num\_requests\_running | Scheduler | Requests currently being processed | 
| vllm:num\_requests\_waiting | Scheduler | Requests waiting to be processed | 
| vllm:kv\_cache\_usage\_perc | Cache | Fraction of the KV cache in use, from 0 to 1 | 
| vllm:num\_preemptions\_total | Cache | Requests preempted because the KV cache was full | 
| vllm:prefix\_cache\_queries\_total | Cache | Tokens looked up in the prefix cache | 
| vllm:prefix\_cache\_hits\_total | Cache | Tokens found in the prefix cache | 
| vllm:prompt\_tokens\_total | Tokens | Prompt tokens processed | 
| vllm:generation\_tokens\_total | Tokens | Tokens generated | 
| vllm:request\_success\_total | Requests | Finished requests, by finished\_reason | 
| vllm:time\_to\_first\_token\_seconds | Latency | Time from request arrival to the first generated token | 
| vllm:inter\_token\_latency\_seconds | Latency | Time between generated tokens | 
| vllm:e2e\_request\_latency\_seconds | Latency | End-to-end request latency | 
| vllm:request\_queue\_time\_seconds | Latency | Time a request spent waiting before processing started | 
| vllm:request\_prefill\_time\_seconds | Latency | Time spent processing the prompt | 
| vllm:request\_decode\_time\_seconds | Latency | Time spent generating tokens | 
| http\_requests\_total | API server | HTTP requests, by handler, method, and status | 
| http\_request\_duration\_seconds | API server | HTTP request duration, by handler and method | 