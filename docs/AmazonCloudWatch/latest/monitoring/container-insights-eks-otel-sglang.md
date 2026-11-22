

# Collecting SGLang metrics with OTel Container Insights

SGLang is an open-source serving framework for large language models. You can run it as your own Kubernetes Deployment, or as the model server of a KServe InferenceService. Container Insights collects the metrics that each SGLang server exports on its `/metrics` endpoint. You don't need to label or annotate your pods.

The SGLang metrics also feed . For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

## Prerequisites
<a name="container-insights-eks-otel-sglang-prereqs"></a>

SGLang metrics collection is on by default when the following requirements are met.
+ Version 8.0.0 or later of the `amazon-cloudwatch-observability` add-on or Helm chart
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ One or more SGLang servers started with `--enable-metrics`. Without this flag, the agent still finds the server, but the scrape fails. To also collect the `sglang:estimated_*` counters, add `--enable-mfu-metrics`.

## Configuring SGLang metrics collection
<a name="container-insights-eks-otel-sglang-enable"></a>

To turn off SGLang metrics collection, set `otelContainerInsights.solutions.sglang.enabled` to `false`. To turn off all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`.

To turn off SGLang metrics with the Amazon EKS add-on, run the following AWS CLI command.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":true,"solutions":{"sglang":{"enabled":false}}}}' \
  --resolve-conflicts OVERWRITE
```

{{cluster-name}}  
Replace with the name of your Amazon EKS cluster.

`--configuration-values`  
Keeps OTel Container Insights on and sets `otelContainerInsights.solutions.sglang.enabled` to `false`.

`--resolve-conflicts OVERWRITE`  
Replaces the existing add-on configuration. To keep other settings, include them in the `--configuration-values` JSON.

To turn off SGLang metrics with the Helm chart, run the following command.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.sglang.enabled=false
```

## Which SGLang servers are scraped
<a name="container-insights-eks-otel-sglang-discovery"></a>

You get the metrics of an SGLang container, from the CloudWatch agent on its node, when either of the following applies:

KServe InferenceService pods  
The model container of each predictor pod, whatever its image. The agent scrapes each predictor once for both the vLLM and SGLang solutions, and this solution keeps the `sglang:*` series.

Other SGLang servers  
A container whose image name contains `sglang`, such as `lmsysorg/sglang` or a mirror of it. This includes the model container of a KServe LLMInferenceService. It excludes pods that KubeRay labels `ray.io/is-ray-node=yes`, which the Ray solution scrapes (see [Collecting Ray metrics with OTel Container Insights](container-insights-eks-otel-ray.md)).

The agent resolves the port in the following order, highest precedence first:

1. The serving runtime's `prometheus.kserve.io/port` annotation on KServe pods, with its `prometheus.kserve.io/path` annotation for the path

1. The port that the container declares

1. The server's default port, which is 8080 on KServe pods and otherwise 30000, the default of `sglang.launch_server`

The agent doesn't read scrape annotations from your pods. To collect the metrics of an SGLang server that it doesn't find, describe it with a PodMonitor (see [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md)).

## SGLang metric attributes
<a name="container-insights-eks-otel-sglang-attributes"></a>

Each metric carries the following resource attributes, in addition to the Kubernetes pod, namespace, workload, and node attributes:
+ `service.name` – The `resource.opentelemetry.io/service.name` pod annotation if it is set. Otherwise the InferenceService name for KServe pods, or the workload name. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).
+ `aws.service.type` – Always `ai_inference`. Use it to find model-serving telemetry without knowing the metric names.

## Querying SGLang metrics
<a name="container-insights-eks-otel-sglang-query"></a>

SGLang metric names contain a colon (`:`), so put the name in quotes inside the selector when you query it with PromQL. The following query returns the number of running requests for each model server in a cluster.

```
sum by ("@resource.service.name") ({"sglang:num_running_reqs", "@resource.k8s.cluster.name"="{{cluster-name}}"})
```

{{cluster-name}}  
Replace with the name of your Amazon EKS cluster.

`"sglang:num_running_reqs"`  
The metric name, in quotes because it contains a colon.

## Available metrics
<a name="container-insights-eks-otel-sglang-metrics"></a>

Container Insights collects every `sglang:*` metric that the server exports. The following list describes commonly used metrics.

`sglang:num_running_reqs`  
Requests currently running. Category: scheduler.

`sglang:num_queue_reqs`  
Requests in the waiting queue. Category: scheduler.

`sglang:token_usage`  
Fraction of the token pool in use. Category: cache.

`sglang:num_used_tokens`  
Tokens in use. Category: cache.

`sglang:cache_hit_rate`  
Prefix cache hit rate. Category: cache.

`sglang:gen_throughput`  
Generation throughput, in tokens per second. Category: tokens.

`sglang:prompt_tokens_total`  
Prompt (prefill) tokens processed. Category: tokens.

`sglang:generation_tokens_total`  
Tokens generated. Category: tokens.

`sglang:time_to_first_token_seconds`  
Time from request arrival to the first token. Category: latency.

`sglang:inter_token_latency_seconds`  
Time between generated tokens. Category: latency.

`sglang:e2e_request_latency_seconds`  
End-to-end request latency. Category: latency.

`sglang:estimated_flops_per_gpu_total`  
Estimated floating-point operations per GPU. Needs `--enable-mfu-metrics`. Category: utilization.

AWS doesn't publish a full list of SGLang metrics, because the SGLang project defines them. For the full list, see [Production Metrics](https://docs.sglang.ai/references/production_metrics.html) on the SGLang website.