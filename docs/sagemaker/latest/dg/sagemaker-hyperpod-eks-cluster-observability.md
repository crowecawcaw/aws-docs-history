# Observability for

Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS

To achieve comprehensive observability into your Amazon SageMaker HyperPod (SageMaker HyperPod) cluster
resources and software components, integrate the cluster with [Amazon CloudWatch Container
Insights](../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md "../../../AmazonCloudWatch/latest/monitoring/ContainerInsights.md"), [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md "../../../prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.md"), and [Amazon Managed Grafana](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md"). These tools provide visibility into cluster health, performance metrics, and
resource utilization.

The integration with Amazon Managed Service for Prometheus enables the export of metrics related to your HyperPod
cluster resources, providing insights into their performance, utilization, and health. The
integration with Amazon Managed Grafana enables the visualization of these metrics through various Grafana
dashboards that offer intuitive interface for monitoring and analyzing the cluster's
behavior. By leveraging these services, you gain a centralized and unified view of your
HyperPod cluster, facilitating proactive monitoring, troubleshooting, and
optimization of your distributed training workloads.

###### Note

While CloudWatch, Amazon Managed Service for Prometheus, and Amazon Managed Grafana focus on operational metrics (for example, system health,
training job performance), SageMaker HyperPod Usage Reports complement [Task
Governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md") to provide financial and resource accountability insights. These
reports track:

- Compute utilization (GPU/CPU/Neuron Core hours) across namespaces/teams
- Cost attribution for allocated vs. borrowed resources
- Historical trends (up to 180 days) for auditing and optimization
  For more information about setting up and generating usage reports, see [Reporting Compute
  Usage in HyperPod](sagemaker-hyperpod-usage-reporting.md "sagemaker-hyperpod-usage-reporting.md").

###### Tip

To find practical examples and solutions, see also the [Observability](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/06-observability "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/06-observability") section in the [Amazon EKS Support in SageMaker HyperPod workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e").

Proceed to the following topics to set up for SageMaker HyperPod cluster observability.

###### Topics

- [Model observability
  for training jobs on SageMaker HyperPod clusters orchestrated by Amazon EKS](sagemaker-hyperpod-eks-cluster-observability-model.md "sagemaker-hyperpod-eks-cluster-observability-model.md")
- [Cluster and task
  observability](sagemaker-hyperpod-eks-cluster-observability-cluster.md "sagemaker-hyperpod-eks-cluster-observability-cluster.md")
