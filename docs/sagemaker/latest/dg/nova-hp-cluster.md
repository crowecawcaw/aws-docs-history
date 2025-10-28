# Creating a HyperPod EKS cluster with restricted instance group (RIG)

This topic covers the steps to create a Amazon SageMaker HyperPod EKS cluster with a restricted
instance group (RIG). A RIG configuration in SageMaker HyperPod EKS clusters provides a specialized
environment for training Amazon Nova models. RIG has the following restrictions:

- RIG workloads run in an internet-free VPC, all ingress and egress are strictly
  regulated.
- RIG has restrictions on the observability of Kubernetes functions such as kubectl exec
  and logs to ensure a secured environment for Nova model training.
- RIG only allows Nova customization images, and jobs running with other images will be
  denied.
  You can create a RIG when setting up instance groups in your HyperPod EKS
  cluster. While you can control the size and scaling of these resources, you cannot
  directly access the worker nodes. This architecture ensures Nova components (model
  weights, checkpoints, training data, and code) are only accessible through regulated
  channels and a service-managed account system.

Nova model customization on SageMaker HyperPod relies on a service-managed FSx for Lustre
file system to achieve optimal performance. When creating a RIG, you must specify the volume
size and throughput for the FSx for Lustre file system, which will be mounted to all worker nodes in the
instance group. FSx for Lustre is used to store intermediate checkpoints and internal model states
during distributed training. Follow the guidance provided in the recipe to choose an appropriate
volume size and throughput to ensure sufficient capacity and performance. FSx for Lustre usage costs will
apply to your AWS account.

**Important notes for RIG in HyperPod EKS
clusters**

- RIG only supports the execution role for permissions. Ensure that the execution role
  includes the necessary IAM permissions, such as access to Amazon S3.
- When using service-managed Amazon FSx for Lustre and Amazon S3, ensure that your FSx for Lustre file
  system is appropriately sized for your workload. The training data manifest is uploaded to
  Amazon S3, which must be accessible by the execution role.
- RIG must be created or updated on a new SageMaker HyperPod EKS cluster-specifically, one
  created on or after July 16, 2025. Clusters created before this date might contain
  incompatible software versions or configurations that are not supported by RIG.
- Creating HyperPod EKS clusters with RIGs is only supported in the following
  AWS Region: `us-east-1`.

## Create a HyperPod EKS cluster with a

restricted instance group (Console - recommended)

This section provides detailed instructions for creating a HyperPod EKS
cluster with a restricted instance group for Amazon Nova customization using the
AWS Management Console. For more information, see [Creating
a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").

###### Note

You must create the cluster in `us-east-1` because it's the only
supported AWS Region for restricted instance groups.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **HyperPod Clusters** in the left
   navigation pane and then **Cluster Management**.
3. On the **SageMaker HyperPod Clusters** page, choose
   **Create HyperPod cluster**.
4. On the **Create HyperPod cluster** drop-down,
   choose **Orchestrated by Amazon EKS**.
5. On the cluster creation page, choose **Quick setup**.
   With this option, you can get started immediately with default settings.
   SageMaker AI will create new resources such as VPC, subnets, security groups, Amazon S3
   bucket, IAM role, and FSx for Lustre in the process of creating your
   cluster.
6. On **General settings**, specify a name for the new
   cluster. You can’t change the name after the cluster is created.
7. On **Instance groups**, choose **Add
   group**. Each instance group can be configured differently, and
   you can create a heterogeneous cluster that consists of multiple instance
   groups with various instance types. To deploy a cluster, you must add at
   least one instance group. You can add one instance group at a time. To
   create multiple instance groups, repeat the process for each instance
   group.

Follow these steps to add an instance group.

    1. For **Instance group type**, choose
     **Restricted Instance Group (RIG)**.
     **Restricted Instance Group (RIG)** is a
     specialized environment for foundational models customization such
     as Amazon Nova. **Standard** provides a general purpose
     computing environment without additional security
     restrictions.
    2. For **Name**, specify a name for the instance
     group.
    3. For **Instance capacity**, choose either
     on-demand capacity or a training plan to reserve your compute
     resources.
    4. For **Instance type**, choose the instance for
     the instance group. You must choose an instance type that supports
     Amazon Nova model customization, for example,
     `ml.p5.48xlarge`. Also ensure that you choose the
     instance type with sufficient quotas in your AWS account. To
     request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas").
    5. For **Instance quantity**, specify an integer not
     exceeding the instance quota for cluster usage. For this quickstart,
     enter **1** for the restricted instance you are
     creating.
    6. For **Target Availability Zone**, choose the
     Availability Zone where your instances will be provisioned. The
     Availability Zone should correspond to the location of your
     accelerated compute capacity.
    7. For **Additional storage volume per instance (GB) -
     optional**, specify an integer between 1 and 16384 to
     set the size of an additional Elastic Block Store (EBS) volume in
     gigabytes (GB). The EBS volume is attached to each instance of the
     instance group. The default mount path for the additional EBS volume
     is `/opt/sagemaker`. After the cluster is successfully
     created, you can SSH into the cluster instances (nodes) and verify
     that the EBS volume is mounted correctly by running the `df
     -h` command. Attaching an additional EBS volume provides
     stable, off-instance, and independently persisting storage, as
     described in the [Amazon EBS
     volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the *Amazon Elastic Block Store User
     Guide*.
    8. For **Instance deep health checks**, choose your
     option. Deep health checks monitor instance health during creation
     and after software updates, automatically recovering faulty
     instances through reboots or replacements when enabled.
    9. Choose **Add instance group**.

8. On **Quick configuration defaults**, review the default
   settings. This section lists all the default settings for your cluster
   creation, including all the new AWS resources that will be created during
   the cluster creation process.
9. Choose **Submit**.

## Create a HyperPod EKS cluster with a restricted

instance group (CLI)

Follow [these
instructions](sagemaker-hyperpod-eks-operate-cli-command-create-cluster.md "sagemaker-hyperpod-eks-operate-cli-command-create-cluster.md") to create a HyperPod EKS cluster with a RIG using the
AWS CLI.
