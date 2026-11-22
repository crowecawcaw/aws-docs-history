

# Observability for Amazon SageMaker HyperPod clusters orchestrated by Slurm

To achieve comprehensive observability into your SageMaker HyperPod cluster resources and software components, integrate the cluster with [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html). The integration with Amazon Managed Service for Prometheus enables the export of metrics related to your HyperPod cluster resources, providing insights into their performance, utilization, and health. The integration with Amazon Managed Grafana enables the visualization of these metrics through various Grafana dashboards that offer intuitive interface for monitoring and analyzing the cluster's behavior. By leveraging these services, you gain a centralized and unified view of your HyperPod cluster, facilitating proactive monitoring, troubleshooting, and optimization of your distributed training workloads.

To set up observability on your cluster, install the SageMaker HyperPod observability extension. The extension sends cluster metrics to Amazon CloudWatch or Amazon Managed Service for Prometheus. For more information, see [Setting up observability with the SageMaker HyperPod observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md).

**Tip**  
To find practical examples and solutions, see also the [SageMaker HyperPod workshop](https://catalog.workshops.aws/sagemaker-hyperpod).

![An overview of configuring SageMaker HyperPod with Amazon Managed Service for Prometheus and Amazon Managed Grafana.](https://docs.aws.amazon.com/sagemaker/latest/dg/images/hyperpod-observability-architecture.png)


Figure: This architecture diagram shows an overview of configuring SageMaker HyperPod with Amazon Managed Service for Prometheus and Amazon Managed Grafana.

Proceed to the following topics to set up for SageMaker HyperPod cluster observability.

**Important**  
If your cluster already collects metrics with exporters that your lifecycle scripts installed, remove them before you install the extension. Otherwise the install fails with a port conflict. For the steps, see [Migrating from lifecycle scripts](sagemaker-hyperpod-cluster-observability-slurm-extension.md#sagemaker-hyperpod-cluster-observability-slurm-extension-migrating-from-lifecycle-scripts).

**Topics**
+ [Setting up observability with the SageMaker HyperPod observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md)
+ [Prerequisites for SageMaker HyperPod cluster observability](sagemaker-hyperpod-cluster-observability-slurm-prerequisites.md)
+ [Setting up an Amazon Managed Grafana workspace](sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws.md)
+ [Exported metrics reference](sagemaker-hyperpod-cluster-observability-slurm-exported-metrics-reference.md)
+ [Amazon SageMaker HyperPod Slurm metrics](smcluster-slurm-metrics.md)