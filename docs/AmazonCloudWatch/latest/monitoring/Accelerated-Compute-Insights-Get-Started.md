

# Get started with Accelerated Compute Insights
<a name="Accelerated-Compute-Insights-Get-Started"></a>

Amazon CloudWatch Accelerated Compute Insights monitors self-hosted AI inference workloads that run on accelerated compute in Amazon EKS clusters. Collection uses the Amazon CloudWatch Observability Amazon EKS add-on with OTel Container Insights enabled.

This topic shows you how to enable Accelerated Compute Insights for your workloads, verify that accelerator metrics arrive, and explore the dashboard.

Accelerated Compute Insights collects the following accelerator telemetry:
+ NVIDIA GPU metrics from the DCGM exporter, with the `DCGM_FI_DEV_` prefix. These metrics cover utilization, framebuffer memory, temperature, and power.

Accelerated Compute Insights stores your accelerator metrics as CloudWatch OpenTelemetry metrics, and you query them with PromQL. For where to run a query and which labels to filter on, see [Query your accelerator metrics](Accelerated-Compute-Insights.md#Accelerated-Compute-Insights-query).

## Prerequisites
<a name="Accelerated-Compute-Insights-Get-Started-prerequisites"></a>

Before you enable Accelerated Compute Insights, verify that you meet the following requirements:
+ An Amazon EKS cluster with Linux nodes
+ (Optional) GPU nodes from the `p` or `g` instance families, with the NVIDIA driver installed
+ The `amazon-cloudwatch-observability` Amazon EKS add-on, version `v7.0.0-eksbuild.1` or later, with OTel Container Insights enabled

Accelerator collection requires no per-accelerator configuration flags. A GPU node reports GPU metrics automatically.

## Enabling collection
<a name="Accelerated-Compute-Insights-Get-Started-enable-addon"></a>

Accelerated Compute Insights collects telemetry through the same `amazon-cloudwatch-observability` add-on that OTel Container Insights uses. If you have not installed the add-on yet, follow the setup in [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md).

For more information about the add-on and its configuration, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md).

To enable OTel Container Insights on a cluster that already has the add-on, run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

```
aws eks update-addon \
  --cluster-name {{cluster-name}} \
  --addon-name amazon-cloudwatch-observability \
  --configuration-values '{"otelContainerInsights":{"enabled":true}}'
```

**Important**  
The `otelContainerInsights.enabled` configuration value must be `true`. OTel Container Insights is not enabled by default.

**Note**  
After you enable OTel Container Insights, CloudWatch OpenTelemetry metric ingestion pricing applies to the accelerator metrics that the add-on sends.

## Verifying collection
<a name="Accelerated-Compute-Insights-Get-Started-verify"></a>

After you enable collection, confirm that the collector pods run on your accelerated nodes and that accelerator metrics reach CloudWatch.

### Checking the collector pods
<a name="Accelerated-Compute-Insights-Get-Started-verify-pods"></a>

The add-on runs an exporter on the nodes that have an accelerator. To list the collector pods and the nodes that run them, run the following command.

```
kubectl -n amazon-cloudwatch get pods -o wide
```

The output lists `dcgm-exporter` pods on your GPU nodes.

### Confirming that metrics arrive
<a name="Accelerated-Compute-Insights-Get-Started-verify-metrics"></a>

To confirm that accelerator metrics arrive, count the series for one metric in Query Studio.

**To confirm that metrics arrive**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Query Studio**.

1. Run the following query. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

   ```
   count(DCGM_FI_DEV_GPU_UTIL{"@resource.k8s.cluster.name"="{{cluster-name}}"})
   ```

   A result greater than `0` confirms that GPU metrics arrive for that cluster.

For more query examples, and where else you can run them, see [Query your accelerator metrics](Accelerated-Compute-Insights.md#Accelerated-Compute-Insights-query).

**Note**  
An idle accelerator reports utilization near `0`. Before you conclude that collection is broken, correlate your query with a running inference workload.