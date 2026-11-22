

# Cluster and task observability

There are two options for monitoring SageMaker HyperPod clusters:

**The SageMaker HyperPod observability add-on**—SageMaker HyperPod provides preconfigured dashboards that give you insights into foundation model (FM) development tasks and cluster resources. The add-on collects health and performance metrics from NVIDIA DCGM, instance-level Kubernetes node exporters, Elastic Fabric Adapter, Kubernetes APIs, Kueue, and SageMaker HyperPod task operators. It sends the metrics from all these sources to one metric store, Amazon CloudWatch or Amazon Managed Service for Prometheus, and displays them in Amazon Managed Grafana dashboards. The dashboards show the hardware health and resource utilization of the cluster, the CPU, memory, GPU, and GPU memory use of each task, and the restarts, faults, and recovery times of training tasks. They also show Amazon FSx for Lustre metrics from CloudWatch.

**Amazon CloudWatch Insights**—Amazon CloudWatch Insights collects metrics for compute resources, such as CPU, memory, disk, and network. Container Insights also provides diagnostic information, such as container restart failures, to help you isolate issues and resolve them quickly. You can also set CloudWatch alarms on metrics that Container Insights collects.

**Topics**
+ [Amazon SageMaker HyperPod observability add-on](sagemaker-hyperpod-observability-addon.md)
+ [Observability with Amazon CloudWatch](sagemaker-hyperpod-eks-cluster-observability-cluster-cloudwatch-ci.md)