

# Orchestrating SageMaker HyperPod clusters with Amazon EKS
<a name="sagemaker-hyperpod-eks"></a>

SageMaker HyperPod is a SageMaker AI-managed service that enables large-scale training of foundation models on long-running and resilient compute clusters, integrating with Amazon EKS for orchestrating the HyperPod compute resources. You can run uninterrupted training jobs spanning weeks or months at scale using Amazon EKS clusters with HyperPod resiliency features that check for various hardware failures and automatically recover faulty nodes. 

Key features for cluster admin users include the following.
+ Provisioning resilient HyperPod clusters and attaching them to an EKS control plane
+ Enabling dynamic capacity management, such as adding more nodes, updating software, and deleting clusters
+ Enabling access to the cluster instances directly through `kubectl` or SSM/SSH
+ Offering [resiliency capabilities](sagemaker-hyperpod-eks-resiliency.md), including basic health checks, deep health checks, a health-monitoring agent, and support for PyTorch job auto-resume
+ Integrating with observability tools such as [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html)

For data scientist users, EKS support in HyperPod enables the following.
+ Running containerized workloads for training foundation models on the HyperPod cluster
+ Running inference on the EKS cluster, leveraging the integration between HyperPod and EKS
+ Leveraging the job auto-resume capability for [Kubeflow PyTorch training (PyTorchJob)](https://www.kubeflow.org/docs/components/training/user-guides/pytorch/)

**Note**  
Amazon EKS enables user-managed orchestration of tasks and infrastructure on SageMaker HyperPod through the Amazon EKS Control Plane. Ensure that user access to the cluster through the Kubernetes API Server endpoint follows the principle of least-privilege, and that network egress from the HyperPod cluster is secured.  
To learn more about securing access to the Amazon EKS API Server, see [Control network access to cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html).  
To learn more about securing network access on HyperPod, see [Setting up SageMaker HyperPod with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc).

The high-level architecture of Amazon EKS support in HyperPod involves a 1-to-1 mapping between an EKS cluster (control plane) and a HyperPod cluster (worker nodes) within a VPC, as shown in the following diagram.

![EKS control plane connected to HyperPod cluster nodes via cross-account ENIs within VPCs.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/hyperpod-eks-diagram.png)
