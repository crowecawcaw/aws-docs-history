

# Accelerated Compute Insights

Amazon CloudWatch Accelerated Compute Insights provides monitoring and observability for self-hosted AI workloads that run on accelerated compute in Amazon EKS clusters. It currently supports inference workloads.

Accelerated Compute Insights collects telemetry from across the inference stack: the accelerators that serve your models, the nodes that hold them, and the pods and containers that use them. It covers NVIDIA GPUs, and it resolves each accelerator metric to the pod and container that used that accelerator.

Accelerated Compute Insights then presents that data as dashboards you can read and query. You can use it in the Amazon CloudWatch console, and on the Accelerated Compute Insights page in CloudWatch Omni, which adds an agentic interface over the same telemetry. For more information about the Omni experience, see [AI Inference Insights](omni-ai-inference-insights.md).

**Important**  
Accelerated Compute Insights requires the OTel Container Insights configuration of the `amazon-cloudwatch-observability` Amazon EKS add-on. For more information, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).

To get started with Accelerated Compute Insights, see the following topic.

**Topics**
+ [Get started with Accelerated Compute Insights](Accelerated-Compute-Insights-Get-Started.md)

## Prerequisites
<a name="Accelerated-Compute-Insights-prerequisites"></a>

To use Accelerated Compute Insights, you need the following:
+ An Amazon EKS cluster that runs your inference workloads on accelerated compute nodes, such as NVIDIA GPU nodes
+ The `amazon-cloudwatch-observability` Amazon EKS add-on, version `v7.0.0-eksbuild.1` or later, with OTel Container Insights enabled on the cluster

For the add-on setup steps, see [OTel Container Insights quick start](container-insights-eks-otel-quickstart.md). For more information about the Accelerated Compute Insights prerequisites, see [Get started with Accelerated Compute Insights](Accelerated-Compute-Insights-Get-Started.md).

## Key capabilities
<a name="Accelerated-Compute-Insights-capabilities"></a>

Accelerated Compute Insights provides the following capabilities for your inference workloads:

NVIDIA GPU telemetry  
With the DCGM exporter, you get `DCGM_FI_DEV_*` metrics, which cover utilization, framebuffer memory, temperature, and power, and `DCGM_FI_PROF_*` profiling metrics.

Inference engine metrics  
The vLLM, SGLang, and Ray solutions of OTel Container Insights collect the metrics of your model servers, including the engine metrics of Ray Serve LLM. The SGLang and Ray solutions need add-on version 8.0.0 or later. For more information, see [Solutions](container-insights-eks-otel-solutions.md).

DRA correlation  
On clusters that allocate devices with Kubernetes Dynamic Resource Allocation (DRA), the add-on attributes device metrics to the pods that use them. For more information, see [Correlating DRA-allocated devices to pods with OTel Container Insights](container-insights-eks-otel-dra.md).

No per-accelerator configuration  
Accelerator collection needs no configuration flags. A GPU node reports GPU metrics automatically.

Multi-account and multi-Region views  
With CloudWatch cross-account observability set up, you can see accelerated compute across your source accounts and Regions from one monitoring account. For how to set that up, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md).

Curated views  
Three built-in views: **Overview** for fleet health and utilization, **Workloads** for metrics grouped by inference workload, and **Accelerators** for node-level accelerator metrics.

## Query your accelerator metrics
<a name="Accelerated-Compute-Insights-query"></a>

Accelerated Compute Insights collects your accelerator metrics with OpenTelemetry, stores them as CloudWatch OpenTelemetry metrics, and you query them with PromQL. For more information, see [OTel metrics pricing and storage](metrics-otel-pricing.md).

You can run a query in any of the following places:
+ **Query Studio** – In the navigation pane of the CloudWatch console, choose **Query Studio**, and then enter a PromQL query.
+ **From a widget** – On any Accelerated Compute Insights widget, choose **View in Query Studio** to open the PromQL query behind that widget. Use this to see how a widget is built, and to adapt it.
+ **A dashboard** – Choose **Add to dashboard** on a widget, or add a PromQL query to a dashboard yourself.

Filter and group your queries by the cluster, namespace, pod, and container that the metric came from. The following example query returns average GPU utilization for each pod in a namespace, which shows you which workloads are using your accelerators. Replace {{namespace}} with your namespace.

```promql
avg by ("@resource.k8s.pod.name") (
  DCGM_FI_DEV_GPU_UTIL{"@resource.k8s.namespace.name"="{{namespace}}"}
)
```

## How Accelerated Compute Insights identifies inference workloads
<a name="Accelerated-Compute-Insights-workload-classification"></a>

Accelerated Compute Insights currently supports inference workloads. The add-on automatically recognizes and tags your workloads according to the following logic, so you do not need to add a CloudWatch-specific label to your pods. Accelerated Compute Insights applies these rules in order and uses the first one that matches.


| Evidence on the workload's metrics | Workload type | 
| --- | --- | 
| An inference engine reports running requests from the workload's pods, such as vllm:num\_requests\_running or sglang:num\_running\_reqs | Inference | 
| A serving framework labels the pod (KServe, Knative, or Ray Serve) | Inference | 

A workload that matches none of these rules is not shown as an inference workload.

## Viewing the Accelerated Compute Insights dashboard
<a name="Accelerated-Compute-Insights-access"></a>

To open the dashboard, open the CloudWatch console, and then choose **GenAI Observability**, **Accelerated Compute Insights** in the navigation pane.

The dashboard groups accelerator metrics into three views. Use them to assess the health of your accelerated fleet, compare inference workloads, and inspect individual nodes.
+ **Overview** summarizes the health and utilization of your accelerated fleet.
+ **Workloads** groups accelerator metrics by inference workload.
+ **Accelerators** shows node-level accelerator metrics.

You can narrow what the dashboard shows with the **Account**, **Region**, and **Workload** filters. The **Workload** filter is scoped to the selected workload type. For how Accelerated Compute Insights decides which workloads are inference workloads, see [How Accelerated Compute Insights identifies inference workloads](#Accelerated-Compute-Insights-workload-classification).

Each widget provides two actions. Choose **View in Query Studio** to open the widget query in Query Studio. Choose **Add to dashboard** to add the widget to a CloudWatch dashboard.

In CloudWatch Omni, you can ask about a workload in plain language instead of assembling queries yourself, and Omni correlates engine metrics, accelerator metrics, traces, and logs for you. Omni also covers inference workloads that run on Amazon ECS as well as on Amazon EKS. For more information, see [AI Inference Insights](omni-ai-inference-insights.md).

## Pricing
<a name="Accelerated-Compute-Insights-pricing"></a>

Standard CloudWatch pricing applies to the telemetry that you collect from your AI workloads. There is no additional charge for Accelerated Compute Insights itself. You pay the usual CloudWatch rates for the metrics that the add-on ingests, at the same rates as any other CloudWatch OpenTelemetry metrics. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).