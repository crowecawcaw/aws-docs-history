

# Getting started with Amazon EKS support in SageMaker HyperPod
<a name="sagemaker-hyperpod-eks-prerequisites"></a>

In addition to the general [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md) for SageMaker HyperPod, check the following requirements and considerations for orchestrating SageMaker HyperPod clusters using Amazon EKS.

**Important**  
You can set up resources configuration for creating SageMaker HyperPod clusters using the AWS Management Console and CloudFormation. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md) and [Creating SageMaker HyperPod clusters using CloudFormation templates](smcluster-getting-started-eks-console-create-cluster-cfn.md).

**Requirements**

**Note**  
Before creating a HyperPod cluster, you need a running Amazon EKS cluster configured with VPC and installed using Helm.
+ If using the SageMaker AI console, you can create an Amazon EKS cluster within the HyperPod cluster console page. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md).
+ If using AWS CLI, you should create an Amazon EKS cluster before creating a HyperPod cluster to associate with. For more information, see [Create an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html) in the Amazon EKS User Guide.

When provisioning your Amazon EKS cluster, consider the following:

1. **Kubernetes version support**
   + SageMaker HyperPod supports Kubernetes versions 1.30, 1.31, 1.32, 1.33, 1.34, and 1.35.

1. **Amazon EKS cluster authentication mode**
   + The authentication mode of an Amazon EKS cluster supported by SageMaker HyperPod are `API` and `API_AND_CONFIG_MAP`.

1. **Networking**
   + SageMaker HyperPod requires the Amazon VPC Container Network Interface (CNI) plug-in version 1.18.3 or later.
**Note**  
[AWS VPC CNI plugin for Kubernetes](https://github.com/aws/amazon-vpc-cni-k8s) is the only CNI supported by SageMaker HyperPod.
   + The [type of the subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-types) in your VPC must be private for HyperPod clusters.

1. **IAM roles**
   + Ensure the necessary IAM roles for HyperPod are set up as guided in the [AWS Identity and Access Management for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md) section.

1. **Amazon EKS cluster add-ons**
   + You can continue using the various add-ons provided by Amazon EKS such as [Kube-proxy](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-kube-proxy.html), [CoreDNS](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-coredns.html), the [Amazon VPC Container Network Interface (CNI)](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-vpc-cni.html) plugin, Amazon EKS pod identity, the GuardDuty agent, the Amazon FSx Container Storage Interface (CSI) driver, the Mountpoint for Amazon S3 CSI driver, the AWS Distro for OpenTelemetry, and the CloudWatch Observability agent.
**Important**  
Do not install a CSI driver that manages NVMe instance storage (sometimes called a Local Instance Storage CSI driver) on HyperPod nodes that use the SageMaker HyperPod AMI. The AMI configures an LVM volume group (`vg.01`) on the NVMe instance store at boot, before the CSI driver starts, and a CSI driver that targets the same NVMe devices will conflict with this configuration and cause I/O failures. The Amazon EBS CSI driver, the Amazon FSx CSI driver, the Amazon EFS CSI driver, and the Mountpoint for Amazon S3 CSI driver are not affected because they do not manage local NVMe instance storage. For details and remediation steps, see the Considerations section in [Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](sagemaker-hyperpod-eks-ebs.md).

**Considerations for configuring SageMaker HyperPod clusters with Amazon EKS**
+ You must use distinct IAM roles based on the type of your nodes. For HyperPod nodes, use a role based on [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod). For Amazon EKS nodes, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html).
+ You can provision and mount additional Amazon EBS volumes on SageMaker HyperPod nodes using two approaches: use [*InstanceStorageConfigs*](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs) for cluster-level volume provisioning (available when creating or updating instance groups), or use the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver for dynamic pod-level volume management. With [*InstanceStorageConfigs*](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceGroupSpecification.html#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs), set the [local path](https://kubernetes.io/docs/concepts/storage/volumes/#local) to `/opt/sagemaker` to properly mount the volumes to your Amazon EKS pods. For information about how to deploy the [Amazon EBS CSI](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) controller on HyperPod nodes, see [Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](sagemaker-hyperpod-eks-ebs.md). To use NVMe instance storage on HyperPod, rely on the AMI's built-in LVM configuration through `/opt/sagemaker` rather than installing a separate NVMe-targeting CSI driver.
+ If you use instance-type labels to define scheduling constraints, ensure that you use the SageMaker AI ML instance types prefixed with `ml.`. For example, for P5 instances, use `ml.p5.48xlarge` instead of `p5.48xlarge`.

**Considerations for configuring network for SageMaker HyperPod clusters with Amazon EKS**
+ Each HyperPod cluster instance supports one Elastic Network Interface (ENI). For the maximum number of Pods per instance type, refer to the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html)
+ Only Pods with `hostNetwork = true` have access to the Amazon EC2 Instance Metadata Service (IMDS) by default. Use the Amazon EKS Pod identity or the [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to manage access to the AWS credentials for Pods.
+ EKS-orchestrated HyperPod clusters support dual IP addressing modes, allowing configuration with IPv4 or IPv6 for IPv6 Amazon EKS clusters in IPv6-enabled VPC and subnet environments. For more information, see [Setting up SageMaker HyperPod with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc).

**Considerations for using the HyperPod cluster resiliency features**
+ Node auto-replacement is not supported for CPU instances.
+ The HyperPod health monitoring agent needs to be installed for node auto-recovery to work. The agent can be installed using Helm. For more information, see [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md).
+ The HyperPod deep health check and health monitoring agent supports GPU and Trn instances.
+ SageMaker AI applies the following taint to nodes when they are undergoing deep health checks:

  ```
  effect: NoSchedule
  key: sagemaker.amazonaws.com/node-health-status
  value: Unschedulable
  ```
**Note**  
You cannot add custom taints to nodes in instance groups with `DeepHealthChecks` turned on.

 Once your Amazon EKS cluster is running, configure your cluster using the Helm package manager as instructed in [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md) before creating your HyperPod cluster.