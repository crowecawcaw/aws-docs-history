

# Amazon SageMaker HyperPod observability with Amazon Managed Grafana and Amazon Managed Service for Prometheus
<a name="sagemaker-hyperpod-observability-addon"></a>

Amazon SageMaker HyperPod (SageMaker HyperPod) provides a comprehensive, out-of-the-box dashboard that gives you insights into foundation model (FM) development tasks and cluster resources. This unified observability solution automatically publishes key metrics to Amazon Managed Service for Prometheus and displays them in Amazon Managed Grafana dashboards. The dashboards are optimized specifically for FM development with deep coverage of hardware health, resource utilization, and task-level performance. With this add-on, you can consolidate health and performance data from NVIDIA DCGM, instance-level Kubernetes node exporters, Elastic Fabric Adapter, integrated file systems, Kubernetes APIs, Kueue, and SageMaker HyperPod task operators.

## Restricted Instance Group (RIG) support
<a name="hyperpod-observability-addon-rig-support"></a>

The observability add-on also supports clusters that contain Restricted Instance Groups. In RIG clusters, the add-on automatically adapts its deployment strategy to comply with the network isolation and security constraints of restricted nodes. DaemonSet components (node exporter, DCGM exporter, EFA exporter, Neuron monitor, and node collector) run on both standard and restricted nodes. Deployment components (central collector, Kube State Metrics, and Training Metrics Agent) are scheduled with boundary-aware logic to respect network isolation between instance groups. Container log collection with Fluent Bit is not available on restricted nodes.

For information about setting up the add-on on clusters with Restricted Instance Groups, see [Setting up the SageMaker HyperPod observability add-on](hyperpod-observability-addon-setup.md).

**Topics**
+ [Restricted Instance Group (RIG) support](#hyperpod-observability-addon-rig-support)
+ [Setting up the SageMaker HyperPod observability add-on](hyperpod-observability-addon-setup.md)
+ [Amazon SageMaker HyperPod observability dashboards](hyperpod-observability-addon-viewing-dashboards.md)
+ [Exploring SageMaker HyperPod cluster metrics in Amazon Managed Grafana](hyperpod-observability-addon-exploring-metrics.md)
+ [Customizing SageMaker HyperPod cluster metrics dashboards and alerts](hyperpod-observability-addon-customizing.md)
+ [Creating custom SageMaker HyperPod cluster metrics](hyperpod-observability-addon-custom-metrics.md)
+ [SageMaker HyperPod cluster metrics](hyperpod-observability-cluster-metrics.md)
+ [Preconfigured alerts](hyperpod-observability-addon-alerts.md)
+ [Troubleshooting the Amazon SageMaker HyperPod observability add-on](hyperpod-observability-addon-troubleshooting.md)