# Getting started with Amazon EKS support in SageMaker HyperPod

In addition to the general [Prerequisites for using SageMaker HyperPod](sagemaker-hyperpod-prerequisites.md "sagemaker-hyperpod-prerequisites.md") for
SageMaker HyperPod, check the following requirements and considerations for orchestrating
SageMaker HyperPod clusters using Amazon EKS.

###### Important

You can set up resources configuration for creating SageMaker HyperPod clusters using the
AWS Management Console and CloudFormation. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md") and [Creating SageMaker HyperPod clusters using CloudFormation templates](smcluster-getting-started-eks-console-create-cluster-cfn.md "smcluster-getting-started-eks-console-create-cluster-cfn.md").

**Requirements**

###### Note

Before creating a HyperPod cluster, you need a running Amazon EKS cluster
configured with VPC and installed using Helm.

- If using the SageMaker AI console, you can create an Amazon EKS cluster within the
  HyperPod cluster console page. For more information, see [Creating a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").
- If using AWS CLI, you should create an Amazon EKS cluster before creating a
  HyperPod cluster to associate with. For more information, see [Create an
  Amazon EKS cluster](../../../eks/latest/userguide/create-cluster.md "../../../eks/latest/userguide/create-cluster.md") in the Amazon EKS User Guide.
  When provisioning your Amazon EKS cluster, consider the following:

1. **Kubernetes version support**

   - SageMaker HyperPod supports Kubernetes versions 1.30, 1.31, 1.32, 1.33, 1.34, and 1.35.

2. **Amazon EKS cluster authentication mode**

   - The authentication mode of an Amazon EKS cluster supported by SageMaker HyperPod are
     `API` and `API_AND_CONFIG_MAP`.

3. **Networking**

   - SageMaker HyperPod requires the Amazon VPC Container Network Interface (CNI)
     plug-in version 1.18.3 or later.

   ###### Note

   [AWS VPC CNI
   plugin for Kubernetes](https://github.com/aws/amazon-vpc-cni-k8s "https://github.com/aws/amazon-vpc-cni-k8s") is the only CNI supported by
   SageMaker HyperPod.
   - The [type of
     the subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types") in your VPC must be private for HyperPod
     clusters.

4. **IAM roles**

   - Ensure the necessary IAM roles for HyperPod are set up as
     guided in the [AWS Identity and Access Management for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md "sagemaker-hyperpod-prerequisites-iam.md")
     section.

5. **Amazon EKS cluster add-ons**

   - You can continue using the various add-ons provided by Amazon EKS such as
     [Kube-proxy](../../../eks/latest/userguide/add-ons-kube-proxy.md "../../../eks/latest/userguide/add-ons-kube-proxy.md"),
     [CoreDNS](../../../eks/latest/userguide/add-ons-coredns.md "../../../eks/latest/userguide/add-ons-coredns.md"), the
     [Amazon VPC Container
     Network Interface (CNI)](../../../eks/latest/userguide/add-ons-vpc-cni.md "../../../eks/latest/userguide/add-ons-vpc-cni.md") plugin, Amazon EKS pod identity, the GuardDuty
     agent, the Amazon FSx Container Storage Interface (CSI) driver, the Mountpoint
     for Amazon S3 CSI driver, the AWS Distro for OpenTelemetry, and the CloudWatch
     Observability agent.

   ###### Important

   Do not install a CSI driver that manages NVMe instance storage
   (sometimes called a Local Instance Storage CSI driver) on
   HyperPod nodes that use the SageMaker HyperPod AMI. The AMI
   configures an LVM volume group (`vg.01`) on the NVMe
   instance store at boot, before the CSI driver starts, and a CSI driver
   that targets the same NVMe devices will conflict with this
   configuration and cause I/O failures. The Amazon EBS CSI driver, the Amazon FSx
   CSI driver, the Amazon EFS CSI driver, and the Mountpoint for Amazon S3 CSI driver are not affected
   because they do not manage local NVMe instance storage. For details and
   remediation steps, see the Considerations section in [Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](sagemaker-hyperpod-eks-ebs.md "sagemaker-hyperpod-eks-ebs.md").
   **Considerations for configuring SageMaker HyperPod clusters with
   Amazon EKS**

- You must use distinct IAM roles based on the type of your nodes. For
  HyperPod nodes, use a role based on [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod"). For
  Amazon EKS nodes, see [Amazon EKS node IAM
  role](../../../eks/latest/userguide/create-node-role.md "../../../eks/latest/userguide/create-node-role.md").
- You can provision and mount additional Amazon EBS volumes on SageMaker HyperPod nodes using
  two approaches: use [InstanceStorageConfigs](../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs "../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs") for
  cluster-level volume provisioning (available when creating or updating instance
  groups), or use the Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver for
  dynamic pod-level volume management. With [InstanceStorageConfigs](../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs "../APIReference/API_ClusterInstanceGroupSpecification.md#sagemaker-Type-ClusterInstanceGroupSpecification-InstanceStorageConfigs"), set
  the [local
  path](https://kubernetes.io/docs/concepts/storage/volumes/#local "https://kubernetes.io/docs/concepts/storage/volumes/#local") to `/opt/sagemaker` to properly mount the volumes to
  your Amazon EKS pods. For information about how to deploy the [Amazon EBS CSI](../../../eks/latest/userguide/ebs-csi.md "../../../eks/latest/userguide/ebs-csi.md") controller on
  HyperPod nodes, see [Using the Amazon EBS CSI driver on SageMaker HyperPod EKS clusters](sagemaker-hyperpod-eks-ebs.md "sagemaker-hyperpod-eks-ebs.md"). To use
  NVMe instance storage on HyperPod, rely on the AMI's built-in LVM configuration
  through `/opt/sagemaker` rather than installing a separate
  NVMe-targeting CSI driver.
- If you use instance-type labels to define scheduling constraints, ensure that
  you use the SageMaker AI ML instance types prefixed with `ml.`. For example, for
  P5 instances, use `ml.p5.48xlarge` instead of
  `p5.48xlarge`.
  **Considerations for configuring network for SageMaker HyperPod clusters
  with Amazon EKS**

- Each HyperPod cluster instance supports one Elastic Network Interface
  (ENI). For the maximum number of Pods per instance type, refer to the following
  table.

| Instance type       | Max number of pods |
| ------------------- | ------------------ |
| ml.p4d.24xlarge     | 49                 |
| ml.p4de.24xlarge    | 49                 |
| ml.p5.48xlarge      | 49                 |
| ml.trn1.32xlarge    | 49                 |
| ml.trn1n.32xlarge   | 49                 |
| ml.g5.xlarge        | 14                 |
| ml.g5.2xlarge       | 14                 |
| ml.g5.4xlarge       | 29                 |
| ml.g5.8xlarge       | 29                 |
| ml.g5.12xlarge      | 49                 |
| ml.g5.16xlarge      | 29                 |
| ml.g5.24xlarge      | 49                 |
| ml.g5.48xlarge      | 49                 |
| ml.c5.large         | 9                  |
| ml.c5.xlarge        | 14                 |
| ml.c5.2xlarge       | 14                 |
| ml.c5.4xlarge       | 29                 |
| ml.c5.9xlarge       | 29                 |
| ml.c5.12xlarge      | 29                 |
| ml.c5.18xlarge      | 49                 |
| ml.c5.24xlarge      | 49                 |
| ml.c5n.large        | 9                  |
| ml.c5n.2xlarge      | 14                 |
| ml.c5n.4xlarge      | 29                 |
| ml.c5n.9xlarge      | 29                 |
| ml.c5n.18xlarge     | 49                 |
| ml.m5.large         | 9                  |
| ml.m5.xlarge        | 14                 |
| ml.m5.2xlarge       | 14                 |
| ml.m5.4xlarge       | 29                 |
| ml.m5.8xlarge       | 29                 |
| ml.m5.12xlarge      | 29                 |
| ml.m5.16xlarge      | 49                 |
| ml.m5.24xlarge      | 49                 |
| ml.t3.medium        | 5                  |
| ml.t3.large         | 11                 |
| ml.t3.xlarge        | 14                 |
| ml.t3.2xlarge       | 14                 |
| ml.g6.xlarge        | 14                 |
| ml.g6.2xlarge       | 14                 |
| ml.g6.4xlarge       | 29                 |
| ml.g6.8xlarge       | 29                 |
| ml.g6.12xlarge      | 29                 |
| ml.g6.16xlarge      | 49                 |
| ml.g6.24xlarge      | 49                 |
| ml.g6.48xlarge      | 49                 |
| ml.gr6.4xlarge      | 29                 |
| ml.gr6.8xlarge      | 29                 |
| ml.g6e.xlarge       | 14                 |
| ml.g6e.2xlarge      | 14                 |
| ml.g6e.4xlarge      | 29                 |
| ml.g6e.8xlarge      | 29                 |
| ml.g6e.12xlarge     | 29                 |
| ml.g6e.16xlarge     | 49                 |
| ml.g6e.24xlarge     | 49                 |
| ml.g6e.48xlarge     | 49                 |
| ml.p5e.48xlarge     | 49                 |
| ml.p6-b300.48xlarge | 49                 |
| ml.r5d.16xlarge     | 49                 |
| ml.g7e.2xlarge      | 49                 |
| ml.g7e.4xlarge      | 49                 |
| ml.g7e.8xlarge      | 49                 |
| ml.g7e.12xlarge     | 49                 |
| ml.g7e.24xlarge     | 49                 |
| ml.g7e.48xlarge     | 49                 |
| ml.g4dn.xlarge      | 9                  |
| ml.g4dn.2xlarge     | 9                  |
| ml.g4dn.4xlarge     | 9                  |
| ml.g4dn.8xlarge     | 14                 |
| ml.g4dn.12xlarge    | 29                 |
| ml.g4dn.16xlarge    | 14                 |
| ml.c6g.medium       | 3                  |
| ml.c6g.large        | 9                  |
| ml.c6g.xlarge       | 14                 |
| ml.c6g.2xlarge      | 14                 |
| ml.c6g.4xlarge      | 29                 |
| ml.c6g.8xlarge      | 29                 |
| ml.c6g.12xlarge     | 29                 |
| ml.c6g.16xlarge     | 49                 |
| ml.c7g.medium       | 3                  |
| ml.c7g.large        | 9                  |
| ml.c7g.xlarge       | 14                 |
| ml.c7g.2xlarge      | 14                 |
| ml.c7g.4xlarge      | 29                 |
| ml.c7g.8xlarge      | 29                 |
| ml.c7g.12xlarge     | 29                 |
| ml.c7g.16xlarge     | 49                 |
| ml.c8g.medium       | 3                  |
| ml.c8g.large        | 9                  |
| ml.c8g.xlarge       | 14                 |
| ml.c8g.2xlarge      | 14                 |
| ml.c8g.4xlarge      | 29                 |
| ml.c8g.8xlarge      | 29                 |
| ml.c8g.12xlarge     | 29                 |
| ml.c8g.16xlarge     | 49                 |
| ml.c8g.24xlarge     | 49                 |
| ml.c8g.48xlarge     | 49                 |
| ml.c6a.large        | 9                  |
| ml.c6a.xlarge       | 14                 |
| ml.c6a.2xlarge      | 14                 |
| ml.c6a.4xlarge      | 29                 |
| ml.c6a.8xlarge      | 29                 |
| ml.c6a.12xlarge     | 29                 |
| ml.c6a.16xlarge     | 49                 |
| ml.c6a.24xlarge     | 49                 |
| ml.c6a.32xlarge     | 49                 |
| ml.c6a.48xlarge     | 49                 |
| ml.m6a.large        | 9                  |
| ml.m6a.xlarge       | 14                 |
| ml.m6a.2xlarge      | 14                 |
| ml.m6a.4xlarge      | 29                 |
| ml.m6a.8xlarge      | 29                 |
| ml.m6a.12xlarge     | 29                 |
| ml.m6a.16xlarge     | 49                 |
| ml.m6a.24xlarge     | 49                 |
| ml.m6a.32xlarge     | 49                 |
| ml.m6a.48xlarge     | 49                 |
| ml.m6g.medium       | 3                  |
| ml.m6g.large        | 9                  |
| ml.m6g.xlarge       | 14                 |
| ml.m6g.2xlarge      | 14                 |
| ml.m6g.4xlarge      | 29                 |
| ml.m6g.8xlarge      | 29                 |
| ml.m6g.12xlarge     | 29                 |
| ml.m6g.16xlarge     | 49                 |
| ml.m7g.medium       | 3                  |
| ml.m7g.large        | 9                  |
| ml.m7g.xlarge       | 14                 |
| ml.m7g.2xlarge      | 14                 |
| ml.m7g.4xlarge      | 29                 |
| ml.m7g.8xlarge      | 29                 |
| ml.m7g.12xlarge     | 29                 |
| ml.m7g.16xlarge     | 49                 |
| ml.m8g.medium       | 3                  |
| ml.m8g.large        | 9                  |
| ml.m8g.xlarge       | 14                 |
| ml.m8g.2xlarge      | 14                 |
| ml.m8g.4xlarge      | 29                 |
| ml.m8g.8xlarge      | 29                 |
| ml.m8g.12xlarge     | 29                 |
| ml.m8g.16xlarge     | 49                 |
| ml.m8g.24xlarge     | 49                 |
| ml.m8g.48xlarge     | 49                 |

- Only Pods with `hostNetwork = true` have access to the Amazon EC2 Instance
  Metadata Service (IMDS) by default. Use the Amazon EKS Pod identity or the [IAM roles for
  service accounts (IRSA)](../../../eks/latest/userguide/iam-roles-for-service-accounts.md "../../../eks/latest/userguide/iam-roles-for-service-accounts.md") to manage access to the AWS credentials for
  Pods.
- EKS-orchestrated HyperPod clusters support dual IP addressing modes, allowing
  configuration with IPv4 or IPv6 for IPv6 Amazon EKS clusters in IPv6-enabled VPC and
  subnet environments. For more information, see [Setting up SageMaker HyperPod with a custom Amazon VPC](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-optional-vpc").
  **Considerations for using the HyperPod cluster resiliency
  features**

- Node auto-replacement is not supported for CPU instances.
- The HyperPod health monitoring agent needs to be installed for node
  auto-recovery to work. The agent can be installed using Helm. For more information,
  see [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md").
- The HyperPod deep health check and health monitoring agent supports GPU
  and Trn instances.
- SageMaker AI applies the following taint to nodes when they are undergoing deep health
  checks:

```
effect: NoSchedule
key: sagemaker.amazonaws.com/node-health-status
value: Unschedulable
```

###### Note

You cannot add custom taints to nodes in instance groups with
`DeepHealthChecks` turned on.
Once your Amazon EKS cluster is running, configure your cluster using the Helm package manager
as instructed in [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md")
before creating your HyperPod cluster.
