

# Observability for Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS
<a name="sagemaker-hyperpod-eks-cluster-observability"></a>

To achieve comprehensive observability into your Amazon SageMaker HyperPod (SageMaker HyperPod) cluster resources and software components, integrate the cluster with [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html). These tools provide visibility into cluster health, performance metrics, and resource utilization.

The integration with Amazon Managed Service for Prometheus enables the export of metrics related to your HyperPod cluster resources, providing insights into their performance, utilization, and health. The integration with Amazon Managed Grafana enables the visualization of these metrics through various Grafana dashboards that offer intuitive interface for monitoring and analyzing the cluster's behavior. By leveraging these services, you gain a centralized and unified view of your HyperPod cluster, facilitating proactive monitoring, troubleshooting, and optimization of your distributed training workloads.

**Note**  
While CloudWatch, Amazon Managed Service for Prometheus, and Amazon Managed Grafana focus on operational metrics (for example, system health, training job performance), SageMaker HyperPod Usage Reports complement [Task Governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md) to provide financial and resource accountability insights. These reports track:  
Compute utilization (GPU/CPU/Neuron Core hours) across namespaces/teams
Cost attribution for allocated vs. borrowed resources
Historical trends (up to 180 days) for auditing and optimization
For more information about setting up and generating usage reports, see [Reporting Compute Usage in HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.html). 

**Tip**  
To find practical examples and solutions, see also the [Observability](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e/en-US/06-observability) section in the [Amazon EKS Support in SageMaker HyperPod workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e).

Proceed to the following topics to set up for SageMaker HyperPod cluster observability.

**Topics**
+ [Model observability for training jobs on SageMaker HyperPod clusters orchestrated by Amazon EKS](sagemaker-hyperpod-eks-cluster-observability-model.md)
+ [Cluster and task observability](sagemaker-hyperpod-eks-cluster-observability-cluster.md)