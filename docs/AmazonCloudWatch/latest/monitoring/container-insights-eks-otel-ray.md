

# Collecting Ray metrics with OTel Container Insights

Ray is an open-source framework for distributed Python applications. On Kubernetes, KubeRay runs Ray clusters as `RayCluster`, `RayService`, and `RayJob` resources. Container Insights collects the metrics that each Ray node exports on its metrics port. One scrape covers the following metrics:
+ Ray core metrics, such as `ray_node_*`, `ray_tasks`, `ray_actors`, and `ray_object_store_memory`
+ Ray Serve metrics (`ray_serve_*`)
+ The engine metrics of Ray Serve LLM (`ray.serve.llm`), for vLLM (`ray_vllm_*`) and SGLang (`ray_sglang_*`)

The Ray metrics also feed . For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

## Prerequisites
<a name="container-insights-eks-otel-ray-prereqs"></a>

Ray metrics collection is on by default when the following requirements are met.
+ Version 8.0.0 or later of the `amazon-cloudwatch-observability` add-on or Helm chart
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ One or more Ray clusters that KubeRay manages

## Configuring Ray metrics collection
<a name="container-insights-eks-otel-ray-enable"></a>

To turn off Ray metrics collection, set `otelContainerInsights.solutions.ray.enabled` to `false`. To turn off all solutions at once, set `otelContainerInsights.solutions.enabled` to `false`.

To turn off Ray metrics with the Amazon EKS add-on, run the following AWS CLI command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```bash
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":true,"solutions":{"ray":{"enabled":false}}}}' \
  --resolve-conflicts OVERWRITE
```

To turn off Ray metrics with the Helm chart, run the following command.

```bash
helm upgrade amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  -n amazon-cloudwatch \
  --reuse-values \
  --set otelContainerInsights.solutions.ray.enabled=false
```

If another collector already scrapes your Ray pods, for example through `prometheus.io/scrape` annotations or a PodMonitor, the two collectors send the same series twice. Turn off one of them.

## Which Ray pods are scraped
<a name="container-insights-eks-otel-ray-discovery"></a>

The CloudWatch agent on each node scrapes every pod on that node that KubeRay labels `ray.io/is-ray-node=yes`, which are the head and worker pods of a `RayCluster`, `RayService`, or `RayJob`. It scrapes the container port named `metrics`. KubeRay declares port 8080 with that name on the Ray container when the pod template doesn't. You don't need to configure anything.

The agent scrapes pods, not Services, because a `RayService` puts its head pod behind two Services, and a Service scrape would count it twice.

A Ray container started with a custom `--metrics-export-port` and no port named `metrics` isn't found. Name its metrics port `metrics`.

Ray Serve LLM runs vLLM as a library, so its engine metrics arrive as `ray_vllm_*` through the Ray metrics port while its `log_engine_metrics` setting is on, which is the default. Other ways of running vLLM in a Ray pod, such as `vllm serve --distributed-executor-backend ray`, serve `vllm:*` metrics on their own port, which no solution scrapes. To collect them, describe that port with a PodMonitor (see [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md)).

## Ray metric attributes
<a name="container-insights-eks-otel-ray-attributes"></a>

`service.name` is the `resource.opentelemetry.io/service.name` pod annotation if it is set. KubeRay pods are owned by a `RayCluster`, which is not a workload kind, so without the annotation `service.name` is the pod name. To give a Ray cluster a stable name, set the annotation in the head and worker pod templates. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).

**Note**  
KubeRay sets `app.kubernetes.io/name` to `kuberay` on every Ray pod. With `otelServiceIdentity.useAppLabels` on, every Ray pod without the annotation is named `kuberay`. Set the annotation instead.

The following list describes the KubeRay pod labels that stay on every series as resource attributes. You can group metrics by them.

`k8s.pod.label.ray.io/cluster`  
The `RayCluster` name. For a `RayService` or `RayJob`, the resource name plus a generated suffix.

`k8s.pod.label.ray.io/node-type`  
The node type, `head` or `worker`.

`k8s.pod.label.ray.io/group`  
The worker group name, or `headgroup` on the head.

`k8s.pod.label.ray.io/serve`  
Whether the pod serves Ray Serve traffic. The value is `true` on pods that do.

The `ray_vllm_*` and `ray_sglang_*` series carry `aws.service.type` with the value `ai_inference`. Ray core and Ray Serve series don't, because a Ray cluster can run work that is not inference.

## Reading Ray metrics
<a name="container-insights-eks-otel-ray-reading"></a>
+ `ray_tasks` and `ray_actors` are reported per process, and partial values can be negative. Read them with `sum()`.
+ Engine metrics keep the engine's own names with a `ray_` prefix, and with `:` replaced by `_`. For example, vLLM's `vllm:num_requests_running` is `ray_vllm_num_requests_running`, and SGLang's `sglang:num_running_reqs` is `ray_sglang_num_running_reqs`. A dashboard that covers both a standalone engine and the same engine in Ray Serve must query both names.
+ Series carry the Ray labels `SessionName`, `NodeAddress`, `Component`, and `Version`. Ray Serve and engine series also carry `WorkerId` and `ReplicaId`. These change when a replica restarts, so each restart starts a new set of series. To reduce cardinality, set `RAY_metric_cardinality_level=low` to drop task and actor names from core metrics.
+ GPU metrics can show the wrong pod for Ray. The Ray `-gpu` images see every GPU on the node, so a Ray pod that requests no GPU, usually the head, can still run GPU work. To avoid this, set `num-gpus: "0"` in the head's `rayStartParams`, and set `NVIDIA_VISIBLE_DEVICES=void` on Ray pods that request no GPU.

The following query returns the CPU utilization of each Ray node in a cluster.

```
avg by ("@resource.k8s.pod.name") (ray_node_cpu_utilization{"@resource.k8s.cluster.name"="{{cluster-name}}"})
```

{{cluster-name}}  
Replace with the name of your Amazon EKS cluster.

For the metrics that Ray exports, see [System Metrics](https://docs.ray.io/en/latest/ray-observability/reference/system-metrics.html) and [Monitor Your Application](https://docs.ray.io/en/latest/serve/monitoring.html) on the Ray website.