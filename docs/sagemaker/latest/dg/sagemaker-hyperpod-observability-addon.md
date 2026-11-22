

# Amazon SageMaker HyperPod observability add-on

Amazon SageMaker HyperPod (SageMaker HyperPod) provides preconfigured dashboards that give you insights into foundation model (FM) development tasks and cluster resources. The add-on collects health and performance metrics from NVIDIA DCGM, instance-level Kubernetes node exporters, Elastic Fabric Adapter, Kubernetes APIs, Kueue, and SageMaker HyperPod task operators. It sends the metrics from all these sources to one metric store, Amazon CloudWatch or Amazon Managed Service for Prometheus, and displays them in Amazon Managed Grafana dashboards. The dashboards show the hardware health and resource utilization of the cluster, the CPU, memory, GPU, and GPU memory use of each task, and the restarts, faults, and recovery times of training tasks. They also show Amazon FSx for Lustre metrics from CloudWatch.

The add-on sends metrics to one metric store. You choose the metric store when you set up the add-on:
+ **Amazon CloudWatch**—Available in add-on version `v1.5.0-eksbuild.1` and later. The add-on sends the metrics to CloudWatch as OpenTelemetry metrics, and you query them with the Prometheus Query Language (PromQL). With Amazon CloudWatch, you don't create or manage an Amazon Managed Service for Prometheus workspace. When you turn on logging, the add-on sends the logs to CloudWatch too, so the metrics and logs are in the same service. You can query the metrics in Query Studio in the CloudWatch console, create CloudWatch alarms from PromQL queries, and view the metrics in Amazon Managed Grafana. For more information, see [Viewing SageMaker HyperPod cluster metrics in Amazon CloudWatch](hyperpod-observability-addon-cloudwatch-metrics.md).
+ **Amazon Managed Service for Prometheus**—Available in all versions of the add-on. Versions earlier than `v1.5.0-eksbuild.1` send metrics only to Amazon Managed Service for Prometheus.

The add-on can't send metrics to both metric stores at the same time. With both metric stores, the add-on sends logs to Amazon CloudWatch Logs when you turn on logging.

## Restricted Instance Group (RIG) support
<a name="hyperpod-observability-addon-rig-support"></a>

The observability add-on also supports clusters that contain Restricted Instance Groups. In RIG clusters, the add-on automatically adapts its deployment strategy to comply with the network isolation and security constraints of restricted nodes. DaemonSet components (node exporter, DCGM exporter, EFA exporter, Neuron monitor, and node collector) run on both standard and restricted nodes. Deployment components (central collector, Kube State Metrics, and Training Metrics Agent) are scheduled with boundary-aware logic to respect network isolation between instance groups. Container log collection with Fluent Bit is not available on restricted nodes.

For information about setting up the add-on on clusters with Restricted Instance Groups, see [Setting up the SageMaker HyperPod observability add-on](hyperpod-observability-addon-setup.md).

**Topics**
+ [Restricted Instance Group (RIG) support](#hyperpod-observability-addon-rig-support)
+ [Setting up the SageMaker HyperPod observability add-on](hyperpod-observability-addon-setup.md)
+ [Viewing SageMaker HyperPod cluster metrics in Amazon CloudWatch](hyperpod-observability-addon-cloudwatch-metrics.md)
+ [Amazon SageMaker HyperPod observability dashboards](hyperpod-observability-addon-viewing-dashboards.md)
+ [Exploring SageMaker HyperPod cluster metrics in Amazon Managed Grafana](hyperpod-observability-addon-exploring-metrics.md)
+ [Customizing SageMaker HyperPod cluster metrics dashboards and alerts](hyperpod-observability-addon-customizing.md)
+ [Creating custom SageMaker HyperPod cluster metrics](hyperpod-observability-addon-custom-metrics.md)
+ [SageMaker HyperPod cluster metrics](hyperpod-observability-cluster-metrics.md)
+ [Preconfigured alerts](hyperpod-observability-addon-alerts.md)
+ [Troubleshooting the Amazon SageMaker HyperPod observability add-on](hyperpod-observability-addon-troubleshooting.md)