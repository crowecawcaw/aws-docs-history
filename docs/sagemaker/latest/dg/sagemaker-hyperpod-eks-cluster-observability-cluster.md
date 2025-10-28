# Cluster and task

observability

There are two options for monitoring SageMaker HyperPod clusters:

**The SageMaker HyperPod observability
add-on**—SageMaker HyperPod provides a comprehensive, out-of-the-box dashboard
that gives you insights into foundation model (FM) development tasks and cluster
resources. This unified observability solution automatically publishes key metrics to
Amazon Managed Service for Prometheus and displays them in Amazon Managed Grafana dashboards. The dashboards are optimized
specifically for FM development with deep coverage of hardware health, resource
utilization, and task-level performance. With this add-on, you can consolidate health
and performance data from NVIDIA DCGM, instance-level Kubernetes node exporters, Elastic
Fabric Adapter, integrated file systems, Kubernetes APIs, Kueue, and SageMaker HyperPod task
operators.

**Amazon CloudWatch Insights**—Amazon CloudWatch Insights collects
metrics for compute resources, such as CPU, memory, disk, and network. Container
Insights also provides diagnostic information, such as container restart failures, to
help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on
metrics that Container Insights collects.

###### Topics

- [Amazon SageMaker HyperPod
  observability with Amazon Managed Grafana and Amazon Managed Service for Prometheus](sagemaker-hyperpod-observability-addon.md "sagemaker-hyperpod-observability-addon.md")
- [Observability with Amazon CloudWatch](sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.md "sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.md")
