

# Correlating DRA-allocated devices to pods with OTel Container Insights

With Kubernetes Dynamic Resource Allocation (DRA), pods claim devices, such as network adapters and accelerators, through `ResourceClaim` objects instead of device plugin resource requests. With DRA correlation, OTel Container Insights links each AWS Elastic Fabric Adapter (EFA) and AWS Neuron device that DRA allocates to the pod that uses it. The device metrics then carry the pod, namespace, and container attributes of that pod, so you can see which workload uses each device.

To view accelerator metrics by workload in the CloudWatch console, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

## Prerequisites
<a name="container-insights-eks-otel-dra-prereqs"></a>

DRA correlation is on by default when the following requirements are met.
+ Version 8.0.0 or later of the `amazon-cloudwatch-observability` add-on or Helm chart
+ OTel Container Insights enabled on the cluster (see [Quick start](container-insights-eks-otel-quickstart.md))
+ An Amazon EKS cluster that runs Kubernetes 1.34 or later, which serves the generally available DRA API (`resource.k8s.io/v1`)
+ EFA or Neuron devices that a DRA driver allocates to your pods

## Turning off DRA correlation
<a name="container-insights-eks-otel-dra-configure"></a>

On clusters older than Kubernetes 1.34, or clusters that don't use DRA, turn off DRA correlation. The agent then doesn't try to read `ResourceSlice` and `ResourceClaim` objects. The following add-on configuration turns it off:

```json
{
  "otelContainerInsights": {
    "enabled": true,
    "enableDRACorrelation": false
  }
}
```

With the Helm chart, use `--set otelContainerInsights.enableDRACorrelation=false`.

DRA correlation for NVIDIA GPUs is a separate setting, `dcgmExporter.enableDRACorrelation`, which is also on by default. You can change it only with the Helm chart.