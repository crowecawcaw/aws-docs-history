# CloudWatch SageMaker AI Insights

Use CloudWatch SageMaker AI Insights to monitor and troubleshoot SageMaker AI inference endpoints at scale. The dashboard
displays curated metrics and visualizations across three views—**Performance**,
**Capacity**, and **Reliability**—so you can quickly identify
issues, optimize resource utilization, and make sure high availability across your endpoints.

SageMaker AI Insights supports monitoring across endpoint types (single‐model endpoints and inference
component (IC)‐based endpoints) and inference frameworks (vLLM, SGLang, TensorRT‐LLM).

To get started with SageMaker AI Insights, see the following topics.

###### Topics

- [Get started with CloudWatch SageMaker AI Insights](SageMaker-AI-Insights-Get-Started.md "SageMaker-AI-Insights-Get-Started.md")
- [SageMaker AI Insights dashboard](SageMaker-AI-Insights-Dashboard.md "SageMaker-AI-Insights-Dashboard.md")
- [SageMaker AI Insights OpenTelemetry metrics reference](SageMaker-AI-Insights-Metrics.md "SageMaker-AI-Insights-Metrics.md")
- [Troubleshooting SageMaker AI Insights](SageMaker-AI-Insights-Troubleshooting.md "SageMaker-AI-Insights-Troubleshooting.md")

## Key capabilities

- **OpenTelemetry‐native collection.** Metrics are
  collected using an OTel Collector that scrapes Prometheus endpoints from DCGM (GPU metrics), node
  exporters (CPU, memory, disk), and inference framework containers (vLLM, SGLang).
- **Rich dimensional labels.** Every metric includes
  labels such as `aws.sagemaker.endpoint.name`,
  `aws.sagemaker.inference_component.name`, `@resource.host.id`,
  `@resource.cloud.availability_zone`, and `@resource.host.type`.
- **Per‐GPU attribution.** GPU metrics (DCGM)
  include per‐inference‐component attribution for multi‐tenant instances.
- **Inference framework metrics.** Native vLLM and SGLang
  metrics—tokens per second, time to first token (TTFT), inter‐token latency, KV cache
  utilization, queue depth, batch size—without custom instrumentation.
- **PromQL query support.** Query in CloudWatch, CloudWatch Query
  Studio, or Amazon Managed Grafana.
- **Configurable scrape frequency.** Set through
  `MetricPublishFrequencyInSeconds` (10, 30, 60, 120, 180, 240, or 300 seconds; default
  60). Control plane metrics are event‐driven.

## Architecture and data flow

1. The **model container**, **DCGM
   exporter**, and **node exporter** expose
   Prometheus‐compatible metrics on the instance.
2. The **OTel Collector** scrapes these endpoints and
   enriches each metric with labels (endpoint name, IC name, instance ID, AZ).
3. Enriched metrics are **exported through OTLP** to
   CloudWatch.
4. Metrics are **queryable through PromQL** in
   CloudWatch.

```
┌─────────────────────────────────────────────────────────────────┐
│  SageMaker Endpoint Instance                                      │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐    │
│  │ Model        │  │ DCGM         │  │ Node Exporter        │    │
│  │ Container    │  │ Exporter     │  │ (CPU/Mem/Disk)       │    │
│  │ (vLLM/SGLang)│  │ (GPU)        │  │                      │    │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘    │
│         │                 │                     │                 │
│         └─────────────────┼─────────────────────┘                 │
│                           ▼                                       │
│              ┌─────────────────────────┐                          │
│              │   OTel Collector        │                          │
│              │   (scrape + enrich)     │                          │
│              └────────────┬────────────┘                          │
└───────────────────────────┼───────────────────────────────────────┘
                            │ OTLP
                            ▼
              ┌─────────────────────────┐
              │   Amazon CloudWatch     │
              │   (PromQL-queryable)    │
              └─────────────────────────┘
```

## How to access

You can open SageMaker AI Insights from the SageMaker AI console by using any of the following paths.

| Source                                             | Action                                   | Destination                                            |
| -------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------ |
| SageMaker AI console → *_Endpoints_<br>• list      | Choose **Open SageMaker AI Insights**    | Fleet‐level dashboard (no filter)                      |
| SageMaker AI console → endpoint detail page        | Choose **View in SageMaker AI Insights** | Dashboard filtered to that endpoint                    |
| SageMaker AI console → *_IC_<br>• tab → per‐IC row | Choose **Metrics**                       | Dashboard filtered to endpoint and inference component |

You can also navigate directly through the CloudWatch console by choosing
**Infrastructure monitoring** → **SageMaker AI Insights**.

## Prerequisites

- At least one SageMaker AI inference endpoint in the `InService` status
- `EnableDetailedObservability` set to `true` on the endpoint
  configuration (default for new endpoints)
- OTel enrichment enabled in your account
- The `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics`
  IAM permissions

For more information, see [Get started with CloudWatch SageMaker AI Insights](SageMaker-AI-Insights-Get-Started.md "SageMaker-AI-Insights-Get-Started.md").

## Pricing

CloudWatch OpenTelemetry metric ingestion applies. For more information, see
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
