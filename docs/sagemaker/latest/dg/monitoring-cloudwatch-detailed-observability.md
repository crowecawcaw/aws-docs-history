

# Amazon SageMaker AI detailed observability for inference endpoints
<a name="monitoring-cloudwatch-detailed-observability"></a>

Detailed observability is a next-generation metrics experience for Amazon SageMaker AI real-time inference endpoints. Built on OpenTelemetry (OTel), it collects fine-grained operational metrics from GPU, node, and inference framework layers and publishes them to Amazon CloudWatch with rich labels including endpoint name, inference component name, instance ID, availability zone, and instance type.

## Key capabilities
<a name="detailed-observability-capabilities"></a>
+ **OpenTelemetry-native collection**. Metrics are collected using an OTel Collector that scrapes Prometheus endpoints from DCGM (GPU metrics), node exporters (CPU, memory, disk), and inference framework containers (vLLM, SGLang).
+ **Rich dimensional labels**. Every metric is published with labels such as `aws.sagemaker.endpoint.name`, `aws.sagemaker.inference_component.name`, `@resource.host.id`, `@resource.cloud.availability_zone`, and `@resource.host.type` for precise filtering and aggregation.
+ **Per-GPU attribution**. GPU metrics (DCGM) include per-inference-component attribution, allowing you to identify which model is consuming GPU resources on multi-tenant instances.
+ **Inference framework metrics**. Native vLLM and SGLang metrics — including tokens per second, time to first token (TTFT), inter-token latency, KV cache utilization, queue depth, and batch size — are available without custom instrumentation.
+ **PromQL query support**. Query metrics using PromQL syntax in Amazon CloudWatch, CloudWatch Query Studio, or Amazon Managed Grafana.
+ **Configurable scrape frequency**. Control how often metrics are collected using `MetricPublishFrequencyInSeconds` (valid values: 10, 30, 60, 120, 180, 240, 300 seconds). Defaults to 60 seconds. Control plane metrics such as lifecycle, autoscaling, and ICE diagnostics are event-driven and not affected by this setting.

**Note**  
Detailed observability publishes OpenTelemetry (OTel) metrics to Amazon CloudWatch via OTLP. These are *not* Prometheus metrics. The metrics are natively stored in Amazon CloudWatch as OTel metric data and are queryable using PromQL syntax. PromQL is supported as a query language only — no Prometheus server or Prometheus-compatible backend is involved.

## What's included
<a name="detailed-observability-whats-included"></a>


**Detailed observability metric categories**  

| Category | Metrics | Scope | Frequency | 
| --- | --- | --- | --- | 
| Inference framework (vLLM/SGLang) | TTFT, ITL, KV cache, queue depth, batch size, TPS, concurrent requests | Per-IC for inference component endpoints, per-instance/per-endpoint for SME | Configurable | 
| GPU health (DCGM) | GPU utilization, memory copy utilization, GPU temperature | Per-instance, per-GPU | Configurable | 
| Node health | CPU, memory, disk, filesystem | Per-instance | Configurable | 
| Inference component placement and high availability | IC copy count, copies per AZ, AZ skew, IC per instance, instances per AZ | Per-endpoint | Periodic | 
| Lifecycle | Model download time, GPU load time, container start, cold start | Per-IC, per-endpoint | Event-driven | 
| Autoscaling | Scaling events, E2E latency, rebalancing | Per-endpoint | Event-driven | 
| ICE diagnostics | ICE count, failed type, failed AZ | Per-endpoint | Event-driven | 

For the complete list, see [OpenTelemetry metrics reference](inference-monitoring.md).

## Architecture and data flow
<a name="detailed-observability-architecture"></a>

![Architecture diagram showing the metric collection pipeline for detailed observability.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/SageMaker Observability/Observability_Architecture.png)


Each endpoint instance exposes metrics from multiple sources. The OTel Collector scrapes these sources, enriches the data with context labels, and exports it to your Amazon CloudWatch account.

1. **Model container**, **DCGM exporter**, and **node exporter** expose Prometheus-compatible metrics on the instance (inference framework metrics, GPU metrics, and CPU/memory/disk metrics respectively).

1. **OTel Collector** scrapes these endpoints and enriches each metric with labels such as endpoint name, inference component name, instance ID, and availability zone.

1. Enriched metrics are exported via OTLP to Amazon CloudWatch in your account.

1. Metrics are queryable via PromQL in Amazon CloudWatch at `https://monitoring.{{region}}.amazonaws.com`.

## Pricing
<a name="detailed-observability-pricing"></a>

Detailed observability metrics are included at no additional cost. For information about Amazon CloudWatch data ingestion costs related to OTel enrichment, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).