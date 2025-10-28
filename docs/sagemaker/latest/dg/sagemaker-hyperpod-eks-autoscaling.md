# Autoscaling on SageMaker HyperPod EKS

Amazon SageMaker HyperPod provides a managed Karpenter based node autoscaling solution for clusters
created with EKS orchestration. [Karpenter](https://karpenter.sh/ "https://karpenter.sh/") is an
open-source, Kubernetes node lifecycle manager built by AWS that optimizes cluster scaling
and cost efficiency. Unlike self-managed Karpenter deployments, SageMaker HyperPod's managed
implementation eliminates the operational overhead of installing, configuring, and
maintaining Karpenter controllers while providing integrated resilience and fault tolerance.
This managed autoscaling solution is built on HyperPod's [continuous provisioning](sagemaker-hyperpod-scaling-eks.md "sagemaker-hyperpod-scaling-eks.md") capabilities and
enables you to efficiently scale compute resources for training and inference workloads with
automatic failure handling and recovery.

You pay only for what you use. You're responsible for paying for all compute instances
that are automatically provisioned through autoscaling according to standard SageMaker HyperPod
pricing. For detailed pricing information, see [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/pricing/ "https://aws.amazon.com/sagemaker/ai/pricing/").

By enabling Karpenter-based autoscaling with HyperPod, you have access to:

- **Service managed lifecycle** - HyperPod
  handles Karpenter installation, updates, and maintenance, eliminating operational
  overhead.
- **Just in time provisioning** - Karpenter will
  observe your pending pods and provision the required compute for your workloads from
  on-demand pool.
- **Scale to zero** - Scale down to zero nodes without
  maintaining dedicated controller infrastructure.
- **Workload aware node selection** - Karpenter chooses
  optimal instance types based on pod requirements, availability zones, and pricing to
  minimize costs.
- **Automatic node consolidation** - Karpenter
  regularly evaluates cluster for optimization opportunities, shifting workloads to
  eliminate underutilized nodes.
- **Integrated resilience** - Leverages
  HyperPod's built-in fault tolerance and node recovery mechanisms.
  The following topics explain how to enable HyperPod autoscaling with
  Karpenter.

###### Topics

- [Prerequisites](#sagemaker-hyperpod-eks-autoscaling-prereqs "#sagemaker-hyperpod-eks-autoscaling-prereqs")
- [Create an IAM role for
  HyperPod autoscaling with Karpenter](sagemaker-hyperpod-eks-autoscaling-iam.md "sagemaker-hyperpod-eks-autoscaling-iam.md")
- [Create and configure a
  HyperPod cluster with Karpenter autoscaling](sagemaker-hyperpod-eks-autoscaling-cluster.md "sagemaker-hyperpod-eks-autoscaling-cluster.md")
- [Create a
  NodeClass](sagemaker-hyperpod-eks-autoscaling-nodeclass.md "sagemaker-hyperpod-eks-autoscaling-nodeclass.md")
- [Create a NodePool](sagemaker-hyperpod-eks-autoscaling-nodepool.md "sagemaker-hyperpod-eks-autoscaling-nodepool.md")
- [Deploy a workload](sagemaker-hyperpod-eks-autoscaling-workload.md "sagemaker-hyperpod-eks-autoscaling-workload.md")

## Prerequisites

- Continuous provisioning enabled on your HyperPod cluster. Enable
  continuous provisioning by setting `--node-provisioning-mode` to
  `Continuous` when creating your SageMaker HyperPod cluster. For more
  information, see [Continuous provisioning for enhanced
  cluster operations on Amazon EKS](sagemaker-hyperpod-scaling-eks.md "sagemaker-hyperpod-scaling-eks.md").
- Health Monitoring Agent version 1.0.742.0_1.0.241.0 or above installed.
  Required for HyperPod cluster operations and monitoring. The agent must
  be configured before enabling Karpenter autoscaling to ensure proper cluster
  health reporting and node lifecycle management. For more information, see [SageMaker HyperPod
  health-monitoring agent](sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md "sagemaker-hyperpod-eks-resiliency-health-monitoring-agent.md").
- Only if your Amazon EKS cluster has Karpenter running on it, the Karpenter
  `NodePool` and `NodeClaim` versions need to be
  v1.
- `NodeRecovery` set to automatic. For more information, see [Automatic node
  recovery](sagemaker-hyperpod-eks-resiliency-node-recovery.md "sagemaker-hyperpod-eks-resiliency-node-recovery.md").
