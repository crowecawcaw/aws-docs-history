

# Viewing SageMaker HyperPod cluster metrics in Amazon CloudWatch

When Amazon CloudWatch is the metric store, the add-on sends the metrics to the CloudWatch OpenTelemetry Protocol (OTLP) endpoint. CloudWatch stores them as OpenTelemetry metrics. The metric names are the same as with Amazon Managed Service for Prometheus, for example `DCGM_FI_DEV_GPU_UTIL`. For the list of metrics, see [SageMaker HyperPod cluster metrics](hyperpod-observability-cluster-metrics.md). For more information about the endpoint, see [OTLP Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html) in the *Amazon CloudWatch User Guide*.

You can query the metrics with the Prometheus Query Language (PromQL) in the following ways:
+ In Query Studio in the CloudWatch console.
+ With the Prometheus-compatible query API at `https://monitoring.{{region}}.amazonaws.com`. Sign the requests with AWS Signature Version 4 (SigV4) for the service `monitoring`.
+ In Amazon Managed Grafana, with the `CloudWatch OpenTelemetry` data source.

To query the metrics, you need the `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions. For more information, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) in the *Amazon CloudWatch User Guide*.

The add-on adds resource attributes to each metric, for example `aws.sagemaker.hyperpod.cluster.name`, `aws.sagemaker.hyperpod.cluster.id`, `aws.sagemaker.hyperpod.instance_group.name`, `host.name`, `host.type`, `k8s.namespace.name`, and `k8s.pod.name`. In PromQL, add the prefix `@resource.` to a resource attribute and put the label name in quotation marks. The following query counts the GPUs in a cluster. Replace {{cluster-id}} with the ID of your cluster.

```
count(DCGM_FI_DEV_GPU_UTIL{"@resource.aws.sagemaker.hyperpod.cluster.id"="{{cluster-id}}"})
```

## Viewing CloudWatch metrics in Amazon Managed Grafana
<a name="hyperpod-observability-addon-cloudwatch-grafana"></a>

When you set up the add-on in the console with an Amazon Managed Grafana workspace and Amazon CloudWatch as the metric store, the console adds a data source named `CloudWatch OpenTelemetry` to the workspace. The data source uses the Amazon Managed Service for Prometheus data source plugin, the URL `https://monitoring.{{region}}.amazonaws.com`, and SigV4 for the service `monitoring`. The console also installs SageMaker HyperPod dashboards that read from this data source. These dashboards have the same names as the dashboards for Amazon Managed Service for Prometheus. For more information, see [Amazon SageMaker HyperPod observability dashboards](hyperpod-observability-addon-viewing-dashboards.md).

The Amazon Managed Grafana workspace must run Grafana version 12 or later, because the dashboards need the Amazon Managed Service for Prometheus data source plugin.